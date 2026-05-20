print("Zadanie 1")

liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))
operacja = input("Podaj operację (+, -, *, /): ")

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
    if liczba2 != 0:
        wynik = liczba1 / liczba2
        print(f"Wynik: {wynik}")
    else:
        print("Błąd: Nie można dzielić przez zero!")
else:
    print("Nieznana operacja!")