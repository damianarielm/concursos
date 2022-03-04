% Concurso Auxiliar de 2da categoria
% Programacion II
% Damian Ariel Marotte

# Practica 6: Tercera parte (archivos)

**Ejercicio 1**
Escribir un programa, llamado `head` que reciba un archivo y un numero **N** e
imprima las primeras **N** líneas del archivo.

. . .

**lorem.txt**
```{.numberLines}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
```

. . .

**Interprete**

```python
>>> archivo = open("lorem.txt", "r")
```
. . .
```python
>>> archivo.readline()
'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor\n'
```
. . .
```python
>>> archivo.readline()
'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis\n'
```

# Practica 6: Tercera parte (archivos)

**head.py**

```python
# Representamos la ruta del archivo como una cadena y la cantidad de lineas con
# un entero.
```
. . .
```python
def head(ruta: str, n: int) -> None:
```
. . .
```python
    """
    Dada la 'ruta' de un archivo y un numero de lineas 'n', imprime las
    primeras 'n' lineas de dicho archivo.















```

# Practica 6: Tercera parte (archivos)

**head.py**

```python
# Representamos la ruta del archivo como una cadena y la cantidad de lineas con
# un entero.
def head(ruta: str, n: int) -> None:
    """
    Dada la 'ruta' de un archivo y un numero de lineas 'n', imprime las
    primeras 'n' lineas de dicho archivo.

    Ejemplos:

    >>> head('lorem.txt', 1)
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor

    >>> head('lorem.txt', 2)
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis

    >>> head('/dev/null', 4)
    """
```

# Practica 6: Tercera parte (archivos)

**head.py**

```{.numberLines .python}
# Representamos la ruta del archivo como una cadena y la cantidad de lineas con
# un entero.
def head(ruta: str, n: int) -> None:
    """
    Dada la 'ruta' de un archivo y un numero de lineas 'n', imprime las
    primeras 'n' lineas de dicho archivo.

    Ejemplos:

    >>> head('lorem.txt', 1)
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor

    >>> head('lorem.txt', 2)
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis

    >>> head('/dev/null', 4)
    """
    with open(ruta, "r") as archivo:
        for _ in range(n):
            print(archivo.readline())
```

# Practica 6: Tercera parte (archivos)

```bash
$ python -m doctest head.py
```
. . .
```
**********************************************************************
File "/home/damian/head.py", line 10, in head.head
Failed example:
    head('lorem.txt', 1)
Expected:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
Got:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    <BLANKLINE>
**********************************************************************
File "/home/damian/head.py", line 13, in head.head
Failed example:
    head('lorem.txt', 2)
Expected:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
Got:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    <BLANKLINE>
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    <BLANKLINE>
**********************************************************************
```

# Practica 6: Tercera parte (archivos)

**head.py**

```{.numberLines .python}
# Representamos la ruta del archivo como una cadena y la cantidad de lineas con
# un entero.
def head(ruta: str, n: int) -> None:
    """
    Dada la 'ruta' de un archivo y un numero de lineas 'n', imprime las
    primeras 'n' lineas de dicho archivo.

    Ejemplos:

    >>> head('lorem.txt', 1)
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor

    >>> head('lorem.txt', 2)
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis

    >>> head('/dev/null', 4)
    """
    with open(ruta, "r") as archivo:
        for _ in range(n):
            print(archivo.readline())
```

# Practica 6: Tercera parte (archivos)

**head.py**

```{.numberLines .python}
# Representamos la ruta del archivo como una cadena y la cantidad de lineas con
# un entero.
def head(ruta: str, n: int) -> None:
    """
    Dada la 'ruta' de un archivo y un numero de lineas 'n', imprime las
    primeras 'n' lineas de dicho archivo.

    Ejemplos:

    >>> head('lorem.txt', 1)
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor

    >>> head('lorem.txt', 2)
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis

    >>> head('/dev/null', 4)
    """
    with open(ruta, "r") as archivo:
        for _ in range(n):
            print(archivo.readline(), end="")
```

# Practica 6: Tercera parte (archivos)

```bash
$ python -m doctest head.py -v
```
```
Trying:
    head('lorem.txt', 1)
Expecting:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
ok
Trying:
    head('lorem.txt', 2)
Expecting:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
ok
Trying:
    head('/dev/null', 4)
Expecting nothing
ok
1 items had no tests:
    head
1 items passed all tests:
   3 tests in head.head
3 tests in 2 items.
3 passed and 0 failed.
Test passed.
```

# Practica 6: Tercera parte (archivos)

**Ejercicio 2**
Escribir un programa, llamado `cp.py`, que copie todo el contenido de un
archivo a otro, de modo que quede exactamente igual.

*Observación: usar `archivo.read(bytes)` para leer como máximo una cantidad
de bytes.*

. . .

```python
# Representamos las rutas de los archivos como cadenas y la cantidad de bytes
# con un entero.
```
. . .
```python
def cp(ruta_org: str, ruta_dst: str, n: int) -> None:
```
. . .
```python
    """
    Dada las rutas de los archivos origen y destino, copia como maximo 'n'
    bytes del archivo origen en la ruta destino.
    """











```

# Practica 6: Tercera parte (archivos)

**Ejercicio 2**
Escribir un programa, llamado `cp.py`, que copie todo el contenido de un
archivo a otro, de modo que quede exactamente igual.

*Observación: usar `archivo.read(bytes)` para leer como máximo una cantidad
de bytes.*

```{.numberLines .python}
# Representamos las rutas de los archivos como cadenas y la cantidad de bytes
# con un entero.
def cp(ruta_org: str, ruta_dst: str, n: int) -> None:
    """
    Dada las rutas de los archivos origen y destino, copia como maximo 'n'
    bytes del archivo origen en la ruta destino.
    """
    with open(ruta_org, "rb") as origen:
        with open(ruta_dst, "wb") as destino:
            destino.write(origen.read(n))
```

. . .

**Interprete Python**
```python
>>> cp("/bin/cat", "/tmp/cat", 50000)
```

. . .

**Bash**
```bash
$ sha1sum /bin/cat /tmp/cat
eec36875ac1c33d5544df46334debc0af8249179  /bin/cat
eec36875ac1c33d5544df46334debc0af8249179  /tmp/cat
```
