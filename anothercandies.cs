/*
@Author Brian Chalfant 2020
Hawaii Pacific University
CSCI3106 - Programming Challenges - Fall 2020
*/
using System;

namespace AnotherCandies
{
    class Program
    {
        static void Main(string[] args)
        {
            int cases = Int32.Parse(Console.ReadLine());
            for (int i = 0; i<cases; i++)
            {
                Console.ReadLine();
                System.Numerics.BigInteger students = System.Numerics.BigInteger.Parse(Console.ReadLine());
                System.Numerics.BigInteger candies = 0;
                for (int j = 0; j < students; j++)
                {
                    candies += System.Numerics.BigInteger.Parse(Console.ReadLine());
                }
                String result = (candies % students == 0) ? "YES" : "NO";
                Console.WriteLine(result);

            }
        }
    }
}