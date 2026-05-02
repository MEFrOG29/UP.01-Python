using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace libraryPR17
{
    public class Class1
    {
        public static string CreateFile(string path, string content)
        {
            File.WriteAllText(path, content);
            return $"Файл создан по пути: {path}";
        }

        public static string ReadFile(string path)
        {
            if (File.Exists(path))
                return File.ReadAllText(path);
            return "Ошибка: Файл не найден";
        }

        public static string AppendToFile(string path, string content)
        {
            if (File.Exists(path))
            {
                File.AppendAllText(path, Environment.NewLine + content);
                return "Данные добавлены в файл";
            }
            return "Ошибка: Файл для изменения не найден";
        }

        public static bool DeleteFile(string path)
        {
            if (File.Exists(path))
            {
                File.Delete(path);
                return true;
            }
            return false;
        }
    }
}

