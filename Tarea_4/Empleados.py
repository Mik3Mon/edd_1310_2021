class Empleados:
    def __init__( self , nt , n , ap , am , x , s , a):
        self.__numerodeTrabajador = nt
        self.__nombre = n
        self.__apellidoPaterno = ap
        self.__apellidoMaterno = am
        self.__horasExtras = x
        self.__sueldoBase = s
        self.__aniodeIngreso = a

    def to_string( self ):
        return "Numero de trabajdor:"+self.__numerodeTrabajador+" Nombres:"+self.__nombre+" Appelido Paterno:"+self.__apellidoPaterno+" Apellido Materno:"+self.__apellidoMaterno+" Horas Extra:"+self.__horasExtras+" Sueldo Base:"+self.__sueldoBase+"Año de Ingreso:"+self.__aniodeIngreso
