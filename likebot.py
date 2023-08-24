from telegram import Bot
import time
import os

TOKEN = os.environ.get('TOKEN')


bot = Bot(token=TOKEN)

LIKES: int = 0
DISLIKES: int = 0

def echo():
    update_id = 0

    global LIKES
    global DISLIKES

    while True:
        time.sleep(0.5)
        
        updates = bot.get_updates()
        if updates[-1].update_id == update_id:
            continue
        else:
            last_update = updates[-1]
            message = last_update.message

            chat_id = message.chat.id

            if message.text != None:
                text = message.text

                if text == '/start':
                    keyboard = {"keyboard": [["👍", "👎"]], "resize_keyboard": True}
                    print('start')
                    bot.send_message(chat_id=chat_id, text='Hello, World!', reply_markup=keyboard)
                elif text == '👍':
                    LIKES += 1
                    bot.send_message(chat_id=chat_id, text=f'LIKES: {LIKES}\nDISLIKES: {DISLIKES}')
                elif text == '👎':
                    DISLIKES += 1
                    bot.send_message(chat_id=chat_id, text=f'DISLIKES: {DISLIKES}\nLIKES: {LIKES}')
                else:
                    bot.send_message(chat_id=chat_id, text='you are wrong')

            update_id = updates[-1].update_id

echo()