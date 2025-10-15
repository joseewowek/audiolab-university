# 🎛️ AL1-12 · Synthesis I (osciladores, envolventes)

> **Familia:** Síntesis
> **Bloque:** L0 / CORE
> **Duración:** 30 capítulos (5 bloques × 6 temas)
> **Objetivo general:** construir un **sinte minimal** offline (render a WAV) con **osciladores básicos**, **ADSR**, **LFO**, mezcla simple y **presets iniciales**, listo para integrarse con `ALCore` y el sistema de parámetros.

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

### 🧭 BLOQUE I · Bases de Síntesis Subtractiva
Arquitecturas clásicas (VCO→VCF→VCA), osciladores básicos, afinación nota↔frecuencia, amplitud y dBFS.

### 🧪 BLOQUE II · Osciladores Numéricos (L0)
Fase acumulativa, seno eficiente, saw/square ingenuas, triangle, anti-click, anti-aliasing básico (polyBLEP preview).

### 🧷 BLOQUE III · Envolventes y Modulación
ADSR mínimo, curvas lin/exp, gate y note on/off, LFO, rutas de modulación, smoothing de parámetros.

### 🎚️ BLOQUE IV · Voz, Polifonía y Render
Objeto Voz, asignación de 8 voces, portamento (glide), unison/detune (esqueleto), render offline a WAV, presets iniciales.

### 🚀 BLOQUE V · Proyecto y Validación
Blueprint del sinte, integración con ALCore, tests de tiempo y clicks, métricas de aliasing, export y preset bank v0, demo musical.

---

## 🧾 Entregables del Curso

- 📦 `/synth/minimal/` con osciladores (Sine/Saw/Square/Tri), ADSR, LFO, Voice (8 voces), mezclador y WAV render
- 🎛️ Parámetros via `Parameter` de ALCore: oscMix, gain, attack, decay, sustain, release, lfoRate, lfoDepth, glide, unisonDetune
- 🗂️ `/presets/` con 6 presets iniciales (JSON/YAML) + audio de referencia
- 🧪 Tests: click test, pitch stability, alias probe
- 📄 `SYNTH_README.md` con arquitectura y cómo renderizar la demo

---

## 🔗 Navegación

- [⬅️ Volver a Asignaturas](../)
- [➡️ Comenzar con Introducción](introduccion.md)
