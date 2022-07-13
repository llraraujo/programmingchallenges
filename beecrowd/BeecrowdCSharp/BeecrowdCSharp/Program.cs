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
         
            int tests = int.Parse(Console.ReadLine());
            for(int i = 0; i < tests; i++)
            {
                string[] entrada = Console.ReadLine().Split(' ');
                int x = int.Parse(entrada[0]);
                int y = int.Parse(entrada[1]);

                if (x % 2 == 0) x += 1;

                int soma = 0;
                int count = 0;

                while (true)
                {
                    if (x % 2 != 0)
                    {
                        soma += x;
                        count += 1;
                    }

                    if (count == y) break;

                    x += 1;

                }
                Console.WriteLine(soma);

            }


        }
    }
}
