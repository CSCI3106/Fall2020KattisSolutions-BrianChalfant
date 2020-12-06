/*
@Author Brian Chalfant 2020
Hawaii Pacific University
CSCI3106 - Programming Challenges - Fall 2020
*/

using System;
using System.Globalization;
using System.Linq;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {

            String[] numbers = (Console.ReadLine().Split());
            int[] reversed_numbers = new int[numbers.Length];
            for (int i = 0; i < numbers.Length; i++)
            {
                Char[] converted_number = numbers[i].ToCharArray();
                Array.Reverse(converted_number);
                reversed_numbers[i] = Convert.ToInt32(new String(converted_number));
            }

            Console.WriteLine(reversed_numbers.Max());

        }
    }
}