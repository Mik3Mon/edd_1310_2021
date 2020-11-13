from generacion_y_reglas import Generacion

print("\n>Partida de ejemplo Excel<")
ejemplo = Generacion(10, 10, 6, [(1, 2), (2, 1), (2, 2), (2, 3)])
print("Generacion Inical\n")
ejemplo.imprime_grid()

for g in range(ejemplo.generaciones()):
    ejemplo.reglas_evolutivas()
    print(f"Generacion {g + 1 }\n")
    ejemplo.imprime_grid()

print("\n>Partida aleatoria<")
aleatorio = Generacion(15, 15, 10, [(4, 7), (5, 6), (5, 5), (4, 6), (1, 2), (2, 1), (2, 2), (2, 3)])
print("Generacion Inical\n")
aleatorio.imprime_grid()

for g in range(aleatorio.generaciones()):
    aleatorio.reglas_evolutivas()
    print(f"Generacion {g + 1 }\n")
    aleatorio.imprime_grid()
