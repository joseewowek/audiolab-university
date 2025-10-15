# Capítulo 2: Matrices y Transformaciones Lineales

## Idea Clave

Una **matriz** representa una transformación lineal que mapea vectores de entrada a vectores de salida. En audio, usamos matrices para routing, conversiones Mid/Side, rotaciones de imagen estéreo y sistemas multicanal.

## Objetivos de Aprendizaje

Al completar este capítulo serás capaz de:

1. Interpretar matrices como transformaciones de señales
2. Multiplicar matrices y vectores
3. Calcular determinantes e inversas de matrices 2×2 y 3×3
4. Implementar Mid/Side encoding/decoding con matrices
5. Resolver sistemas lineales simples relacionados con audio

## Índice

- [Definición y Notación](#definición-y-notación)
- [Multiplicación Matriz-Vector](#multiplicación-matriz-vector)
- [Matrices 2×2: Mid/Side](#matrices-2×2-midside)
- [Determinante e Inversa](#determinante-e-inversa)
- [Matrices 3×3: Multicanal](#matrices-3×3-multicanal)
- [Micro-laboratorio](#micro-laboratorio)
- [Checklist de Conceptos](#checklist-de-conceptos)
- [Ejercicios](#ejercicios)

## Definición y Notación

### Matriz m×n

Una matriz $A$ de $m$ filas y $n$ columnas:

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

Notación: $A \in \mathbb{R}^{m \times n}$

### Matriz Cuadrada

Cuando $m = n$, la matriz es **cuadrada**. Casos importantes:

- **Matriz identidad** $I$: diagonal con unos
  $$
  I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
  $$

- **Matriz diagonal**: solo elementos en diagonal principal
  $$
  D = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}
  $$
  (aplicar ganancias independientes)

## Multiplicación Matriz-Vector

### Definición

Para $A \in \mathbb{R}^{m \times n}$ y $\vec{x} \in \mathbb{R}^n$:

$$
\vec{y} = A\vec{x} \in \mathbb{R}^m
$$

Cada componente:

$$
y_i = \sum_{j=1}^{n} a_{ij} x_j
$$

### Ejemplo: Ganancia Diferencial

$$
A = \begin{bmatrix} 2 & 0 \\ 0 & 0.5 \end{bmatrix}, \quad
\vec{x} = \begin{bmatrix} 0.8 \\ 0.6 \end{bmatrix}
$$

$$
\vec{y} = A\vec{x} = \begin{bmatrix} 2 \cdot 0.8 + 0 \cdot 0.6 \\ 0 \cdot 0.8 + 0.5 \cdot 0.6 \end{bmatrix}
= \begin{bmatrix} 1.6 \\ 0.3 \end{bmatrix}
$$

**Interpretación**: Canal L amplificado +6dB, canal R atenuado -6dB.

## Matrices 2×2: Mid/Side

### Concepto Mid/Side

Transformar señal estéreo L/R a Mid/Side:

- **Mid (M)**: Suma de L y R (señal mono, centro)
- **Side (S)**: Diferencia de L y R (información estéreo)

### Encoding: L/R → M/S

$$
\begin{bmatrix} M \\ S \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} L \\ R \end{bmatrix}
$$

Expandido:

$$
M = L + R
$$
$$
S = L - R
$$

### Decoding: M/S → L/R

$$
\begin{bmatrix} L \\ R \end{bmatrix} = \frac{1}{2} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} M \\ S \end{bmatrix}
$$

Expandido:

$$
L = \frac{M + S}{2}
$$
$$
R = \frac{M - S}{2}
$$

### Verificación

Componiendo encoding y decoding:

$$
\begin{bmatrix} L \\ R \end{bmatrix} = \frac{1}{2} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} L \\ R \end{bmatrix}
$$

Multiplicación de matrices:

$$
\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}
$$

Por tanto:

$$
\frac{1}{2} \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I
$$

Verificado: la transformación es reversible.

### Ejemplo Numérico

$$
L = 0.8, \quad R = 0.4
$$

Encoding:

$$
M = 0.8 + 0.4 = 1.2
$$
$$
S = 0.8 - 0.4 = 0.4
$$

Decoding:

$$
L = \frac{1.2 + 0.4}{2} = 0.8 \quad \checkmark
$$
$$
R = \frac{1.2 - 0.4}{2} = 0.4 \quad \checkmark
$$

## Determinante e Inversa

### Determinante de Matriz 2×2

Para

$$
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
$$

el determinante es:

$$
\det(A) = ad - bc
$$

**Significado**:

- $\det(A) \neq 0$: Transformación invertible
- $\det(A) = 0$: Transformación singular (colapsa dimensión)

### Inversa de Matriz 2×2

Si $\det(A) \neq 0$:

$$
A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
$$

**Propiedad**: $A A^{-1} = I$

### Ejemplo: Inversa de M/S Encoding

$$
A = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
$$

$$
\det(A) = 1 \cdot (-1) - 1 \cdot 1 = -2
$$

$$
A^{-1} = \frac{1}{-2} \begin{bmatrix} -1 & -1 \\ -1 & 1 \end{bmatrix}
= \frac{1}{2} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
$$

(coincide con matriz de decoding multiplicada por $1/2$).

### Determinante de Matriz 3×3

Para

$$
A = \begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
$$

usando expansión por cofactores (primera fila):

$$
\det(A) = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31})
$$

**Forma resumida**:

$$
\det(A) = a_{11} \begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix}
- a_{12} \begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix}
+ a_{13} \begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}
$$

