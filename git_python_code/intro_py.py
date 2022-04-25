# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:37:25 2021

@author: emman
"""

import matplotlib.pyplot as plt
import numpy as np
### tipo de variables
a = 5  # int
type(a)
b = 5.  # float
type(b)
STRING = "# Este no es un comentario"  # cadena (asignas el nombre de la cadena)
type(STRING)
c = True
type(c)
print(STRING)
print("STRING")
print("El valor de la variable a es:", a, "unidades")


# =============================================================================
# Operadores Aritméticos básicas
# =============================================================================
"""
Símbolo Operación
+       Suma
−       Resta
∗       Producto
∗∗      Potencia
/       División
//      División entera
%       Módulo
"""

# =============================================================================
# Operadores aritméticos: de números reales y enteros.
# =============================================================================
# """
r = 3+2    # + Suma
r = 4-7    # -	 Resta
r = -7     # -	Negación
r = 2*6    # *	Multiplicación
r = 2**6   # **	Exponente
r = 3.5/2  # /	División
r = 3.5//2  # //	División Entera
r = 7 % 2    # %	Módulo


# =============================================================================
# Operadores Lógicos
# =============================================================================
"""
Símbolo  Operación
and, &   “and” lógico
or, |    “or” lógico
not      negación lógica

"""

# =============================================================================
# Operadores de Asignación
# =============================================================================
a = 5  # Asigna a la variable a cualquier variable o resultado del lado derecho
a += 3  # Suma a la variable a el valor del lado derecho (a = a + 3)
# Resta a la variable del lado izquierdo el valor del lado derecho (a = a - 3)
a -= 3
# Multiplica a la variable del lado izquierdo el valor del lado derecho (a = 3*a)
a *= 3
#Ejemplo

b=5
b*=3
print(b)

# =============================================================================
# Operadores de comparación
# =============================================================================
print(a == b)  # True si a es igual a b
a != b  # True si a es diferente de b
a > b  # True si a es mayor que b
a < b  # True si a es menor que b
a >= b  # True si a es mayor o igual que b
a <= b  # True si a es mayor o igual que b

# Condicionales
# Python hace uso de variables booleanas para evaluar condiciones. Cuando una expresión es comparada o evaluada los valores que se retorna son falso o verdadero. Por ejemplo:
# operadores relacionales
x = 2
y = 3
print(x == y)  # == Igual que
print(x < y)  # < menor que
print(x <= y)  # <= menor o igual que
print(x != y)  # != Diferente a
print(x > y)  # > mayor que
print(x >= y)  # <= mayor o igual que

# =============================================================================
# Cadenas de caracteres
# =============================================================================
""" Los caracteres deben estar encerradas en comillas simples o dobles
Las cadenas de texto literales pueden contener múltiples líneas de distintas
formas. Las líneas continuas \n indica que continuara lo de la siguiente linea
se pueden usar, con una barra invertida como el último carácter de la línea para 
indicar que la siguiente línea es la continuación lógica de la línea"""

a = 'huevos y pan '  # comillas simples
b = 'doesn\'t '     # usa \' para escapar comillas simples...
c = "doesn't"      # ...o de lo contrario usa comillas doblas
a + b + c
type(a)
hola = " Esta es una larga cadena que contiene varias líneas\n\
Notar que los espacios en blanco al principio de la linea \n\
son significantes."
print(hola)  # Entre parentesis, es una función.

# Concatenar +
palabra = 'Tengo' + 'Hambre'
print(palabra)
print(5*palabra)  # Repite la cadena

'cad' 'ena'  # Concatena tambien

# Los índices empiezan en 0
palabra[0]
palabra[2:]  # Despúes de los primeros dos caracteres
palabra[2:-1]  # No incluye el último
palabra[:2] + palabra[2:]  # Concatena
palabra[-2]  # Cuenta inversa: el penúltimo carácter
len(palabra)  # longitud de la cadena

# =============================================================================
# Tipos de datos complejos: contenedores
# =============================================================================
""" Python, posee además de los tipos ya vistos, 3 tipos más complejos, que admiten una
colección de datos"""

