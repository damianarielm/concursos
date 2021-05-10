% Concurso Auxiliar de 2da categoria
% Programacion I
% Damian Ariel Marotte

# Enunciado

## Practica 5: Primera parte

**Ejercicio 13**
Diseñe la funcion `cortas`{.scheme} que tome una *una lista de strings* y
devuelva una *lista* con aquellas palabras de longitud menor a 5.

*Ejemplo:*

```{.scheme}
(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")
```

# Receta

1. Diseño de datos

2. Signatura

3. Declaracion de proposito

4. Ejemplos

5. Codigo

6. Testing

7. Correccion

# Diseño de datos

Una *ListaDeStrings* es:

* `Una lista vacia        '()`{.scheme}
* `Una expresion del tipo (cons String ListaDeStrings)`{.scheme}

. . .

Predicados:

* `empty?        ; Reconoce unicamente la lista vacia`{.scheme}
* `cons?         ; Reconoce listas no vacias`{.scheme}

. . .

Selectores:

* `first         ; Devuelve el primer elemento de una lista`{.scheme}
* `rest          ; Devuelve la lista sin su primer elemento`{.scheme}

. . .

Funciones de strings:

* `string-length ; Devuelve la cantidad de caracteres de un string`{.scheme}

# Diseño de datos

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)




















```

# Signatura

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings



















```

# Declaracion de proposito

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.


















```

# Ejemplos

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.









;(cortas '())                                            == '()
;(cortas (list "Palabras" "largas"))                     == '()
;(cortas (list "Yo" "soy" "asi"))                        == (list "Yo" "soy" "asi")
;(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")





```

# Codigo

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.

(define (cortas l)





)

