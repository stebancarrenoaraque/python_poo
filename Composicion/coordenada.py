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

    # Metodo para mostrar la coordenada

    def mostrarcoordenada(self):
        print("(", self.__x ,",", self.__y , ")")