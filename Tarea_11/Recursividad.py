def suma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop() + suma_lista_rec(lista)
