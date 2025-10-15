"""
Conversor de Markdown a bloques de Notion API.

Soporta:
- Headings (H1-H3)
- Párrafos con texto enriquecido
- Listas (ordenadas y no ordenadas)
- Bloques de código (code fences)
- Ecuaciones matemáticas (inline $ y display $$)
- Callouts (admonitions tipo MkDocs)

Uso:
    from md_to_notion_blocks import to_blocks

    markdown = "# Título\\n\\nPárrafo con $x^2$ ecuación."
    blocks = to_blocks(markdown)
"""

import re
from typing import List, Dict, Any


def to_blocks(markdown: str) -> List[Dict[str, Any]]:
    """
    Convierte Markdown a lista de bloques de Notion API.

    Args:
        markdown: Contenido Markdown (sin front-matter YAML)

    Returns:
        Lista de bloques en formato Notion API v2022-06-28
    """
    blocks = []
    lines = markdown.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Ignorar líneas vacías
        if not line.strip():
            i += 1
            continue

        # Bloques de código (fenced)
        if line.strip().startswith('```'):
            code_block, consumed = _parse_code_fence(lines[i:])
            if code_block:
                blocks.append(code_block)
                i += consumed
                continue

        # Ecuaciones display ($$)
        if line.strip().startswith('$$'):
            eq_block, consumed = _parse_display_equation(lines[i:])
            if eq_block:
                blocks.append(eq_block)
                i += consumed
                continue

        # Callouts (admonitions)
        if line.strip().startswith('!!!'):
            callout_block, consumed = _parse_callout(lines[i:])
            if callout_block:
                blocks.append(callout_block)
                i += consumed
                continue

        # Headings
        heading_match = re.match(r'^(#{1,3})\s+(.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()
            # Notion soporta heading_1, heading_2, heading_3
            blocks.append(_create_heading(level, text))
            i += 1
            continue

        # Listas ordenadas
        ol_match = re.match(r'^(\d+)\.\s+(.+)$', line)
        if ol_match:
            text = ol_match.group(2).strip()
            blocks.append(_create_numbered_list_item(text))
            i += 1
            continue

        # Listas no ordenadas
        ul_match = re.match(r'^[-*+]\s+(.+)$', line)
        if ul_match:
            text = ul_match.group(1).strip()
            blocks.append(_create_bulleted_list_item(text))
            i += 1
            continue

        # Párrafos (default)
        # Agrupar líneas consecutivas hasta encontrar línea vacía o bloque especial
        paragraph_lines = []
        while i < len(lines) and lines[i].strip():
            current_line = lines[i].strip()

            # Detener si encontramos inicio de bloque especial
            if (current_line.startswith('#') or
                current_line.startswith('```') or
                current_line.startswith('$$') or
                current_line.startswith('!!!') or
                re.match(r'^[-*+]\s+', current_line) or
                re.match(r'^\d+\.\s+', current_line)):
                break

            paragraph_lines.append(current_line)
            i += 1

        if paragraph_lines:
            paragraph_text = ' '.join(paragraph_lines)
            blocks.append(_create_paragraph(paragraph_text))

    return blocks


def _parse_code_fence(lines: List[str]) -> tuple:
    """
    Parsea un bloque de código fenced (```).

    Returns:
        (block_dict, lines_consumed) o (None, 0) si no es válido
    """
    if not lines[0].strip().startswith('```'):
        return None, 0

    language = lines[0].strip()[3:].strip() or 'plain text'
    code_lines = []
    i = 1

    while i < len(lines):
        if lines[i].strip() == '```':
            # Fin del bloque
            code_content = '\n'.join(code_lines)
            block = {
                "object": "block",
                "type": "code",
                "code": {
                    "rich_text": [{"type": "text", "text": {"content": code_content}}],
                    "language": _map_language(language)
                }
            }
            return block, i + 1

        code_lines.append(lines[i])
        i += 1

    # No se encontró cierre, tratar como código
    code_content = '\n'.join(code_lines)
    block = {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [{"type": "text", "text": {"content": code_content}}],
            "language": _map_language(language)
        }
    }
    return block, len(lines)


def _parse_display_equation(lines: List[str]) -> tuple:
    """
    Parsea ecuación display ($$...$$).

    Returns:
        (block_dict, lines_consumed) o (None, 0) si no es válido
    """
    if not lines[0].strip().startswith('$$'):
        return None, 0

    equation_lines = []
    i = 0

    # Caso 1: $$ en línea separada (inicio)
    if lines[0].strip() == '$$':
        i = 1
        while i < len(lines):
            if lines[i].strip() == '$$':
                # Fin del bloque
                equation_content = '\n'.join(equation_lines).strip()
                block = {
                    "object": "block",
                    "type": "equation",
                    "equation": {
                        "expression": equation_content
                    }
                }
                return block, i + 1

            equation_lines.append(lines[i])
            i += 1

    # Caso 2: $$....$$ en la misma línea
    single_line = lines[0].strip()
    match = re.match(r'^\$\$(.+)\$\$$', single_line)
    if match:
        equation_content = match.group(1).strip()
        block = {
            "object": "block",
            "type": "equation",
            "equation": {
                "expression": equation_content
            }
        }
        return block, 1

    return None, 0


