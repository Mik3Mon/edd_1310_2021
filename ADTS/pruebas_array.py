from Arrays import Array

algo = Array(10)
print(algo.get_item(6363))
algo.set_item(555,3)
print(algo.get_item(3))
print(f"El arreglo tiene {algo.get_length()} elementos")
algo.clear(777)
print(algo.get_item(3))
print("------------------")
print("Aqui empieza mi prueba del iterador")
for x in algo:
    print(x)
for x in range(algo.get_length()):
    print(f"{x}->{algo.get_item(x)}")
