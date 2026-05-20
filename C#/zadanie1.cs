Console.WriteLine("Zadanie 1");

Console.Write("Podaj pierwszą liczbę: ");
double liczba1 = Convert.ToDouble(Console.ReadLine());

Console.Write("Podaj drugą liczbę: ");
double liczba2 = Convert.ToDouble(Console.ReadLine());

Console.Write("Podaj operację (+, -, *, /): ");
string operacja = Console.ReadLine();

if (operacja == "+")
{
    Console.WriteLine("Wynik: " + (liczba1 + liczba2));
}
else if (operacja == "-")
{
    Console.WriteLine("Wynik: " + (liczba1 - liczba2));
}
else if (operacja == "*")
{
    Console.WriteLine("Wynik: " + (liczba1 * liczba2));
}
else if (operacja == "/")
{
    if (liczba2 != 0)
    {
        Console.WriteLine("Wynik: " + (liczba1 / liczba2));
    }
    else
    {
        Console.WriteLine("Błąd: Nie można dzielić przez zero!");
    }
}
else
{
    Console.WriteLine("Nieznana operacja!");
}