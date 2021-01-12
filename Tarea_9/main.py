from PriorityQueue import PriorityQueue

print("Lista de prioridad de desembarqu en caso de emergencia\n")

cp = PriorityQueue()
cp.enqueue(4, "Maestres")
cp.enqueue(2, "Niños")
cp.enqueue(4, "Mecanico")
cp.enqueue(3, "Hombres")
cp.enqueue(4, "Vigia")
cp.enqueue(5, "Capitan")
cp.enqueue(4, "Timonel")
cp.enqueue(3, "Mujeres")
cp.enqueue(2, "3ra Edad")
cp.enqueue(1, "Niñas")

print(cp.to_string())

while cp.is_empty() != True:
    siguiente = cp.dequeue()
    print(f"\nLa tripulacion {siguiente} ha abandonado el barco")
    if cp.is_empty() != True:
        print(f"Tripulacion que falta por evacuar{cp.to_string()}")
    else:
        print("\nLa tripulacion ha evacuado exitosamente")