### Ejemplo: Matriz Diagonal 3×3

$$
D = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 5 \end{bmatrix}
$$

$$
\det(D) = 2 \cdot (3 \cdot 5 - 0) - 0 + 0 = 30
$$

Para matrices diagonales: $\det(D) = d_{11} \cdot d_{22} \cdot d_{33}$

## Matrices 3×3: Multicanal

### Sistema LCR (Left-Center-Right)

Convertir señal estéreo L/R a sistema de 3 canales:

$$
\begin{bmatrix} L_{\text{out}} \\ C \\ R_{\text{out}} \end{bmatrix}
= \begin{bmatrix}
0.7 & 0 \\
0.5 & 0.5 \\
0 & 0.7
\end{bmatrix}
\begin{bmatrix} L \\ R \end{bmatrix}
$$

Donde:

- Canal centro $C$ recibe suma igual de L y R
- Canales L/R de salida atenúan entrada (0.7 ≈ -3dB)

### Ejemplo Numérico

Entrada: $L = 0.8$, $R = 0.6$

$$
L_{\text{out}} = 0.7 \cdot 0.8 + 0 \cdot 0.6 = 0.56
$$
$$
C = 0.5 \cdot 0.8 + 0.5 \cdot 0.6 = 0.70
$$
$$
R_{\text{out}} = 0 \cdot 0.8 + 0.7 \cdot 0.6 = 0.42
$$

### Matriz de Rotación 2D

Rotar imagen estéreo por ángulo $\theta$:

$$
R(\theta) = \begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
$$

**Ejemplo**: Rotar 45° (enfatizar centro)

$$
R(45°) = \begin{bmatrix}
0.707 & -0.707 \\
0.707 & 0.707
\end{bmatrix}
$$

Para $\vec{x} = [L, R]^T$, aplicar $\vec{y} = R(45°) \vec{x}$ mueve información hacia el centro.

## Micro-laboratorio

### Objetivo

Implementar M/S encoding y decoding en Python, verificar reversibilidad.

### Setup

```python
import numpy as np

# Señal estéreo sintética
L = np.array([0.8, 0.6, -0.4, 0.2])
R = np.array([0.4, 0.8, -0.2, 0.1])

# Matrices M/S
MS_encode = np.array([
    [1, 1],
    [1, -1]
])

MS_decode = 0.5 * np.array([
    [1, 1],
    [1, -1]
])
```

### Tareas

1. **Encoding L/R → M/S**

```python
# Stack L y R como columnas (cada muestra por separado)
# O procesar todo el buffer sample-by-sample

M = L + R
S = L - R

print("Mid:", M)
print("Side:", S)
```

2. **Decoding M/S → L/R**

```python
L_decoded = 0.5 * (M + S)
R_decoded = 0.5 * (M - S)

print("L original:", L)
print("L decoded:", L_decoded)
print("Match:", np.allclose(L, L_decoded))
```

### Código Completo

```python
import numpy as np

L = np.array([0.8, 0.6, -0.4, 0.2])
R = np.array([0.4, 0.8, -0.2, 0.1])

# Encoding
M = L + R
S = L - R

print("=== Encoding ===")
print(f"L: {L}")
print(f"R: {R}")
print(f"M: {M}")
print(f"S: {S}")

# Decoding
L_dec = 0.5 * (M + S)
R_dec = 0.5 * (M - S)

print("\n=== Decoding ===")
print(f"L decoded: {L_dec}")
print(f"R decoded: {R_dec}")

print("\n=== Verification ===")
print(f"L match: {np.allclose(L, L_dec)}")
print(f"R match: {np.allclose(R, R_dec)}")
```

