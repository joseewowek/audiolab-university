# Introducción a AL1-20 · Proyecto I: Mini-pipeline + 6 átomos L0

## ¿Por qué esta asignatura?

Este proyecto integrador consolida todo lo aprendido en el año 1. Te permite:

- **Ensamblar** un pipeline reproducible completo
- **Implementar** 6 átomos DSP fundamentales
- **Integrar** UI, tests y telemetría
- **Entregar** un producto funcional y documentado

## Prerrequisitos

**TODAS las asignaturas AL1-01 a AL1-19** o conocimientos equivalentes:

- Programación (C++, Python)
- DSP básico (señales, sistemas, filtros)
- Arquitectura (Core, módulos, parámetros)
- Testing y QA
- UI/UX básica
- Gestión de proyectos

## Estructura del Curso

### Bloque I: Plan y Arquitectura del Proyecto (Caps. 1-6)
Visión y alcance (M1), árbol de módulos, contratos y APIs, roadmap interno (3 sprints), métricas de salida, seguridad y privacidad.

### Bloque II: 6 Átomos L0 - DSP Mínimo (Caps. 7-12)
A1: Gain (lin/dB) con smoothing, A2: Pan estéreo + equal-power, A3: HPF/LPF 1º orden, A4: Biquad peaking, A5: Delay simple, A6: Soft clip (tanh).

### Bloque III: Tooling, Tests y Observabilidad (Caps. 13-18)
CMake preset + monorepo, test unitarios (≥30), golden audio (≥5 casos), pluginval smoke, telemetría L0, scripts CLI.

### Bloque IV: UI/UX y Presets Básicos (Caps. 19-24)
tokens.json (light/dark), controles básicos, panel demo, UX de rangos/mapas, presets de demo (8), accesibilidad mínima.

### Bloque V: Packaging, Release y Documentos (Caps. 25-30)
Artefactos `/dist`, release script, docs de uso, QA_REPORT.md, demo musical (≤60 s), retro y next steps.

## Metodología

Este es un **proyecto práctico intensivo**:

- **Sprints semanales** con entregas incrementales
- **Revisiones de código** entre pares
- **Tests continuos** con CI
- **Demo funcional** al final de cada sprint

## Tiempo Estimado

- **Planificación**: 10-15 horas
- **Implementación**: 80-100 horas
- **Testing y QA**: 20-30 horas
- **Documentación y release**: 10-15 horas
- **Total**: ~130 horas

## Evaluación

### Sumativa (Proyecto Completo)

- 📂 Repositorio `al-mini-pipeline/` con:
  - `alcore/` (buffers, parámetros, eventos)
  - `modules/atoms/` → A1–A6 implementados
  - `ui/` → tokens.json, components/, panel demo
  - `tools/` → CLIs (siggen, fftview, batchnorm, labreport)
  - `tests/` → ≥30 unit + ≥5 golden + pluginval smoke
  - `dist/` → artefactos empaquetados

- 🎨 UI funcional con bindings a parámetros
- 📦 8 presets demo profesionales
- 📊 `QA_REPORT.md` completo
- 🎵 Demo musical (≤60 s) renderizada
- 📄 Documentación de usuario y desarrollador

## Próximos Pasos

1. [Revisar plan detallado del proyecto](programa/)
2. [Configurar entorno de desarrollo](practicas/)
3. Comenzar con Sprint 1: Core + A1-A2

---

**Este es el proyecto culminante del Año 1.** Integra todo lo aprendido en un entregable profesional.

¿Listo para empezar? Comienza con el Capítulo 1: Visión y Alcance en la sección [Programa](programa/)
