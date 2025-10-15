# AudioLab University

Repositorio de documentación técnica del programa **AudioLab** - Matemáticas y DSP para audio profesional.

## Objetivo

Este repositorio contiene la documentación completa del programa AudioLab, estructurada con **MkDocs Material** para generar un sitio web estático con soporte completo para:

- LaTeX (ecuaciones matemáticas vía KaTeX)
- Diagramas Mermaid
- Notebooks Jupyter interactivos
- Sintaxis destacada de código
- Navegación multi-nivel

## Estructura del Proyecto

```
audiolab-university/
├── docs/                      # Contenido de documentación
│   ├── 00_about/             # Información del proyecto
│   ├── 01_programa/          # Contenido académico por bloques
│   │   └── AL1-04_algebra_calculo/
│   ├── 02_practicas/         # Guías de prácticas y laboratorios
│   ├── 03_notebooks/         # Jupyter notebooks
│   ├── 04_recursos/          # Bibliografía y glosario
│   ├── js/                   # JavaScript (KaTeX init)
│   └── styles/               # CSS personalizado
├── templates/                 # Plantillas para nuevos contenidos
├── agents/                    # Configuración para agentes MCP
│   ├── guards/               # Políticas de validación
│   ├── schemas/              # JSON Schemas
│   ├── prompts/              # Prompts para agentes
│   └── mcp_config.json       # Configuración MCP
├── .github/workflows/        # CI/CD con GitHub Actions
├── mkdocs.yml                # Configuración de MkDocs
├── requirements.txt          # Dependencias Python
└── README.md                 # Este archivo
```

## Desarrollo Local

### Instalación

1. Crear entorno virtual:
   ```bash
   python -m venv .venv
   ```

2. Activar entorno:
   - Windows: `.venv\Scripts\activate`
   - Linux/Mac: `source .venv/bin/activate`

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Servir Localmente

Ejecutar servidor de desarrollo:

```bash
mkdocs serve
```

El sitio estará disponible en `http://127.0.0.1:8000`

Cambios en archivos Markdown se reflejarán automáticamente (hot reload).

### Build de Producción

Generar sitio estático:

```bash
mkdocs build --strict
```

El sitio se genera en `site/`. Modo `--strict` falla si hay warnings (enlaces rotos, etc.).

## Publicación

### GitHub Pages (Automático)

El workflow `.github/workflows/build-deploy.yml` despliega automáticamente a GitHub Pages al hacer push a `main`.

**Requisitos previos:**
1. Habilitar GitHub Pages en Settings → Pages → Source: `gh-pages` branch
2. El workflow se ejecuta automáticamente

### Manual

Desplegar manualmente:

```bash
mkdocs gh-deploy
```

## Convenciones de Escritura

### Matemáticas

Usar notación **KaTeX compatible**:

- Inline: `$x^2 + y^2 = z^2$`
- Display: `$$\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$$`

**NO usar** `\(...\)` o `\[...\]` (no son compatibles con nuestro setup).

### Headings

- **H1** (`#`): Título del capítulo (uno por archivo)
- **H2** (`##`): Secciones principales
- **H3** (`###`): Subsecciones
- **H4+**: Evitar si es posible

### Enlaces

Usar rutas relativas desde `docs/`:

```markdown
[Ver Capítulo 1](01_programa/AL1-04_algebra_calculo/cap01_vectores.md)
```

### Imágenes

Guardar en carpeta local del módulo:

```
docs/01_programa/AL1-04_algebra_calculo/images/vector_diagram.png
```

Referenciar:

```markdown
![Diagrama de vector](images/vector_diagram.png)
```

## Contribución con Agentes MCP

Los agentes pueden crear/editar contenido siguiendo el workflow:

1. **Crear rama**: `ai/feature-description`
2. **Usar template**: Copiar de `templates/template_capitulo.md` o `template_practica.md`
3. **Validar contra schema**: `agents/schemas/chapter.schema.json`
4. **Cumplir políticas**: Ver `agents/guards/policy.md`
5. **Crear PR**: Título formato `feat(chapter): añadir cap03_transformadas`
6. **CI valida**: Workflow `validate-pr.yml` ejecuta `mkdocs build --strict`
7. **Merge**: Solo humanos aprueban merge a `main`

### Configuración MCP

Editar `agents/mcp_config.json` con:

- Token GitHub (para crear PRs)
- Endpoint de agente (si aplica)
- Políticas específicas del equipo

**IMPORTANTE**: No commitear tokens. Usar variables de entorno o GitHub Secrets.

## Prompts de Agentes

Ver carpeta `agents/prompts/` para instrucciones detalladas:

- `doc_writer.md`: Crear/editar capítulos
- `reviewer.md`: Revisar PRs
- `curator.md`: Mantener navegación en `mkdocs.yml`

