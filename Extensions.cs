using System;
using System.Net.Http;


namespace Extensions
{ 
    public static class Extensions
    {
        //Добавляем метод 'map' для быстрого пересчёта
        public static int Map(this int value, int sourceMin, int sourceMax, int targetMin, int targetMax)
        {
            // (Перетащил с Arduino)
            // <summary> Переносит число из одного диапазона в другой.</summary>
            return (value - sourceMin) / (sourceMax - sourceMin) * (targetMax - targetMin) + targetMin;
        }


        //Это для расчёта UNIX-времени из DateTime
        public static long ToUnixTimestamp(this DateTime self)
        {
            DateTimeOffset offset = new DateTimeOffset(self);
            return offset.ToUnixTimeSeconds();
        }


        public static int StatusCode(this Exception self)
        {
            //Для извлечения кода ошибки HTTP
            int code = Int32.Parse(self.Message.Split(':')[1].Split('(')[0].Trim());
            return code;
        }
    }
}
