% Concurso Auxiliar de 2da categoria
% Programacion I
% Damian Ariel Marotte

# Enunciado

Diseñe la funcion `sumanat`{.scheme} que toma dos *numeros naturales* y sin usar `+`{.scheme} devuelve un *natural* que es la suma de ambos.

Tenga en cuenta la definicion dada en clase de los *numeros naturales*, sus constructores, y predicados para la definicion de la funcion pedida.

# Numeros naturales

Un *Natural* es:

* `0`{.scheme}
* `(add1 Natural)`{.scheme}

. . .

Predicados:

* `zero?     ; Reconoce al natural 0`{.scheme}
* `positive? ; Reconoce naturales construidos con add1`{.scheme}

. . .

Selector:

* `sub1      ; Devuelve el predecesor de un numero natural`{.scheme}

# Receta

1. Diseño de datos

2. Signatura

3. Declaracion de proposito

4. Ejemplos

5. Codigo

6. Testing

7. Correccion

# Diseño de datos

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)


















```

# Signatura

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)





;sumanat : Natural Natural -> Natural












```

# Declaracion de proposito

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)





;sumanat : Natural Natural -> Natural
;Dados los numeros naturales n y m, devuelve el numero natural n + m











```

# Ejemplos

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)
;(sumanat 0 0) = 1 (Ambos 0)
;(sumanat 0 3) = 3 (Primero 0)
;(sumanat 7 0) = 7 (Segundo 0)
;(sumanat 2 3) = 5 (Ninguno 0)
;(sumanat 3 2) = 5 (Conmutatividad)
;sumanat : Natural Natural -> Natural
;Dados los numeros naturales n y m, devuelve el numero natural n + m











```

# Codigo

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)
;(sumanat 0 0) = 1 (Ambos 0)
;(sumanat 0 3) = 3 (Primero 0)
;(sumanat 7 0) = 7 (Segundo 0)
;(sumanat 2 3) = 5 (Ninguno 0)
;(sumanat 3 2) = 5 (Conmutatividad)
;sumanat : Natural Natural -> Natural
;Dados los numeros naturales n y m, devuelve el numero natural n + m
(define (sumanat n m)



)






```

# Codigo

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)
;(sumanat 0 0) = 1 (Ambos 0)
;(sumanat 0 3) = 3 (Primero 0)
;(sumanat 7 0) = 7 (Segundo 0)
;(sumanat 2 3) = 5 (Ninguno 0)
;(sumanat 3 2) = 5 (Conmutatividad)
;sumanat : Natural Natural -> Natural
;Dados los numeros naturales n y m, devuelve el numero natural n + m
(define (sumanat n m)
    (cond [(zero? n)                                ] ; caso base
          [(positive? n)                            ] ; caso recursivo
    )
)






```

# Codigo

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)
;(sumanat 0 0) = 1 (Ambos 0)
;(sumanat 0 3) = 3 (Primero 0)
;(sumanat 7 0) = 7 (Segundo 0)
;(sumanat 2 3) = 5 (Ninguno 0)
;(sumanat 3 2) = 5 (Conmutatividad)
;sumanat : Natural Natural -> Natural
;Dados los numeros naturales n y m, devuelve el numero natural n + m
(define (sumanat n m)
    (cond [(zero? n)      m                         ] ; caso base
          [(positive? n)                            ] ; caso recursivo
    )
)






```

# Codigo

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)
;(sumanat 0 0) = 1 (Ambos 0)
;(sumanat 0 3) = 3 (Primero 0)
;(sumanat 7 0) = 7 (Segundo 0)
;(sumanat 2 3) = 5 (Ninguno 0)
;(sumanat 3 2) = 5 (Conmutatividad)
;sumanat : Natural Natural -> Natural
;Dados los numeros naturales n y m, devuelve el numero natural n + m
(define (sumanat n m)
    (cond [(zero? n)      m                         ] ; caso base
          [(positive? n) (sumanat n m)              ] ; caso recursivo
    )
)






```

