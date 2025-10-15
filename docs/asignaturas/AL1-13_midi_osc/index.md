# 🧪 AL1-13 · Testing I (unit + pluginval básico)

> **Familia:** Testing/QA
> **Bloque:** L0 / CORE
> **Duración:** 30 capítulos (5 bloques × 6 temas)
> **Objetivo general:** instaurar **cultura de pruebas** desde el día 1: unit tests C++/Python, **golden tests de audio**, **pluginval (smoke)**, y CI mínima para que "si no se prueba, no existe".

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

### 🧭 BLOQUE I · Fundamentos de Calidad
Filosofía de testing en audio, Definition of Done, determinismo y semillas, estructura de un test, dobles de prueba, reproducibilidad.

### 🧩 BLOQUE II · Unit Tests en C++ y Python
Frameworks (Catch2/GoogleTest), pruebas de utilidades numéricas, AudioBuffer, parámetros y smoothing, pytest, cobertura básica.

### 🎧 BLOQUE III · Golden Audio & Métricas Objetivas
Golden files, tolerancias para audio, null tests, métricas RMS/peak/crest, curvas de respuesta, detección de clicks.

### 🖥️ BLOQUE IV · Pluginval (Smoke) + CI Esqueleto
Qué es pluginval, caso smoke mínimo, test de parámetros, integración con CI, logs y artefactos de fallo, matrices de plataforma.

### 🚀 BLOQUE V · Proyecto QA L0
Arquetipo `/tests/`, suite unit minimal (≥20 tests), suite golden (≥3 casos), job CI build+unit+golden, job pluginval-smoke, playbook de fallos.

---

## 🧾 Entregables del Curso

- 📂 `/tests/` con unit C++ (Catch2/GTest) y pytest — ≥20 casos
- 🎧 Golden audio: WAV/CSV + driver de comparación con tolerancias
- 🔍 Null tests para gain/bypass (residuo ≤ −80 dBFS)
- ⚙️ CI básico (YAML): build+unit+golden + pluginval-smoke
- 📄 `QA_GUIDE.md` con cómo escribir tests y regenerar goldens
- 🧰 Plantillas de caso de prueba y scripts para goldens

---

## 🔗 Navegación

- [⬅️ Volver a Asignaturas](../)
- [➡️ Comenzar con Introducción](introduccion.md)
