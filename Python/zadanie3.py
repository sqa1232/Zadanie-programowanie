print("Zadanie 3")

liczba_ocen = int(input("Podaj liczbę ocen: "))
suma_ocen = 0.0

for i in range(liczba_ocen):
    ocena = float(input(f"Podaj ocenę {i + 1}: "))
    suma_ocen += ocena


srednia = suma_ocen / liczba_ocen


print(f"Średnia: {srednia:.2f}")


if srednia >= 3.0:
    print("Uczeń zdał.")
else:
    print("Uczeń nie zdał.")