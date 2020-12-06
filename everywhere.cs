/*
@Author Brian Chalfant 2020
Hawaii Pacific University
CSCI3106 - Programming Challenges - Fall 2020
*/
using System;
using System.Collections.Generic;
using System.Linq;

namespace IveBeenEverywhereMan
{
    class Program
    {
        static void Main(string[] args)
        {
            Int32 tc = Int32.Parse(Console.ReadLine());
            for(int i = 0; i < tc; i++)
            {
                int n = Int32.Parse(Console.ReadLine());
                var cities = new String[n];
                for (int j = 0; j < n; j++)
                {
                    cities[j] = Console.ReadLine();
                }
                var cset = new HashSet<string>(cities);
                Console.WriteLine(cset.Count());
            }
        }
    }
}
