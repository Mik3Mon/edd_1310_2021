class NodoArbol:
    def __init__(self , value , left = None , right = None):
        self.data = value
        self.right = right
        self.left = left

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert(self , value):
        # Regla 1
        if self.__root == None:
            self.__root = NodoArbol(value)
        # Regla 2
        else:
            self.__insert__(self.__root , value)

    def __insert__(self , nodo , value):
        if nodo.data == value:
            print("El Dato ya existe, no se ingresa nada")
        elif value < nodo.data:
            # Regla 1
            if nodo.left == None:
                nodo.left = NodoArbol(value)
            #Regla 2
            else:
                self.__insert__(nodo.left , value)
        else:
            # Regla 1
            if nodo.right == None:
                nodo.right = NodoArbol(value)
            # Regla 2
            else:
                self.__insert__(nodo.right , value)

    def __recorrido_in(self , nodo):
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data , end = ", ")
            self.__recorrido_in(nodo.right)

    def __recorrido_pre(self , nodo):
        if nodo != None:
            print(nodo.data , end = ", ")
            self.__recorrido_pre(nodo.left)
            self.__recorrido_pre(nodo.right)

    def __recorrido_pos(self , nodo):
        if nodo != None:
            self.__recorrido_pre(nodo.left)
            self.__recorrido_pre(nodo.right)
            print(nodo.data , end = ", ")

    def transversal(self , format = "inorden"):
        if format == "inorden":
            print("Inorden")
            self.__recorrido_in(self.__root)
        elif format == "preorden":
            print("Preorden")
            self.__recorrido_pre(self.__root)
        elif format == "posorden":
            print("Posorden")
            self.__recorrido_pos(self.__root)
        else:
            print("Error , ese formato no existe")
        print("")

    def search(self , value):
        if self.__root == None:
            return None
        else:
            return self.__search(self.__root , value)

    def __search(self , nodo , value):
        if nodo == None:
            return None
        elif nodo.data == value:
            print("Encontrado")
            return nodo.data
        elif value < nodo.data:
            print("Bucar a la izquierda")
            return self.__search(nodo.left , value)
        else:
            print("Bucar a la derecha")
            return self.__search(nodo.right , value)

    def remove(self , value):
        if self.__root == None:
            print("Nada que eliminar")
        else:
            self.__remove(None , None , self.__root , value)

    def __remove(self , padre_hi , padre_hd , actual , value):
        if actual == None:
            print("Caso base")
            return None
        elif actual.data == value:
            print("Encontrado" , actual.data)
            # Caso 1: Hoja
            if actual.left == None and actual.right == None:
                if padre_hi != None:
                    padre_hi.left = None
                else:
                    padre_hd.right = None
            # Caso 2: Con un hijo
            if (actual.left != None and actual.right == None) or (actual.left == None and actual.right != None):
                print("Es un nodo con un hijo" , actual.data)
                if actual.left != None:
                    actual.data = actual.left.data
                    actual.left = None
                else:
                    actual.data = actual.right.data
                    actual.right = None
            # Caso 3: Con dos hijos


        elif value < actual.data:
            print("Buscar a la izquierda")
            self.__remove(actual , None , actual.left , value)
        else:
            print("Buscar a la derecha")
            self.__remove(None , actual , actual.right , value)
