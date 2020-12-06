using System;

namespace StuckInATimeLoop
{
    class Program
    {
        static void Main(string[] args)
        {
           int n = Int32.Parse(Console.ReadLine());
           for (int i = 0; i<n; i++)
            {
                Console.WriteLine("{0} Abracadabra", i+1);
            }

        }
    }
}