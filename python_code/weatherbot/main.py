import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


API_URL = "https://api.chucknorris.io/jokes/random"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send /joke to get a Chuck Norris joke.")


async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(API_URL)
        data = response.json()
        joke_text = data["value"]
        icon_url = data["icon_url"]

        
        await update.message.reply_photo(photo=icon_url, caption=joke_text)

    except Exception as e:
        logging.error(f"Error fetching joke: {e}")
        await update.message.reply_text("Sorry, I couldn't fetch a joke right now.")


def main():
    TOKEN = "7897277368:AAGWAePiHqHDhwKcuceNAMNFHzOXkevIcsk"
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("joke", joke))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
