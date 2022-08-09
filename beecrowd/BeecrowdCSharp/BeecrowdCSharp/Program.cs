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
            var N = new int[20];

           
            // Armazenando os dados do vetor
            for(int i = 0; i < N.Length; i++)
            {
                N[i] = int.Parse(Console.ReadLine());
            }

            var j = N.Length - 1;

            // Trocando os valores do vetor
            for(int i = 0; i < N.Length/2; i++)
            {
                int aux = N[i];
                N[i] = N[j];
                N[j] = aux;
                j--;
            }

            // Imprimindo o vetor na tela
            for(int i = 0; i < N.Length; i++)
            {
                Console.WriteLine("N[" + i + "]" + " = " + N[i]);
            }
            

        }
    }
}
