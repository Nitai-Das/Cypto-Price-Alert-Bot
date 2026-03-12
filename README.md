Crypto Price Alert Telegram Bot

Overview
This Crypto Price Alert Telegram Bot is a FinTech automation built with python that monitors cryptocurrency prices and sends an alert to the user when a target price has been reached or exceeded.
The bot retrieves real-time cryptocurrency information from CoinGecko’s API and would notify the users through telegram, allowing users to track the crypto prices without checking the market manually.

Features
-	Automated Telegram notifications
-	Real-Time cryptocurrency price tracking
-	Utilises CoinGecko API for accurate market data

How it Works
1.	The program defines a list of cryptocurrencies and its target prices.
2.	Every 1 hour, the bot collects the latest data from CoinGecko
3.	The program would then compare the current price and the target price
4.	If the target price has been reached or exceeded, the telegram notification is sent.  

Technologies
-	Python 
-	CoinGecko API
-	Telegram BOT
-	Asyncio 

Installation
1.	Clone the repository: https://github.com/Nitai-Das/Robo-Adivsor-Simulator.git
2.	Install the dependency in bash: 
•	pip install pycoingecko 
•	pip install python-telegram-bot –upgrade
Configuration
Setting up Telegram bot token
•	Create a bot in Telegram using BotFather and replace:
bot_token = 'BOT_TOKEN' with your own bot token

Setting up Chat ID
- Replace:  chatID = 'CHAT_ID' with your own chat id

Setting Crypto names and its Target Prices
- Within the price_tracking() method, you can modify the “targets” dictionary to track your preferred cryptocurrencies and set their target prices

e.g. 
targets = 
{

        	'bitcoin': 65000,
 	        ‘ethereum’: 2000
    }

Future improvement
-	Deploy Telegram bot to a cloud server for running non-stop
-	Allow users to add the cryptocurrencies and target prices directly through Telegram.

