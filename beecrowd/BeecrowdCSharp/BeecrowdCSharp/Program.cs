using System;
using System.Collections.Generic;
using System.Linq;
using System.Globalization;

namespace BeecrowdCSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            var X = new int[10];

            for (int i = 0; i < 10; i++ )
            {
                X[i] = int.Parse(Console.ReadLine());

            }

            for(int i = 0; i < X.Length; i++)
            {
                if (X[i] <= 0) X[i] = 1;
                Console.WriteLine($"X[{i}] = {X[i]}");
            }


        }
    }
}
