from Colas import Queue,BoundedPriorityQueue
q1 = Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print("\nPrueba 2 de Queue")
c1 = {"ID":1 , "Nombre":"Mario" , "Balance":28.5}
c2 = {"ID":2 , "Nombre":"Diana" , "Balance":3456.5}
c3 = {"ID":3 , "Nombre":"Bartolo" , "Balance":100000.0}

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)

print(atencion.to_string())
siguiente = atencion.dequeue()

print(f"\nBienvenido Sr. { siguiente['Nombre'] }, en que podemos servirle el dia de hoy\n")
print(atencion.to_string())
print("\nPruebas de las colas con prioridad acotada\n")

maestres = {"prioridad":4 , "descripcion":"Maestre" , "personas":["Juan P", "Diego H"]}
niños = {"prioridad":2 , "descripcion":"Niños" , "personas":["Santi H", "Angel H"]}
mecanicos = {"prioridad":4 , "descripcion":"Mecanicos" , "personas":["Diana T", "Maria Z"]}
mujeres = {"prioridad":3 , "descripcion":"Mujeres" , "personas":["Valentina M", "Veronica L"]}
tercera_edad = {"prioridad":2 , "descripcion":"3ra edad" , "personas":["Teresa G", "Carmen B"]}
ninias = {"prioridad":1 , "descripcion":"Niñas" , "personas":["Victoria M", "Camila R"]}
hombres = {"prioridad":3 , "descripcion":"Hombres" , "personas":["Miguel M", "Miguel M"]}
vigia = {"prioridad":4 , "descripcion":"Vigia" , "personas":["Francisco O"]}
capitan = {"prioridad":5 , "descripcion":"Capitan" , "personas":["Jose M"]}
timonel = {"prioridad":4 , "descripcion":"timonel" , "personas":["Hugo R"]}

cpa = BoundedPriorityQueue( 7 )
cpa.enqueue(maestres['prioridad'] , maestres)
cpa.enqueue(niños['prioridad'] , niños)
cpa.enqueue(mecanicos['prioridad'] , mecanicos)
cpa.enqueue(mujeres['prioridad'], mujeres)
cpa.enqueue(tercera_edad['prioridad'], tercera_edad)
cpa.enqueue(ninias['prioridad'], ninias)
cpa.enqueue(hombres['prioridad'], hombres)
cpa.enqueue(vigia['prioridad'], vigia)
cpa.enqueue(capitan['prioridad'], capitan)
cpa.enqueue(timonel['prioridad'], timonel)
cpa.to_string()

while cpa.is_empty() != True:
    siguiente = cpa.dequeue()
    print(f"\nLa tripulacion con prioridad { siguiente['prioridad'] }, han abandonado el barco\n")
    cpa.to_string()
    if cpa.is_empty() == False:
        print("Aun quedan personas en la cola")
    else:
        print("Ya no quedan personas en la cola")
        print("El barco ha sido evacuado por completo!")
