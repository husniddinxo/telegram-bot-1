from telegram import Bot
import time

token = "6567664761:AAEi3kspotCXSdGZr7H849nudbEj31p5mE8"

bot = Bot(token=token)

def echo():
    update_id = 0

    while True:
        time.sleep(0.5)

        # print(f'updates: {update_id}')
        updates = bot.get_updates()
        if updates[-1].update_id == update_id:
            continue
        else:
            last_update = updates[-1]
            
            message = last_update.message
            # pprint(message)
            print("-"*50)

            chat_id = message.chat.id
            text = message.text 

            bot.send_message(chat_id=chat_id, text=text)

            update_id = updates[-1].update_id

echo()