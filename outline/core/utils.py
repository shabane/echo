"""some tools are writed here
"""    
from telegram import Bot


def re_wrapp_domain(key: str, domain: str, port: int):
    pre_domain = key[key.find('@')+1:key.find('/?')]
    return key.replace(pre_domain, f'{domain}:{port}')


def send_to_telegram(channel_id: str|int, caption: str, img: bytes) -> bool:    
    bot = Bot('806045748:AAGyPYfcE7EM6C9SWlPRKuIyHbcgZsvIn2Y')
    bot.send_document(chat_id=channel_id, caption=caption, document=img)
