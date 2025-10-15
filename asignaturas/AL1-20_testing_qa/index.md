# 🧱 AL1-20 · Proyecto I: Mini-pipeline + 6 átomos L0

> **Familia:** Proyecto Integral
> **Bloque:** L0 / CORE
> **Duración:** 30 capítulos (5 bloques × 6 temas)
> **Objetivo general:** ensamblar todo lo aprendido en un **pipeline reproducible** (build→test→artefactos) y entregar **6 "átomos" DSP L0** listos para integrarse como módulos, con UI básica, tests y telemetría mínima.

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

### 🧭 BLOQUE I · Plan y Arquitectura del Proyecto
Visión y alcance (M1), árbol de módulos, contratos y APIs, roadmap interno (3 sprints), métricas de salida, seguridad y privacidad.

### 🧪 BLOQUE II · 6 Átomos L0 (DSP Mínimo)
A1: Gain (lin/dB) con smoothing, A2: Pan estéreo + equal-power, A3: HPF/LPF 1º orden, A4: Biquad peaking (esqueleto), A5: Delay simple, A6: Soft clip (tanh).

### 🧰 BLOQUE III · Tooling, Tests y Observabilidad
CMake preset + monorepo, test unitarios (≥30), golden audio (≥5 casos), pluginval smoke (stub), telemetría L0, scripts CLI.

### 🎨 BLOQUE IV · UI/UX y Presets Básicos
tokens.json (light/dark), controles básicos, panel demo, UX de rangos/mapas, presets de demo (8), accesibilidad mínima.

### 🚀 BLOQUE V · Packaging, Release y Documentos
Artefactos `/dist`, release script, docs de uso, QA_REPORT.md, demo musical (≤60 s), retro y next steps.

---

## 🧾 Entregables del Curso

- 📂 Repositorio `al-mini-pipeline/` con alcore/, modules/atoms/ (A1–A6), ui/, tools/, tests/, dist/
- 🧪 ≥30 unit tests + ≥5 golden audio tests + pluginval smoke
- 🎨 UI con tokens.json, controles (Slider/Knob/Toggle) y panel demo con bindings
- 📦 8 presets demo (Clean Gain, HP Vocal, LP Warm, Mid Lift, Mono Bass, Slapback, Gentle Clip, Air Tilt)
- 📊 QA_REPORT.md con resultados de tests, CPU/latencia, pluginval logs
- 🎵 Demo musical (≤60 s) usando A1–A6 con proyecto y audio adjuntos
- 📄 QUICK_START.md + USER_GUIDE.md

---

## 🔗 Navegación

- [⬅️ Volver a Asignaturas](../)
- [➡️ Comenzar con Introducción](introduccion.md)
