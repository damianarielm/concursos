% Concurso Programacion 2
% Tecnicatura Universitaria en Inteligencia Artificial
% Dámian Ariel Marotte

# Fuerza Bruta

## Problema

Perdida de contraseña.

## Analisis

### Intentos desordenados

* m8l
* 6ey7mf
* bc
* r3pe6aeo
* 7

. . .

### Intentos ordenados

* a
* b
* c
* d
* e

## Ingredientes

* Funcion `siguiente` que dado el intento actual, determina el siguiente.

. . .

* Funcion `es_solucion` que dado el intento actual, determina si es solucion.

## Algoritmo

```{.numberLines .python}
from password import es_solucion, siguiente

intento_actual = siguiente()

while not es_solucion(intento_actual):
    intento_actual = siguiente(intento_actual)

print(intento_actual)
```

## Caracteristicas

### Ventajas

* Es facil de implementar.
* Si existe una solucion, la encuentra.
* Si existen varias, encuentra todas.
* Si existe una solucion optima la encuentra.

. . .

### Desventajas

* Es muy costoso.

. . .

### Casos de uso

Solo tiene sentido cuando no se conoce una mejor forma de resolver el problema.

## Detalles

```{.numberLines .python}
alfabeto = "0123456789abcdefghijklmnopqrstuvwxyz"

def es_solucion(intento):
    return intento == "abcde"

def siguiente(intento = ""):
    if intento == alfabeto[-1] * len(intento):
        return alfabeto[0] * (len(intento) + 1)
    elif intento[-1] != alfabeto[-1]:
        return intento[:-1] + alfabeto[alfabeto.find(intento[-1]) + 1]
    else:
        return siguiente(intento[:-1]) + alfabeto[0]
```

## Ejemplo

* a

. . .

* b

. . .

* c

. . .

* ...
* z

. . .

* aa

. . .

* ab

. . .

* ac
* ...

. . .

* aaaaa
* ...

. . .

* abcdd
* abcde

# Greedy

## Problema

Dar el vuelto.

## Analisis

Observemos que en principio la solucion de fuerza bruta sigue estando
disponibles.

Sin embargo a veces es preferible resignar presicion con el objetivo de ganar
velocidad.

## Ingredientes

* Un conjunto de `candidatos` de donde elegir.

. . .

* Funcion `elegir_candidato` que elige la mejor opcion del momento.

. . .

* Funcion `es_factible` que determina si una determinada eleccion puede llevar
a la solucion.

. . .

* Funcion `es_solucion` que dada la seleccion actual, determina si es una
solucion al problema.

## Algoritmo

```{.numberLines .python}
from coins import es_solucion, elegir_candidato, candidatos, es_factible

eleccion_actual = []

while not es_solucion(eleccion_actual):
    x = elegir_candidato()
    candidatos.remove(x)
    if es_factible(eleccion_actual + [x]):
        eleccion_actual.append(x)

print(eleccion_actual)
```

## Caracteristicas

### Ventajas

* Es facil de implementar.
* Si existe una solucion, la encuentra.
* Es un algoritmo rapido.
* Usa poca memoria.

. . .

### Desventajas

* No siempre encuentra la mejor solucion.

. . .

### Casos de uso

Podemos usar este algoritmo cuando necesitamos una buena solucion, aunque no
necesariamente la mejor.

## Detalles

```{.numberLines .python}
total = 6
candidatos = [4] * 2 + [3] * 2 + [1] * 2

def es_solucion(eleccion_actual):
    return sum(eleccion_actual) == total

def elegir_candidato():
    return max(candidatos)

def es_factible(eleccion):
    return sum(eleccion) <= total
```

## Ejemplo

### Iteracion 0

* `candidatos = [4, 4, 3, 3, 1, 1]`.

. . .

### Iteracion 1

* `x = 4`.
* `candidatos = [4, 3, 3, 1, 1]`.
* `eleccion_actual = [4]`.

. . .

### Iteracion 2

* `x = 4`.
* `candidatos = [3, 3, 1, 1]`.
* `eleccion_actual = [4]`.

. . .

### Iteracion 3

* `x = 3`.
* `candidatos = [3, 1, 1]`.
* `eleccion_actual = [4]`.

## Ejemplo

### Iteracion 4

