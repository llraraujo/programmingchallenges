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
         
            while (true)
            {
                int n = int.Parse(Console.ReadLine());
              
                if (n == 0) break;
                if (n % 2 != 0) n++;
                int soma = n;

                for (int i = 2; i < 10; i+=2)
                {
                    soma += (n + i);
                }

                Console.WriteLine(soma);
            }


        }
    }
}
