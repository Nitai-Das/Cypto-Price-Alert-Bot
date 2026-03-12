from pycoingecko import CoinGeckoAPI
from telegram import Bot
import asyncio
import time
import sys


# Retrieve Crypto prices
def price_tracking():
    cg = CoinGeckoAPI()
    targets = {
        'bitcoin': 65000
    }

    met_targets = {}

    for crypto, crypto_target in targets.items():
        response = cg.get_price(ids=crypto, vs_currencies='usd')
        current_price = response[crypto]['usd']
        target_price = targets[crypto]

        if current_price >= target_price:
            met_targets[crypto] = current_price

    if met_targets:
        message_body = '🎉Congrats, you made some money\n'

        for crypto, crypto_price in met_targets.items():
            current_price = crypto_price
            target_price = targets[crypto]
            message_body += (f'\n{crypto.upper()}\n'
                             f'Current price: ${current_price:.2f}\n'
                             f'Target price: ${target_price:.2f}\n')

        asyncio.run(send_telegram_message(message_body))

# Sending telegram message


async def send_telegram_message(message):
    bot_token = 'BOT_TOKEN'
    chatID = 'CHAT_ID'

    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chatID, text=message)


while True:
    price_tracking()
    time.sleep(60)

