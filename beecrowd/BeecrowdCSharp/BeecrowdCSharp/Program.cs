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
            int quantidadeDeTestes = int.Parse(Console.ReadLine());

            for(int t = 0; t < quantidadeDeTestes; t++)
            {
                int posicao = int.Parse(Console.ReadLine());
                Console.WriteLine("Fib(" + posicao + ") = " + Fibonacci(posicao));
            }
                   
        }

        private static long Fibonacci(int posicao)
        {
            if (posicao == 0) return 0;
            if (posicao == 1) return 1;
            List<long> fibonacci = new List<long>() { 0, 1 };
            while(posicao >= fibonacci.Count)
            {
                long ultimo = fibonacci[fibonacci.Count - 1];
                long penultimo = fibonacci[fibonacci.Count - 2];
                fibonacci.Add(ultimo + penultimo);
            }
            return fibonacci[posicao];           
        }
    }
}