# =============================================================================
# Tuplas
# =============================================================================
"""
Una tupla es una variable que permite almacenar varios datos
(que no pueden ser modificados una vez creados) de tipos diferentes:
Secuencias ordenadas de elementos, separados por comas y usualmente entre
paréntesis. Se le pueden aplicar operaciones similares a las de cadenas.
"""

r = (1, 2, 3, 4)
# Se puede acceder a cada uno de los datos mediante su índice correspondiente, siendo 0 (cero), el índice del primer elemento:
print(r[1])
print(r[:])  # Es lo mismo que r[::]
print(r[::-1])
r[2] = 4  # Inmutables (Igual para los str)
3*r

a, b, c = 1, 2, 3
a, b, *c = (1, 2, 3, 4)
type(c)

# También se puede acceder a una porción de la tupla, indicando (opcionalmente) desde el índice de inicio hasta el índice de fin.
print(r[1:3])
print(r[2:])
print(r[:2])


# Otra forma de acceder a la tupla de forma inversa (de atrás hacia adelante), es colocando un índice negativo:
print(r[-1])
print(r[-2])

# =============================================================================
# listas
# =============================================================================
"""Secuencias ordenadas de elementos, separados por comas o entre corchetes.
Una lista es similar a una tupla con la diferencia fundamental de que permite modificar los
datos una vez creados.
"""

a = ['pan', 'leche', 100, 1234]
a[2] = a[2] + 23  # Suma a lo que es numérico (a[2] += 23)
# Reemplazar algunos elementos:
a[0:2] = [1]  # Mutables
print(a)
# Borrar algunos:
a[0:2] = []
# Insertar algunos:
a[1:1] = ['Más', 'hambre']
# Insertar (una copia de) la misma lista al principio (es lo mismo que a[0:0] = a)
a[:0] = a  # Es lo mismo que 2*a
# Insertar al final de la lista (es lo mismo que a[len(a):len(a)] = a)
a[len(a):] = ["menos"]
# Vaciar la lista: reemplazar todos los items con una lista vacía
a[:] = []
a
# Longitud de la lista
a = ['a', 'b', 'c', 'd']
len(a)

# Lista de listas
q = [2, 3]
q.append(4)  # Agrega un valor a una lista
print(q)
p = [1, q, 4]
p[1][0]
print(p)

# =============================================================================
# Algunos métodos en listas
# =============================================================================
[i for i in range(2, 51)]
[(x, y) for x in [1, 2, 3] for y in ["a", "b", "c"]]
[0]*5 #crea una lista con 5 ceros
x = ["tengo", "hambre"]
type(x)
x.__str__()  # Representacion en cadena de caracteres´
# Agrega un ítem al final de la lista. Equivale a x[len(x):] = ["quiero"].
x.append("quiero")
print(x)
iterable = ["quesadillas", "chilaquiles"]
# Extiende la lista agregándole todos los ítems del iterable. Equivale a x[len(x):] = iterable.
x.extend(iterable)
x.insert(4, "o")  # Inserta un ítem en una posición dada.
# Quita el primer ítem de la lista cuyo valor sea x. Es un error si no existe tal ítem.
x.remove("quesadillas")
# Quita el ítem en la posición dada de la lista, y lo devuelve. Si no se especifica un índice.
x.pop(3)
x.count("quiero")  # Devuelve el número de veces que a aparece en la lista.
x.sort(reverse=False)  # Ordena los ítems de la lista in situ.
x.reverse()  # Invierte los elementos de la lista in situ.
x.clear()  # Quita todos los elementos de la lista. Equivalente a del x[:]=[].

# =============================================================================
# Conjuntos
# =============================================================================
"""Colecciones de datos, sin orden y sin duplicados,
representados entre llaves y separados por comas"""
cesta = {"peras", "manzanas", "peras", "manzanas"}
"peras" in cesta

# =============================================================================
# Diccionarios
# =============================================================================

