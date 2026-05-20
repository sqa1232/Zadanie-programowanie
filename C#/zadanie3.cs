using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Zadanie 3");

        Console.Write("Podaj liczbę ocen: ");
        int liczbaOcen = Convert.ToInt32(Console.ReadLine());

        double sumaOcen = 0;

        for (int i = 0; i < liczbaOcen; i++)
        {
            Console.Write("Podaj ocenę " + (i + 1) + ": ");
            double ocena = Convert.ToDouble(Console.ReadLine());
            sumaOcen += ocena;
        }

        double srednia = sumaOcen / liczbaOcen;
        Console.WriteLine("Średnia: {0:F2}", srednia);

        if (srednia >= 3.0)
        {
            Console.WriteLine("Uczeń zdał.");
        }
        else
        {
            Console.WriteLine("Uczeń nie zdał.");
        }
    }
}