def _parse_callout(lines: List[str]) -> tuple:
    """
    Parsea callout/admonition estilo MkDocs.

    Formato: !!! info "Título"
             Contenido del callout

    Returns:
        (block_dict, lines_consumed)
    """
    match = re.match(r'^!!!\s+(info|tip|warning|note|danger)\s*(?:"([^"]+)")?', lines[0].strip())
    if not match:
        return None, 0

    callout_type = match.group(1)
    title = match.group(2) or callout_type.capitalize()

    # Leer contenido (líneas indentadas o hasta línea vacía)
    content_lines = []
    i = 1

    while i < len(lines):
        line = lines[i]

        # Si línea vacía o no indentada, fin del callout
        if not line.strip() or (not line.startswith('    ') and not line.startswith('\t')):
            break

        # Eliminar indentación
        dedented = line.lstrip()
        content_lines.append(dedented)
        i += 1

    content = '\n'.join(content_lines).strip() if content_lines else ""

    # Mapear tipo a emoji/estilo
    emoji_map = {
        'info': 'ℹ️',
        'tip': '💡',
        'warning': '⚠️',
        'note': '📝',
        'danger': '🚨'
    }

    emoji = emoji_map.get(callout_type, 'ℹ️')

    # Notion callout block
    block = {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": [
                {"type": "text", "text": {"content": f"{title}\n{content}"}}
            ],
            "icon": {"type": "emoji", "emoji": emoji}
        }
    }

    return block, i


def _create_heading(level: int, text: str) -> Dict[str, Any]:
    """Crea bloque heading (1, 2 o 3)."""
    heading_type = f"heading_{min(level, 3)}"

    # Procesar inline math si existe
    rich_text = _parse_inline_math(text)

    return {
        "object": "block",
        "type": heading_type,
        heading_type: {
            "rich_text": rich_text
        }
    }


def _create_paragraph(text: str) -> Dict[str, Any]:
    """Crea bloque de párrafo."""
    # Procesar inline math
    rich_text = _parse_inline_math(text)

    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": rich_text
        }
    }


def _create_bulleted_list_item(text: str) -> Dict[str, Any]:
    """Crea item de lista no ordenada."""
    rich_text = _parse_inline_math(text)

    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": rich_text
        }
    }


def _create_numbered_list_item(text: str) -> Dict[str, Any]:
    """Crea item de lista ordenada."""
    rich_text = _parse_inline_math(text)

    return {
        "object": "block",
        "type": "numbered_list_item",
        "numbered_list_item": {
            "rich_text": rich_text
        }
    }


def _parse_inline_math(text: str) -> List[Dict[str, Any]]:
    """
    Convierte texto con $...$ inline a rich_text con ecuaciones.

    Estrategia conservadora:
    - Detectar $...$ inline
    - Alternar entre texto plano y ecuaciones inline
    """
    rich_text = []

    # Regex para capturar $...$ (no greedy, no $$)
    # Evitar capturar $$ (display)
    pattern = r'\$(?!\$)(.+?)\$(?!\$)'

    last_end = 0
    for match in re.finditer(pattern, text):
        # Texto antes de la ecuación
        before = text[last_end:match.start()]
        if before:
            rich_text.append({
                "type": "text",
                "text": {"content": before}
            })

        # Ecuación inline
        equation_content = match.group(1)
        rich_text.append({
            "type": "equation",
            "equation": {"expression": equation_content}
        })

        last_end = match.end()

    # Texto restante
    remaining = text[last_end:]
    if remaining:
        rich_text.append({
            "type": "text",
            "text": {"content": remaining}
        })

    # Si no hay ecuaciones, retornar texto simple
    if not rich_text:
        rich_text = [{"type": "text", "text": {"content": text}}]

    return rich_text


def _map_language(lang: str) -> str:
    """Mapea identificadores de lenguaje Markdown a Notion."""
    lang_map = {
        'py': 'python',
        'js': 'javascript',
        'ts': 'typescript',
        'sh': 'shell',
        'bash': 'shell',
        'yml': 'yaml',
        'md': 'markdown',
        'json': 'json',
        'cpp': 'c++',
        'c': 'c',
        'java': 'java',
        'go': 'go',
        'rust': 'rust',
        'sql': 'sql',
        'html': 'html',
        'css': 'css',
        'plain text': 'plain text'
    }

    return lang_map.get(lang.lower(), 'plain text')


# Test básico
if __name__ == '__main__':
    sample_md = """# Título de Prueba

Este es un párrafo con una ecuación inline $x^2 + y^2 = z^2$ y más texto.

## Sección 2

$$
\\int_0^\\infty e^{-x^2} dx = \\frac{\\sqrt{\\pi}}{2}
$$

Lista:
- Item 1 con $\\alpha$
- Item 2

Código:
```python
def hello():
    print("world")
```

!!! info "Nota importante"
    Este es un callout de ejemplo.
"""

    blocks = to_blocks(sample_md)

    import json
    print(json.dumps(blocks, indent=2, ensure_ascii=False))
