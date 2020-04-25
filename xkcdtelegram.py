import xkcdhelper
from telegram.ext import Updater, CommandHandler

TOKEN = '1240765482:AAGx-Fb_4RJg76wzYRk3NLtRFQM37n-kL9k'
print('Hello world')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', xkcdhelper.start))
dispatcher.add_handler(CommandHandler('getxkcd', xkcdhelper.getxkcd))

updater.start_polling()


