# 📚 AL1-18 · Research Literacy I (leer specs/papers)

> **Familia:** Innovación/Research
> **Bloque:** L0 / CORE
> **Duración:** 30 capítulos (5 bloques × 6 temas)
> **Objetivo general:** adquirir **alfabetización técnica** para leer **especificaciones**, **papers** y **patentes**; extraer conocimiento aplicable y **replicarlo** en código/pruebas.

---

## 📚 Contenido de la Asignatura

### [📖 Introducción](introduccion.md)
Visión general, prerrequisitos y estructura del curso.

### [📝 Programa](programa/)
Contenido teórico organizado en capítulos.

### [⚙️ Prácticas](practicas/)
Laboratorios y ejercicios aplicados.

### [📓 Notebooks](notebooks/)
Jupyter notebooks interactivos.

### [📚 Recursos](recursos/)
Material complementario y referencias.

---

## 🎯 Bloques Temáticos

### 🧭 BLOQUE I · Metodología de Lectura Técnica
Dónde buscar y cómo filtrar, tipos de documentos, estrategia de lectura en 3 pasadas, identificar hipótesis y contribuciones, extraer definiciones, replicabilidad.

### 📑 BLOQUE II · Leer Especificaciones (Specs/RFCs)
Anatomía de una spec, extraer requisitos verificables, diagramas y tablas → código, compliance y tolerancias, change logs y errata, documentar decisiones (ADR).

### 📰 BLOQUE III · Papeles Científicos (DSP/ML/Acústica)
Estructura IMRaD, leer ecuaciones sin perderse, figuras y métricas, pseudocódigo → prototipo, comparativas justas, negative results y límites.

### 🧠 BLOQUE IV · Patentes y Propiedad Intelectual (Visión)
Qué protege una patente, leer claims y embodiments, Freedom to Operate (FTO) básico, design-around conceptual, licencias standards-essential, ética y responsible research.

### 🚀 BLOQUE V · Del Papel al Prototipo Reproducible
Plantilla de research brief, Reference Implementation (RI) mínima, experiment card y trazabilidad, validación cruzada y golden data, tech transfer a módulos, informe y next steps.

---

## 🧾 Entregables del Curso

- 📁 `/research/` con RESEARCH_BRIEF.md (≥2), GLOSSARY.md con notación → código, ADR_* (≥1)
- 🧪 `/research/ri/` con Reference Implementation (notebook/CLI) que replique 1 figura/resultado
- 📊 config.yaml con parámetros + seed y results.json con métricas
- 🎧 Golden data (CSV/WAV/PNG) y script de verificación con tolerancias
- 📄 `FTO_NOTE.md` (1 pág) con resumen de patentes cercanas
- 🗂️ Plantilla de experiment card y checklist de reproducibilidad

---

## 🔗 Navegación

- [⬅️ Volver a Asignaturas](../)
- [➡️ Comenzar con Introducción](introduccion.md)
