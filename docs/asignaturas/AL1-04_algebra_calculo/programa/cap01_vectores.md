# Capítulo 1: Vectores en Procesamiento de Audio

## Idea Clave

Una señal de audio digital es una secuencia ordenada de números (muestras). Podemos representarla como un **vector** y aplicar operaciones algebraicas para calcular métricas, proyecciones y transformaciones.

## Objetivos de Aprendizaje

Al completar este capítulo serás capaz de:

1. Representar señales de audio como vectores
2. Calcular normas (L1, L2) y su relación con RMS
3. Aplicar producto escalar para medir similitud entre señales
4. Proyectar vectores ortogonalmente
5. Implementar cálculos básicos en Python con NumPy

## Índice

- [Vector como Señal](#vector-como-señal)
- [Operaciones Básicas](#operaciones-básicas)
- [Normas de Vectores](#normas-de-vectores)
- [Producto Escalar](#producto-escalar)
- [Proyección Ortogonal](#proyección-ortogonal)
- [Micro-laboratorio](#micro-laboratorio)
- [Checklist de Conceptos](#checklist-de-conceptos)
- [Ejercicios](#ejercicios)

## Vector como Señal

### Definición

Un **vector** en $\mathbb{R}^n$ es una tupla ordenada de $n$ números reales:

$$
\vec{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}
$$

### Interpretación en Audio

Para una señal de audio con $N$ muestras a frecuencia de muestreo $f_s$:

- $x[n]$ es la amplitud de la muestra $n$
- $n = 0, 1, 2, \ldots, N-1$ (índices discretos)
- Tiempo: $t_n = n / f_s$

**Ejemplo**: Sinusoide de 1kHz a 48kHz durante 10ms

$$
x[n] = A \sin(2\pi f \cdot n / f_s), \quad n = 0, 1, \ldots, 479
$$

donde $N = 0.01 \times 48000 = 480$ muestras.

## Operaciones Básicas

### Suma de Vectores

$$
\vec{x} + \vec{y} = \begin{bmatrix} x_1 + y_1 \\ x_2 + y_2 \\ \vdots \\ x_n + y_n \end{bmatrix}
$$

**Aplicación**: Mezcla de dos señales mono.

### Multiplicación por Escalar

$$
\alpha \vec{x} = \begin{bmatrix} \alpha x_1 \\ \alpha x_2 \\ \vdots \\ \alpha x_n \end{bmatrix}
$$

**Aplicación**: Ganancia o atenuación ($\alpha = 0.5$ → -6dB aprox).

### Ejemplo Numérico

Sean dos buffers de 4 muestras:

$$
\vec{a} = \begin{bmatrix} 0.5 \\ 0.8 \\ -0.3 \\ 0.1 \end{bmatrix}, \quad
\vec{b} = \begin{bmatrix} 0.2 \\ -0.4 \\ 0.6 \\ 0.0 \end{bmatrix}
$$

Mezcla 50/50:

$$
\vec{m} = 0.5\vec{a} + 0.5\vec{b} = \begin{bmatrix} 0.35 \\ 0.20 \\ 0.15 \\ 0.05 \end{bmatrix}
$$

## Normas de Vectores

### Norma L1

$$
\|\vec{x}\|_1 = \sum_{i=1}^{n} |x_i|
$$

**Uso**: Suma de amplitudes absolutas (relacionada con energía perceptual).

### Norma L2 (Euclidiana)

$$
\|\vec{x}\|_2 = \sqrt{\sum_{i=1}^{n} x_i^2}
$$

**Uso**: Energía de la señal, base del cálculo de RMS.

### Relación con RMS

El **RMS** (Root Mean Square) normaliza la norma L2 por el número de muestras:

$$
\text{RMS} = \frac{\|\vec{x}\|_2}{\sqrt{N}} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} x_i^2}
$$

**Ejemplo**: Buffer de 4 muestras $\vec{x} = [0.5, -0.5, 0.5, -0.5]$

$$
\|\vec{x}\|_2 = \sqrt{0.25 + 0.25 + 0.25 + 0.25} = 1.0
$$

$$
\text{RMS} = \frac{1.0}{\sqrt{4}} = 0.5
$$

En dBFS (asumiendo fullscale = 1.0):

$$
\text{dBFS} = 20 \log_{10}(0.5) \approx -6.02 \text{ dB}
$$

## Producto Escalar

### Definición

$$
\vec{x} \cdot \vec{y} = \sum_{i=1}^{n} x_i y_i = x_1 y_1 + x_2 y_2 + \cdots + x_n y_n
$$

### Propiedades

- **Conmutativo**: $\vec{x} \cdot \vec{y} = \vec{y} \cdot \vec{x}$
- **Distributivo**: $\vec{x} \cdot (\vec{y} + \vec{z}) = \vec{x} \cdot \vec{y} + \vec{x} \cdot \vec{z}$
- **Relación con norma**: $\vec{x} \cdot \vec{x} = \|\vec{x}\|_2^2$

### Interpretación Geométrica

$$
\vec{x} \cdot \vec{y} = \|\vec{x}\|_2 \|\vec{y}\|_2 \cos(\theta)
$$

donde $\theta$ es el ángulo entre los vectores.

**Ortogonalidad**: $\vec{x} \perp \vec{y} \iff \vec{x} \cdot \vec{y} = 0$

### Aplicación: Correlación

La **correlación** mide similitud entre señales:

$$
\text{corr}(\vec{x}, \vec{y}) = \frac{\vec{x} \cdot \vec{y}}{\|\vec{x}\|_2 \|\vec{y}\|_2}
$$

Rango: $[-1, 1]$

- $+1$: Señales idénticas (en fase)
- $0$: No correlacionadas (ortogonales)
- $-1$: Antifase completa

**Ejemplo**: Detección de fase entre L y R

```python
import numpy as np

L = np.array([0.5, 0.8, 0.3, -0.2])
R = np.array([0.5, 0.8, 0.3, -0.2])  # Idéntico

corr = np.dot(L, R) / (np.linalg.norm(L) * np.linalg.norm(R))
print(f"Correlación: {corr:.3f}")  # 1.000
```

## Proyección Ortogonal

### Problema

Dado un vector $\vec{x}$ y una dirección unitaria $\hat{u}$, encontrar la componente de $\vec{x}$ en dirección $\hat{u}$.

### Fórmula

La **proyección escalar** de $\vec{x}$ sobre $\hat{u}$:

$$
\text{proj}_{\hat{u}}(\vec{x}) = \vec{x} \cdot \hat{u}
$$

El **vector proyección**:

$$
\vec{p} = (\vec{x} \cdot \hat{u}) \hat{u}
$$

### Ejemplo: Señal sobre Coseno

Sea $\vec{x}$ un buffer y $\hat{u}$ un coseno normalizado:

$$
u[n] = \cos(2\pi f n / f_s), \quad \hat{u} = \frac{\vec{u}}{\|\vec{u}\|_2}
$$

La proyección $\vec{x} \cdot \hat{u}$ da la **amplitud** de la componente frecuencial $f$ en $\vec{x}$ (base de la DFT).

## Micro-laboratorio

### Objetivo

Calcular RMS y correlación entre canales L/R de un archivo estéreo sintético.

### Setup

```python
import numpy as np

# Generar señal estéreo: L = tono, R = tono con ruido
fs = 48000
duration = 0.1  # 100ms
t = np.arange(int(fs * duration)) / fs

# Canal L: sinusoide pura 1kHz
L = 0.5 * np.sin(2 * np.pi * 1000 * t)

# Canal R: mismo tono + ruido
np.random.seed(42)
R = 0.5 * np.sin(2 * np.pi * 1000 * t) + 0.1 * np.random.randn(len(t))
```

### Tareas

1. **Calcular RMS de cada canal**

```python
rms_L = np.sqrt(np.mean(L**2))
rms_R = np.sqrt(np.mean(R**2))

print(f"RMS L: {rms_L:.4f}")
print(f"RMS R: {rms_R:.4f}")
```

2. **Calcular correlación L-R**

```python
corr = np.dot(L, R) / (np.linalg.norm(L) * np.linalg.norm(R))
print(f"Correlación L-R: {corr:.4f}")
```

### Preguntas

- ¿Por qué el RMS de R es mayor que el de L?
- ¿Qué indica una correlación cercana a 1?
- ¿Cómo afectaría invertir la fase de R?

### Código Completo

```python
import numpy as np

fs = 48000
duration = 0.1
t = np.arange(int(fs * duration)) / fs

L = 0.5 * np.sin(2 * np.pi * 1000 * t)
np.random.seed(42)
R = 0.5 * np.sin(2 * np.pi * 1000 * t) + 0.1 * np.random.randn(len(t))

rms_L = np.sqrt(np.mean(L**2))
rms_R = np.sqrt(np.mean(R**2))
corr = np.dot(L, R) / (np.linalg.norm(L) * np.linalg.norm(R))

print(f"RMS L: {rms_L:.4f}")
print(f"RMS R: {rms_R:.4f}")
print(f"Correlación: {corr:.4f}")
```

**Salida esperada**:
```
RMS L: 0.3536
RMS R: 0.3571
Correlación: 0.9889
```

## Checklist de Conceptos

Antes de continuar, verifica que puedes:

- [ ] Representar un buffer de audio como vector
- [ ] Calcular suma y multiplicación por escalar
- [ ] Calcular norma L2 y RMS a mano
- [ ] Interpretar producto escalar como correlación
- [ ] Explicar cuándo dos vectores son ortogonales
- [ ] Proyectar un vector sobre una dirección dada
- [ ] Implementar operaciones básicas en NumPy

## Ejercicios

### Ejercicio 1: Cálculo de RMS

Dado el buffer $\vec{x} = [0.8, -0.6, 0.4, -0.2]$:

a) Calcula $\|\vec{x}\|_2$
b) Calcula el RMS
c) Convierte a dBFS

**Solución**:

a) $\|\vec{x}\|_2 = \sqrt{0.64 + 0.36 + 0.16 + 0.04} = \sqrt{1.2} \approx 1.095$

b) $\text{RMS} = 1.095 / \sqrt{4} = 0.548$

c) $\text{dBFS} = 20 \log_{10}(0.548) \approx -5.22$ dB

