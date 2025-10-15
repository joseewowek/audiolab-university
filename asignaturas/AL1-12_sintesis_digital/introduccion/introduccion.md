# Introducción a AL1-12 · Synthesis I (osciladores, envolventes)

## ¿Por qué esta asignatura?

La síntesis de audio es fundamental para crear instrumentos virtuales y efectos generativos. Esta asignatura te proporciona:

- **Fundamentos** de síntesis subtractiva (VCO→VCF→VCA)
- **Osciladores** numéricos eficientes y estables
- **Envolventes** ADSR y LFO para modulación
- **Arquitectura** de voces y polifonía básica

## Prerrequisitos

- Álgebra y cálculo para DSP (AL1-04 recomendado)
- C++ Básico y STL (AL1-02 recomendado)
- Conceptos de señales y sistemas (AL1-05 deseable)

## Estructura del Curso

### Bloque I: Bases de Síntesis Subtractiva (Caps. 1-6)
Arquitecturas clásicas, osciladores básicos (seno/saw/square), afinación nota↔frecuencia, amplitud y dBFS.

### Bloque II: Osciladores Numéricos L0 (Caps. 7-12)
Fase acumulativa, seno eficiente, saw/square ingenuas, triangle, anti-click, anti-aliasing básico (polyBLEP preview).

### Bloque III: Envolventes y Modulación (Caps. 13-18)
ADSR mínimo, curvas lin/exp, gate y note on/off, LFO, rutas de modulación L0, smoothing de parámetros.

### Bloque IV: Voz, Polifonía y Render (Caps. 19-24)
Objeto Voz, asignación de 8 voces, portamento (glide), unison/detune (esqueleto), render offline a WAV, presets iniciales.

### Bloque V: Proyecto y Validación (Caps. 25-30)
Blueprint del sinte, integración con ALCore, tests de clicks, métricas de aliasing, export y preset bank v0, demo musical.

## Metodología

Cada capítulo incluye:

- **Teoría**: Fundamentos de síntesis digital
- **Ejemplos de código**: Implementaciones C++ funcionales
- **Audio samples**: Archivos de referencia
- **Micro-laboratorio**: Construcción incremental del sintetizador
- **Ejercicios**: Diseño de patches y presets

## Herramientas

- **C++17** o superior
- **Python/NumPy** para prototipado
- **DAW** para escuchar resultados
- **Audacity** para análisis espectral

## Tiempo Estimado

- **Teoría**: 40-50 horas
- **Prácticas e implementación**: 30-40 horas
- **Proyecto final**: 15-20 horas
- **Total**: ~95 horas

## Evaluación

### Formativa
- Checklists de autoevaluación
- Implementaciones incrementales verificables
- Listening tests de cada oscilador

### Sumativa
- `/synth/minimal/` con osciladores, ADSR, LFO, Voice (8 voces)
- Parámetros via `Parameter` de ALCore
- 6 presets iniciales con audio de referencia
- Tests: click test, pitch stability, alias probe
- Demo musical renderizada

## Próximos Pasos

1. [Ver estructura completa del programa](programa/)
2. [Explorar presets de ejemplo](recursos/)
3. Comenzar con Capítulo 1: Arquitecturas Clásicas

---

¿Listo para empezar? Comienza con el Capítulo 1 en la sección [Programa](programa/)
