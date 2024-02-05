import telebot
import g4f


TELEGRAM_API_KEY = '6424189145:AAHZ9PClkZhcPO7Pw_OOedvUSUycz1OSWI8'
bot = telebot.TeleBot(TELEGRAM_API_KEY)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, я новый искусственный интеллект на базе OpenAI 🫡')

@bot.message_handler(['gpt3'])
def main(message):
    args = message.text.split()[1:]
    if args:
        response_text = ' '.join(args)
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=[{"role" : "user", "content": response_text}],
        )
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "Задать вопрос по такой схеме: /gpt3 [вопрос]\
                         Пример: /gpt3 Как образуется радуга?")

@bot.message_handler(commands=['gpt4'])
def main(message):
    args = message.text.split()[1:]
    if args:
        response_text = ' '.join(args)
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role" : "user", "content": response_text}],
        )
        bot.send_message(message.chat.id, response, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "Задать вопрос по такой схеме: /gpt4 [вопрос]\
                         Пример: /gpt4 Какая сейчас погода в Амстердаме?")
    
@bot.message_handler(commands=['llama'])
def main(message):
    args = message.text.split()[1:]
    if args:
        response_text = ' '.join(args)
        response = g4f.ChatCompletion.create(
            model=g4f.models.llama2_70b,
            messages=[{"role" : "user", "content": response_text}],
        )
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "Задать вопрос по такой схеме: /llama [вопрос]")

bot.polling(none_stop=True)