**Salida esperada**:
```
=== Encoding ===
L: [ 0.8  0.6 -0.4  0.2]
R: [ 0.4  0.8 -0.2  0.1]
M: [ 1.2  1.4 -0.6  0.3]
S: [ 0.4 -0.2 -0.2  0.1]

=== Decoding ===
L decoded: [ 0.8  0.6 -0.4  0.2]
R decoded: [ 0.4  0.8 -0.2  0.1]

=== Verification ===
L match: True
R match: True
```

### Preguntas

- ¿Qué representa una señal con $S = 0$?
- ¿Cómo afecta amplificar solo el canal Side al ancho estéreo?
- Calcula el determinante de la matriz de encoding.

## Checklist de Conceptos

Antes de continuar, verifica que puedes:

- [ ] Multiplicar matriz 2×2 por vector
- [ ] Explicar encoding/decoding Mid/Side
- [ ] Calcular determinante de matriz 2×2 y 3×3
- [ ] Calcular inversa de matriz 2×2
- [ ] Interpretar matriz diagonal como ganancias
- [ ] Verificar reversibilidad con multiplicación matricial
- [ ] Implementar transformaciones en NumPy

## Ejercicios

### Ejercicio 1: Determinante

Calcula el determinante de:

$$
A = \begin{bmatrix} 3 & 2 \\ 1 & 4 \end{bmatrix}
$$

**Solución**:

$$
\det(A) = 3 \cdot 4 - 2 \cdot 1 = 12 - 2 = 10
$$

### Ejercicio 2: Inversa

Encuentra la inversa de:

$$
B = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}
$$

**Solución**:

$$
\det(B) = 2 \cdot 1 - 1 \cdot 1 = 1
$$

$$
B^{-1} = \frac{1}{1} \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}
= \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}
$$

Verificación:

$$
BB^{-1} = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}
= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \quad \checkmark
$$

### Ejercicio 3: M/S con Ángulo Arbitrario

Generaliza M/S usando ángulo $\theta$:

$$
M = L \cos\theta + R \sin\theta
$$
$$
S = L \sin\theta - R \cos\theta
$$

¿Cuál es el valor de $\theta$ para M/S clásico?

**Solución**:

Para M/S clásico: $M = L + R$, $S = L - R$

Comparando: $\cos\theta = \sin\theta = 1/\sqrt{2}$

Por tanto: $\theta = 45°$

### Ejercicio 4: Sistema LCR

Dada la matriz LCR del texto, calcula salidas para entrada $L = 1.0$, $R = 0.0$ (señal mono hard-panned izquierda).

**Solución**:

$$
\begin{bmatrix} L_{\text{out}} \\ C \\ R_{\text{out}} \end{bmatrix}
= \begin{bmatrix}
0.7 & 0 \\
0.5 & 0.5 \\
0 & 0.7
\end{bmatrix}
\begin{bmatrix} 1.0 \\ 0.0 \end{bmatrix}
= \begin{bmatrix} 0.7 \\ 0.5 \\ 0.0 \end{bmatrix}
$$

Interpretación: La señal panned izquierda aparece mayormente en L (70%), parcialmente en C (50%), nada en R.

### Ejercicio 5: Implementación

Implementa una función que rote un vector 2D por ángulo $\theta$ en grados.

**Solución**:

```python
import numpy as np

def rotate_2d(vec, theta_deg):
    theta_rad = np.deg2rad(theta_deg)
    R = np.array([
        [np.cos(theta_rad), -np.sin(theta_rad)],
        [np.sin(theta_rad), np.cos(theta_rad)]
    ])
    return R @ vec

# Ejemplo: rotar [1, 0] por 90°
v = np.array([1.0, 0.0])
v_rot = rotate_2d(v, 90)
print(v_rot)  # [0, 1] (aprox con error numérico)
```

## Referencias

- [Capítulo 1: Vectores](cap01_vectores.md)
- [Índice del Módulo](index.md)
- [Bibliografía](../../04_recursos/bibliografia.md)

---

**Próximo**: Módulo AL5-08 - Análisis de Fourier (próximamente)
