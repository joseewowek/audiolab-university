# Introducción a AL1-09 · Núcleo CORE

## ¿Por qué esta asignatura?

El núcleo de un motor de audio es su componente más crítico. Esta asignatura te proporciona:

- **Conocimiento** de arquitecturas de motores de audio profesionales
- **Habilidad** para diseñar sistemas de procesamiento real-time
- **Comprensión** de gestión de hilos y estructuras lock-free
- **Experiencia** construyendo infraestructura tipo JUCE/iPlug2

## Prerrequisitos

- C++ Básico y STL (AL1-02 recomendado)
- Lógica y estructuras de datos (AL1-01 recomendado)
- Conceptos de señales y sistemas (deseable)
- Familiaridad con CMake y Git (AL1-08 deseable)

## Estructura del Curso

El curso se divide en **5 bloques temáticos** con **6 capítulos** cada uno:

### Bloque I: Diseño de AudioBuffer y Gestión de Memoria (Caps. 1-6)
Buffers circulares, interleaved/deinterleaved, memory alignment, estructuras SIMD-ready.

### Bloque II: AudioEngine y Callback Real-Time (Caps. 7-12)
Audio callback, latencia, buffer size, sample rate, sincronización con hardware.

### Bloque III: ProcessingNode y Graph de Audio (Caps. 13-18)
Arquitectura de grafo de procesamiento, nodos, conexiones, topological sort.

### Bloque IV: PluginHost y Extensibilidad (Caps. 19-24)
Sistema de plugins, carga dinámica de librerías (dlopen/LoadLibrary), hot-reloading.

### Bloque V: Proyecto - Motor de Audio Básico (Caps. 25-30)
Implementar `AudioEngine` completo con grafo de nodos, cargar plugins, procesar audio real-time.

## Metodología

Cada capítulo incluye:

- **Teoría**: Arquitectura de sistemas de audio con patrones de diseño
- **Ejemplos de código**: Implementaciones profesionales comentadas
- **Análisis de latencia**: Mediciones y optimizaciones
- **Micro-laboratorio**: Construcción incremental del motor
- **Ejercicios**: Problemas de diseño y optimización

## Herramientas

- **C++17** o superior
- **CMake** para build multiplataforma
- **RtAudio** o **PortAudio** para I/O de audio
- **GDB/LLDB** para depuración real-time
- **Valgrind**, **Helgrind** para análisis de concurrencia
- **Tracy** o **Superluminal** para profiling (opcional)

## Tiempo Estimado

- **Teoría**: 50-60 horas
- **Prácticas y labs**: 35-45 horas
- **Proyecto final**: 20-30 horas
- **Total**: ~110 horas

## Evaluación

### Formativa (durante el curso)
- Checklists de autoevaluación en cada capítulo
- Ejercicios con mediciones de latencia
- Implementaciones incrementales verificables

### Sumativa (final)
- Cuaderno con 40+ ejercicios de arquitectura resueltos
- Implementación completa de `AudioBuffer` y `AudioEngine`
- Sistema de plugins con carga dinámica funcional
- Informe técnico con análisis de latencia y performance

## Próximos Pasos

1. [Ver estructura completa del programa](programa/)
2. [Instalar RtAudio/PortAudio](practicas/)
3. Comenzar con Capítulo 1: Diseño de AudioBuffer

---

**Tiempo de inicio estimado:** 3-4 horas para configurar entorno y primeros conceptos
**Primera práctica recomendada:** Implementación de buffer circular básico

¿Listo para empezar? Comienza con el Capítulo 1 en la sección [Programa](programa/)
