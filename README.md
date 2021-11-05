# Curso Profesional de Python

Python es un lenguaje interpretado lo que significa que tu código es transformado por el intérprete (máquina virtual de Python) a bytecode antes de ser ejecutado por un ordenador con x sistema operativo. El bytecodees un lenguaje de programación de más bajo nivel (si esto no te es claro, te recomiendo que vayas a tomar los cursos sobre lenguajes y paradigmas de programación y el de fundamentos de ing. de software. (Básicamente desde que corres tu programa hasta que la PC lo ejecuta hay una carrera de relevos de lenguajes o protocolos hasta llegar al transistor y la señal eléctrica)

Garbage collector
Recuerda que el garbage collector toma los objetos y variables que no están en uso y los elimina.

Pycache
_pycache _ es el directorio (carpeta) que contiene el bytecode (el código intermedio) que crea Python para que lo pueda leer la máquina virtual.

![alt text](https://static.platzi.com/media/user_upload/Untitled-c7a26d9b-2668-49ee-8df4-835d523cf55b.jpg)

Cómo organizar las carpetas de tus proyectos
--------------------------------------------
- Un módulo es cualquier archivo de Python. Generalmente, contiene código que puedes reutilizar.
- Un paquete es un conjunto de módulos. Siempre posee el archivo __init__.py.
- Una ejemplo de organizar los archivos de 🐍Python es de la siguiente manera.

![alt text](https://static.platzi.com/media/user_upload/paquettes-5a4095f3-0811-4e56-8f06-296b42b2e497.jpg)

¿Qué son los tipados?
---------------------
Los tipados es una clasificación de los lenguajes de programación, tenemos cuatro tipos:
- Estático
- Dinámico
- Débil
- Fuerte


- Estático: Son los que levantan los errores de tipo en tiempo de compilación. Esto es, si al estar programando tenemos un error de tipo, entonces el lenguaje nos avisa antes de que se ejecute (mientras compila). 😯 (C/C++)
- Dinámico: Opuesto al estático, levantan los errores de tipo en el tiempo de compilación, es decir, el error sale mientras el programa se ejecuta en esa línea donde está el error. 🛑 (Python)
- Fuerte: Son los que tratan con mas severidad a los datos de diferente tipo. 😠 (Python)
- Débil: Son mas relajados con datos de diferente tipo. 🦜 (Javascript)

![alt text](https://i.imgur.com/qYICZCe.png)



El tipado del lenguaje depende de cómo trata a los tipos de datos.

El tipado estático es el que levanta un error en el tiempo de compilación, ejemplo en JAVA:
```
String str = "Hello" // Variable tipo String
str = 5 // ERROR: no se puede convertir un tipo de dato en otro de esta forma.
```

El tipado dinámico levantan el error en tiempo de ejecución, ejemplo en Python:
```
str = "Hello" # Variable tipo String
str = 5 # La variable ahora es de tipo Entero, no hay error
## TIPADO FUERTE
x = 1
y = "2"
z = x + y # ERROR: no podemos hacer estas operaciones con tipos de datos distintos entre sí.
```

El tipado débil es el que hace un cambio en un tipo de dato para poder operar con el, como lo hace JavaScript y PHP.

🐍 Python es un lenguaje de tipado 👾 Dinámico y 💪 Fuerte.

Tipado estático en Python
-------------------------
Para hacer que Python sea de tipado estático es necesario agregar algo de sintaxis adicional a lo aprendido, además, esta característica solo se puede aplicar a partir de la versión 3.6.

De esta manera se declara una variable, se colocan los dos puntos (:), el tipo de dato y para finalizar se usa el signo igual para asignar el valor a la variable.
```
<variable> : <tipo_de_dato> = <valor_asignado>

a: int = 5
print(a)

b: str = "Hola"
print(b)

c: bool = True
print(c)
```
Del mismo modo se puede usar esta metodología de tipado en Python a funciones adicionando el signo menos a continuación del signo mayor que para determinar el tipo de dato. Ejemplo:
```
def <nombre_func> ( <parametro1> : <tipo_de_dato>, <parametro2> : <tipo_de_dato> ) ->  <tipo_de_dato> :
	pass

def suma(a: int, b: int) -> int :
	return a + b

print(suma(1,2))
```
Existe una librería de fabrica que viene preinstalada con Python que se llama typing, que es de gran utilidad para trabajar con tipado con estructuras de datos entre la versión 3.6 y 3.9, entonces:

Ejemplo 1 :
```
from typing import Dict, List

positives: List [int] = [1,2,3,4,5]

users: Dict [str, int] = {
	"argentina": 1.
	"mexico": 34,
	"colombia": 45,
}

countries: List[Dict[str, str]] = [
	{
		"name" : "Argentina",
		"people" : "45000",
	},
	{
		"name" : "México",
		"people" : "9000000",
	},
	{
		"name" : "Colombia",
		"people" : "99999999999",
	}
]

Ejemplo2:
from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
	{
		"coord1": (1,2),
		"coord2": (3,5)
	},
	{
		"coord1": (0,1),
		"coord2": (2,5)
	}
]
```
Modulo mypy:
El modulo mypy se complementa con el modulo typing ya que permitirá mostrar los errores de tipado debil en Python.

El modulo mypy se complementa con el modulo typing ya que permitirá mostrar los errores de tipado débil en Python.

Para revisar si algún archivo contiene errores de tipado ejecutamos en la línea de comandos lo siguiente:

mypy "nombre del archivo" --check-untyped-defs
```
mypy palindrome.py --check-untyped-defs
```
nos muestra el error de esta manera:
```
palindrome.py:7: error: Argument 1 to "is_palindrome" has incompatible type "int"; expected "str"
Found 1 error in 1 file (checked 1 source file)
```

Scope: alcance de las variables
-------------------------------
El scope es el alcance que tienen las variables. Depende de donde declares o inicialices una variable para saber si tienes acceso. Regla de oro:
    "una variable solo esta disponible dentro de la region donde fue creada"

Local Scope
Es la región que corresponde el ámbito de una función, donde podremos tener una o mas variables, las variables van a ser accesibles únicamente en esta region y no serán visibles para otras regiones.

Global Scope
Al escribir una o mas variables en esta region, estas podrán ser accesibles desde cualquier parte del código.

Closures
--------
Es una forma de acceder a variables de otros scopes a través de una nested function. Se retorna la nested function y esta recuerda el valor que imprime, aunque a la hora de ejecutarla no este dentro de su alcance.

Nested functions: Las funciones anidadas son simplemente funciones creadas dentro de otra función. Podemos hacer return de una función creada dentro de otra función 😵 y luego guardar esas funciones en variables que podemos utilizar.
```
def main():
	a = 1
	def nested():
		print(a)
	return nested

my_func = main()
my_func()
```
Eso anterior es un closure 🤯 y es básicamente cuando una variable de un scope superior es recordada por una función de scope inferior (aunque luego se elimine la de scope superior).
```
def main():
	a = 1
	def nested():
		print(a)
	return nested

my_func = main()
my_func()

del(main)
my_func()
```


Reglas para encontrar un closure: 🔥
- Debemos tener una nested function.
- La nested function debe referenciar un valor de un scope superior.
- La función que envuelve a la nested function debe retornarla también.

Ejemplo de closures para crear funciones:
```
def make_multiplier(x):
	def multiplier(n):
		return x*n
	return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3)) # 30
print(times4(5)) #20
print(times10(times4(2))) # 80
```
Los closure aparecen en dos casos particulares: cuando tenemos una clase corta (con un solo método), los usamos para que sean elegantes. El segundo caso, es cuando usamos decoradores 👀

Decoradores
-----------
Es una función que recibe como parámetro otra función, le añade cosas y retorna una función diferente. Tienen la misma estructura que los Closures pero en vez de variables lo que se envía es una función.
```
def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje' 


print(mensaje('Cesar'))
```


![alt text](https://static.platzi.com/media/user_upload/carbon%20%289%29-a5820f5d-379e-4221-968e-428a10ce6803.jpg)