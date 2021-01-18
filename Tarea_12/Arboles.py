class NodoArbol:
    def __init__(self , value , left = None , right = None):
        self.data = value
        self.left = left
        self.right = right

def main():

    arbolT1 = NodoArbol("+" , NodoArbol("-" , NodoArbol(5) , NodoArbol(4)) , NodoArbol("*" , NodoArbol(3) , NodoArbol(2)))
    print("\nInfija o Inorden")
    print("\nPrefija o Preorden")
    print("\nPosfija o Postorden")
    print("\nArbol #2")
    arbolT2 = NodoArbol(40 , NodoArbol(30 , NodoArbol(25) , NodoArbol(35)) , NodoArbol(50 , NodoArbol(45) , NodoArbol(60)))
    print("Infija o Inorden")
    print("\nPrefija o Preorden")
    print("\nPosfija o Postorden")

main()
