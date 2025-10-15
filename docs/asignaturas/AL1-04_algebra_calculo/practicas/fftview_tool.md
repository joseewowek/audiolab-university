# Práctica: FFTView Tool

## Objetivo

Utilizar **FFTView** para análisis espectral avanzado de señales de audio: visualización de espectrograma, identificación de armónicos, detección de resonancias y medición de respuesta en frecuencia.

## Requisitos

- Python 3.10 o superior
- NumPy, SciPy, Matplotlib
- Archivo de audio para analizar

## Instalación

### 1. Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 2. Instalar FFTView

```bash
pip install fftview-audio
```

Verificar instalación:

```bash
fftview --version
```

### 3. Dependencias adicionales

```bash
pip install soundfile scipy matplotlib
```

## Conceptos Previos

### Transformada de Fourier

La **FFT** (Fast Fourier Transform) descompone una señal temporal en sus componentes frecuenciales:

$$
X(k) = \sum_{n=0}^{N-1} x[n] e^{-j 2\pi kn/N}
$$

Donde:

- $x[n]$: Señal en tiempo
- $X(k)$: Coeficientes de frecuencia (bins)
- $k$: Índice de bin (frecuencia)
- $N$: Tamaño de ventana FFT

### Ventanas

Para reducir leakage espectral, aplicamos ventanas:

- **Hann**: Buena para señales tonales
- **Hamming**: Similar a Hann, menos leakage
- **Blackman**: Máxima supresión de lóbulos laterales
- **Rectangular**: Sin ventana (solo para señales periódicas exactas)

## Uso Básico

### Sintaxis General

```bash
fftview <archivo> [opciones]
```

### Opciones Principales

| Opción | Descripción |
|--------|-------------|
| `--size` | Tamaño de FFT (potencia de 2, defecto: 2048) |
| `--window` | Tipo de ventana (hann, hamming, blackman) |
| `--overlap` | Overlap en % (defecto: 75) |
| `--range` | Rango de frecuencias a visualizar (e.g., 20-20000) |
| `--output` | Archivo de salida (PNG, PDF) |
| `--log` | Escala logarítmica de frecuencia |

## Ejemplos Prácticos

### 1. Espectrograma Básico

```bash
fftview mi_audio.wav --output espectrograma.png
```

Genera visualización tiempo-frecuencia con configuración por defecto.

### 2. Análisis de Armónicos

```bash
fftview nota_la_440.wav --size 4096 --window hann --range 20-5000 --output armonicos.png
```

**Interpretación**:

Si la señal es un La 440 Hz puro, verás picos en:

- 440 Hz (fundamental)
- 880 Hz (2º armónico)
- 1320 Hz (3º armónico)
- ...

### 3. Respuesta en Frecuencia de Sala

```bash
fftview sweep_sala.wav --size 8192 --log --output sala_fr.png
```

Para señal sweep (barrido de frecuencias), visualiza respuesta acústica de la sala.

### 4. Comparar Canales L/R

```bash
fftview estereo.wav --channels separate --output lr_spectrum.png
```

Genera dos espectrogramas superpuestos para comparar contenido frecuencial de cada canal.

### 5. Ventana Específica para Análisis de Transitorios

```bash
fftview kick_drum.wav --size 1024 --window blackman --overlap 50 --output kick_spectrum.png
```

Ventana pequeña (1024) con menos overlap para capturar mejor transitorios.

## Flujo de Trabajo: Análisis de Mezcla

### Paso 1: Overview General

```bash
fftview mezcla.wav --size 4096 --log --range 20-20000 --output mezcla_overview.png
```

Visualiza distribución espectral completa.

**Puntos a verificar**:

- Balance tonal (graves, medios, agudos)
- Presencia de picos resonantes
- Energía más allá de 16 kHz

### Paso 2: Análisis de Graves (20-200 Hz)

```bash
fftview mezcla.wav --size 8192 --range 20-200 --output mezcla_graves.png
```

Aumenta resolución (8192 samples) para mejor definición en bajas frecuencias.

**Buscar**:

- Resonancias de sala
- Fundamental de kick y bajo
- Mud (acumulación 200-400 Hz)

### Paso 3: Análisis de Medios (200-5000 Hz)

```bash
fftview mezcla.wav --size 4096 --range 200-5000 --output mezcla_medios.png
```

**Buscar**:

- Claridad vocal (1-4 kHz)
- Presencia de snare (2-5 kHz)
- Posibles masking entre instrumentos

### Paso 4: Análisis de Agudos (5-20 kHz)

```bash
fftview mezcla.wav --size 2048 --range 5000-20000 --output mezcla_agudos.png
```

**Buscar**:

- Air (>10 kHz)
- Sibilancia excesiva (6-8 kHz)
- Ruido de fondo

## Integración con Python

### Script Básico

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import hann
import soundfile as sf

# Cargar audio
audio, fs = sf.read("mi_audio.wav")

# Configuración FFT
N = 4096
window = hann(N)

