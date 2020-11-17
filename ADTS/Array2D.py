class Array2D:
    def __init__(self , rens , cols , value):
        self.__cols = cols
        self.__rens = rens
        self.__array=[[value for x in range(self.__cols)] for y in range(self.__rens)]

    def to_string(self):
        [print("---",end="") for x in range(self.__cols)]
        print("")
        for ren in self.__array:
            print(ren)
        [print("---",end = "") for x in range(self.__cols)]
        print("")

    def get_num_rens(self):
        return self.__rens

    def get_num_cols(self):
        return self.__cols

    def get_item(self , ren , col):
        return self.__array[ren][col]

    def set_item( self , ren , col , valor ):
        self.__array[ren][col] = valor

    def clearing(self, valor = 0):
        for ren in range(self.__rens):
            for col in range(self.__cols):
                self.__array[ren][col] = valor
