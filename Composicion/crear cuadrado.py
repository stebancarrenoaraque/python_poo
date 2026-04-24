from cuadrado import cuadrado

def main():
    v1 = coordenada(1,1)
    v2 = coordenada(4,1)
    v3 = coordenada(4,4)
    v4 = coordenada(1,4)
    cuadrado = cuadrado(v1, v2, v3, v4)
    cuadrado.mostrarvertices()


if __name__ == main():
    main()