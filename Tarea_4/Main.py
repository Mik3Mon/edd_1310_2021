from Arrays import Array

arch = open("junio.dat","rt")
Empleado = arch.readlines()
Empleado = [ e.replace('','').strip().split(',') for e in Empleado ]
lista = len(Empleado)
Empleados = Array(lista)
extra = float(276.5)

for x in range(1,lista):
    Empleados.set_item(Empleado[x],x)

print("SUELDOS DE EMPLEADOS")
for x in range(1,lista):
    hora_extra = int(Empleados.get_item(x)[4])
    año_ingreso = int(Empleados.get_item(x)[6])
    sueldo = int(Empleados.get_item(x)[5])
    sueldo_extra = sueldo + (hora_extra * extra)
    sueldo_prestacion = (2020 - año_ingreso) * 0.03
    sueldo_total = float((sueldo*sueldo_prestacion)+sueldo_extra)
    print(f" N. empleado:{Empleado[x][0]} Nombre:{Empleado[x][1]} {Empleado[x][2]} {Empleado[x][3]} tiene un sueldo de ${sueldo_total}")

print("\nEMPLEADOS CON MAYOR ANTIGUEDAD")
for x in range(1,lista):
        if int(Empleados.get_item(x)[6]) == 2016:
            print(f" N. empleado:{Empleado[x][0]} Nombre: {Empleado[x][1]} {Empleado[x][2]} {Empleado[x][3]}, Año de ingreso:{Empleado[x][6]}")

print("\nEMPLEADOS CON MENOR ANTIGUEDAD")
for x in range(1,lista):
        if int(Empleados.get_item(x)[6]) == 2020:
            print(f" N. empleado:{Empleado[x][0]} Nombre:{Empleado[x][1]} {Empleado[x][2]} {Empleado[x][3]}, Año de ingreso:{Empleado[x][6]}")