;(cortas '())                                            == '()
;(cortas (list "Palabras" "largas"))                     == '()
;(cortas (list "Yo" "soy" "asi"))                        == (list "Yo" "soy" "asi")
;(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")





```

# Codigo

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.

(define (cortas l)
    (cond [(empty? l)    ]                                   ; Caso base
          [(cons? l)                                         ; Caso recursivo

                                            ]
    )
)

;(cortas '())                                            == '()
;(cortas (list "Palabras" "largas"))                     == '()
;(cortas (list "Yo" "soy" "asi"))                        == (list "Yo" "soy" "asi")
;(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")





```

# Codigo

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.

(define (cortas l)
    (cond [(empty? l) '()]                                   ; Caso base
          [(cons? l)                                         ; Caso recursivo

                                            ]
    )
)

;(cortas '())                                            == '()
;(cortas (list "Palabras" "largas"))                     == '()
;(cortas (list "Yo" "soy" "asi"))                        == (list "Yo" "soy" "asi")
;(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")





```

# Codigo

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.

(define (cortas l)
    (cond [(empty? l) '()]                                   ; Caso base
          [(cons? l)  (if (< (string-length (first l)) 5)    ; Condicion
                          (                                ) ; Caso verdadero
                          (               ))]                ; Caso falso
    )
)

;(cortas '())                                            == '()
;(cortas (list "Palabras" "largas"))                     == '()
;(cortas (list "Yo" "soy" "asi"))                        == (list "Yo" "soy" "asi")
;(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")





```

# Codigo

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.

(define (cortas l)
    (cond [(empty? l) '()]                                   ; Caso base
          [(cons? l)  (if (< (string-length (first l)) 5)    ; Condicion
                          (cons (first l)                  ) ; Caso verdadero
                          (               ))]                ; Caso falso
    )
)

;(cortas '())                                            == '()
;(cortas (list "Palabras" "largas"))                     == '()
;(cortas (list "Yo" "soy" "asi"))                        == (list "Yo" "soy" "asi")
;(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")





```

# Codigo

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.

(define (cortas l)
    (cond [(empty? l) '()]                                   ; Caso base
          [(cons? l)  (if (< (string-length (first l)) 5)    ; Condicion
                          (cons (first l) (cortas (rest l))) ; Caso verdadero
                          (               ))]                ; Caso falso
    )
)

;(cortas '())                                            == '()
;(cortas (list "Palabras" "largas"))                     == '()
;(cortas (list "Yo" "soy" "asi"))                        == (list "Yo" "soy" "asi")
;(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")





```

# Codigo

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.

(define (cortas l)
    (cond [(empty? l) '()]                                   ; Caso base
          [(cons? l)  (if (< (string-length (first l)) 5)    ; Condicion
                          (cons (first l) (cortas (rest l))) ; Caso verdadero
                          (cortas (rest l)))]                ; Caso falso
    )
)

;(cortas '())                                            == '()
;(cortas (list "Palabras" "largas"))                     == '()
;(cortas (list "Yo" "soy" "asi"))                        == (list "Yo" "soy" "asi")
;(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")





```

# Testing

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.

(define (cortas l)
    (cond [(empty? l) '()]                                   ; Caso base
          [(cons? l)  (if (< (string-length (first l)) 5)    ; Condicion
                          (cons (first l) (cortas (rest l))) ; Caso verdadero
                          (cortas (rest l)))]                ; Caso falso
    )
)

;(cortas '())                                            == '()
;(cortas (list "Palabras" "largas"))                     == '()
;(cortas (list "Yo" "soy" "asi"))                        == (list "Yo" "soy" "asi")
;(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")
(check-expect (cortas '()) '())
(check-expect (cortas (list "Palabras" "largas")) '())
(check-expect (cortas (list "Yo" "soy" "asi")) (list "Yo" "soy" "asi"))
(check-expect (cortas (list "Lista" "de" "palabras" "sin" "sentido")) (list "de" "sim"))
```

# Correccion

Ran 4 tests.  
1 of the 4 tests failed.  

No signature violations.

Check failures:  
\ \ \ \ \ \ \ \ \ \ \ \ \ \ Actual value **(list "de" "sin")** differs from
                            **(list "de" "sim")**, the expected value.  
*at line 20, column 0*

# Correccion

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.

(define (cortas l)
    (cond [(empty? l) '()]                                   ; Caso base
          [(cons? l)  (if (< (string-length (first l)) 5)    ; Condicion
                          (cons (first l) (cortas (rest l))) ; Caso verdadero
                          (cortas (rest l)))]                ; Caso falso
    )
)

;(cortas '())                                            == '()
;(cortas (list "Palabras" "largas"))                     == '()
;(cortas (list "Yo" "soy" "asi"))                        == (list "Yo" "soy" "asi")
;(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")
(check-expect (cortas '()) '())
(check-expect (cortas (list "Palabras" "largas")) '())
(check-expect (cortas (list "Yo" "soy" "asi")) (list "Yo" "soy" "asi"))
(check-expect (cortas (list "Lista" "de" "palabras" "sin" "sentido")) (list "de" "sim"))
```

# Correccion

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.

(define (cortas l)
    (cond [(empty? l) '()]                                   ; Caso base
          [(cons? l)  (if (< (string-length (first l)) 5)    ; Condicion
                          (cons (first l) (cortas (rest l))) ; Caso verdadero
                          (cortas (rest l)))]                ; Caso falso
    )
)

;(cortas '())                                            == '()
;(cortas (list "Palabras" "largas"))                     == '()
;(cortas (list "Yo" "soy" "asi"))                        == (list "Yo" "soy" "asi")
;(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")
(check-expect (cortas '()) '())
(check-expect (cortas (list "Palabras" "largas")) '())
(check-expect (cortas (list "Yo" "soy" "asi")) (list "Yo" "soy" "asi"))
(check-expect (cortas (list "Lista" "de" "palabras" "sin" "sentido")) (list "de" "sin"))
```

# Testing

*All 4 test passed!*

# Codigo

```{.numberLines .scheme}
;l: ListaDeStrings (Representa la lista de cadenas a filtrar)
;cortas : ListaDeStrings -> ListaDeStrings
;Dada una lista de strings, devuelve una lista con aquellas palabras de largo menor a 5.

(define (cortas l)
    (cond [(empty? l) '()]                                   ; Caso base
          [(cons? l)  (if (< (string-length (first l)) 5)    ; Condicion
                          (cons (first l) (cortas (rest l))) ; Caso verdadero
                          (cortas (rest l)))]                ; Caso falso
    )
)

;(cortas '())                                            == '()
;(cortas (list "Palabras" "largas"))                     == '()
;(cortas (list "Yo" "soy" "asi"))                        == (list "Yo" "soy" "asi")
;(cortas (list "Lista" "de" "palabras" "sin" "sentido")) == (list "de" "sin")
(check-expect (cortas '()) '())
(check-expect (cortas (list "Palabras" "largas")) '())
(check-expect (cortas (list "Yo" "soy" "asi")) (list "Yo" "soy" "asi"))
(check-expect (cortas (list "Lista" "de" "palabras" "sin" "sentido")) (list "de" "sin"))
```
