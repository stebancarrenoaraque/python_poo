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