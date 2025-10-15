# Glosario Técnico

Términos clave de matemáticas, DSP y audio digital usados en AudioLab University.

---

## A

**Alias / Aliasing**
Distorsión que ocurre cuando una señal es muestreada a frecuencia insuficiente ($f_s < 2f_{\text{max}}$), causando que frecuencias altas se "reflejen" como frecuencias bajas espurias.

**Amplitud**
Valor máximo de una señal periódica desde su línea de referencia (normalmente cero). En audio digital, típicamente entre -1.0 y +1.0 para full scale.

**Armónico**
Componente frecuencial múltiplo entero de la frecuencia fundamental. El $n$-ésimo armónico tiene frecuencia $f_n = n \cdot f_0$.

## B

**Bin (FFT)**
Cada elemento del array de salida de una FFT. Representa un rango de frecuencias $\Delta f = f_s / N$ donde $N$ es el tamaño de la FFT.

**Bit Depth**
Número de bits usados para representar cada muestra de audio. Común: 16-bit (CD), 24-bit (profesional), 32-bit float (DAW).

**Buffer**
Bloque de muestras procesadas juntas. En audio en tiempo real, típicamente 64, 128, 256 o 512 muestras.

## C

**Canal (Channel)**
Stream individual de audio. Sistemas comunes: mono (1), estéreo (2), 5.1 (6), 7.1 (8).

**Convolución**
Operación matemática que combina dos señales: $y[n] = \sum_{k} x[k] h[n-k]$. Base de filtrado lineal y reverb.

**Correlación**
Medida de similitud entre dos señales. Rango: $[-1, 1]$. Ver producto escalar normalizado.

## D

**dB (Decibel)**
Unidad logarítmica para relaciones de amplitud: $\text{dB} = 20 \log_{10}(A / A_{\text{ref}})$. Común: dBFS (ref = fullscale), dBu (ref = 0.775 V).

**dBFS (Decibels Full Scale)**
Escala donde 0 dBFS es la amplitud máxima representable digitalmente. Valores típicos: -6 dBFS (picos), -18 dBFS (RMS promedio).

**Determinante**
Escalar asociado a matriz cuadrada. Para matriz $A$ de $2 \times 2$: $\det(A) = ad - bc$. Si $\det(A) = 0$, la matriz no es invertible.

**DFT (Discrete Fourier Transform)**
Transformada que convierte señal discreta temporal en frecuencial: $X[k] = \sum_{n=0}^{N-1} x[n] e^{-j2\pi kn/N}$.

**DSP (Digital Signal Processing)**
Procesamiento matemático de señales digitalizadas. Incluye filtrado, modulación, compresión, etc.

## E

**Espectrograma**
Representación visual de espectro en función del tiempo. Eje X: tiempo, Eje Y: frecuencia, Color: magnitud.

**Estéreo**
Sistema de dos canales (L/R) para reproducir imagen espacial sonora.

## F

**FFT (Fast Fourier Transform)**
Algoritmo eficiente para calcular DFT. Complejidad $O(N \log N)$ vs. $O(N^2)$ de DFT directa.

**Filtro**
Sistema que modifica contenido frecuencial de señal. Tipos: lowpass, highpass, bandpass, notch.

**Frecuencia de Muestreo (Sample Rate)**
Número de muestras por segundo. Común: 44.1 kHz (CD), 48 kHz (video/pro), 96 kHz (alta resolución). Notación: $f_s$.

**Frecuencia de Nyquist**
Máxima frecuencia representable sin aliasing: $f_{\text{Nyquist}} = f_s / 2$. Para 48 kHz: 24 kHz.

**Fundamental**
Frecuencia más baja de señal periódica compleja. Determina el pitch percibido.

## G

**Ganancia**
Factor de amplificación/atenuación. Lineal: $y = g \cdot x$. En dB: $\text{dB} = 20 \log_{10}(g)$.

## H

**Hertz (Hz)**
Unidad de frecuencia: ciclos por segundo. 1 kHz = 1000 Hz.

## I

**Inversa (Matriz)**
Matriz $A^{-1}$ tal que $A A^{-1} = I$. Solo existe si $\det(A) \neq 0$.

## L

**Latencia**
Retardo entre entrada y salida en sistema de procesamiento. Causada por buffering y procesamiento.

**Leakage (Spectral)**
Dispersión de energía espectral a bins adyacentes en FFT. Mitigado con ventanas (Hann, Hamming, etc.).

**LUFS (Loudness Units Full Scale)**
Medida perceptual de loudness según ITU-R BS.1770. Usada en mastering (ej. -14 LUFS para streaming).

## M

