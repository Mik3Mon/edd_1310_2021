from generacion_y_reglas import Generacion

print("\n>Partida de ejemplo Excel<")
ejemplo = Generacion(10, 10, 6, [(1, 2), (2, 1), (2, 2), (2, 3)])
print("\nGeneracion Inical")
ejemplo.imprime_grid()

for g in range(ejemplo.generaciones()):
    sig_generacion = g + 1
    ejemplo.reglas_evolutivas()
    print(f"\nGeneracion {sig_generacion}")
    ejemplo.imprime_grid()

print("\n>Partida aleatoria<")
aleatorio = Generacion(15, 15, 10, [(4, 7), (5, 6), (5, 5), (4, 6), (1, 2), (2, 1), (2, 2), (2, 3)])
print("\nGeneracion Inical")
aleatorio.imprime_grid()

for g in range(aleatorio.generaciones()):
    sig_generacion = g + 1
    aleatorio.reglas_evolutivas()
    print(f"\nGeneracion {sig_generacion}")
    aleatorio.imprime_grid()
