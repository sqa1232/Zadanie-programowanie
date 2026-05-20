print("--- ZADANIE 3: Średnia ocen ucznia ---")

liczba_ocen = int(input("Podaj liczbę ocen: "))
suma_ocen = 0.0

# Pętla for do pobierania kolejnych ocen
for i in range(liczba_ocen):
    ocena = float(input(f"Podaj ocenę {i + 1}: "))
    suma_ocen += ocena

# Obliczanie średniej
srednia = suma_ocen / liczba_ocen

# Wypisanie wyniku (:.2f wymusza wyświetlenie 2 miejsc po przecinku)
print(f"Średnia: {srednia:.2f}")

# Warunek zaliczenia
if srednia >= 3.0:
    print("Uczeń zdał.")
else:
    print("Uczeń nie zdał.")