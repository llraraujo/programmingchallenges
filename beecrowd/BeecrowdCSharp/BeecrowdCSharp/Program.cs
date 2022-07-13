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
            int n = int.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            
            for(int i = 1; i <= n; i++)
            {
                if (n % i == 0) Console.WriteLine(i);
            }

        }
    }
}
