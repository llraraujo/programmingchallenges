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
            int valor = int.Parse(Console.ReadLine());
            int[] vetor = new int[1000];
            int aux = 0;

            for(int t = 0; t < vetor.Length; t++)
            {
                if(t > 1 && (t % valor) == 0)
                {
                    aux = 0;
                    vetor[t] = aux;
                    Console.WriteLine("N[" + t + "] = " + vetor[t]);
                }
                else
                {
                    vetor[t] = aux;
                    Console.WriteLine("N[" + t + "] = " + vetor[t]);
                }
                aux++;
            }
                   
        }
    }
}
