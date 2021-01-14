from Stack import Stack

def suma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop() + suma_lista_rec(lista)

def countdown(n):
    if n >= 0:
        print(f"La bomba explotara en {n} segundos")
        countdown(n-1)
    else:
        print("BOOOOOOOM!")

def eliminar_pila(pila):
    
