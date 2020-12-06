/*
@Author Brian Chalfant 2020
Hawaii Pacific University
CSCI3106 - Programming Challenges - Fall 2020
*/
using System;

namespace Chicken
{
    class Program
    {
        static void Main(string[] args)
        {
            String[] nums = Console.ReadLine().Split();
            int numberOfPeople = int.Parse(nums[0]);
            int numberOfChicken = int.Parse(nums[1]);
            String plurality = "pieces";

            if (numberOfPeople < numberOfChicken)
            {
                int leftovers = numberOfChicken - numberOfPeople;
                if (leftovers == 1)
                {
                    plurality = "piece";
                }
                Console.WriteLine("Dr. Chaz will have {0:} {1:} of chicken left over!", leftovers, plurality);
            }
            else
            {
                int missing = numberOfPeople - numberOfChicken;
                if (missing == 1)
                {
                    plurality = "piece";
                }
                Console.WriteLine("Dr. Chaz needs {0:} more {1:} of chicken!", missing, plurality);
            }

            {
            }
        }
    }
}