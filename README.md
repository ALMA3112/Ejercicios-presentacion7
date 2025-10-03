# Ejercicios-presentacion7
## EJERCICIO 1
Gramática original
  ```
S → A B C
S → D E
A → dos B tres
A → ε
B → B cuatro C cinco
B → ε
C → seis A B
C → ε
D → uno A E
D → B
E → tres
```
a) Eliminación de recursividad por la izquierda

La regla con recursividad directa es B → B cuatro C cinco | ε. La eliminamos introduciendo Bp:
```
S  → A B C
S  → D E
A  → dos B tres | ε
B  → Bp
Bp → cuatro C cinco Bp | ε
C  → seis A B | ε
D  → uno A E | B
E  → tres
```
b) Conjuntos

PRIMEROS
```
PRIMEROS(S)  = { dos, cuatro, seis, tres, uno, ε }
PRIMEROS(A)  = { dos, ε }
PRIMEROS(B)  = { cuatro, ε }   
PRIMEROS(Bp) = { cuatro, ε }
PRIMEROS(C)  = { seis, ε }
PRIMEROS(D)  = { uno, cuatro, ε }
PRIMEROS(E)  = { tres }
```
SIGUIENTES
```
SIGUIENTES(S)  = { $ }
SIGUIENTES(A)  = { $, cinco, cuatro, seis, tres }
SIGUIENTES(B)  = { $, cinco, seis, tres }   
SIGUIENTES(Bp) = { $, cinco, seis, tres }
SIGUIENTES(C)  = { $, cinco }
SIGUIENTES(D)  = { tres }
SIGUIENTES(E)  = { $, tres }
```
PREDICCION

```
S → A B C      : { $, cuatro, dos, seis }
S → D E        : { cuatro, tres, uno }

A → dos B tres : { dos }
A → ε          : { $, cinco, cuatro, seis, tres }

B → Bp         : { $, cinco, cuatro, seis, tres } 
Bp → cuatro C cinco Bp : { cuatro }
Bp → ε         : { $, cinco, seis, tres }

C → seis A B   : { seis }
C → ε          : { $, cinco }

D → uno A E    : { uno }
D → B          : { cuatro, tres }
E → tres       : { tres }
```
## EJERCICIO 2.
Gramática original

```
S → B uno
S → dos C
S → ε
A → S tres B C
A → cuatro
A → ε
B → A cinco C seis
B → ε
C → siete B
C → ε
```
Conjuntos:

PRMEROS
```
PRIMEROS(S) = { dos, cuatro, cinco, tres, uno, ε }
PRIMEROS(A) = { cuatro, dos, cinco, tres, uno, ε }
PRIMEROS(B) = { cuatro, dos, cinco, tres, uno, ε }
PRIMEROS(C) = { siete, ε }
```
SIGUIENTES
```
SIGUIENTES(S) = { $, tres }
SIGUIENTES(A) = { cinco }
SIGUIENTES(B) = { $, cinco, seis, siete, tres, uno }
SIGUIENTES(C) = { $, cinco, seis, tres }
```

PREDICCION
```
S → B uno    : { cinco, cuatro, dos, tres, uno }
S → dos C    : { dos }
S → ε        : { $, tres }

A → S tres B C : { cinco, cuatro, dos, tres, uno }
A → cuatro     : { cuatro }
A → ε          : { cinco }

B → A cinco C seis : { cinco, cuatro, dos, tres, uno }
B → ε              : { $, cinco, seis, siete, tres, uno }

C → siete B    : { siete }
C → ε          : { $, cinco, seis, tres }
```

## EJERCICIO 3.
Gramática original
```
S → A B C
S → S uno
A → dos B C
A → ε
B → C tres
B → ε
C → cuatro B
C → ε
```
a) Eliminación de recursividad por la izquierda
La recursividad en S → S uno se elimina introduciendo Sp:
```
S  → A B C Sp
Sp → uno Sp | ε
A  → dos B C | ε
B  → C tres | ε
C  → cuatro B | ε
```
b) Conjuntos

PRIMEROS
```
PRIMEROS(S)  = { dos, cuatro, tres, uno, ε }
PRIMEROS(Sp) = { uno, ε }
PRIMEROS(A)  = { dos, ε }
PRIMEROS(B)  = { cuatro, tres, ε }
PRIMEROS(C)  = { cuatro, ε }
```
SIGUIENTES
```
SIGUIENTES(S)  = { $ }
SIGUIENTES(Sp) = { $ }
SIGUIENTES(A)  = { $, cuatro, tres, uno }
SIGUIENTES(B)  = { $, cuatro, tres, uno }
SIGUIENTES(C)  = { $, cuatro, tres, uno }
```
PREDICCION

```
S  → A B C Sp  : { $, cuatro, dos, tres, uno }
Sp → uno Sp     : { uno }
Sp → ε          : { $ }

A  → dos B C    : { dos }
A  → ε          : { $, cuatro, tres, uno }

B  → C tres     : { cuatro, tres }
B  → ε          : { $, cuatro, tres, uno }

C  → cuatro B   : { cuatro }
C  → ε          : { $, cuatro, tres, uno }
```
