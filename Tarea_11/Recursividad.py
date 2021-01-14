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
    tamanio = pila.length()
    contador =+ 1
    if (pila.is_empty() == True or pila.length() <= 2):
        return "La pila esta vacia o no tiene suficientes elementos"
    copia = pila.peek()
    pila.pop()
    eliminar_pila(pila)
    mitad = (tamanio/2)
    if mitad == int(mitad):
        if (contador != mitad and contador != (mitad-1)):
            pila.push(copia)
    else:
        if (contador != int(tamanio/2)):
            pila.push(copia)
    
