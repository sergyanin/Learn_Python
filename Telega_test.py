from telethon import TelegramClient, sync, events
import re
import sqlite3
import time
from datetime import datetime
from datetime import timedelta


# Вставляем api_id и api_hash
api_id = 1012339
api_hash = '9aaad9a87a58f309f44d599d2da55bde'

client = TelegramClient('Second', api_id, api_hash)


def href_search(text):
    url = re.search(r'https?://[^\"\s>]+', text).group()
    return url

@client.on(events.NewMessage(chats=(-1001329672585)))
async def normal_handler(event):
    print('Test')
    print(event.message)
    # event.message.to_dict()['date'].strftime("%d.%m.%Y\n%H:%M\n")    
    mess= event.message.to_dict()['message']
    print(href_search(mess))

    print('\n\n\n')

    

while True:
    try:
        client.start()

    except KeyboardInterrupt:
        break

    except Exception as e:

        print(e)
        time.sleep(15)
        client.run_until_disconnected()
