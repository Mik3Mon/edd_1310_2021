from Listas_Circulares import CircularList

cl = CircularList()
print(f"cl esta vacia? {cl.is_empty()}\n")
cl.insert(10)
print(f"cl esta vacia? {cl.is_empty()}\n")
cl.insert(20)
cl.insert(11)
cl.insert(21)
cl.insert(1)
cl.insert(5)
cl.transversal()
cl.insert(-1)
cl.transversal()
cl.insert(0)
cl.transversal()
cl.insert(7)
cl.transversal()
cl.insert(7)
cl.transversal()
cl.get_size()
