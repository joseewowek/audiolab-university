# Políticas de Validación para Contenido

Normas que deben cumplir todos los documentos creados o editados por agentes MCP en el repositorio AudioLab University.

## 1. Formato de Matemáticas

### Regla: Usar Delimitadores KaTeX Compatibles

**Obligatorio**:
- Inline: `$expresión$`
- Display: `$$expresión$$`

**Prohibido**:
- `\(expresión\)` (LaTeX puro, no compatible con nuestro setup)
- `\[expresión\]` (LaTeX puro, no compatible)

**Ejemplo correcto**:
```markdown
La frecuencia angular es $\omega = 2\pi f$.

$$
X(k) = \sum_{n=0}^{N-1} x[n] e^{-j2\pi kn/N}
$$
```

**Ejemplo incorrecto**:
```markdown
La frecuencia angular es \(\omega = 2\pi f\).  ❌

\[X(k) = ...\]  ❌
```

### Validación

Antes de crear PR, verificar que no existen instancias de `\(` o `\[` en el documento.

```bash
grep -n '\\(' archivo.md  # No debe retornar resultados
grep -n '\\[' archivo.md  # No debe retornar resultados
```

---

## 2. Estructura de Headings

### Regla: Jerarquía Estricta

- **H1** (`#`): Solo uno por archivo, título del capítulo/documento
- **H2** (`##`): Secciones principales
- **H3** (`###`): Subsecciones
- **H4** (`####`): Sub-subsecciones (usar con moderación)
- **H5+**: Evitar

**Ejemplo correcto**:
```markdown
# Capítulo 1: Vectores

## Definición

### Vector en R^n

### Operaciones Básicas

## Normas

### Norma L2
```

**Ejemplo incorrecto**:
```markdown
# Capítulo 1: Vectores

#### Definición  ❌ (saltar niveles)

## Normas

##### Norma L2  ❌ (H5 innecesario)
```

### Validación

Usar herramienta de linting Markdown:

```bash
markdownlint archivo.md
```

---

## 3. Enlaces

### Regla: Solo Enlaces Relativos para Contenido Interno

Para referencias a otros documentos del repositorio, usar rutas relativas desde `docs/`.

**Ejemplo correcto**:
```markdown
Ver [Capítulo 1](01_programa/AL1-04_algebra_calculo/cap01_vectores.md).

[Glosario](../../04_recursos/glosario.md)
```

**Ejemplo incorrecto**:
```markdown
Ver [Capítulo 1](https://audiolab-university.github.io/audiolab-university/01_programa/AL1-04_algebra_calculo/cap01_vectores/)  ❌
```

### Excepción

Enlaces a recursos externos (libros, papers, sitios web) deben ser absolutos:

```markdown
[NumPy Docs](https://numpy.org/doc/)  ✅
```

### Validación

Verificar que todos los links internos son relativos:

```bash
grep -E '\[.*\]\(https?://.*github.io.*\)' archivo.md  # No debe retornar resultados
```

---

## 4. Imágenes

### Regla: Almacenar Localmente

Todas las imágenes deben estar en el repositorio, no referenciadas desde URLs externas.

**Estructura de carpetas**:
```
docs/01_programa/AL1-04_algebra_calculo/
├── index.md
├── cap01_vectores.md
└── images/
    ├── vector_diagram.png
    └── projection_example.svg
```

**Ejemplo correcto**:
```markdown
![Diagrama de vector](images/vector_diagram.png)
```

**Ejemplo incorrecto**:
```markdown
![Diagrama](https://external-site.com/image.png)  ❌
```

### Excepción

Badges de servicios externos (CI status, version badges) son permitidos.

### Validación

```bash
grep -E '!\[.*\]\(https?://.*\)' archivo.md
# Revisar manualmente cada match (puede ser badge legítimo)
```

---

## 5. Longitud de Línea

### Regla: Máximo 120 Caracteres (Recomendado)

Para facilitar revisión en diffs de Git, mantener líneas de código/texto no mayores a ~120 caracteres.

**Excepción**: URLs largas y ecuaciones LaTeX complejas.

**Nota**: Esta es una guía, no un requerimiento estricto.

### Configuración en Editor

VSCode: Agregar a `.editorconfig`:
```ini
[*.md]
max_line_length = 120
```

---

## 6. Formato de Código

### Regla: Bloques de Código con Lenguaje Especificado

Siempre especificar el lenguaje del bloque de código para syntax highlighting.

**Ejemplo correcto**:
````markdown
```python
import numpy as np
x = np.array([1, 2, 3])
```
````

**Ejemplo incorrecto**:
````markdown
```
import numpy as np  ❌ (sin especificar lenguaje)
```
````

### Lenguajes Comunes

- `python`
- `bash`
- `javascript`
- `c++`
- `json`
- `yaml`

---

## 7. Front Matter YAML

### Regla: Front Matter en Capítulos y Prácticas