* `x = 3`.
* `candidatos = [1, 1]`.
* `eleccion_actual = [4]`.

. . .

### Iteracion 5

* `x = 1`.
* `candidatos = [1]`.
* `eleccion_actual = [4, 1]`.

. . .

### Iteracion 6

* `x = 1`.
* `candidatos = []`.
* `eleccion_actual = [4, 1, 1]`.

# Divide & Conquer

## Problema

Ordenar numeros.

## Analisis

```
                       [3, 5, 22, 1, 0, 2, -1, 6]
```
. . .
```
                           /                \
                     [3, 5, 22, 1]    [0, 2, -1, 6]
```
. . .
```
                        /     \          /      \
                    [3, 5]  [22, 1]   [0, 2]  [-1, 6]
```
. . .
```
                     /   \   /    \    /   \    /  \
                   [3]  [5] [22] [1]  [0] [2] [-1] [6]
```
. . .
```
                     \   /   \    /    \   /    \  /
                    [3, 5]  [1, 22]   [0, 2]  [-1, 6]
```
. . .
```
                        \     /          \      /
                     [1, 3, 5, 22]    [-1, 0, 2, 6]
```
. . .
```
                           \                /
                       [-1, 0, 1, 2, 3, 5, 6, 22]
```
## Ingredientes

* Funcion `es_caso_base` que dado un problema determina si el problema es
trivial.

. . .

* Funcion `dividir` que dado un problema, lo divide en dos problemas mas
pequeños.

. . .

* Funcion `fusionar` que dados dos problemas resueltos, los combina en una
unica solucion.

## Algoritmo

```{.numberLines .python}
from sort import problema, es_caso_base, dividir, fusionar

def resolver(problema):
    if es_caso_base(problema):
        return problema

    subproblema1, subproblema2 = dividir(problema)
    solucion1, solucion2 = resolver(subproblema1), resolver(subproblema2)

    return fusionar(solucion1, solucion2)

print(resolver(problema))
```

## Caracteristicas

### Ventajas

* Es facil de implementar.
* Suele ser un algoritmo rapido.
* Si existe una solucion, la encuentra.

. . .

### Desventajas

* No puede aplicarse siempre.
* Puede consumir mucha memoria.

. . .

### Casos de uso

Solo puede usarse si es factible dividir el problema y combinar las soluciones
independientes para formar la solucion general.

## Detalles

```{.numberLines .python}
problema = [3, 5, 22, 1, 0, 2, -1, 6, 7, 11]

def es_caso_base(problema):
    return len(problema) <= 1

def dividir(problema):
    mitad = len(problema) // 2
    return problema[:mitad], problema[mitad:]

def fusionar(solucion1, solucion2):
    solucion = []

    while solucion1 and solucion2:
        if solucion1[0] <= solucion2[0]:
            solucion.append(solucion1.pop(0))
        else:
            solucion.append(solucion2.pop(0))

    return solucion + (solucion1 if solucion1 else solucion2)
```

## Ejemplo

### Iteracion 0

```python
solucion1 = [1, 3, 5, 22]
solucion2 = [-1, 0, 2, 6]
solucion = []
```

. . .

### Iteracion 1

```python
solucion1 = [1, 3, 5, 22]
solucion2 = [0, 2, 6]
solucion = [-1]
```

. . .

### Iteracion 2

```python
solucion1 = [1, 3, 5, 22]
solucion2 = [2, 6]
solucion = [-1, 0]
```

. . .

### Iteracion 3

```python
solucion1 = [3, 5, 22]
solucion2 = [2, 6]
solucion = [-1, 0, 1]
```

## Ejemplo

### Iteracion 4

```python
solucion1 = [3, 5, 22]
solucion2 = [6]
solucion = [-1, 0, 1, 2]
```

. . .

### Iteracion 5

```python
solucion1 = [5, 22]
solucion2 = [6]
solucion = [-1, 0, 1, 2, 3]
```

. . .

### Iteracion 6

```python
solucion1 = [22]
solucion2 = [6]
solucion = [-1, 0, 1, 2, 3, 5]
```

. . .

### Iteracion 7

```python
solucion1 = [22]
solucion2 = []
solucion = [-1, 0, 1, 2, 3, 5, 6]
```
