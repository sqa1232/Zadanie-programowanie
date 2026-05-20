Console.WriteLine("Zadanie 2");

Console.Write("Wybierz kierunek (C - z Celsjusza na Fahrenheit, F - z Fahrenheita na Celsjusz): ");
string kierunek = Console.ReadLine().ToUpper();

if (kierunek == "C")
{
    Console.Write("Podaj temperaturę w °C: ");
    double celsjusz = Convert.ToDouble(Console.ReadLine());
    double fahrenheit = celsjusz * 1.8 + 32;
    Console.WriteLine(celsjusz + "°C = " + fahrenheit + "°F");
}
else if (kierunek == "F")
{
    Console.Write("Podaj temperaturę w °F: ");
    double fahrenheit = Convert.ToDouble(Console.ReadLine());
    double celsjusz = (fahrenheit - 32) / 1.8;
    Console.WriteLine(fahrenheit + "°F = " + celsjusz + "°C");
}
else
{
    Console.WriteLine("Niepoprawny wybór! Wybierz C lub F.");
}