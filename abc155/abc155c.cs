using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            var N = int.Parse(Console.ReadLine());

            var d = new Dictionary<string, int>();
            for (var i = 0; i < N; i++)
            {
                var S = Console.ReadLine();
                if (!d.ContainsKey(S)) d[S] = 0;
                d[S]++;
            }

            var m = d.Values.Max();
            var l = new List<string>();
            foreach (var kv in d)
            {
                if (kv.Value != m) continue;
                l.Add(kv.Key);
            }

            l.Sort(StringComparer.Ordinal);
            Console.WriteLine(string.Join("\n", l));
        }
    }
}