# Tomar segmento y aplicar ventana
segment = audio[:N] * window

# Calcular FFT
spectrum = fft(segment)
freqs = fftfreq(N, 1/fs)

# Magnitud en dB
magnitude_db = 20 * np.log10(np.abs(spectrum[:N//2]))

# Plotear
plt.figure(figsize=(12, 6))
plt.plot(freqs[:N//2], magnitude_db)
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.title("Espectro de Frecuencia")
plt.grid(True)
plt.xlim(20, 20000)
plt.xscale('log')
plt.savefig("espectro_python.png")
plt.show()
```

### Espectrograma Completo

```python
from scipy.signal import spectrogram

# Calcular espectrograma
f, t, Sxx = spectrogram(audio, fs, window='hann', nperseg=2048, noverlap=1536)

# Plotear
plt.figure(figsize=(14, 6))
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud', cmap='viridis')
plt.ylabel('Frecuencia (Hz)')
plt.xlabel('Tiempo (s)')
plt.title('Espectrograma')
plt.colorbar(label='Magnitud (dB)')
plt.ylim(20, 20000)
plt.yscale('log')
plt.savefig("espectrograma_python.png")
plt.show()
```

## Interpretación de Resultados

### Identificación de Armónicos

Para un tono puro de frecuencia $f_0$, los armónicos aparecen en:

$$
f_n = n \cdot f_0, \quad n = 1, 2, 3, \ldots
$$

**Ejemplo**: Tono 100 Hz

- Fundamental: 100 Hz
- 2º armónico: 200 Hz
- 3º armónico: 300 Hz

### Ancho de Banda

Mide la frecuencia de corte (-3 dB) para filtros:

$$
f_c = \text{frecuencia donde magnitud cae 3 dB respecto al pico}
$$

### THD (Distorsión Armónica Total)

Suma de energía de armónicos respecto a fundamental:

$$
\text{THD} = \frac{\sqrt{P_2^2 + P_3^2 + \cdots}}{P_1} \times 100\%
$$

Donde $P_n$ es la potencia del $n$-ésimo armónico.

## Validación de la Práctica

### Checklist

- [ ] Instalar FFTView correctamente
- [ ] Generar espectrograma de archivo de audio
- [ ] Identificar fundamental y armónicos de tono puro
- [ ] Analizar respuesta en frecuencia por bandas
- [ ] Exportar visualizaciones en alta resolución
- [ ] Implementar análisis FFT básico en Python

### Ejercicio: Análisis de Nota Musical

1. Genera señal de nota La (440 Hz) con armónicos:

```python
import numpy as np
import soundfile as sf

fs = 48000
duration = 2.0
t = np.linspace(0, duration, int(fs * duration))

# Fundamental + armónicos
signal = (
    1.0 * np.sin(2 * np.pi * 440 * t) +      # Fundamental
    0.5 * np.sin(2 * np.pi * 880 * t) +      # 2º armónico
    0.25 * np.sin(2 * np.pi * 1320 * t) +    # 3º armónico
    0.125 * np.sin(2 * np.pi * 1760 * t)     # 4º armónico
)

# Normalizar
signal = signal / np.max(np.abs(signal)) * 0.8

sf.write("nota_la_armonicos.wav", signal, fs)
```

2. Analiza con FFTView:

```bash
fftview nota_la_armonicos.wav --size 8192 --window hann --range 200-2000 --output nota_spectrum.png
```

3. Verifica presencia de picos en 440, 880, 1320 y 1760 Hz.

## Entregables

1. **Espectrograma** de archivo de audio personal
2. **Análisis escrito** identificando:
   - Rango dinámico frecuencial
   - Frecuencias dominantes
   - Posibles problemas (resonancias, ruido)
3. **Script Python** que replique análisis básico de FFTView

## Troubleshooting

### FFT muy ruidoso

Incrementa tamaño de ventana (e.g., 8192 o 16384) y usa ventana Blackman.

### Resolución temporal insuficiente

Reduce tamaño de FFT (e.g., 1024) y overlap (e.g., 50%).

### Escala de colores poco clara

Ajusta rango dinámico con `--vmin` y `--vmax`:

```bash
fftview audio.wav --vmin -80 --vmax 0
```

## Próximos Pasos

- Estudia [Capítulo sobre Transformadas de Fourier](../01_programa/AL1-04_algebra_calculo/cap01_vectores.md)
- Explora [Notebook de FFT Basics](../03_notebooks/fft_basics.ipynb)
- Compara resultados con análisis por [SigLab CLI](siglab_cli.md)

## Referencias

- Documentación FFTView: https://fftview-audio.readthedocs.io
- NumPy FFT: https://numpy.org/doc/stable/reference/routines.fft.html
- SciPy Signal Processing: https://docs.scipy.org/doc/scipy/reference/signal.html

---

**Nota**: FFTView es una herramienta ficticia para este curso. Para análisis espectral real, usa `librosa`, `scipy.signal`, o herramientas como Sonic Visualiser.
