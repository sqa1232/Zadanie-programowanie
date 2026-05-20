print("Zadanie 2")

kierunek = input("Wybierz kierunek (C - z Celsjusza na Fahrenheit, F - z Fahrenheita na Celsjusz): ").upper()

if kierunek == "C":
    celsjusz = float(input("Podaj temperaturę w °C: "))
    fahrenheit = celsjusz * 1.8 + 32
    print(f"{celsjusz}°C = {fahrenheit}°F")
elif kierunek == "F":
    fahrenheit = float(input("Podaj temperaturę w °F: "))
    celsjusz = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit}°F = {celsjusz}°C")
else:
    print("Niepoprawny wybór! Wybierz C lub F.")