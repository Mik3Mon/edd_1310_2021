class NodoDoble:
    def __init__(self , value , siguiente = None , anterior = None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
