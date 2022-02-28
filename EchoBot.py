import telebot
from pyowm import OWM
from pyowm.commons.enums import SubscriptionTypeEnum

from TokenKeeper import PYOWMToken
from TokenKeeper import TelegramToken

RU_CONFIG = {
    'subscription_type': SubscriptionTypeEnum.FREE,
    'language': 'ru',
    'connection': {
        'use_ssl': True,
        'verify_ssl_certs': True,
        'use_proxy': False,
        'timeout_secs': 5
    },
    'proxies': {
        'http': 'http://user:pass@host:port',
        'https': 'socks5://user:pass@host:port'
    }
}
TOKEN = TelegramToken

bot = telebot.TeleBot(TOKEN, parse_mode=None)
owm = OWM(PYOWMToken, RU_CONFIG)
mgr = owm.weather_manager()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    bot.send_message(message.chat.id, "Сейчас в городе " + message.text + " " + w.detailed_status)


bot.infinity_polling()
