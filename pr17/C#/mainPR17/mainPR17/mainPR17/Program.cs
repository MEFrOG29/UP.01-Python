using System;
using System.Collections.Generic;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;

namespace IronPythonIntegration
{
    class Program
    {
        static void Main(string[] args)
        {
            ScriptEngine engine = Python.CreateEngine();
            ScriptScope scope = engine.CreateScope();

            List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
            scope.SetVariable("input_data", numbers);

            try
            {
                engine.ExecuteFile("script.py", scope);

                dynamic output = scope.GetVariable("output");

                Console.WriteLine("--- Результаты из IronPython ---");
                Console.WriteLine($"Сумма: {output["sum"]}");
                Console.WriteLine($"Количество: {output["count"]}");
                Console.Write("Квадраты чисел: ");
                foreach (var s in output["squared"])
                {
                    Console.Write(s + " ");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Ошибка выполнения скрипта: " + ex.Message);
            }

            Console.ReadLine();
        }
    }
}