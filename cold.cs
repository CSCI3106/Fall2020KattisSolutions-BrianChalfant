/*
@Author Brian Chalfant 2020
Hawaii Pacific University
CSCI3106 - Programming Challenges - Fall 2020
*/
using System;

namespace ColdputerScience
{
    class Program
    {
        static void Main(string[] args)
        {
            int cases = Convert.ToInt32(Console.ReadLine());
            int[] vs = Array.ConvertAll(Console.ReadLine().Split(' '), (item) => Convert.ToInt32(item));
            int numberOfCases = 0;
            for(int i = 0; i<vs.Length;i++)
            {
                if(vs[i] < 0)
                {
                    numberOfCases += 1;
                }
            }
            Console.WriteLine(numberOfCases);
        }
    }
}