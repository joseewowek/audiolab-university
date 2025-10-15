# 📊 AL1-15 · Telemetría / Crashes I (conceptos)

> **Familia:** Telemetry/Cloud
> **Bloque:** L0 / CORE
> **Duración:** 30 capítulos (5 bloques × 6 temas)
> **Objetivo general:** construir el **andamiaje básico de observabilidad** para tus plugins: registro de eventos, métricas ligeras, trazas de fallos y **crash reporting offline**, todo con respeto a la privacidad y *performance safe*.

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

### 🧭 BLOQUE I · Fundamentos de Observabilidad
Qué es telemetría, propósitos en audio software, latencia y coste, privacidad por diseño, categorías de eventos, telemetría estructurada (JSONL).

### 🧾 BLOQUE II · Métricas y Logging Local
Logger asincrónico, rotación de logs, event queue thread-safe, tipos de eventos AudioLab, performance tracing, local metrics file.

### 💥 BLOQUE III · Crash Detection y Reportes
Qué es un crash, captura básica de excepción, señales nativas, stacktrace mínimo, dump y "last session state", reanudación segura.

### ☁️ BLOQUE IV · Sincronización & Reportes (Simulados)
Consentimiento y opt-in UX, batch uploader simulado, anonimización ligera, integración con CI/QA, etiquetado de eventos, mini-dashboard local.

### 🚀 BLOQUE V · Proyecto: Telemetría L0 + Crash System
Diseño del logger, crash handler básico, report viewer CLI, integración con QA, simulación de upload, informe final.

---

## 🧾 Entregables del Curso

- 📁 `/telemetry/` con telemetry_logger (JSONL), metrics_snapshot.json, crash_handler, telemetry_cli.py, upload_simulator.py
- 💥 Crash Reports: crash_report_*.json con stacktrace + last_session.json
- 📄 `TELEMETRY_GUIDE.md` con flujo de datos, privacidad y ejemplos
- 📊 Dashboard local (CLI o notebook) con % CPU, crashes/host, top eventos

---

## 🔗 Navegación

- [⬅️ Volver a Asignaturas](../)
- [➡️ Comenzar con Introducción](introduccion.md)