"""Mientras que a las listas y tuplas se accede solo y únicamente por un número de índice,
los diccionarios permiten utilizar una clave para declarar y acceder a un valor:
"""

# Para más información (o seleccionar y Ctrl+i)
help(np)


mi_diccionario = {'clave_1': np.sin, 'clave_2': 'valor2', 'clave_7': [5, 3]}
print(mi_diccionario['clave_7'])  # Salida: valor_2
print(mi_diccionario)
# Un diccionario permite eliminar cualquier entrada:
del(mi_diccionario['clave_2'])
print(mi_diccionario)
print(mi_diccionario['clave_1'])
# Al igual que las listas, el diccionario permite modificar los valores
mi_diccionario['Clave_1'] = [1, 2]  # 'Nuevo Valor'
print(mi_diccionario)

mi_diccionario['clave_1'](3) #asi es como se aplica un elemto del diccionario a un valor

# =============================================================================
# Operadores
# =============================================================================
# El operador "in"
"""El operador "in" puede ser usado para checar si un objeto especifico existe mientras el
 mismo objeto itera en un contenedor, tanto com una lista:"""
name = "John"
if name in ["John", "Rick"]:
    print("Su nombre puede ser John or Rick.")

"""Python usa indentacion para definir bloques de código, en lugar de llaves o paréntesis.
El estandar de indentacion de python es 4 espacios, aunque el tab y algunos otros espacios
funcionará, siempre y cuando sean consistente, es decir tengan el mismo tipo de separación.
Los bloques de código no necesitan de una terminación.

Este es un ejemplo de como usar en python la declaración de la sentencia if usando bloques de códigos:"""

x = 2
if x == 3:
    print("x es igual tres!")
elif (x == 2):
    print("x es igual a dos!")
else:
    print("x no es igual a dos.")

"""El operador "is"
A diferencia del doble operador de igualdad "==", el operador "is" no
sola iguala los valores de las variables,
si no entre ellos, si ocupan la misma posicion en memoria. Por ejemplo
"""

y = [1, 2, 3]
x = y.copy()
print(x == y)
print(x is y)
# Podemos tener problemas al asignar x = y

# =============================================================================
# Sentencia while
# =============================================================================
# Series de Fibonacci:
a, b = 0, 1
while b < 100:
    print(b, end=',')
    a, b = b, a+b


# =============================================================================
# Sentencia if
# =============================================================================
x = int(input("Ingresa un entero, por favor: "))
if x < 0:
    x = 0
    print('Negativo cambiado a cero')
elif x == 0:
    print('Cero')
elif x == 1:
    print('Simple')
else:
    print('Más')

# =============================================================================
# Sentencia for
# =============================================================================
palabras = ['gato', 'ventana', 'defenestrado']
for i in range(5, 10):
    print(i)
for p in palabras:
    print(p, len(p))
    #funcion imprime numeros de fibonacci anteriores a n.
def fib(n):
    a, b=0,1
    while a<n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(300)

def PROM(x):
    n = len(x)   # Longitud del vector
    m = sum(x)/n  # Sumamos y dividimos entre el número de datos
    return [m, n]
    """
    PROM:
        Calcula el promedio de un conjunto de datos

    Parameters
    ----------
    x  : array
        Conjunto de datos.

    Returns
    -------
        m=promedio de x.
    """
# Ejemplo
x = [1, 5, 9, 4, 8, 4, 4, 6]
PROM(x)

"""
Las funciones lambda, filter y map

La filosofia de Python es la simplificación del código. Por tanto, se
trata de que las operaciones sobre volúmenes de datos sean simples
para el programador.

lambda
Sirve para hacer funciones “al vuelo”, que son
sencillas y no vale la pena hacer una definición de función.

filter
Crea una lista a partir de los elementos que no cumplan con
un criterio específico.

map
Se utiliza para evaluar cada uno de los elementos de una lista
en una función específica.


Las tres funciones se utilizan en conjunto, veremos ejemplos.

"""
x = 5
y = (lambda z: z+2)(7)
y(x)

