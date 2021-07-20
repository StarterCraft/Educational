using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Json;
using System.Linq;
using Newtonsoft.Json.Linq;
using Telegram.Bot;
using StarterWeatherProvider;

class Program
{
    static WeatherProvider provider;
    static TelegramBotClient botClient;

    static void Main()
    {
        provider = new WeatherProvider();
        botClient = new TelegramBotClient(System.IO.File.ReadAllText("config.ini"));

        botClient.OnMessage += OnMessage;
        botClient.StartReceiving();
        while (true);
    }

    private static void OnMessage(object sender, Telegram.Bot.Args.MessageEventArgs e)
    {
        string command = e.Message.Text.ToLower();

        Console.WriteLine($"{e.Message.From.FirstName} {e.Message.From.LastName}: {command}");

        switch (command)
        {
            case "/start":
                botClient.SendTextMessageAsync(
                    e.Message.Chat.Id,
                    $"ℹ Введите имя населённого пункта, чтобы узнать текущую погоду в нём",
                    replyToMessageId: e.Message.MessageId);
                break;

            default:
                try
                {
                    string forecastString = provider.GetForecast(command).ToString();
                    botClient.SendTextMessageAsync(
                        e.Message.Chat.Id,
                        $"{e.Message.From.FirstName}, ваш прогноз погоды:\n\n{forecastString}",
                        replyToMessageId: e.Message.MessageId);

                    forecastString = null;
                    break;
                }


                catch (Exception exception)
                {
                    botClient.SendTextMessageAsync(
                        e.Message.Chat.Id,
                        $"{e.Message.From.FirstName}, произошла ошибка:\n🚫 {exception.Message}",
                        replyToMessageId: e.Message.MessageId);
                    break;
                }
        }
    }
}
