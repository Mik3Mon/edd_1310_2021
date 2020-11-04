from Arrays import Array

arch = open("junio.txt","rt")
Empleado = arch.readlines()
Empleado = [ e.replace('','').strip().split(',') for e in Empleado ]
lista = len(Empleado)
Empleados = Array(leer)
extra = float(276.5)

for x in range(0,lista,1):
    Empleados.set_item(Empleado[x],x)
    x = x+1

for x in Empleados:
    print(x)

for y in range(0,lista,1):
    ml = int(Empleados.get_item(y)[4])
    ant = int(Empleados.get_item(y)[6])
    sl = int(Empleados.get_item(y)[5])
    lm = ml*extra
    to = sl+lm
    tna = float((((2020-ant)*0.03)*sl)+to)
    print(f"{Empleado[y][1]} tiene un sueldo de {tna}")
    y = y+1

for i in range(0,lista,1):
        if int(Empleados.get_item(i)[6]) == 2016:
            print(Empleados.get_item(i))
        i = i+1

for x in range(0,lista,1):
        if int(Empleados.get_item(x)[6]) == 2020:
            print(Empleados.get_item(x))
        x = x+1
