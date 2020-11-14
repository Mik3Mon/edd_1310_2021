from generacion_y_reglas import Generacion

ejemplo = Generacion(10, 10, 6, [(1, 2), (2, 1), (2, 2), (2, 3)])

print("\n>Partida de ejemplo Excel<")
print("\nGeneracion Inical")

ejemplo.imprime_grid()

for gen in range(ejemplo.generaciones()):
    sig_generacion = gen + 1
    ejemplo.reglas_evolutivas()
    print(f"\nGeneracion {sig_generacion}")
    ejemplo.imprime_grid()

aleatorio = Generacion(15, 15, 10, [(4, 7), (5, 6), (5, 5), (4, 6), (1, 2), (2, 1), (2, 2), (2, 3)])

print("\n>Partida aleatoria<")
print("\nGeneracion Inical")

aleatorio.imprime_grid()

for gen in range(aleatorio.generaciones()):
    sig_generacion = gen + 1
    aleatorio.reglas_evolutivas()
    print(f"\nGeneracion {sig_generacion}")
    aleatorio.imprime_grid()
