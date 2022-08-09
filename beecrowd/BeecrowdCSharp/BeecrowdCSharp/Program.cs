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
            float[] A = new float[100];

           
            for(int i = 0; i < A.Length; i++)
            {
                A[i] = float.Parse(Console.ReadLine(), CultureInfo.InvariantCulture); 
            }

            for (int i = 0; i < A.Length; i++) {

                if (A[i] <= 10.0)
                {
                     Console.WriteLine("A[" + i + "]" + " = " + A[i].ToString("F1", CultureInfo.InvariantCulture));
                }
            }


        }
    }
}
