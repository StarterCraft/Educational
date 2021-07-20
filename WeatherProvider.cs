/*
 Всё для получения погоды
 */

using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Linq;
using Newtonsoft.Json.Linq;
using Extensions;


namespace StarterWeatherProvider
{
    public class WeatherForecast
    {
        /*Класс прогноза*/

        public struct TemperatureData
        {
            /*Всё, что связано с температурой*/
            public float Current { get; set; }
            public float CurrentFeelsLike { get; set; }


            public TemperatureData(float current, float currentFeelsLike)
            {
                Current = current;
                CurrentFeelsLike = currentFeelsLike;
            }
        }


        public struct WindData
        {
            /*Всё, что связано с ветром*/
            public float Speed { get; set; }
            public int Heading { get; set; }

            public WindData(float speed, int heading)
            {
                Speed = speed;
                Heading = heading;
            }
        }


        public string CityName { get; set; }
        public string Description { get; set; }

        public TemperatureData Temperature { get; set; }
        public WindData Wind { get; set; }

        public int Pressure { get; set; }
        public int Humidity { get; set; }
        public DateTimeOffset DateTime { get; set; }


        public WeatherForecast(JObject json)
        {
            CityName = json.Value<string>("name");
            Description = json["weather"][0].Value<string>("description");

            Temperature = new TemperatureData(
                json["main"].Value<float>("temp"),
                json["main"].Value<float>("feels_like"));

            Wind = new WindData(
                json["wind"].Value<float>("speed"),
                json["wind"].Value<int>("deg"));

            Pressure = json["main"].Value<int>("pressure") * 3 / 4;
            Humidity = json["main"].Value<int>("humidity");
            DateTime = DateTimeOffset.FromUnixTimeSeconds(json.Value<long>("dt")).ToLocalTime();
        }


        public override string ToString()
        {
            return (
                $"🌏 В населённом пункте {CityName} сейчас {Description}.\n " +
                $"🌡 Текущая температура — {Temperature.Current}°C, ощущается как {Temperature.CurrentFeelsLike}°C.\n\n" +
                $"💨 Ветер: {Wind.Speed} м/с с направлением {Wind.Heading}°.\n" +
                $"🌫 Атмосферное давление: {Pressure} мм. рт. ст.\n" +
                $"💧 Влажность: {Humidity}%\n\n" +
                $"⏱ Обновлено: {DateTime.ToString()}");
        }
    }


    public class WeatherProvider
    {
        private HttpClient Client { get; set; }


        [Serializable]
        public class InvalidCityName: Exception
        {
            public InvalidCityName(string cityName): base($"Неизвестное имя города: {cityName}") {}
        }


        [Serializable]
        public class InvalidResponse: Exception
        {
            public InvalidResponse(int code) : base(code.ToString()) {}
        }


        public WeatherProvider()
        {
            Client = new HttpClient();
        }


        public WeatherForecast GetForecast(string cityName)
        {
            //Метод получения прогноза погоды
            try
            {
                JObject openWeatherData = JObject.Parse(
                Client.GetStringAsync($"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid=f999beed5e2620b235528559dade33e9&lang=ru&units=metric")
                .Result);
                return new WeatherForecast(openWeatherData);
            }


            catch (AggregateException exception)
            {
                switch (exception.InnerException.StatusCode())
                {
                    case 404: throw new InvalidCityName(cityName);
                    default: throw new InvalidResponse(exception.StatusCode());
                }
                
            }
        }
    }
}
