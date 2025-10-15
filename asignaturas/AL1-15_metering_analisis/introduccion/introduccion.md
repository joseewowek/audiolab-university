# Introducción a AL1-15 · Telemetría / Crashes I (conceptos)

## ¿Por qué esta asignatura?

La observabilidad es clave para mejorar productos de audio. Esta asignatura te proporciona:

- **Telemetría** ligera y respetuosa con la privacidad
- **Crash reporting** offline con stacktraces
- **Métricas** de performance sin impactar audio-thread
- **Herramientas** para diagnosticar problemas en producción

## Prerrequisitos

- C++ Básico y STL (AL1-02)
- Python para Automatización (AL1-03)
- Conceptos de threading (deseable)

## Estructura del Curso

### Bloque I: Fundamentos de Observabilidad (Caps. 1-6)
Qué es telemetría, propósitos en audio software, latencia y coste, privacidad por diseño, categorías de eventos, telemetría estructurada (JSONL).

### Bloque II: Métricas y Logging Local (Caps. 7-12)
Logger asincrónico, rotación de logs, event queue thread-safe, tipos de eventos AudioLab, performance tracing, local metrics file.

### Bloque III: Crash Detection y Reportes (Caps. 13-18)
Qué es un crash, captura de excepción, señales nativas, stacktrace mínimo, dump y last session state, reanudación segura.

### Bloque IV: Sincronización & Reportes Simulados (Caps. 19-24)
Consentimiento opt-in UX, batch uploader simulado, anonimización, integración con CI/QA, etiquetado de eventos, mini-dashboard local.

### Bloque V: Proyecto - Telemetría L0 + Crash System (Caps. 25-30)
Diseño del logger, crash handler básico, report viewer CLI, integración con QA, simulación de upload, informe final.

## Tiempo Estimado

- **Teoría**: 30-40 horas
- **Prácticas**: 25-35 horas
- **Proyecto**: 10-15 horas
- **Total**: ~75 horas

## Evaluación

### Sumativa
- `/telemetry/` con logger JSONL, metrics_snapshot.json, crash_handler, telemetry_cli.py
- Crash reports con stacktrace + last_session.json
- `TELEMETRY_GUIDE.md`
- Dashboard local (CLI/notebook)

---

¿Listo para empezar? Comienza con el Capítulo 1 en la sección [Programa](programa/)
