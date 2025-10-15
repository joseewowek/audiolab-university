# Introducción a AL1-19 · _BRAIN I (IA básica para ingenieros)

## ¿Por qué esta asignatura?

La IA práctica puede acelerar desarrollo y mejorar productos de audio. Esta asignatura te proporciona:

- **Features** de audio (MFCC, espectrales básicas)
- **Modelos** pequeños on-device (kNN, SVM, MLP mini)
- **Evaluación** rigurosa (métricas, latencia, CPU%)
- **Copilotos** que automatizan tareas repetitivas

## Prerrequisitos

- Python para Automatización (AL1-03)
- Conceptos de señales y sistemas (AL1-05 deseable)
- C++ Básico (AL1-02) para integración
- Matemáticas básicas (probabilidad, álgebra lineal nivel introductorio)

## Estructura del Curso

### Bloque I: Fundamentos Prácticos de ML (Caps. 1-6)
Qué puede (y no) la IA en audio, pipeline ML minimal, datasets y splits, métricas esenciales, overfitting vs bias, ética y privacidad.

### Bloque II: Features de Audio L0 (Caps. 7-12)
Ventaneo y STFT, MFCC y variantes, espectrales básicas, energía/RMS y dinámica, agregación temporal, paquetes y formatos.

### Bloque III: Modelos Pequeños y Despliegue (Caps. 13-18)
Modelos clásicos (kNN, SVM, Logistic, RF), MLP mini y tiny convs, serialización y portabilidad, cuantización (visión), inference budget, integración C++.

### Bloque IV: Copilotos, Prompts y Automation (Caps. 19-24)
Copiloto para ingeniería, prompt engineering L0, agentes simples, evaluación de salidas LLM, IA + QA, riesgos y guardrails.

### Bloque V: Proyectos BRAIN L0 (Caps. 25-30)
VAD (detector de voz) mini, tagger de presets, recomendador de presets, inference wrapper C++, copiloto de release notes, evaluación y model card.

## Tiempo Estimado

- **Teoría**: 35-45 horas
- **Prácticas**: 30-40 horas
- **Proyecto**: 15-20 horas
- **Total**: ~90 horas

## Evaluación

### Sumativa
- `/brain/` con features/, models/, inference/BrainBridge
- Eval: EVAL.md con métricas (F1/AUROC), latencia, CPU%
- Golden sets pequeños + scripts de scoring
- Copiloto: prompts/, release_notes_gen.py
- `MODEL_CARD.md` por modelo

---

¿Listo para empezar? Comienza con el Capítulo 1 en la sección [Programa](programa/)
