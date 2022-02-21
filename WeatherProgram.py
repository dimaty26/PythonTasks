from pyowm import OWM
from pyowm.commons.enums import SubscriptionTypeEnum

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

owm = OWM('#TODO: insert your own API key', RU_CONFIG)
mgr = owm.weather_manager()

place = input("В каком городе посмотреть погоду? ")

observation = mgr.weather_at_place(place)
w = observation.weather
print("Сейчас в городе " + place + " " + w.detailed_status)
print(w.temperature('celsius')['temp'])
