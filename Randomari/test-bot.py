from telegram.ext import Updater, MessageHandler, Filters, CommandHandler


def start(bot, update):
    update.message.reply_text("Это то, что видит пользователь при первом обращении к боту")


def echo(bot, update):
    update.message.reply_text("Пользователь только что написал: " + update.message.text)


updater = Updater("1979131568:AAEgwUNOWNK33DFNacKPE9eEfadsB22_5kU")

dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))

text_handler = MessageHandler(Filters.text, echo)

dp.add_handler(text_handler)

updater.start_polling()

updater.idle()
