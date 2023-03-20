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
            decimal valor = decimal.Parse(Console.ReadLine());
            decimal[] vetor = new decimal[100];

            for(int t = 0; t < vetor.Length; t++)
            {
                if(t == 0)
                {
                    vetor[t] = valor;
                }
                else
                {
                    vetor[t] = vetor[t - 1] / 2;
                }
                
                Console.WriteLine("N[" + t + "] = " + vetor[t].ToString("0.0000"));
            }
                   
        }
    }
}
