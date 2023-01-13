import os
import openai
import telebot

openai.api_key = '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'
bot=telebot.TeleBot("5904307834:AAF0TvFZkTCWz17LifeTXN0YxUM_wPC3qLo")

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])

bot.polling()

