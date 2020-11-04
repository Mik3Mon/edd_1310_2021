from Arrays import Array

arch = open("junio.txt","rt")
Empleado = arch.readlines()
Empleado = [ e.replace('','').strip().split(',') for e in Empleado ]
lista = len(Empleado)
Empleados = Array(lista)
extra = float(276.5)

for x in range(lista):
    Empleados.set_item(Empleado[x],x)

for x in range(lista):
    hora_extra = int(Empleados.get_item(x)[4])
    año_ingreso = int(Empleados.get_item(x)[6])
    sueldo = int(Empleados.get_item(x)[5])
    sueldo_extra = hora_extra * extra
    sueldo_total = sueldo + sueldo_extra
    sueldo_prestacion = float((((2020 - año_ingreso)*0.03)*sueldo)+sueldo_total)
    print(f" N. empleado:{Empleado[x][0]} Nombre:{Empleado[x][1]} {Empleado[x][2]} {Empleado[x][3]} tiene un sueldo de {sueldo_prestacion}")

for i in range(lista):
        if int(Empleados.get_item(i)[6]) == 2016:
            print(Empleados.get_item(i))

for x in range(lista):
        if int(Empleados.get_item(x)[6]) == 2020:
            print(Empleados.get_item(x))
