print("--- ZADANIE 1: Kalkulator ---")

# Pobieranie danych od użytkownika
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))
operacja = input("Podaj operację (+, -, *, /): ")

# Sprawdzanie operacji i obliczanie wyniku
if operacja == "+":
    wynik = liczba1 + liczba2
    print(f"Wynik: {wynik}")
elif operacja == "-":
    wynik = liczba1 - liczba2
    print(f"Wynik: {wynik}")
elif operacja == "*":
    wynik = liczba1 * liczba2
    print(f"Wynik: {wynik}")
elif operacja == "/":
    # Warunek zabezpieczający przed dzieleniem przez zero
    if liczba2 != 0:
        wynik = liczba1 / liczba2
        print(f"Wynik: {wynik}")
    else:
        print("Błąd: Nie można dzielić przez zero!")
else:
    print("Nieznana operacja!")