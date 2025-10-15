# AL1-04: Álgebra y Cálculo para DSP

Módulo fundacional que introduce álgebra lineal y cálculo aplicado a procesamiento digital de señales de audio.

## Descripción General

Este bloque cubre los fundamentos matemáticos necesarios para entender y diseñar sistemas de procesamiento de audio:

- Representación vectorial de señales
- Operaciones matriciales para transformaciones
- Espacios lineales y proyecciones
- Cálculo diferencial e integral aplicado

## Contenidos

### Capítulo 1: Vectores

Representación de señales como vectores, operaciones básicas, normas, producto escalar y proyecciones.

[Ir al Capítulo 1](cap01_vectores.md)

**Conceptos clave:**
- Vector como secuencia de muestras
- Norma L2 y RMS
- Producto punto y correlación
- Proyección ortogonal

### Capítulo 2: Matrices

Transformaciones lineales, sistemas Mid/Side, determinantes e inversas.

[Ir al Capítulo 2](cap02_matrices.md)

**Conceptos clave:**
- Matriz 2×2 para M/S encoding
- Determinante e invertibilidad
- Matriz 3×3 para sistemas multicanal
- Aplicaciones en mezcla

## Objetivos de Aprendizaje

Al completar este módulo serás capaz de:

1. Representar señales de audio como vectores y aplicar operaciones algebraicas
2. Calcular métricas de señal (RMS, energía, correlación)
3. Implementar transformaciones matriciales (M/S, rotaciones)
4. Resolver sistemas lineales relacionados con routing de audio
5. Usar notación matemática precisa para documentar diseños

## Prerrequisitos

- Álgebra básica (ecuaciones, exponentes)
- Trigonometría elemental (seno, coseno)
- Familiaridad con Python (deseable)

## Herramientas

Para las prácticas usaremos:

- **Python 3.10+** con NumPy
- **SigLab CLI** para visualización rápida
- **Jupyter** para experimentación

Ver [guía de instalación de SigLab](../../02_practicas/siglab_cli.md).

## Secuencia Recomendada

```mermaid
graph LR
    A[Cap 1: Vectores] --> B[Micro-lab: RMS de señal]
    B --> C[Cap 2: Matrices]
    C --> D[Micro-lab: M/S encoding]
    D --> E[Ejercicios integradores]
```

## Tiempo Estimado

- **Teoría**: 6-8 horas
- **Micro-labs**: 3-4 horas
- **Ejercicios**: 4-6 horas
- **Total**: ~15 horas

## Evaluación

Cada capítulo incluye:

- Checklist de conceptos (autoevaluación)
- Ejercicios con soluciones
- Micro-laboratorio práctico

Se recomienda completar todos los ejercicios antes de avanzar al siguiente módulo.

## Recursos Adicionales

- [Bibliografía](../../04_recursos/bibliografia.md) - Textos de referencia
- [Glosario](../../04_recursos/glosario.md) - Términos técnicos

## Próximo Módulo

AL5-08: **Análisis de Fourier y Representación Frecuencial** (próximamente)

---

**Inicio del contenido**: [Capítulo 1 - Vectores](cap01_vectores.md)
