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
            var N = new int[10];

            N[0] = int.Parse(Console.ReadLine());

            for(int i = 0; i < N.Length; i++)
            {
                Console.WriteLine($"N[{i}] = {N[i]}");

                if(i != N.Length - 1)
                    N[i + 1] = N[i] * 2;

            }

            


        }
    }
}