## Sincronización con Notion

Este repositorio sincroniza automáticamente la documentación con una Notion Database tras cada push a `main`.

### Configuración Inicial

#### 1. Crear Notion Integration

1. Visitar https://www.notion.so/my-integrations
2. Crear nueva integración:
   - Nombre: `AudioLab University Sync`
   - Associated workspace: Tu workspace
   - Capabilities: Read content, Update content, Insert content
3. Copiar el **Internal Integration Token** (formato: `secret_XXX...`)

#### 2. Crear Notion Database

1. En Notion, crear nueva página de tipo Database (Full page)
2. Nombrar: `AudioLab Docs`
3. Añadir propiedades:
   - `Title`: Title (predeterminado)
   - `Slug`: Text (identificador único del archivo)
   - `Status`: Select (opciones: Draft, In_progress, Published)
   - `Tags`: Multi-select
   - `GitHash`: Text (hash SHA1 del contenido)

4. Conectar la integración:
   - Click en `...` (esquina superior derecha)
   - Add connections → Seleccionar tu integración

5. Copiar Database ID:
   - Desde la URL: `https://notion.so/<workspace>/<DATABASE_ID>?v=...`
   - El Database ID es el string de 32 caracteres (con guiones)

#### 3. Configurar GitHub Secrets

En tu repositorio GitHub:

1. Settings → Secrets and variables → Actions
2. Añadir secrets:
   - `NOTION_TOKEN`: El token de integración (`secret_XXX...`)
   - `NOTION_DATABASE_ID`: El ID de la database (32 caracteres)

### Uso

#### Front-matter en Archivos Markdown

Añadir al inicio de cada archivo `.md` en `docs/`:

```yaml
---
title: Capítulo 1 - Vectores en Audio
slug: cap01_vectores
status: published
tags:
  - algebra
  - vectores
  - dsp
---
```

Campos:
- **title**: Título visible en Notion (requerido)
- **slug**: Identificador único para sincronización (requerido)
- **status**: draft | in_progress | published (default: draft)
- **tags**: Lista de etiquetas (opcional)

#### Sincronización Automática

El workflow `.github/workflows/export-notion.yml` se ejecuta:
- Automáticamente tras push a `main` que modifique `docs/**/*.md`
- Manualmente desde Actions → Export to Notion → Run workflow

Comportamiento:
- Si el archivo no existe en Notion (busca por `slug`): se crea
- Si existe y el hash SHA1 del contenido cambió: se actualizan propiedades y bloques
- Si existe y el hash es idéntico: se omite (no hay cambios)

#### Prueba Local

Exportar manualmente desde tu máquina:

```bash
# Instalar dependencias
pip install requests pyyaml

# Configurar variables de entorno (Linux/Mac)
export NOTION_TOKEN="secret_XXX..."
export NOTION_DATABASE_ID="abc123..."

# Windows (PowerShell)
$env:NOTION_TOKEN="secret_XXX..."
$env:NOTION_DATABASE_ID="abc123..."

# Ejecutar export
python tools/export_to_notion.py --root docs

# Dry run (sin ejecutar requests reales)
python tools/export_to_notion.py --root docs --dry-run
```

### Notas Importantes

- Notion es **salida de solo escritura**: edita siempre en el repositorio Git
- Las ediciones manuales en Notion serán sobrescritas en el siguiente sync
- Archivos sin `slug` en front-matter se omiten automáticamente
- Throttle automático: 2.5 req/s (respeta límite de Notion)

### Formatos Soportados

El conversor `md_to_notion_blocks.py` soporta:

- Headings (H1-H3)
- Párrafos con texto enriquecido
- Listas ordenadas y no ordenadas
- Bloques de código con sintaxis
- Ecuaciones matemáticas:
  - Display: `$$...$$`
  - Inline: `$...$`
- Callouts (admonitions):
  ```markdown
  !!! info "Título"
      Contenido del callout
  ```

## Próximos Pasos

### Activar GitHub Pages

1. Push inicial a `main`:
   ```bash
   git add .
   git commit -m "feat: initial repo scaffold"
   git push origin main
   ```

2. Configurar Pages:
   - Ir a Settings → Pages
   - Source: Deploy from branch
   - Branch: `gh-pages` / `(root)`
   - Save

3. Esperar workflow (1-2 minutos)

4. Visitar `https://<tu-usuario>.github.io/audiolab-university`

### Añadir Contenido

- Usar templates en `templates/`
- Seguir convenciones de `agents/guards/policy.md`
- Ejecutar `mkdocs serve` para preview local
- Hacer PR para revisión

## Soporte

Para dudas sobre MkDocs: https://www.mkdocs.org
Material theme: https://squidfunk.github.io/mkdocs-material
KaTeX: https://katex.org

---

Generado con agentes MCP para AudioLab University
