% Concurso JTP
% Lenguajes Formales y Computabilidad
% Damian Ariel Marotte

# Enunciado

**Ejercicio 1b**
Definir como $FRP$ a la funcion $TR(a, b, c)$ la cual determina si los argumentos
conforman un triangulo rectangulo o no. Donde $TR(a, b, c) = 1$ si $a, b, c$ se
corresponde con los lados de un triangulo rectangulo y $TR(a, b, c) = 0$ si
$a, b, c$ no forman un triangulo rectangulo.

Recuerde que en un triangulo rectangulo la suma de los cuadrados de los catetos
es igual al cuadrado de la hipotenusa.

# Cuadrado

* $\square^{\left(1\right)}\left(x\right)=x\cdot x$

. . .

* $\square^{\left(1\right)}=\Phi\left(\Pi^{\left(2\right)},p_{1}^{\left(1\right)},p_{1}^{\left(1\right)}\right)$

# Delta

* $\Delta^{\left(3\right)}\left(x,y,z\right)=
   \begin{cases}
       1 & \text{si }x^{2}+y^{2}=z^{2}\\
       0
   \end{cases}$

. . .

* $\Delta^{\left(3\right)}\left(x,y,z\right)=E^{\left(2\right)}\left({\color{red}x^{2}}+{\color{blue}y^{2}},{\color{magenta}z^{2}}\right)=E^{\left(2\right)}\left({\color{red}\square^{\left(1\right)}\left(x\right)}+{\color{blue}\square^{\left(1\right)}\left(y\right)},{\color{magenta}\square^{\left(1\right)}\left(z\right)}\right)=$
  $=E^{\left(2\right)}\left(\Sigma^{\left(2\right)}\left({\color{red}\square^{\left(1\right)}\left(x\right)},{\color{blue}\square^{\left(1\right)}\left(y\right)}\right),{\color{magenta}\square^{\left(1\right)}\left(z\right)}\right)$

. . .

* $\Delta^{\left(3\right)}=\Phi\left(E^{\left(2\right)},\Phi\left(\Sigma^{\left(2\right)},{\color{red}\Phi\left(\square^{\left(1\right)},p_{1}^{\left(3\right)}\right)},{\color{blue}\Phi\left(\square^{\left(1\right)},p_{2}^{\left(3\right)}\right)}\right),{\color{magenta}\Phi\left(\square^{\left(1\right)},p_{3}^{\left(3\right)}\right)}\right)$

# TR

* $TR^{\left(3\right)}\left(a,b,c\right)={\color{red}\Delta^{\left(3\right)}\left(a,b,c\right)}\lor{\color{blue}\Delta^{\left(3\right)}\left(a,c,b\right)}\lor{\color{magenta}\Delta^{\left(3\right)}\left(b,c,a\right)}$

. . .

* $TR^{\left(3\right)}={\color{red}\Phi\left(\Delta^{\left(3\right)},p_{1}^{\left(3\right)},p_{2}^{\left(3\right)},p_{3}^{\left(3\right)}\right)}\lor{\color{blue}\Phi\left(\Delta^{\left(3\right)},p_{1}^{\left(3\right)},p_{3}^{\left(3\right)},p_{2}^{\left(3\right)}\right)}\lor{\color{magenta}\Phi\left(\Delta^{\left(3\right)},p_{2}^{\left(3\right)},p_{3}^{\left(3\right)},p_{1}^{\left(3\right)}\right)}=$
  $=\Phi\left(\bigvee^{\left(2\right)},\Phi\left(\bigvee^{\left(2\right)},{\color{red}\alpha^{\left(3\right)}},{\color{blue}\beta^{\left(3\right)}}\right),{\color{magenta}\gamma^{\left(3\right)}}\right)$

# Or

$x$ $y$  $x+y$   $D_{0}^{\left(1\right)}\left(x+y\right)$   $D_{0}^{\left(1\right)}\left(D_{0}^{\left(1\right)}\left(x+y\right)\right)$
--- --- ------- ------------------------------------------ -----------------------------------------------------------------------------
 0   0     0                         1                     0
 0   1     1                         0                     1
 1   0     1                         0                     1
 1   1     2                         0                     1

. . .

* $\bigvee^{\left(2\right)}\left(x,y\right)=
   \begin{cases}
     0 & \text{si }x=y=0\\
     1
   \end{cases}$

. . .

* $\bigvee^{\left(2\right)}=\Phi\left(D_{0}^{\left(1\right)},\Phi\left(D_{0}^{\left(1\right)},\Phi\left(\Sigma^{\left(2\right)},p_{1}^{\left(2\right)},p_{2}^{\left(2\right)}\right)\right)\right)$

# Ejercicio MT

Sea
$$f(n) = \begin{cases}
           n / 2  & $si $ n $ es par$ \\
           3n + 1 & $si $ n $ es impar$
         \end{cases}$$

Construya una maquina de turing *F* que recibe una cinta con un numero natural
escrito como una sucesion de puntos y con el cabezal a la izquierda del primer
punto; y devuelva una cinta con la *minima* cantidad de aplicaciones sucesivas
de $f$ que son necesarias para llegar a 1. La cinta final debe contener la
respuesta solamente y debe finalizar con el cabezal a la izquierda del primer
punto.

Por ejemplo:

* $f(f(f(8))) = 1$, por lo que $F(8) = 3$.

* $f(f(f(f(f(f(f(f(f(13))))))))) = 1$, por lo que $F(13) = 9$.

*Ayuda*: no intente resolver analiticamente cual es el mınimo numero de veces
que se necesita aplicar $f$ para un argumento $n$ cualquiera con la intencion
de luego implementar dicha solucion analitica. En cambio, proponga directamente
una funcion que haga el trabajo de encontrar dicho numero por usted.
