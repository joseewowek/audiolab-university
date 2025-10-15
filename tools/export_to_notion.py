#!/usr/bin/env python3
"""
Exporta documentación Markdown a Notion Database.

Uso:
    python tools/export_to_notion.py --root docs

Variables de entorno requeridas:
    NOTION_TOKEN: Integration token (secrets.XXX)
    NOTION_DATABASE_ID: ID de la database destino

Comportamiento:
- Lee archivos .md con front-matter YAML
- Calcula hash SHA1 del contenido
- Busca página por slug en Notion Database
- Si no existe: crea nueva página
- Si existe y hash cambió: actualiza propiedades y reemplaza bloques
- Throttle: 0.4s entre llamadas (2.5 req/s, bajo límite 3 req/s)

Front-matter esperado:
---
title: Título del capítulo
slug: cap01_vectores
status: draft | in_progress | published
tags:
  - algebra
  - vectores
---
"""

import os
import sys
import hashlib
import time
import argparse
from pathlib import Path
from typing import Optional, Dict, Any, List
import yaml
import re

try:
    import requests
except ImportError:
    print("ERROR: Instala requests: pip install requests")
    sys.exit(1)

# Importar conversor local
try:
    from md_to_notion_blocks import to_blocks
except ImportError:
    print("ERROR: md_to_notion_blocks.py debe estar en el mismo directorio")
    sys.exit(1)


NOTION_VERSION = "2022-06-28"
THROTTLE_DELAY = 0.4  # segundos (≈ 2.5 req/s)


