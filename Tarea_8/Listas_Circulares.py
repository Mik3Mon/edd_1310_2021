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
        return print(f"Tamanio de la Lista Circular --> {self.__size}\n")

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
            print(f" >Se agrego el elemento {value}<\n")
            self.__size += 1
        elif self.search(value) == True:
            print(f" >Se intento agregar el elemento {value} pero este ya existe<\n")
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
            print(f" >Se agrego el elemento {value}<\n")

    def transversal(self):
        curr_node = self.__referencia
        while curr_node.siguiente != self.__referencia:
            print(f"{curr_node.siguiente.data} --> " , end = "")
            curr_node = curr_node.siguiente
        print(f"{curr_node.siguiente.data} --> {self.__head.data}\n")

    def remove(self , value = None):
        curr_node = self.__referencia
        curr_node2 = self.__head
        if value != curr_node.data and value != curr_node2.data:
            print(f" >El elemento {value} no existe<\n")
        else:
            curr_ref = self.__referencia
            while curr_ref.data != value and curr_ref.siguiente != self.__referencia:
                curr_prev = curr_ref
                curr_ref = curr_ref.siguiente
            print(f" >Se elimino el elemento {curr_ref.data}<\n")
            if curr_ref.data == self.__head.data:
                self.__head = self.__head.siguiente
                self.__referencia.siguiente = self.__head
                self.__size -= 1
            elif curr_ref.data == self.__referencia.data:
                curr_ref = self.__head
                while curr_ref.siguiente != self.__referencia:
                    curr_ref = curr_ref.siguiente
                curr_ref.siguiente = self.__head
                self.__referencia = curr_ref
                self.__size -= 1
            else:
                curr_prev.siguiente = curr_prev.siguiente.siguiente
                self.__size -= 1
