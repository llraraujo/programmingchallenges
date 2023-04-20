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
            const int QUANTIDADE_DE_DADOS = 15;
            int[] vetorPares = new int[5];
            int[] vetorImpares = new int[5];
            int tamanhoVetor = vetorPares.Length;
            int countQtdRepeticoes = 0;
            int indexPares = 0;
            int indexImpares = 0;
;
            for(int t = 0; t < QUANTIDADE_DE_DADOS; t++)
            {
                int valor = int.Parse(Console.ReadLine());
                if(valor % 2 == 0)
                {
                    vetorPares[indexPares] = valor;
                    indexPares++;
                    if (indexPares == tamanhoVetor)
                    {
                        ImprimirValoresDoVetor(ref vetorPares, "par");
                        indexPares = 0;
                    }
                }
                else
                {                    
                    vetorImpares[indexImpares] = valor;
                    indexImpares++;
                    if (indexImpares == tamanhoVetor)
                    {                        
                        ImprimirValoresDoVetor(ref vetorImpares, "impar");
                        indexImpares = 0;
                    }
                }
                countQtdRepeticoes++;
            }

            ImprimirValoresDoVetor(ref vetorImpares, "impar");
            ImprimirValoresDoVetor(ref vetorPares, "par");
        }

        static void ImprimirValoresDoVetor(ref int[] vetor, string saida)
        {                        
            for(int i = 0; i < vetor.Length; i++)
            {
                if (vetor[i] != 0)
                {
                    Console.WriteLine(saida + "[" + i + "] = " + vetor[i]);
                }   
            }
            vetor = new int[5];
        }
    }
}
