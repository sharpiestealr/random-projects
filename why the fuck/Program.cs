using System;

namespace why_the_fuck
{
    class Program
    {
        static void Main(string[] args)
        {
            int enquanto = 0;

            while (enquanto != 10)
            {
                Console.WriteLine(enquanto);
                enquanto++;
            }

            for (int para = 0; para != 10; para++)
            {
                Console.WriteLine(para);
            }

            Console.ReadKey();
        }
    }
}