Todos los capítulos y prácticas deben incluir front matter YAML.

**Template capítulo**:
```yaml
---
title: "Título del Capítulo"
tags: ["algebra", "vectores", "fundamentos"]
status: "draft"  # draft | review | published
slug: "cap01-vectores"
author: "AudioLab Team"
date: "2025-10-15"
---
```

**Template práctica**:
```yaml
---
title: "Práctica: SigLab CLI"
tags: ["practica", "lab", "herramientas"]
status: "draft"
slug: "practica-siglab"
author: "AudioLab Team"
date: "2025-10-15"
tool: "siglab-cli"
difficulty: "principiante"
---
```

### Validación

Verificar que existe front matter:

```bash
head -10 archivo.md | grep -q '---'
```

---

## 8. Convenciones de Nomenclatura

### Archivos Markdown

- **Capítulos**: `cap01_nombre.md`, `cap02_nombre.md`
- **Prácticas**: `nombre_practica.md` (lowercase, guiones bajos)
- **Recursos**: `nombre_recurso.md`

### Slugs

- Lowercase
- Palabras separadas por guiones `-`
- Sin caracteres especiales ni tildes

**Ejemplo**: `cap01-vectores`, `practica-fftview`

---

## 9. Validación Pre-Commit

### Checklist Manual

Antes de crear PR, verificar:

- [ ] Matemáticas usan `$...$` y `$$...$$`
- [ ] Headings siguen jerarquía H1 → H2 → H3
- [ ] Enlaces internos son relativos
- [ ] Imágenes locales en carpeta `images/`
- [ ] Bloques de código especifican lenguaje
- [ ] Front matter YAML presente (si aplica)
- [ ] Sin trailing whitespace
- [ ] Build de MkDocs exitoso localmente

### Script de Validación

Ejecutar antes de commit:

```bash
# Verificar build
mkdocs build --strict

# Verificar matemáticas LaTeX incorrectas
find docs -name "*.md" -exec grep -l '\\(' {} \;

# Verificar enlaces absolutos internos
find docs -name "*.md" -exec grep -l 'github.io/audiolab-university' {} \;
```

Si alguno retorna resultados, corregir antes de proceder.

---

## 10. Estilo de Escritura

### Tono

- Técnico pero accesible
- Evitar jerga innecesaria
- Definir términos especializados en primera mención

### Estructura

- **Introducción**: Contexto y motivación
- **Desarrollo**: Teoría con ejemplos
- **Práctica**: Código ejecutable
- **Ejercicios**: Verificación de comprensión

### Ejemplos

Siempre incluir ejemplos numéricos concretos después de fórmulas abstractas.

**Mal**:
```markdown
La norma L2 es $\|\vec{x}\|_2 = \sqrt{\sum x_i^2}$.
```

**Bien**:
```markdown
La norma L2 es $\|\vec{x}\|_2 = \sqrt{\sum x_i^2}$.

**Ejemplo**: Para $\vec{x} = [3, 4]$:

$$
\|\vec{x}\|_2 = \sqrt{3^2 + 4^2} = \sqrt{25} = 5
$$
```

---

## 11. Referencias Cruzadas

### Regla: Proveer Contexto

Al referenciar otros capítulos, proveer contexto breve.

**Mal**:
```markdown
Ver capítulo 1.
```

**Bien**:
```markdown
Ver [Capítulo 1: Vectores](cap01_vectores.md) para repaso de producto escalar.
```

---

## 12. Commits y PRs

### Formato de Commit

```
tipo(scope): descripción corta

Descripción extendida opcional.
```

**Tipos**:
- `feat`: Nueva feature (capítulo, práctica)
- `fix`: Corrección de error
- `docs`: Cambio en documentación
- `style`: Formato, typos (sin cambio de contenido)
- `refactor`: Reorganización sin cambio de contenido

**Ejemplos**:
```
feat(chapter): añadir cap03 transformadas
fix(math): corregir fórmula de DFT en cap02
docs(readme): actualizar instrucciones de instalación
```

### PRs

**Título**: Formato similar a commit

**Cuerpo**: Incluir:
- Descripción de cambios
- Checklist de validación completada
- Screenshots (si cambios visuales)

---

## Resumen: Validación Rápida

```bash
# 1. Build estricto
mkdocs build --strict

# 2. Matemáticas
grep -r '\\(' docs/  # Debe estar vacío

# 3. Headings (revisar manualmente estructura)

# 4. Enlaces internos absolutos
grep -r 'github.io/audiolab-university' docs/  # Debe estar vacío

# 5. Bloques de código sin lenguaje
grep -Pzo '```\n[^`]' docs/**/*.md  # Debe estar vacío

# 6. Trailing whitespace
git diff --check

# Todo OK → Crear PR
```

---

**Última actualización**: 2025-10-15
**Próxima revisión**: Q2 2025

Para sugerencias sobre estas políticas, abrir issue con label `policy`.
