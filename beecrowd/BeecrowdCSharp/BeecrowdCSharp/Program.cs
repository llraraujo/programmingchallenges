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
            var testes = int.Parse(Console.ReadLine());

            for (int i = 0; i < testes; i++ )
            {
                int n = int.Parse(Console.ReadLine());

                int soma_divisores = 0;

                for(int j = 1; j < n; j++)
                {
                    if (n % j == 0) soma_divisores += j;
                }

                if(soma_divisores == n) Console.WriteLine(n + " eh perfeito"); 
                else Console.WriteLine(n + " nao eh perfeito"); 


            }


        }
    }
}