class NotionExporter:
    def __init__(self, token: str, database_id: str):
        self.token = token
        self.database_id = database_id
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json"
        }
        self.base_url = "https://api.notion.com/v1"

    def _throttle(self):
        """Espera para respetar rate limit."""
        time.sleep(THROTTLE_DELAY)

    def query_page_by_slug(self, slug: str) -> Optional[Dict[str, Any]]:
        """
        Busca página en Database filtrando por propiedad Slug.

        Returns:
            Dict con datos de página si existe, None si no
        """
        url = f"{self.base_url}/databases/{self.database_id}/query"

        payload = {
            "filter": {
                "property": "Slug",
                "rich_text": {
                    "equals": slug
                }
            }
        }

        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()

            results = data.get("results", [])
            if results:
                return results[0]  # Retornar primera coincidencia
            return None

        except requests.exceptions.RequestException as e:
            print(f"ERROR al buscar slug '{slug}': {e}")
            return None
        finally:
            self._throttle()

    def create_page(self, title: str, slug: str, status: str, tags: List[str], git_hash: str, blocks: List[Dict]) -> Optional[str]:
        """
        Crea nueva página en Database.

        Returns:
            page_id si se creó, None si falló
        """
        url = f"{self.base_url}/pages"

        payload = {
            "parent": {"database_id": self.database_id},
            "properties": {
                "Title": {
                    "title": [{"text": {"content": title}}]
                },
                "Slug": {
                    "rich_text": [{"text": {"content": slug}}]
                },
                "Status": {
                    "select": {"name": status.capitalize()}
                },
                "Tags": {
                    "multi_select": [{"name": tag} for tag in tags]
                },
                "GitHash": {
                    "rich_text": [{"text": {"content": git_hash}}]
                }
            },
            "children": blocks[:100]  # Notion limita 100 bloques por request
        }

        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()
            page_id = data["id"]
            print(f"✓ Página creada: {title} (slug: {slug})")

            # Si hay más de 100 bloques, añadirlos en batch
            if len(blocks) > 100:
                self._append_blocks(page_id, blocks[100:])

            return page_id

        except requests.exceptions.RequestException as e:
            print(f"ERROR al crear página '{title}': {e}")
            if hasattr(e.response, 'text'):
                print(f"  Respuesta: {e.response.text}")
            return None
        finally:
            self._throttle()

    def update_page(self, page_id: str, title: str, status: str, tags: List[str], git_hash: str) -> bool:
        """
        Actualiza propiedades de página existente.

        Returns:
            True si actualizó, False si falló
        """
        url = f"{self.base_url}/pages/{page_id}"

        payload = {
            "properties": {
                "Title": {
                    "title": [{"text": {"content": title}}]
                },
                "Status": {
                    "select": {"name": status.capitalize()}
                },
                "Tags": {
                    "multi_select": [{"name": tag} for tag in tags]
                },
                "GitHash": {
                    "rich_text": [{"text": {"content": git_hash}}]
                }
            }
        }

        try:
            response = requests.patch(url, headers=self.headers, json=payload)
            response.raise_for_status()
            print(f"✓ Propiedades actualizadas: {title}")
            return True

        except requests.exceptions.RequestException as e:
            print(f"ERROR al actualizar página '{title}': {e}")
            return False
        finally:
            self._throttle()

    def replace_page_blocks(self, page_id: str, blocks: List[Dict]) -> bool:
        """
        Reemplaza TODOS los bloques de una página.

        Pasos:
        1. Obtener lista de bloques actuales
        2. Eliminar todos
        3. Añadir nuevos bloques

        Returns:
            True si reemplazó, False si falló
        """
        # 1. Listar bloques actuales
        try:
            url = f"{self.base_url}/blocks/{page_id}/children"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            existing_blocks = data.get("results", [])

            self._throttle()

            # 2. Eliminar bloques existentes
            for block in existing_blocks:
                block_id = block["id"]
                delete_url = f"{self.base_url}/blocks/{block_id}"
                try:
                    requests.delete(delete_url, headers=self.headers)
                    self._throttle()
                except Exception as e:
                    print(f"  Advertencia: no se pudo eliminar bloque {block_id}: {e}")

            # 3. Añadir nuevos bloques
            self._append_blocks(page_id, blocks)
            print(f"✓ Bloques reemplazados ({len(blocks)} bloques)")
            return True

        except requests.exceptions.RequestException as e:
            print(f"ERROR al reemplazar bloques: {e}")
            return False

    def _append_blocks(self, block_id: str, blocks: List[Dict]) -> bool:
        """
        Añade bloques a un bloque/página (en batches de 100).

        Returns:
            True si añadió todos, False si alguno falló
        """
        url = f"{self.base_url}/blocks/{block_id}/children"

        # Procesar en batches de 100
        for i in range(0, len(blocks), 100):
            batch = blocks[i:i+100]

            payload = {"children": batch}

            try:
                response = requests.patch(url, headers=self.headers, json=payload)
                response.raise_for_status()
                print(f"  + Añadidos {len(batch)} bloques")

            except requests.exceptions.RequestException as e:
                print(f"ERROR al añadir bloques (batch {i//100 + 1}): {e}")
                if hasattr(e.response, 'text'):
                    print(f"  Respuesta: {e.response.text}")
                return False
            finally:
                self._throttle()

        return True


def parse_front_matter(content: str) -> tuple:
    """
    Extrae front-matter YAML y contenido Markdown.

    Returns:
        (metadata_dict, markdown_content)
    """
    # Regex para detectar front-matter entre ---
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)

    if not match:
        # No hay front-matter
        return {}, content

    yaml_content = match.group(1)
    markdown_content = match.group(2)

    try:
        metadata = yaml.safe_load(yaml_content)
        return metadata or {}, markdown_content
    except yaml.YAMLError as e:
        print(f"ERROR al parsear YAML: {e}")
        return {}, content


def calculate_hash(content: str) -> str:
    """Calcula SHA1 del contenido Markdown (sin front-matter)."""
    return hashlib.sha1(content.encode('utf-8')).hexdigest()


