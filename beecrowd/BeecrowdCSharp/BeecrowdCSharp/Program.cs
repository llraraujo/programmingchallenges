using System;

namespace BeecrowdCSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            int tamanhoDoVetor = int.Parse(Console.ReadLine());
            int[] vetorValores = new int[tamanhoDoVetor];
            string[] valores = Console.ReadLine().Split();
          
            for(int i = 0; i < tamanhoDoVetor; i++)
            {
                vetorValores[i] = int.Parse(valores[i]);
            }

            Tuple<int, int> valorMinimoEPosicao = RetornaValorMinimoEPosicao(vetorValores);

            Console.WriteLine("Menor valor: " + valorMinimoEPosicao.Item1);
            Console.WriteLine("Posicao: " + valorMinimoEPosicao.Item2);

        }

        static Tuple<int, int> RetornaValorMinimoEPosicao(int[] vetor)
        {
            int menorValor = vetor[0];
            int posicao = 0;

            for (int i = 0; i < vetor.Length; i++)
            {
                if (vetor[i] < menorValor)
                {
                    menorValor = vetor[i];
                    posicao = i;
                }
            }

            return Tuple.Create(menorValor, posicao);
        }
    }
}
