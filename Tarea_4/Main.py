from Empleados import Empleado
from Arrays import Array

arch = open("junio.txt","rt")
datos = 'dato'

while(datos != ('')):
    datos = arch.readline()
    empleados = datos.strip().split(',')
