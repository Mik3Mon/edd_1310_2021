from DoubleLinkedList import DoubleLinkedList

l = DoubleLinkedList()

print("Preguntamos si la lista esta vacia y cuantos elementos contiene\n")

print(f"l esta vacia? {l.is_empty()}\n")
print(f"l cuenta con {l.get_size()} elementos")
print("-------------------------------")

print("\nAgregamos internamente elementos a la lista\n")

l.append(10)
l.append(30)
l.append(100)
l.append(50)
l.append(2)
print("-------------------------------")

print("Volvemos a preguntar si la lista esta vacia y cuantos elementos contiene\n")

print(f"l esta vacia? {l.is_empty()}\n")
print(f"l cuenta con {l.get_size()} elementos")
print("-------------------------------")

print("\nProbamos nuestro transversal y reverse_transversal\n")

l.transversal()
l.reverse_transversal()
print(f"l cuenta con {l.get_size()} elementos\n")
l.append(4)
l.transversal()
l.reverse_transversal()
print(f"l cuenta con {l.get_size()} elementos")
print("-------------------------------")

print("\nBuscamos un elemento desde Head\n")

l.transversal()
l.find_from_head(50)
l.find_from_head(8)
print("-------------------------------")

print("\nBuscamos un elemento desde Tail\n")

l.reverse_transversal()
l.find_from_tail(50)
l.find_from_tail(8)
print("-------------------------------")

print("\nEliminamos un elemento desde Head\n")

l.transversal()
l.remove_from_head(100)
l.remove_from_head(8)
l.transversal()
print(f"l cuenta con {l.get_size()} elementos")
print("-------------------------------")

print("\nEliminamos un elemento desde Tail\n")

l.reverse_transversal()
l.remove_from_tail(50)
l.remove_from_tail(8)
l.reverse_transversal()
print(f"l cuenta con {l.get_size()} elementos")
print("-------------------------------")
