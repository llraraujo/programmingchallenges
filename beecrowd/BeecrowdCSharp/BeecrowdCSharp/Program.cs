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
            List<int> ages = new List<int>();
            while (true)
            {
                int age = int.Parse(Console.ReadLine());
                if (age < 0) break;
                ages.Add(age);
            }
            double media = (double) ages.Sum() / ages.Count();

            Console.Write(media.ToString("F2", CultureInfo.InvariantCulture));
            

        }
    }
}
