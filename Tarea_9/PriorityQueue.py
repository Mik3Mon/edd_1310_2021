class PriorityQueue:
    def __init__(self):
        self.__data = list()

    def is_empty(self):
        return len(self.__data) == 0

    def length(self):
        return len(self.__data)

    def enqueue(self , prioridad , elem):
        self.__data.append((prioridad, elem))
        for x in range(self.length()):
            posicion = x
            actual = self.__data[x]
            while posicion > 0 and self.__data[posicion-1][0] > actual[0]:
                self.__data[posicion] = self.__data[posicion-1]
                posicion-=1
            self.__data[posicion] = actual

    def dequeue(self):
        return self.__data.pop(0)

    def to_string(self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + "|" + str(elem)
        cadena = cadena + "|"
        return cadena
