# 🧠 AL1-19 · _BRAIN I (IA básica para ingenieros)

> **Familia:** ML/Audio (BRAIN)
> **Bloque:** L0 / CORE
> **Duración:** 30 capítulos (5 bloques × 6 temas)
> **Objetivo general:** incorporar **IA práctica y ligera** al ecosistema AudioLab: **features de audio**, **modelos pequeñitos (on-device)**, **evaluación rigurosa**, y **copilotos** que aceleran ingeniería sin romper RT ni privacidad.

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

### 🧭 BLOQUE I · Fundamentos Prácticos de ML
Qué puede (y no) la IA en audio, pipeline ML minimal, datasets y splits, métricas esenciales, overfitting vs bias, ética y privacidad.

### 🎧 BLOQUE II · Features de Audio (L0)
Ventaneo y STFT, MFCC y variantes, espectrales básicas, energía/RMS y dinámica, agregación temporal, paquetes y formatos.

### 🧠 BLOQUE III · Modelos Pequeños y Despliegue
Modelos clásicos (kNN, SVM, Logistic, RF), MLP mini y tiny convs, serialización y portabilidad, cuantización y pruning (visión), inference budget, integración C++.

### 🤖 BLOQUE IV · Copilotos, Prompts y Automation
Copiloto para ingeniería, prompt engineering L0, agentes simples, evaluación de salidas LLM, IA + QA, riesgos y guardrails.

### 🚀 BLOQUE V · Proyectos BRAIN L0
VAD (detector de voz) mini, tagger de presets, recomendador de presets, inference wrapper C++, copiloto de release notes, evaluación y model card.

---

## 🧾 Entregables del Curso

- 📁 `/brain/` con features/ (extractor STFT/MFCC), models/ (vad_model.onnx, preset_tagger.json, preset_knn.pkl), inference/BrainBridge (wrapper RT)
- 🧪 Eval: EVAL.md con métricas (F1/AUROC o top-k accuracy), latencia media/p95 y CPU%
- 🎧 Golden sets pequeños (`/eval/audio_*`) y scripts de scoring
- 🧰 Copiloto: prompts/ (spec→tests→impl→docs), release_notes_gen.py
- 📄 `MODEL_CARD.md` por modelo con datos, uso previsto, límites, sesgos y contacto

---

## 🔗 Navegación

- [⬅️ Volver a Asignaturas](../)
- [➡️ Comenzar con Introducción](introduccion.md)
