class Nodo:
    def __init__(self , value , siguiente = None):
        self.data = value
        self.siguiente = siguiente

class CircularList:
    def __init__(self):
        self.__head = None
        self.__referencia = None
        self.__size = 0

    def is_empty(self):
        return self.__head == None

    def get_size(self):
        return print(f"\nSize ==> {self.__size}\n")

    def search(self , value = None):
        valor = False
        curr_ref = self.__referencia
        while curr_ref.siguiente != self.__referencia:
            if curr_ref.data == value:
                valor = True
            curr_ref = curr_ref.siguiente
        if curr_ref.data == value:
            valor = True
        return valor

    def insert(self , value):
        nueva = Nodo(value)
        if self.is_empty():
            self.__head = self.__referencia = nueva
            self.__referencia.siguiente = self.__head
            print(f" Se agrego el elemento {value} a la Lista Circular\n")
            self.__size += 1
        elif self.search(value) == True:
            print(f" El elemento {value} ya existe en la Lista Circular\n")
        else:
            while self.search(value) == False:
                if value > self.__referencia.data:
                    curr_ref = self.__referencia
                    self.__referencia = curr_ref.siguiente = nueva
                    self.__referencia.siguiente = self.__head
                    self.__size += 1
                elif value < self.__head.data:
                    nueva.siguiente = self.__head
                    self.__head = nueva
                    self.__referencia.siguiente = self.__head
                    self.__size += 1
                elif value > self.__head.data:
                    curr_ref = self.__referencia.siguiente
                    while value > curr_ref.data:
                        curr_prev = curr_ref
                        curr_ref = curr_ref.siguiente
                    nueva.siguiente = curr_prev.siguiente
                    curr_prev.siguiente = nueva
                    self.__size += 1
            print(f" Se agrego el elemento {value} a la Lista Circular\n")

    def transversal(self):
        curr_node = self.__referencia
        while curr_node.siguiente != self.__referencia:
            print(f"{curr_node.siguiente.data} --> " , end = "")
            curr_node = curr_node.siguiente
        print(f"{curr_node.siguiente.data} --> {self.__head.data}")

    def remove(self , value = None):
        if self.is_empty():
            print("Lista Circular vacia")
