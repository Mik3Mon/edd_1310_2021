class Nodo:
    def __init__(self , dato):
        self.dato = dato
        self.siguiente = None

#Ejemplo 1, un solo elemento
a = Nodo(12)
print(a.dato)
print(a.siguiente)

#Ejemplo 2
a.siguiente = Nodo(20)

#Ejemplo 3
a.siguiente.siguiente = Nodo(30)

#Ejemplo 4
a.siguiente.siguiente.siguiente = Nodo(40)

#Ejemplo 5
a.siguiente.siguiente.siguiente.siguiente = Nodo(50)

#Ejemplo 6, eliminar valores
a.siguiente.siguiente = a.siguiente.siguiente.siguiente

#Ejemplo 7 cambiar valor
a.siguiente.siguiente.dato = 45

#Ejemplo 8 insertar Nodo
tmp = a.siguiente.siguiente.siguiente
a.siguiente.siguiente.siguiente = Nodo(48)
a.siguiente.siguiente.siguiente.siguiente = tmp

#Recorrido Transversal
curr_node = a
print(curr_node.dato , "---> " , end = "")
while(curr_node.siguiente != None):
    curr_node = curr_node.siguiente
    print(curr_node.dato , "---> " , end = "")
print("")
