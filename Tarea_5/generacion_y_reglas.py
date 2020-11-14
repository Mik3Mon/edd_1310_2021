from array2D import Array2D

class Generacion:
    celula_viva = 1
    celula_muerta = 0

    def __init__(self , rens , cols , generacion , poblacion):
        self.largo = rens
        self.ancho = cols
        self.grid = Array2D(self.largo , self.ancho , 0)
        self.generacion = generacion

        for celula in poblacion:
            self.grid.set_item(celula[0] , celula[1] , self.celula_viva)

    def generaciones(self):
        return self.generacion

    def get_num_rens(self):
        return self.largo

    def get_num_cols(self):
        return self.ancho

    def set_celula_viva(self , ren , col):
        self.grid.set_item(ren, col, self.celula_viva)

    def set_celula_muerta(self , ren , col):
        self.grid.set_item(ren, col, self.celula_muerta)

    def get_celula_viva(self , ren , col):
        return self.grid.get_item(ren , col) == self.celula_viva

    def get_celula_muerta(self , ren , col):
        return self.grid.get_item(ren , col) == self.celula_muerta

    def configura_generacion(self , nueva_poblacion):
        self.grid.clearing()
        for celula in nueva_poblacion:
            self.grid.set_item(celula[0], celula[1], self.celula_viva)

    def imprime_grid(self):
        for r in range(self.grid.get_num_rens()):
            for c in range(self.grid.get_num_cols()):
                if self.grid.get_item(r, c) == 0:
                    print("0 " , end = "")
                else:
                    print("1 " , end = "")
            print("")

    def get_numero_vecinos_vivos(self , ren , col):
        limites = [ren-1 , ren+1 , col-1 , col+1]
        vivos = 0

        if ren >= 0 and ren <= self.largo-1 and col >= 0 and col <= self.ancho -1:
            for r in range(limites[0], limites[1]+1):
                for c in range(limites[2], limites[3]+1):
                    if r == self.get_num_rens():
                        r = 0
                    if c == self.get_num_cols():
                        c = 0
                    if self.get_celula_viva(r, c):
                        vivos += 1
        else:
            print("Coordenada de la celula fuera del grid")

        if self.get_celula_viva(ren, col):
            vivos -= 1

        return (vivos)

    def reglas_evolutivas(self):
        lista = []

        for r in range( self.grid.get_num_rens()):
            lista_r = []

            for c in range( self.grid.get_num_cols()):
                lista_r.append(self.grid.get_item(r, c))

            lista.append(lista_r)

        for ren in range(self.grid.get_num_rens()):
            for col in range(self.grid.get_num_cols()):
                if self.get_celula_viva(ren, col) and (self.get_numero_vecinos_vivos(ren, col) == (2 or 3)):
                    lista[ren][col] = self.celula_viva

                if self.get_celula_viva(ren, col) and (self.get_numero_vecinos_vivos(ren, col) <= 1):
                    lista[ren][col] = self.celula_muerta

                if self.get_celula_viva(ren, col) and (self.get_numero_vecinos_vivos(ren, col) >= 4):
                    lista[ren][col] = self.celula_muerta

                if self.get_celula_muerta(ren, col) and self.get_numero_vecinos_vivos(ren, col) == 3:
                    lista[ren][col] = self.celula_viva

        for ren_nuevo in range(len(lista)):
            for col_nueva in range( len(lista[ren_nuevo])):
                self.grid.set_item( ren_nuevo, col_nueva, lista[ren_nuevo][col_nueva])