### Ejercicio 2: Ortogonalidad

Verifica si los vectores son ortogonales:

$$
\vec{a} = [1, 0, -1], \quad \vec{b} = [1, \sqrt{2}, 1]
$$

**Solución**:

$$
\vec{a} \cdot \vec{b} = 1 \cdot 1 + 0 \cdot \sqrt{2} + (-1) \cdot 1 = 0
$$

Sí son ortogonales.

### Ejercicio 3: Proyección

Proyecta $\vec{x} = [3, 4]$ sobre $\vec{u} = [1, 0]$.

**Solución**:

$\vec{u}$ ya es unitario ($\|\vec{u}\|_2 = 1$).

$$
\text{proj}_{\vec{u}}(\vec{x}) = \vec{x} \cdot \vec{u} = 3
$$

Vector proyección: $\vec{p} = 3 \cdot [1, 0] = [3, 0]$

### Ejercicio 4: Implementación

Escribe una función Python que calcule la correlación entre dos arrays de igual longitud.

**Solución**:

```python
def correlacion(x, y):
    dot = np.dot(x, y)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    return dot / (norm_x * norm_y)

# Ejemplo
a = np.array([1, 2, 3])
b = np.array([2, 4, 6])
print(correlacion(a, b))  # 1.0 (proporcionales)
```

## Referencias

- [Índice del Módulo](index.md)
- [Capítulo 2: Matrices](cap02_matrices.md)
- [Glosario](../../04_recursos/glosario.md)

---

**Próximo**: [Capítulo 2 - Matrices y Transformaciones](cap02_matrices.md)
