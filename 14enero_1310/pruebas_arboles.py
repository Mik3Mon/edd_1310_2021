class NodoArbol:
    def __init__(self , value , left = None , right = None):
        self.data = value
        self.right = right
        self.left = left

arbol = NodoArbol("R" , NodoArbol("C") , NodoArbol("H"))

print(arbol.left.data)

print(arbol.data)

arbol2 = NodoArbol(4 , NodoArbol(3 , NodoArbol(2 , NodoArbol(2))) , NodoArbol(5))

print(arbol2.data)
print(arbol2.left.data)
print(arbol2.left.left.data)
print(arbol2.left.left.left.data)
print(arbol2.rigth.data)
