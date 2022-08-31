% Concurso Programacion 2
% Tecnicatura Universitaria en Inteligencia Artificial
% Dámian Ariel Marotte

# Fuerza Bruta

## Problema

Perdida de contraseña.

## Algoritmo

```{.numberLines .python}
from password import primer_intento, es_solucion, siguiente

intento_actual = primer_intento()

while not es_solucion(intento_actual):
    intento_actual = siguiente(intento_actual)

print(intento_actual)
```

## Detalles

```{.numberLines .python}
alfabeto = "0123456789abcdefghijklmnopqrstuvwxyz"

def es_solucion(intento):
    return intento == "abc123"

def primer_intento():
    return "a"

def siguiente(intento):
    if intento == alfabeto[-1] * len(intento):
        return alfabeto[0] * (len(intento) + 1)
    elif intento[-1] != alfabeto[-1]:
        return intento[:-1] + alfabeto[alfabeto.find(intento[-1]) + 1]
    else:
        return siguiente(intento[:-1]) + alfabeto[0]
```

# Greedy

## Problema

Dar el vuelto.

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

## Detalles

```{.numberLines .python}
total = 6
candidatos = [4] * total + [3] * total + [1] * total

def es_solucion(eleccion_actual):
    return sum(eleccion_actual) == total

def elegir_candidato():
    return max(candidatos)

def es_factible(eleccion):
    return sum(eleccion) <= total
```

# Divide & Conquer

## Problema

Ordenar numeros.

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