""" la forma larga es 
def y(x):
    return x+2
además se puede utilizar en una linea 
"""

def y(x): 
    return np.sin(x)
y(100)

y = (lambda z: z+2)(x)

x = [1, 5, 9, 4, 8, 4, 4, 6]
# Elevar al cuadrado cada uno de los elementos de la lista x.
y = list(map(lambda l: l**2, x))
y = list(map(lambda l: 2*l, x))
print(y)

# Obtener los elementos impares de una lista x
y2 = list(filter(lambda l: l % 2, x))
print(y2)

# =============================================================================
# Leer archivos
# =============================================================================
path = 'C:\Users\emman\Desktop'
os.chdir(path)
os.getcwd()

# apertura para escritura, sobreescribiendo lo existente
f = open("PLTL 2017.1.11 masked", "w")
f.write("HELLO PEOPLE")
f.close()

# apertura para escritura, sobreescribiendo lo existente
f = open("PLTL 2017.1.11 masked", "r")
s = f.read()
f.close()

# apertura para escritura, añadiendo al final de lo existente
f = open("PLTL 2017.1.11 masked", "a")
f = open("PLTL 2017.1.11 masked", "r+")  # apertura para lectura y escritura

import csv


import pandas as pd
f = pd.read_csv(r'C:/Users/emman/Desktop/PLTL 2017.1.11 masked.csv')
#data=f.parse("PLTL 2017.1.11 masked")
#print(data.head(10))
print(f)

f.STRM = pd.Categorical(f.STRM).codes

for col_name in f.columns:
    if(f[col_name].dtype == 'object'):
        f[col_name]= f[col_name].astype('category')
        f[col_name] = f[col_name].cat.codes #cambia todas las variables tipo cadena en categoricas

### ordenar una lista programa
def searchMinList(L,n):
    minV=L[0]
    counter=1
    while(counter<n):
        v=L[counter]
        if(v<minV):
            minV=v
            idx=counter
        else:
            pass
    return minV, idx
           
def sortList(L,n):
    L2=[]
    counter=0
    while(counter<n):
        m, indx=searchMinList(L,n)
        L2.append(m)
        del L2[indx]
        n=n-1
    return L2

import random
randomlist = []   #muestra aleatoria randomlist = random.sample(range(10, 30), 5)
for i in range(0,5):
 n = random.randint(1,30)
 randomlist.append(n)
print(randomlist)

M=sortList(randomlist,i)
print(M)
randomlist.sort()
conda update -n base -c defaults conda
conda install -c conda-forge jupyterlab

##practice

a=int(input("Enter marks:"))
if a>=90:
    print("your grade is A")
elif (a<90) and (a>=80):
    print("your grade is A-")
elif (a<80) and (a>=75):
    print("your grade is B")
elif (a<75) and (a>=70):
    print("your grade is B-")
else:
    print("Below average")

x=float(input("enter a real number:"))
y=round(x)
if x>0:
    if y>x:
        int_portion=y-1
    else:
        int_portion=y
else:
    if y<x:
        int_portion=y+1
    else:
        int_portion=y
print(int_portion)
if int_portion%2==0:
    print("Even")
else:
    print("Odd")

#n=int(input("enter max iterations:"))
#i=1
#while i<n:
#    print(i)
#    i+=1
#print("done")
#fibonacci numbers Fn=Fn-1+Fn-2.
#x,y=0,1
m=int(input("enter an integer number:"))
#while y<m:
#    print(y, end=',')
#    x,y=y, x+y
# Program to check if a number is prime or not
if m>1:
    for i in range (2,m):
        if (m%i)==0:
            print(m, "is not a prime number")
            print(i, "times", m//i, "is", m)
            break
    else:
        print(m, "is a prime number")
else:
    print(i, "is not a prime number")

#print all prime numbers before a given number
k=int(input("enter an integer number:"))
for j in range (1, k):
    if j>1:
        for i in range (2,j):
            if (j%i)==0:
                break
        else:
            print(j)