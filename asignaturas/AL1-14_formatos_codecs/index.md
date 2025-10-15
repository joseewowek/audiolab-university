# 🔐 AL1-14 · Seguridad/Deploy I (conceptos)

> **Familia:** Seguridad/Deploy
> **Bloque:** L0 / CORE
> **Duración:** 30 capítulos (5 bloques × 6 temas)
> **Objetivo general:** entender los **fundamentos de protección y entrega** para plugins de audio: modelos de licencia, empaquetado seguro, firma/notarización (visión), actualizaciones y **privacidad por diseño**.

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

### 🧭 BLOQUE I · Mentalidad de Seguridad & Amenazas
Superficie de ataque, principios (mínimo privilegio, fail-safe), modelo STRIDE, amenazas comunes, secure coding C++, gestión de secretos.

### 🧾 BLOQUE II · Licencias & Activación (Panorámica)
Modelos de licencia, activación online/offline, challenge–response, license cache local, watermarking (noción), UX de licencias.

### 🪪 BLOQUE III · Firma, Integridad & Empaquetado
Firma de código (visión), notarización macOS, integridad de binarios, SBOM/SCA básico, instaladores y layouts, config y datos del usuario.

### 🔄 BLOQUE IV · Updates, Telemetría & Privacidad
Infra de actualizaciones, verificación de updates, telemetría mínima con consentimiento, privacidad por diseño, crash reports seguros, políticas y cumplimiento.

### 🚀 BLOQUE V · Proyecto: Esqueleto de Seguridad/Deploy (L0)
Política de licencias (draft), formato de license cache, mock de activación offline, firma local de artefactos, updater simulado + rollback, paquete de documentos.

---

## 🧾 Entregables del Curso

- 📂 `/security/` con LICENSE_POLICY.md, PRIVACY.md, EULA_TEMPLATE.md, SBOM.json
- 🧰 `/tools/security/` con license_chalresp.py, sign_artifact.py, update_runner.py
- 📦 `/dist/` con Plugin-Demo-Installer.zip + checksums.txt + SIGNATURE.txt
- ✅ Checklist de seguridad L0: sin secretos en binario, caché cifrada, telemetría opt-in, updates verificadas

---

## 🔗 Navegación

- [⬅️ Volver a Asignaturas](../)
- [➡️ Comenzar con Introducción](introduccion.md)
