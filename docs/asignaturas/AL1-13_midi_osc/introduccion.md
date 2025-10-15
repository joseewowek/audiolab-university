# Introducción a AL1-13 · Testing I (unit + pluginval básico)

## ¿Por qué esta asignatura?

El testing es la diferencia entre código que funciona hoy y código que funciona siempre. Esta asignatura te proporciona:

- **Cultura** de testing desde el día 1
- **Unit tests** en C++ y Python
- **Golden tests** de audio con tolerancias adecuadas
- **CI mínima** con pluginval para validación automatizada

## Prerrequisitos

- C++ Básico y STL (AL1-02 recomendado)
- Python para Automatización (AL1-03 recomendado)
- Familiaridad con Git y CI/CD básico

## Estructura del Curso

### Bloque I: Fundamentos de Calidad (Caps. 1-6)
Filosofía de testing, Definition of Done, determinismo y semillas, estructura de un test, dobles de prueba, reproducibilidad.

### Bloque II: Unit Tests en C++ y Python (Caps. 7-12)
Frameworks (Catch2/GoogleTest), pruebas de utilidades, AudioBuffer, parámetros y smoothing, pytest, cobertura básica.

### Bloque III: Golden Audio & Métricas Objetivas (Caps. 13-18)
Golden files, tolerancias para audio, null tests, métricas RMS/peak/crest, curvas de respuesta, detección de clicks.

### Bloque IV: Pluginval (Smoke) + CI Esqueleto (Caps. 19-24)
Qué es pluginval, caso smoke mínimo, test de parámetros, integración con CI, logs y artefactos, matrices de plataforma.

### Bloque V: Proyecto QA L0 (Caps. 25-30)
Arquetipo `/tests/`, suite unit (≥20 tests), suite golden (≥3 casos), jobs CI, playbook de fallos.

## Metodología

- **Teoría**: Principios de testing y QA
- **Ejemplos**: Tests reales de proyectos audio
- **Micro-laboratorio**: Escribir y ejecutar tests
- **Ejercicios**: Detectar y corregir bugs con tests

## Herramientas

- **Catch2** o **GoogleTest** (C++)
- **pytest** (Python)
- **pluginval**
- **GitHub Actions** o **GitLab CI**

## Tiempo Estimado

- **Teoría**: 30-40 horas
- **Prácticas**: 30-40 horas
- **Proyecto**: 15-20 horas
- **Total**: ~85 horas

## Evaluación

### Sumativa
- `/tests/` con ≥20 unit tests (C++/Python)
- Golden audio con tolerancias definidas
- Null tests (≤ −80 dBFS)
- CI básico funcionando
- `QA_GUIDE.md`

---

¿Listo para empezar? Comienza con el Capítulo 1 en la sección [Programa](programa/)
