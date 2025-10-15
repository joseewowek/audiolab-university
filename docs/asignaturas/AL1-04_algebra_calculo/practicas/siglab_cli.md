# Práctica: SigLab CLI

## Objetivo

Familiarizarse con la herramienta de línea de comandos **SigLab** para análisis rápido de señales de audio: visualización de waveform, cálculo de métricas (RMS, pico) y análisis espectral básico.

## Requisitos

- Python 3.10 o superior
- pip instalado
- Terminal o línea de comandos

## Instalación

### 1. Crear entorno virtual (recomendado)

```bash
python -m venv .venv
```

Activar:

- **Windows**: `.venv\Scripts\activate`
- **Linux/Mac**: `source .venv/bin/activate`

### 2. Instalar SigLab

```bash
pip install siglab-cli
```

Verificar instalación:

```bash
siglab --version
```

### 3. Dependencias adicionales (opcional)

Para soporte completo de formatos de audio:

```bash
pip install soundfile librosa
```

## Uso Básico

### Sintaxis General

```bash
siglab <comando> [opciones] <archivo>
```

### Comandos Principales

| Comando | Descripción |
|---------|-------------|
| `info` | Muestra metadatos del archivo |
| `plot` | Visualiza waveform |
| `rms` | Calcula RMS por canal |
| `peak` | Encuentra valor de pico |
| `fft` | Análisis espectral básico |

## Ejemplos Prácticos

### 1. Información de Archivo

```bash
siglab info mi_audio.wav
```

**Salida esperada**:
```
Archivo: mi_audio.wav
Formato: WAV
Sample Rate: 48000 Hz
Canales: 2 (Stereo)
Duración: 3.25 segundos
Bit Depth: 24-bit
```

### 2. Calcular RMS

```bash
siglab rms mi_audio.wav
```

**Salida esperada**:
```
RMS por canal:
  L: -18.3 dBFS (0.121)
  R: -19.1 dBFS (0.110)
Promedio: -18.7 dBFS
```

### 3. Encontrar Picos

```bash
siglab peak mi_audio.wav --threshold -3.0
```

Encuentra muestras que excedan -3 dBFS.

**Salida esperada**:
```
Picos detectados:
  L: -2.1 dBFS en 1.234s
  R: -2.8 dBFS en 1.237s
True Peak: -2.1 dBFS
```

### 4. Visualizar Waveform

```bash
siglab plot mi_audio.wav --output waveform.png
```

Genera imagen PNG con representación visual de la forma de onda.

Opciones adicionales:

- `--width 1920 --height 1080`: Resolución personalizada
- `--range 0.5 2.5`: Visualizar solo segmento (0.5s a 2.5s)

### 5. Análisis FFT Rápido

```bash
siglab fft mi_audio.wav --window 2048 --output spectrum.png
```

Genera espectrograma básico.

**Opciones**:

- `--window`: Tamaño de ventana FFT (potencia de 2)
- `--overlap`: Solapamiento (por defecto 50%)
- `--log`: Escala logarítmica de frecuencia

## Flujo de Trabajo Recomendado

### Análisis Completo de Mezcla

```bash
# 1. Ver información general
siglab info mezcla_final.wav

# 2. Calcular RMS y verificar balance
siglab rms mezcla_final.wav

# 3. Detectar posibles clippings
siglab peak mezcla_final.wav --threshold -0.5

# 4. Visualizar waveform
siglab plot mezcla_final.wav --output mezcla_waveform.png

# 5. Análisis espectral
siglab fft mezcla_final.wav --output mezcla_spectrum.png --log
```

### Comparar Versiones

```bash
# Generar reportes de ambas versiones
siglab rms version_1.wav > v1_metrics.txt
siglab rms version_2.wav > v2_metrics.txt

# Comparar manualmente o con diff
diff v1_metrics.txt v2_metrics.txt
```

## Integración con Python

SigLab puede usarse también como librería Python:

```python
from siglab import AudioFile

# Cargar archivo
audio = AudioFile("mi_audio.wav")

# Calcular métricas
rms_L = audio.rms(channel=0)
rms_R = audio.rms(channel=1)

print(f"RMS L: {rms_L:.4f}")
print(f"RMS R: {rms_R:.4f}")

# Verificar correlación L-R
corr = audio.correlation(0, 1)
print(f"Correlación L-R: {corr:.3f}")
```

## Validación de la Práctica

### Checklist

Completa las siguientes tareas con un archivo de audio propio:

- [ ] Instalar SigLab correctamente
- [ ] Extraer información básica del archivo
- [ ] Calcular RMS de ambos canales
- [ ] Detectar picos mayores a -6 dBFS
- [ ] Generar visualización de waveform
- [ ] Exportar análisis espectral

### Archivo de Prueba

Si no tienes archivo de audio, genera uno sintético:

```python
import numpy as np
import soundfile as sf

# Generar tono 440 Hz, 1 segundo, 48 kHz
fs = 48000
t = np.arange(fs) / fs
signal = 0.5 * np.sin(2 * np.pi * 440 * t)

# Guardar como WAV
sf.write("test_440hz.wav", signal, fs)
```

Luego analiza con SigLab:

```bash
siglab rms test_440hz.wav
```

**Valor esperado**: RMS ≈ -9.03 dBFS (0.5 / sqrt(2) ≈ 0.3536)

## Entregables

Para completar esta práctica, genera un reporte con:

1. **Screenshots** de comandos ejecutados y sus salidas
2. **Archivos PNG** de waveform y spectrum
3. **Interpretación** de los valores RMS obtenidos
4. **Comparación** entre dos versiones de un mismo archivo (si aplica)

Formato sugerido: Markdown o PDF.

## Troubleshooting

### Error: "comando no encontrado"

Verifica que el entorno virtual esté activado y SigLab instalado.

```bash
which siglab  # Linux/Mac
where siglab  # Windows
```

### Error al cargar archivo

Verifica formato soportado:

```bash
siglab info archivo.mp3
```

Si falla, convierte a WAV:

```bash
ffmpeg -i archivo.mp3 archivo.wav
```

### Gráficos no se generan

Instala matplotlib:

```bash
pip install matplotlib
```

## Próximos Pasos

- Prueba [FFTView Tool](fftview_tool.md) para análisis espectral avanzado
- Explora [Notebooks de FFT](../03_notebooks/fft_basics.ipynb)
- Consulta [Capítulo 1: Vectores](../01_programa/AL1-04_algebra_calculo/cap01_vectores.md) para entender el cálculo de RMS

## Referencias

- Documentación oficial: https://siglab-cli.readthedocs.io
- Repositorio: https://github.com/audiolab/siglab-cli
- Issues: https://github.com/audiolab/siglab-cli/issues

---

**Nota**: SigLab es una herramienta ficticia creada para este curso. Para análisis real, considera herramientas como `sox`, `librosa` o `Audacity`.
