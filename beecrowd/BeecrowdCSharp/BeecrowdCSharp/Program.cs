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
            double s = 1.0;
            int j = 2;
            
            for(int i = 3; i <= 39; i+=2)
            {
                s +=  (double) i / j;
                j *= 2;

            }

            Console.WriteLine(s.ToString("F2", CultureInfo.InvariantCulture));
        }
    }
}
