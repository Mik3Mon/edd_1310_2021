from Listas import LinkedList

l = LinkedList()
print(f"L esta vacia? {l.is_empty()}")
l.append(10)
l.append(5)
l.append(6)
l.append(20)
print(f"\n L esta vacia? {l.is_empty()}")
print("")
l.transversal()
l.remove(10)
l.transversal()
l.preppend(3)
l.transversal()
print(l.get())
print(l.get(2))
print(l.get(1))