# Introducción a AL1-11 · UI/UX I (fundamentos, tokens)

## ¿Por qué esta asignatura?

La interfaz de usuario es el único contacto que el usuario tiene con tu motor de audio. Esta asignatura te proporciona:

- **Lenguaje visual** consistente con design tokens portables
- **Componentes** reutilizables y accesibles para plugins
- **Bindings** eficientes entre UI y parámetros DSP
- **Rendimiento** fluido sin bloquear el audio-thread

## Prerrequisitos

- Programación básica (C++ o similar)
- Conceptos de parámetros de audio (deseable)
- Familiaridad con JSON/YAML
- Nociones de accesibilidad web (opcional)

## Estructura del Curso

El curso se divide en **5 bloques temáticos** con **6 capítulos** cada uno:

### Bloque I: Fundamentos de Diseño y Accesibilidad (Caps. 1-6)
Principios UX para audio, jerarquía visual, grid, tipografía, color semántico, accesibilidad AA mínima.

### Bloque II: Design Tokens y Sistema de Estilos (Caps. 7-12)
Qué es un design token, estructura JSON/YAML, tipografía, espaciado, estados y elevación, iconografía.

### Bloque III: Componentes Básicos para Plugins (Caps. 13-18)
Botón/toggle, slider continuo y stepped, knob (rotary), selector, número y campos, indicadores (meter/scope/spectrum stub).

### Bloque IV: Bindings, Estados y Rendimiento (Caps. 19-24)
Modelo de binding parámetro↔control, normalización y formatos, estados de componente, animación sin coste, thread-safety, tests visuales.

### Bloque V: Proyecto - Mini Design System (L0) (Caps. 25-30)
Definir tokens.json, kit de componentes L0, panel base del plugin, binding con parámetros reales, meters básicos, revisión AA + empaquetado.

## Metodología

Cada capítulo incluye:

- **Teoría**: Principios de diseño con enfoque práctico
- **Ejemplos visuales**: Mockups y componentes reales
- **Aplicación a audio**: Controles específicos para DSP
- **Micro-laboratorio**: Implementación de componentes
- **Ejercicios**: Diseño y prototipado de UI

## Herramientas

- **Figma** o **Sketch** para diseño (opcional)
- **JSON/YAML** para tokens
- **C++** (JUCE/Qt) o **Web** (React/Vue) para implementación
- **Accessibility checkers** (WAVE, axe DevTools)

## Tiempo Estimado

- **Teoría**: 30-40 horas
- **Prácticas y diseño**: 25-35 horas
- **Proyecto final**: 15-20 horas
- **Total**: ~80 horas

## Evaluación

### Formativa (durante el curso)
- Checklists de autoevaluación en cada capítulo
- Ejercicios de diseño con feedback visual
- Prototipos funcionales de componentes

### Sumativa (final)
- `/ui/tokens.json` completo con themes claro/oscuro
- Kit de componentes (Button, Toggle, Slider, Knob, ValueField)
- Panel demo con bindings a 3 parámetros
- Tests visuales (golden snapshots) y checklist AA
- `UI_GUIDE.md` con pautas de uso

## Próximos Pasos

1. [Ver estructura completa del programa](programa/)
2. [Explorar ejemplos de componentes](practicas/)
3. Comenzar con Capítulo 1: Principios de UX para Audio

---

**Tiempo de inicio estimado:** 2-3 horas para conceptos fundamentales
**Primera práctica recomendada:** Análisis de UI de plugins profesionales

¿Listo para empezar? Comienza con el Capítulo 1 en la sección [Programa](programa/)
