# POO en Python
Introduccion a la Programacion Orientada a Objetos (POO)

## ¿Porque aprender POO?

- Imagina que quieres crear un video juego, tienes guerreros, magos, dragones... con sus propios puntos de vida, ataques y habilidades y aca aparece una pregunta como los organizo sin repetir todo una y otra vez?

- la **POO** es la respuesta. en lugar de escribir instrucciones sueltas modelas el mundo real con *objetos* que tienen caracteristicas y comportamientos. es la forma en que estan construidos la mayoria de los programas profecionales del mundo.

![alt text](img/poo.png)

## Clase y objeto

- Una clase es un tipo de dato cuyas variables se llaman objetos o instancia.

- la clase es la definicion de objeto del mundo real y los objetos o instancias son el propio "objeto" del mundo real.

- las clases estan compuestas por dos elementos:
    - **atributos:** informacion que almacena la clase.
    - **metodos:** operaciones que puedan realizarse con la clase.

## Definicion de una clase en python

``` py
class nombre de la clase:

    def __init__(self, variable1, variable2):
        self.atributo1 = valor1
        self.atributo2 = valor2

    def nombreMetodo(self):
        BloqueCodigo
```

-  `class` : palabra resevada en python para definir una clase

- `NombreClase` : nombre de la clase que se quiere crear

- `def` : palabra reservada en python que se utiliza para definir tanto el contructor de la clase(metodo que se ejecuta la primera vez que se usa una clase) como los diferentes metodos que tiene.

- `__init__`  : palabra reservada en python para definir el metodo constructor de la clase. el metodo `__init__`  : es lo primero que se ejecuta cuando creas un objeto de una clase.

- `self , variableX`  : parametro del contructor de la clase. el parametro `self`es obligatorio y despues puedes tener tantos parametros como quieras

`self , atributoX` : forma de utilizacion y acceso alos atrubutos de la clase

- `NombreMetodo`  : nombre del metodo de la clase

- `self` : parametro del metodo. el parametro self es obligatorio y despues puedes tener tantos parametros como quieras. la forma de añadir parametros es la misma que las funciones

- `bloquecodigo`  : instrucciones que ejecutara el metodo

**al definir una clase tenga en cuenta:**
- puedes definir tantos atributos como nesesites
- puedes definir tantos metodos como nesesites
- puedes definir tantos parametros en el contructor y en los metodos como nesesites

## Ejemplo 1
- crear una clase que represente una persona
- Atrubutos: nombre apellido y edad.
- metodos: mostrar la informacion de la persona

### Codigo

``` py
class persona:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

# Metodo para mostrar el nombre de la persona
    def mostrarpersona(self):
        print("nombre: ", self.nombre)
        print("apellidos: ", self.apellidos)
        print("edad: ", self.edad)

def main ():
    print("vamos a aprender poo...")
    persona_1 = persona(lorenzo, perez, 18)
    persona_1.mostrarpersona()

if __name__ == main():
    main()
```
## representacion grafica en ram del objeto creado
![RAM](img/RAM.jpeg)

## Composicióon

- Consiste en la creacion de nuevas clases a partir de otras clases ya existentes que actuan como elementos compositores de la nueva.

- las clases existentes seran atributos de la nueva clase

### Ejemplo

- Una coordenada en dos dimensiones que esta compuesta por 2 valores, el valor en el eje de las x y el valor en el eje de las Y esto podria ser una clase.

- Un cuadrado esta compuesto por cuatro coordenadas que son los cuatro vertices, esto podria ser una clase que esta compuesta por cuatro clases del objeto coordenado.

### Codigo Python
```py
class coordenada:
    # Constructor
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def mostrarcoordenada(self):
        print("(", self.x ,",", self.y , ")")

class cuadrado:
    # Metodo constructor
    def __init__(self, v1 , v2 , v3 , v4):
        sef.v1 = v1
        sef.v2 = v2
        sef.v3 = v3
        sef.v4 = v4

    def mostrarvertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.v1.mostrarcoordenada()
        self.v2.mostrarcoordenada()
        self.v3.mostrarcoordenada()
        self.v4.mostrarcoordenada()

```


![alt text](img/RAM2.jpg)

## Encapsulacion

- uno de los objetivos que tiene la POO  es protejer los datos de acceso o usos no controlados, y esto es lo que se conoce como **encapsulacion**
- Los atributos que componen una clase pueden ser de dos tipos
    - **Publicos_** los datos son accesibles sin control es decir los datos pueden ser usados sin ningun tipo de mecanismo que proteja ante usos no autorizadis o indevidos.
    - **privados** los datos no pueden ser accedidos sin control y para acceder a ellos se debera implementar un metodo que acceda a ellos. De esta manera, los datos unicamente seran accedidos directamente por la propia clase.
- La encapsulacion tambien puede realizarse sobre los metodos 
- la definicion de atributos privados se realiza incluyendo los caracteres "__" (dos guiones de piso) entre la palabra **self** y el nombre del atributo

### Ejemplo
### Codigo Python
```py
class coordenada:
    # Constructor
    def __init__(self, x , y):
        self.___x = x
        self.___y = y

    # Metodos de acceso 
    def getx(self):
        return self.__x
    def setx(self, x):
        self.__x = x
    def gety(self):
        return self.__y
    def sety(self, y):
        self.__y = y

    def mostrarcoordenada(self):
        print("(", self.__x ,",", self.__y , ")")

class cuadrado:
    # Metodo constructor
    def __init__(self, v1 , v2 , v3 , v4):
        sef.v1 = v1
        sef.v2 = v2
        sef.v3 = v3
        sef.v4 = v4

    def mostrarvertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.v1.mostrarcoordenada()
        self.v2.mostrarcoordenada()
        self.v3.mostrarcoordenada()
        self.v4.mostrarcoordenada()

```
## Herencia
- Permite la reutilización de código.
- Consiste en la definición de una clase utilizando como base una clase ya existente.
- La nueva clase derivada tendrá todas las caracteristicas de la clase base y ampliará el concepto de esta, es decir, tendrá todos los atributos y métodos de la clase base.
- Significa que entre dos clases existe una relación del tipo "es un".
- La herencia en Python se especifica de la siguiente manera: ```class NombreClase(ClaseBase):```
- Ejemplo:
    - Pensemos en una persona como una clase, la persona tendría una serie de atributos como pueden ser el nombre, los apellidos, la edad, etc.  Esas características de una persona serían compartidas por todas aquellas clases hijas como pueden ser alumno y profesor.  Es decir, alumno y profesor heredarían las propiedades de la clase persona y tendrían sus propias propiedades, diferentes entre ellas, como por ejemplo el curso en el que está el alumno y el horario de tutorias del profesor.

    - Clase base: Persona
        - Atributos:
            - Nombre
            - Apellidos
            - Edad

    - Clase derivada: Alumno
        - Atributos:
            - Curso
            - Asignaturas
    
    - Clase derivada: Profesor
        - Atributos:
            - Antigüedad
            - Tutorias
            - Teléfono