**Matriz**
Arreglo rectangular de números. Notación: $A \in \mathbb{R}^{m \times n}$ (m filas, n columnas).

**Mid/Side (M/S)**
Técnica de encoding estéreo: Mid = L+R (centro), Side = L-R (información estéreo).

**Mono**
Señal de un solo canal. Sin información espacial.

**Muestra (Sample)**
Valor discreto de amplitud en instante de tiempo. Señal digital = secuencia de muestras.

## N

**Norma**
Medida de tamaño de vector. L1: $\|\vec{x}\|_1 = \sum |x_i|$. L2: $\|\vec{x}\|_2 = \sqrt{\sum x_i^2}$.

**Nyquist, Teorema de**
Para reconstruir señal sin pérdida, $f_s \geq 2 f_{\text{max}}$.

## O

**Ortogonal**
Dos vectores son ortogonales si $\vec{x} \cdot \vec{y} = 0$ (perpendiculares, no correlacionados).

**Overlap**
Solapamiento entre ventanas consecutivas en análisis STFT. Típicamente 50% o 75%.

## P

**Pan (Panorama)**
Distribución de señal mono entre canales estéreo. Center = L=R=0.707. Hard left = L=1, R=0.

**Pitch**
Percepción subjetiva de altura tonal. Relacionado (no igual) a frecuencia fundamental.

**Producto Escalar (Dot Product)**
$\vec{x} \cdot \vec{y} = \sum x_i y_i$. Proyección de un vector sobre otro.

## R

**RMS (Root Mean Square)**
Valor eficaz: $\text{RMS} = \sqrt{\frac{1}{N} \sum x_i^2}$. Relacionado con energía percibida.

## S

**Señal**
Función de tiempo que representa información. En audio digital: secuencia discreta de amplitudes.

**STFT (Short-Time Fourier Transform)**
FFT aplicada a ventanas sucesivas con overlap. Base de espectrograma.

## T

**THD (Total Harmonic Distortion)**
Medida de distorsión armónica: relación entre energía de armónicos y fundamental. Expresado en %.

**Transformada**
Función que mapea señal de un dominio a otro (tiempo → frecuencia, espacial → frecuencial, etc.).

## V

**Vector**
Tupla ordenada de números: $\vec{x} = [x_1, x_2, \ldots, x_n]^T$. Representa señal, punto en espacio, etc.

**Ventana (Window)**
Función multiplicada por segmento de señal antes de FFT para reducir leakage. Tipos: Hann, Hamming, Blackman, Kaiser.

## W

**Waveform**
Representación visual de amplitud vs. tiempo.

## Símbolos Matemáticos

| Símbolo | Significado |
|---------|-------------|
| $f_s$ | Frecuencia de muestreo |
| $f_0$ | Frecuencia fundamental |
| $\omega$ | Frecuencia angular ($\omega = 2\pi f$) |
| $N$ | Número de muestras / tamaño FFT |
| $\vec{x}$ | Vector |
| $A$ | Matriz |
| $A^{-1}$ | Inversa de matriz |
| $\det(A)$ | Determinante de matriz |
| $\|\vec{x}\|$ | Norma de vector |
| $\vec{x} \cdot \vec{y}$ | Producto escalar |
| $j$ | Unidad imaginaria ($j^2 = -1$) |
| $e^{j\theta}$ | Fasor: $\cos\theta + j\sin\theta$ |

## Acrónimos Comunes

| Acrónimo | Significado |
|----------|-------------|
| ADC | Analog-to-Digital Converter |
| DAC | Digital-to-Analog Converter |
| DAW | Digital Audio Workstation |
| DSP | Digital Signal Processing |
| DFT | Discrete Fourier Transform |
| FFT | Fast Fourier Transform |
| FIR | Finite Impulse Response (filtro) |
| IIR | Infinite Impulse Response (filtro) |
| LUFS | Loudness Units Full Scale |
| M/S | Mid/Side |
| RMS | Root Mean Square |
| STFT | Short-Time Fourier Transform |
| THD | Total Harmonic Distortion |

---

## Notación de Señales

### Continuas vs. Discretas

- Continua: $x(t)$ (función de tiempo continuo)
- Discreta: $x[n]$ (secuencia indexada por enteros)

### Transformadas

- Temporal: $x[n]$
- Frecuencial: $X[k]$ o $X(f)$

### Vectores y Matrices

- Vector columna: $\vec{x}$ o $\mathbf{x}$
- Matriz: $A$ o $\mathbf{A}$
- Transpuesta: $A^T$

---

**Actualización**: 2025-10-15

Para sugerir adiciones al glosario, abre un issue en el repositorio.