def export_file(exporter: NotionExporter, file_path: Path, dry_run: bool = False):
    """
    Exporta un archivo .md a Notion.

    Args:
        exporter: Instancia de NotionExporter
        file_path: Path al archivo .md
        dry_run: Si True, no ejecuta requests (solo imprime)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"ERROR al leer {file_path}: {e}")
        return

    # Parsear front-matter
    metadata, markdown_content = parse_front_matter(content)

    # Validar campos requeridos
    title = metadata.get('title', file_path.stem)
    slug = metadata.get('slug')

    if not slug:
        print(f"⊘ Omitiendo {file_path}: sin 'slug' en front-matter")
        return

    status = metadata.get('status', 'draft')
    tags = metadata.get('tags', [])

    # Calcular hash
    git_hash = calculate_hash(markdown_content)

    print(f"\n{'='*60}")
    print(f"Procesando: {file_path.name}")
    print(f"  Título: {title}")
    print(f"  Slug: {slug}")
    print(f"  Status: {status}")
    print(f"  Tags: {', '.join(tags) if tags else '(ninguno)'}")
    print(f"  Hash: {git_hash[:8]}...")

    if dry_run:
        print("  [DRY RUN] No se ejecutarán requests reales")
        return

    # Buscar página existente por slug
    existing_page = exporter.query_page_by_slug(slug)

    # Convertir Markdown a bloques
    blocks = to_blocks(markdown_content)
    print(f"  Bloques generados: {len(blocks)}")

    if not existing_page:
        # Crear nueva página
        print("  → No existe en Notion, creando...")
        exporter.create_page(title, slug, status, tags, git_hash, blocks)

    else:
        # Verificar si el hash cambió
        page_id = existing_page["id"]
        existing_hash_prop = existing_page.get("properties", {}).get("GitHash", {})
        existing_hash = ""

        # Extraer hash (puede estar en rich_text)
        if existing_hash_prop.get("rich_text"):
            rich_text_items = existing_hash_prop["rich_text"]
            if rich_text_items:
                existing_hash = rich_text_items[0].get("text", {}).get("content", "")

        print(f"  → Existe en Notion (ID: {page_id[:8]}...)")
        print(f"     Hash actual: {existing_hash[:8]}...")

        if existing_hash == git_hash:
            print("  ✓ Contenido sin cambios, omitiendo")
        else:
            print("  → Hash diferente, actualizando...")
            exporter.update_page(page_id, title, status, tags, git_hash)
            exporter.replace_page_blocks(page_id, blocks)


def main():
    parser = argparse.ArgumentParser(
        description="Exporta documentación Markdown a Notion Database"
    )
    parser.add_argument(
        '--root',
        type=str,
        default='docs',
        help='Directorio raíz con archivos .md (default: docs)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Simular sin ejecutar requests reales'
    )

    args = parser.parse_args()

    # Leer variables de entorno
    notion_token = os.getenv('NOTION_TOKEN')
    database_id = os.getenv('NOTION_DATABASE_ID')

    if not notion_token:
        print("ERROR: Variable de entorno NOTION_TOKEN no definida")
        sys.exit(1)

    if not database_id:
        print("ERROR: Variable de entorno NOTION_DATABASE_ID no definida")
        sys.exit(1)

    print(f"Notion Export Tool")
    print(f"{'='*60}")
    print(f"Root directory: {args.root}")
    print(f"Database ID: {database_id[:8]}...")
    print(f"Dry run: {args.dry_run}")
    print(f"{'='*60}\n")

    # Inicializar exporter
    exporter = NotionExporter(notion_token, database_id)

    # Buscar archivos .md recursivamente
    root_path = Path(args.root)
    if not root_path.exists():
        print(f"ERROR: Directorio '{args.root}' no existe")
        sys.exit(1)

    md_files = list(root_path.rglob('*.md'))

    if not md_files:
        print(f"No se encontraron archivos .md en '{args.root}'")
        sys.exit(0)

    print(f"Encontrados {len(md_files)} archivos .md\n")

    # Exportar cada archivo
    for md_file in md_files:
        export_file(exporter, md_file, dry_run=args.dry_run)

    print(f"\n{'='*60}")
    print(f"✓ Exportación completada")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
