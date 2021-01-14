from Recursividad import suma_lista_rec,countdown,adt_stack
from Stack import Stack

print("Prueba suma lista recursiva")
datos = [4,2,3,5]
res = suma_lista_rec(datos)
print(res)

print("\nPrueba Cuentaregresiva")
countdown(60)

print("\nPrueba ADT Stack")
s = Stack()
s.push(100)
s.push(50)
s.push(30)
s.push(120)
s.push(230)
s.push(10)
s.to_string()
