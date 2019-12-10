import re
from telethon import TelegramClient, sync, events
import sqlite3
import time
from datetime import datetime
from datetime import timedelta
from parser_class import Parser_TTD
import Trip_news_data as tnd


def href_search(text):
    url = re.search(r'https?://[^\"\s>]+', text).group()
    return url

api_id = 1012339
api_hash = '9aaad9a87a58f309f44d599d2da55bde'

client = TelegramClient('Second', api_id, api_hash)


@client.on(events.NewMessage(chats=(-1001067688841)))
async def normal_handler(event):
    from_id = 'TripToDream'
    mess_dat = (datetime.utcnow() + timedelta(hours=3)
                ).strftime("%d.%m.%Y\n%H:%M")
    user_mess = event.message.to_dict()['message']
    url = href_search(user_mess)
    parser = Parser_TTD(url, tnd.data[2])
    text_news = parser.run()


    full_msg = f'**{from_id}**\n{text_news}\n{mess_dat}'
    await client.send_message(-1001329672585, full_msg, parse_mode='md', link_preview=False)

while True:
    try:
        client.start()

    except KeyboardInterrupt:
        break

    except Exception as e:

        print(e)
        time.sleep(15)
        client.run_until_disconnected()

