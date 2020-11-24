class NodoDoble:
    def __init__(self , value = None , siguiente = None , previo = None):
        self.data = value
        self.siguiente = siguiente
        self.previo = previo

class DoubleLinkedList:
    def __init__(self):
        self.__head = NodoDoble(None, None, None)
        self.__tail = NodoDoble(None, None, None)
        self.__head.siguiente = self.__tail
        self.__tail.previo = self.__head
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def append(self , value):
        nuevo = NodoDoble(value)
        curr_node = self.__head
        self.__size += 1
        if self.is_empty():
            self.__head = nuevo
            self.__tail = nuevo
        else:
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente
            curr_node2 = self.__tail
            self.__tail = curr_node.siguiente = nuevo
            self.__tail.previo = curr_node2

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} <--> " , end = "")
            curr_node = curr_node.siguiente
        print("")

    def reverse_transversal(self):
        curr_node = self.__tail
        while curr_node != None:
            print(f"{curr_node.data} <--> " , end = "")
            curr_node = curr_node.previo
        print("")

    def find_from_head(self , value = None , posicion = None):
        curr_node = self.__head
        contador = 0
        elemento = None
        while curr_node != None:
            if curr_node.data == value:
                posicion = contador
                elemento = curr_node.data
            contador +=1
            curr_node = curr_node.siguiente
        if elemento == value:
            print(f"El elemento {elemento} se encuentra en la posicion {posicion}")
        else:
            elemento = value
            print(f"El elemento {elemento} no existe en la lista\n")

    def find_from_tail(self , value = None , posicion = None):
        curr_node = self.__tail
        contador = 0
        elemento = None
        while curr_node != None:
            if curr_node.data == value:
                posicion = contador
                elemento = curr_node.data
            contador +=1
            curr_node = curr_node.previo
        if elemento == value:
            print(f"El elemento {elemento} se encuentra en la posicion {posicion}")
        else:
            elemento = value
            print(f"El elemento {elemento} no existe en la lista\n")

    def remove_from_head(self, value):
        curr_node = self.__head
        self.__size -= 1
        elemento = None
        while curr_node.data != value and curr_node.siguiente != None:
            curr_node = curr_node.siguiente
        if curr_node.data == value:
            curr_node.previo.siguiente = curr_node.siguiente
            curr_node.siguiente.previo = curr_node.previo
            elemento = curr_node.data
            print(f"El elemento {elemento} ha sido removido")
        else:
            self.__size += 1
            elemento = value
            print(f"El elemento {elemento} no existe en la lista\n")

    def remove_from_tail(self, value):
        curr_node = self.__tail
        self.__size -= 1
        elemento = None
        while curr_node.data != value and curr_node.previo != None:
            curr_node = curr_node.previo
        if curr_node.data == value:
            curr_node.siguiente.previo = curr_node.previo
            curr_node.previo.siguiente = curr_node.siguiente
            elemento = curr_node.data
            print(f"El elemento {elemento} ha sido removido")
        else:
            self.__size += 1
            elemento = value
            print(f"El elemento {elemento} no existe en la lista\n")