# Codigo

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)
;(sumanat 0 0) = 1 (Ambos 0)
;(sumanat 0 3) = 3 (Primero 0)
;(sumanat 7 0) = 7 (Segundo 0)
;(sumanat 2 3) = 5 (Ninguno 0)
;(sumanat 3 2) = 5 (Conmutatividad)
;sumanat : Natural Natural -> Natural
;Dados los numeros naturales n y m, devuelve el numero natural n + m
(define (sumanat n m)
    (cond [(zero? n)      m                         ] ; caso base
          [(positive? n) (sumanat (sub1 n) m)       ] ; caso recursivo
    )
)






```

# Codigo

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)
;(sumanat 0 0) = 1 (Ambos 0)
;(sumanat 0 3) = 3 (Primero 0)
;(sumanat 7 0) = 7 (Segundo 0)
;(sumanat 2 3) = 5 (Ninguno 0)
;(sumanat 3 2) = 5 (Conmutatividad)
;sumanat : Natural Natural -> Natural
;Dados los numeros naturales n y m, devuelve el numero natural n + m
(define (sumanat n m)
    (cond [(zero? n)      m                         ] ; caso base
          [(positive? n) (sumanat (sub1 n) (add1 m))] ; caso recursivo
    )
)






```

# Codigo

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)
;(sumanat 0 0) = 1 (Ambos 0)
;(sumanat 0 3) = 3 (Primero 0)
;(sumanat 7 0) = 7 (Segundo 0)
;(sumanat 2 3) = 5 (Ninguno 0)
;(sumanat 3 2) = 5 (Conmutatividad)
;sumanat : Natural Natural -> Natural
;Dados los numeros naturales n y m, devuelve el numero natural n + m
(define (sumanat n m)
    (cond [(zero? n)      m                         ] ; caso base
          [(positive? n) (sumanat (sub1 n) (add1 m))] ; caso recursivo
    )
)
(check-expect (sumanat 0 0) 0)
(check-expect (sumanat 0 3) 3)
(check-expect (sumanat 7 0) 7)
(check-expect (sumanat 2 3) 5)
(check-expect (sumanat 3 2) 9)
```

# Correccion

Ran 5 tests.  
1 of the 5 tests failed.  

No signature violations.

Check failures:  
\ \ \ \ \ \ \ \ \ \ \ \ \ \ Actual value **5** differs from **9**, the expected value.  
*at line 19, column 0*

# Correccion

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)
;(sumanat 0 0) = 1 (Ambos 0)
;(sumanat 0 3) = 3 (Primero 0)
;(sumanat 7 0) = 7 (Segundo 0)
;(sumanat 2 3) = 5 (Ninguno 0)
;(sumanat 3 2) = 5 (Conmutatividad)
;sumanat : Natural Natural -> Natural
;Dados los numeros naturales n y m, devuelve el numero natural n + m
(define (sumanat n m)
    (cond [(zero? n)      m                         ] ; caso base
          [(positive? n) (sumanat (sub1 n) (add1 m))] ; caso recursivo
    )
)
(check-expect (sumanat 0 0) 0)
(check-expect (sumanat 0 3) 3)
(check-expect (sumanat 7 0) 7)
(check-expect (sumanat 2 3) 5)
(check-expect (sumanat 3 2) 9)
```

# Correccion

```{.numberLines .scheme}
;n: Natural (Representa el primer sumando)
;m: Natural (Representa el segundo sumando)
;(sumanat 0 0) = 1 (Ambos 0)
;(sumanat 0 3) = 3 (Primero 0)
;(sumanat 7 0) = 7 (Segundo 0)
;(sumanat 2 3) = 5 (Ninguno 0)
;(sumanat 3 2) = 5 (Conmutatividad)
;sumanat : Natural Natural -> Natural
;Dados los numeros naturales n y m, devuelve el numero natural n + m
(define (sumanat n m)
    (cond [(zero? n)      m                         ] ; caso base
          [(positive? n) (sumanat (sub1 n) (add1 m))] ; caso recursivo
    )
)
(check-expect (sumanat 0 0) 0)
(check-expect (sumanat 0 3) 3)
(check-expect (sumanat 7 0) 7)
(check-expect (sumanat 2 3) 5)
(check-expect (sumanat 3 2) 5)
```

# Testing

*All 5 test passed!*
