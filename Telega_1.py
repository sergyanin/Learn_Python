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




@client.on(events.NewMessage(chats=(-1001164207750)))
async def normal_handler(event):
    # print(event.message)
    # event.message.to_dict()['date'].strftime("%d.%m.%Y\n%H:%M\n")
    mess_dat = (datetime.utcnow() + timedelta(hours=3)
                ).strftime("%d.%m.%Y\n%H:%M\n")
    user_mess = event.message.to_dict()['message']
    full_msg = f'**{mess_dat}**\n{user_mess}'
    # print(mess_date = str(event.message.to_dict()['date']))
    await client.send_message(-1001329672585, full_msg, parse_mode='md')


@client.on(events.NewMessage(chats=(-1001141664489)))
async def normal_handler(event):
    # print(event.message)
    mess_dat = (datetime.utcnow() + timedelta(hours=3)
                ).strftime("%d.%m.%Y\n%H:%M\n")    
    user_mess = event.message.to_dict()['message']
    full_msg = f'**{mess_dat}**\n{user_mess}'
    # print(mess_date = str(event.message.to_dict()['date']))
    await client.send_message(-1001329672585, full_msg, parse_mode='md')


@client.on(events.NewMessage(chats=(-1001067688841)))
async def normal_handler(event):
    # print(event.message)
    mess_dat = (datetime.utcnow() + timedelta(hours=3)
                ).strftime("%d.%m.%Y\n%H:%M\n")    
    user_mess = event.message.to_dict()['message']
    full_msg = f'**{mess_dat}**\n{user_mess}'
    # print(mess_date = str(event.message.to_dict()['date']))
    await client.send_message(-1001329672585, full_msg, parse_mode='md')
while True:
    try:
        client.start()
        
    except Exception as e:

        print(e)
        time.sleep(15)
        client.run_until_disconnected()
    
