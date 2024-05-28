import os
import json
import requests
import random

import telebot

BOT_TOKEN = os.environ['BOT_TOKEN']

bot = telebot.TeleBot(BOT_TOKEN)

DIALOG = {
    'hello':{
        'in': ['/hello', 'hello', 'hi', 'Привет', 'Как сам', 'privet'],
        'out': [
            '✌️Привет, я kp-lr8-bot! Рад знакомству',
            '✌️Здравствуйте.',
            '✌️Привет!'
        ]
    },
    'how are you':{
        'in': ['/howareyou', 'how are you', 'как дела', 'как ты', 'дела'],
        'out': [
            '👍Хорошо',
            '👍Отлично',
            '👍Good. And how are you!'
        ]
    },
    'name':{
        'in': ['/name', 'name', 'имя', 'как зовут', 'зовут'],
        'out': [
            'Меня зовут kp-lr8-bot😊',
            'Я телеграм-бот по имени kp-lr8-bot😊',
            'Я kp-lr8-bot😊'
        ]
    },
    'help':{
        'in': ['/help', 'help', 'импомощь', 'помоги'],
        'out': [
            'Как я могу тебе помочь?',
            'Сегодня я помогу тебе лучше, чем вчера',
            'Не, сегодня ты сам..'
        ]
    },
}

def flatten(l):
    return [item for sublist in l for item in sublist]

def handler(event, context):
    body = json.loads(event['body'])

    update = telebot.types.Update.de_json(body)

    bot.process_new_updates([update])

    return {
        'statusCode': 200,
        'body': 'NULL',
    }

@bot.message_handler(commands=['start','help'])
def start_handler(message):
    message_fragments = flatten([message_case['in'] for message_case in DIALOG.values()])
    bot.send_message(message.chat.id, f"Я не понял, команды: {', '.join(message_fragments)}")

@bot.message_handler(func = lambda message: True)
def simple_chat(message):
    message_text = message.text

    try:
        message_reply = None
        for message_type, message_case in DIALOG.items():
            if any([message_fragment in message_text for message_fragment in message_case['in']]):
                message_reply = random.choice(message_case['out'])
                break
                
        else:
            message_fragments = flatten([message_case['in'] for message_case in DIALOG.values()])
            message_reply = f"Я не понял, команды: {', '.join(message_fragments)}"

        bot.send_message(message.chat.id, message_reply)

    except BaseException as exception:
        print(f"Exception: {exception}")