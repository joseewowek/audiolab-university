# Introducción a AL1-14 · Seguridad/Deploy I (conceptos)

## ¿Por qué esta asignatura?

La seguridad y el deployment profesional son críticos para productos comerciales. Esta asignatura te proporciona:

- **Fundamentos** de protección de software de audio
- **Modelos** de licencia y activación
- **Empaquetado** seguro con firma y notarización
- **Privacidad** por diseño y actualizaciones seguras

## Prerrequisitos

- Programación básica en C++
- Conceptos de criptografía (nivel divulgación)
- Familiaridad con instaladores y sistemas operativos

## Estructura del Curso

### Bloque I: Mentalidad de Seguridad & Amenazas (Caps. 1-6)
Superficie de ataque, principios (mínimo privilegio, fail-safe), modelo STRIDE, amenazas comunes, secure coding, gestión de secretos.

### Bloque II: Licencias & Activación (Caps. 7-12)
Modelos de licencia, activación online/offline, challenge–response, license cache local, watermarking (noción), UX de licencias.

### Bloque III: Firma, Integridad & Empaquetado (Caps. 13-18)
Firma de código, notarización macOS, integridad de binarios, SBOM/SCA, instaladores y layouts, config y datos del usuario.

### Bloque IV: Updates, Telemetría & Privacidad (Caps. 19-24)
Infra de actualizaciones, verificación de updates, telemetría con consentimiento, privacidad por diseño, crash reports, políticas y cumplimiento.

### Bloque V: Proyecto - Esqueleto de Seguridad/Deploy L0 (Caps. 25-30)
Política de licencias, formato de license cache, mock de activación offline, firma local, updater simulado + rollback, documentos.

## Tiempo Estimado

- **Teoría**: 35-45 horas
- **Prácticas**: 20-30 horas
- **Proyecto**: 10-15 horas
- **Total**: ~75 horas

## Evaluación

### Sumativa
- `/security/` con LICENSE_POLICY.md, PRIVACY.md, EULA_TEMPLATE.md, SBOM.json
- `/tools/security/` con scripts de activación, firma y updates
- Plugin-Demo-Installer.zip con checksums y firma
- Checklist de seguridad L0 completo

---

¿Listo para empezar? Comienza con el Capítulo 1 en la sección [Programa](programa/)
