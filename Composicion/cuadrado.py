from coordenada import coordenada
class cuadrado:
    # Metodo constructor
    def __init__(self, v1 , v2 , v3 , v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4

    def mostrarvertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.v1.mostrarcoordenada()
        self.v2.mostrarcoordenada()
        self.v3.mostrarcoordenada()
        self.v4.mostrarcoordenada()

    def main():
        v1 = coordenada(1,1)
        v2 = coordenada(4,1)
        v3 = coordenada(4,4)
        v4 = coordenada(1,4)
        cuadrado = cuadrado(v1, v2, v3, v4)
        cuadrado.mostrarvertices()


    if __name__ == main():
        main()