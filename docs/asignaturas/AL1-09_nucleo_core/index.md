# ⚙️ AL1-09 · Núcleo CORE I

> **Familia:** Arquitectura
> **Bloque:** L0 / CORE
> **Duración:** 30 capítulos (5 bloques × 6 temas)
> **Objetivo general:** diseñar y construir el núcleo C++ del motor de audio: `AudioBuffer`, `AudioEngine`, `ProcessingNode`, `PluginHost`, gestión de hilos, lock-free structures, y arquitectura extensible tipo JUCE/iPlug2.

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

### 🧱 BLOQUE I · Diseño de AudioBuffer y Gestión de Memoria
Buffers circulares, interleaved/deinterleaved, alignment, SIMD-ready structures.

### 🔊 BLOQUE II · AudioEngine y Callback Real-Time
Audio callback, latencia, buffer size, sample rate, sincronización con hardware.

### 🔗 BLOQUE III · ProcessingNode y Graph de Audio
Arquitectura de grafo de procesamiento, nodos, conexiones, topological sort.

### 🔌 BLOQUE IV · PluginHost y Extensibilidad
Sistema de plugins, carga dinámica de librerías, interfaz común, hot-reloading.

### 🚀 BLOQUE V · Proyecto: Motor de Audio Básico
Implementar `AudioEngine` con grafo de nodos, cargar plugins, procesar audio en tiempo real.

---

## 🧾 Entregables del Curso

- 📒 Cuaderno con 40+ ejercicios de arquitectura resueltos
- 💻 Implementación de `AudioBuffer` y `AudioEngine`
- 🔌 Sistema de plugins con carga dinámica
- 📊 Informe de análisis de latencia y performance

---

## 🔗 Navegación

- [⬅️ Volver a Asignaturas](../)
- [➡️ Comenzar con Introducción](introduccion.md)
