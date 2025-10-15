# Introducción a AL1-02 · C++ Básico y STL

## ¿Por qué esta asignatura?

C++ es el lenguaje estándar de la industria de audio profesional. Esta asignatura te proporciona las habilidades fundamentales para:

- **Escribir** código C++ idiomático y seguro
- **Gestionar** memoria eficientemente con RAII
- **Utilizar** la STL para algoritmos y contenedores optimizados
- **Preparar** el terreno para desarrollo de plugins y motores de audio real-time

## Prerrequisitos

- Lógica y estructuras básicas (AL1-01 recomendado)
- Programación básica en cualquier lenguaje
- Familiaridad con línea de comandos

## Estructura del Curso

El curso se divide en **5 bloques temáticos** con **6 capítulos** cada uno:

### Bloque I: Sintaxis y Fundamentos C++ (Caps. 1-6)
Variables, tipos, operadores, control de flujo, funciones, namespaces, compilación básica.

### Bloque II: STL - Contenedores y Algoritmos (Caps. 7-12)
`std::vector`, `std::map`, `std::set`, iteradores, lambdas, algoritmos de `<algorithm>`.

### Bloque III: Gestión de Memoria y RAII (Caps. 13-18)
Punteros, referencias, `new`/`delete`, `std::unique_ptr`, `std::shared_ptr`, RAII pattern.

### Bloque IV: Orientación a Objetos Básica (Caps. 19-24)
Clases, constructores/destructores, métodos, encapsulación, herencia simple.

### Bloque V: Proyecto - Procesador de Audio Básico (Caps. 25-30)
Implementación de clase `AudioBuffer` con RAII, procesamiento con STL algorithms.

## Metodología

Cada capítulo incluye:

- **Teoría**: Conceptos de C++ con explicaciones claras
- **Ejemplos de código**: Código compilable y ejecutable
- **Best practices**: Convenciones y patrones idiomáticos
- **Micro-laboratorio**: Ejercicios prácticos de programación
- **Ejercicios**: Problemas con soluciones comentadas

## Herramientas

- **C++17** o superior
- **GCC/Clang/MSVC** como compiladores
- **CMake** para build system
- **GDB/LLDB** para depuración
- **Valgrind** y **AddressSanitizer** para análisis de memoria

## Tiempo Estimado

- **Teoría**: 40-50 horas
- **Prácticas y labs**: 25-35 horas
- **Proyecto final**: 10-15 horas
- **Total**: ~85 horas

## Evaluación

### Formativa (durante el curso)
- Checklists de autoevaluación en cada capítulo
- Ejercicios con soluciones para verificar comprensión
- Micro-laboratorios con código compilable

### Sumativa (final)
- Cuaderno con 40+ ejercicios C++ resueltos
- Implementación de clase RAII para gestión de recursos
- Proyecto: clase `AudioBuffer` con operaciones STL
- Análisis de memoria con sanitizers

## Próximos Pasos

1. [Ver estructura completa del programa](programa/)
2. [Explorar prácticas disponibles](practicas/)
3. Comenzar con Capítulo 1: Sintaxis Básica de C++

---

**Tiempo de inicio estimado:** 2-3 horas para configurar entorno y primeros conceptos
**Primera práctica recomendada:** Configuración de compilador y primer "Hello, Audio!"

¿Listo para empezar? Comienza con el Capítulo 1 en la sección [Programa](programa/)
