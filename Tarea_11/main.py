from Recursividad import suma_lista_rec,countdown,eliminar_pila
from Stack import Stack

print("Prueba suma lista recursiva")
datos = [4,2,3,5]
res = suma_lista_rec(datos)
print(f"La suma de la lista es {res}")

print("\nPrueba Cuentaregresiva")
countdown(20)

print("\nPrueba ADT Stack")
s = Stack()
s.push(100)
s.push(50)
s.push(30)
s.push(120)
s.push(230)
s.push(10)
print("\nCaso Base")
s.to_string()
eliminar_pila(s)
print("\nCaso despues de la funcion")
s.to_string()
