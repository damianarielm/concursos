% Concurso Programacion 3
% Tecnicatura Universitaria en Inteligencia Artificial
% Dámian Ariel Marotte

# Algoritmos de Búsqueda

## Definicion

Un algoritmo de búsqueda es un algoritmo que toma como entrada un problema y
devuelve una solución de la forma secuencia de acciones.

Para que un problema quede bien definido, necesitamos especificar los
siguientes componentes:

. . .

### Estado Inicial

Necesitamos definir cual es el estado a partir del cual empezamos a resolver
el problema.

. . .

### Funciones sucesores

Tambien necesitamos hacer una lista de todas las posibles transofrmaciones
sobre los estados, esto es, cada una de las acciones que podrian acercarnos
a la solucion.

. . .

### Test objetivo

Finalmente necesitamos una funcion que dado un estado, nos indique si se trata
de una solucion al problema, o no.

## Ejemplo

Un terrorista ha colocado una boma. En el lugar se encuentran disponibles un
bidon con capacidad para 3 litros y otro para 5 litros. Para desactivar la
bomba es necesario apoyar un bidon con exactamente 4 litros sobre una balanza.

. . .

### Estado Inicial

Partimos de un estado donde ambos bidones se encuentran vacios.

. . .

### Funciones sucesores

Las acciones que podemos realizar son:

* Vaciar el bidon de 3 litros.
* Vaciar el bidon de 5 litros.
* Llenar el bidon de 3 litros.
* Llenar el bidon de 5 litros.
* Volcar el bidon de 5 litros en el de 3.
* Volcar el bidon de 3 litros en el de 5.

. . .

### Test objetivo

Podemos determinar si hemos llegado a la solucion observando si hay 4 litros
en el bidon mas grande.

## ¿Como buscar?

Una vez que tenemos definido nuestro problema, podemos buscar una solucion
confeccionando un grafo de busqueda y recorriendo cada uno de sus nodos.

En un grafo de busqueda cada uno de los nodos corresponde con un posible estado
del problema, y cada arista es una de las acciones disponibles en el.

. . .

![Grafo de busqueda](arbol.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

. . .

![Empezamos con el nodo inicial](1.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Realizamos el test objetivo](2.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Generamos sus sucesores](3.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Consideramos el siguiente nodo](4.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Generamos sus sucesores](5.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Consideramos el siguiente nodo](6.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Generamos sus sucesores](7.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Consideramos el siguiente nodo](8.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Generamos sus sucesores](9.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Consideramos el siguiente nodo](10.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Generamos sus sucesores](11.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Consideramos el siguiente nodo](12.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Generamos sus sucesores](13.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Consideramos el siguiente nodo](14.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Generamos sus sucesores](15.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Consideramos el siguiente nodo](16.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Generamos sus sucesores](17.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Consideramos el siguiente nodo](18.png "arbol"){width=60%}

------------------------------

### Recorrido en profundidad

La idea de un recorrido en profundidad es expandir siempre el nodo mas
profundo del grafo hasta que ya no sea posible, en cuyo caso se vuelve hacia
atras y se continua con el siguiente.

![Recorrido en profundidad](profundidad.png "arbol"){width=60%}

------------------------------

### Recorrido en anchura

La búsqueda primero en anchura es una estrategia sencilla en la que se expande
primero el nodo raíz, a continuación se expanden todos los sucesores del nodo
raíz, después sus sucesor, etc.

![Recorrido en anchura](anchura.png "arbol"){width=60%}

------------------------------

### Características

* Si nuestro grafo no es un arbol, debemos tener un cuidado especial: tenemos
que evitar recorrer los ciclos, pues quedaremos atrapados en un bucle infinito.

. . .

* La busqueda en profundidad ocupa menos memoria, pero podría no encontrar la
solución: si una rama se puede expandir infinitamente el algoritmo nunca
visitara las demas ramas.
Además, no garantiza encontrar la solucion con menor cantidad de aristas.

. . .

* La busqueda a lo ancho garantiza encontrar la solucion que recorre la menor
cantidad de aristas, pero ocupa mucha mas memoria.

. . .

* Ambos son algoritmos de fuerza bruta no informados, esto es, que no tienen
ninguna prioridad particular a la hora de elegir un nodo.

. . .

* Si nuestros operadores tienen un costo asociado, ninguno de los algoritmos
garantiza encontrar la solucion de menor costo.

## Algoritmo general

```{.python .numberLines}
def busqueda(inicial):
    visitados = []
    nodos = [inicial]

    while nodos:
        nodo = nodos.pop()

        if nodo.test_objetivo():
            return nodo.acciones
        elif nodo not in visitados:
            visitados.append(nodo)

            for s in nodo.sucesores():
                nodos.append(s)
```

## Solucion al problema

```{.python .numberLines}
class Nodo:
    def __init__(self, bidon3 = 0, bidon5 = 0, acciones = ""):
        self.bidon3, self.bidon5, self.acciones = bidon3, bidon5, acciones
    def __eq__(self, other):
        return self.bidon3 == other.bidon3 and self.bidon5 == other.bidon5
    def test_objetivo(self):
        return self.bidon5 == 4
    def llenar3(self): # Analogo para el bidon de 5 litros.
        self.bidon3 = 3
        self.acciones += "Llenar 3. "
    def vaciar3(self): # Analogo para el bidon de 5 litros.
        self.bidon3 = 0
        self.acciones += "Vaciar 3. "
    def volcar3(self): # Analogo para el bidon de 5 litros.
        volumen = min(5 - self.bidon5, self.bidon3)
        self.bidon3, self.bidon5 = self.bidon3 - volumen, self.bidon5 + volumen
        self.acciones += "Volcar 3. "
    def sucesores(self):
        s1 = Estado(self.bidon3, self.bidon5, self.acciones).llenar3()
        s2 = Estado(self.bidon3, self.bidon5, self.acciones).vaciar3()
        s3 = Estado(self.bidon3, self.bidon5, self.acciones).mover3()
        # Analogo para el bidon de 5 litros...
        return [ s1, s2, s3, s4, s5, s6 ]
```

--------------------------------------

```python
>>> print(busqueda(Nodo()))
Llenar 5. Volcar 5. Vaciar 5. Volcar 3. Llenar 3. Volcar 3. Vaciar 5. Volcar 3.
Llenar 3. Volcar 3.
```

## Recursos

* Stuart Russell & Peter Norvig - Inteligencia Artificial

* https://www.mathsisfun.com/games/jugs-puzzle.html

* https://www.youtube.com/watch?v=giM1Xdu5SlE
