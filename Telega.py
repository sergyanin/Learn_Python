from telethon import TelegramClient, sync
import re
from resorts import resorts

# Вставляем api_id и api_hash
api_id = 1012339
api_hash = '9aaad9a87a58f309f44d599d2da55bde'

client = TelegramClient('First', api_id, api_hash)




# for dialog in client.iter_dialogs():
#     print(dialog.name, 'has ID', dialog.id)
# # messages = client.get_entity('539046925')
# # print(messages)

# channel_list =[]
# for dialog in client.iter_dialogs():
#     channel_list.append({
#         'ID': dialog.id,
#         'Name': dialog.title
#     })
#     # print('{:>14}: {}'.format(dialog.id,  dialog.title))

# with open('channel_list.txt', 'w', encoding='utf-8') as f:
#     i = 1
#     for item in channel_list:
#         f.write(f'{i}. Канал: {item["Name"]} ID: {item["ID"] } \n')
#         i += 1
#     print(f'{dialog.id}: {dialog.title}')

words = resorts['Таиланд']

# for i in reads:
#     if re.search(word, i['title']):
#         print(i)


result = client.iter_messages(-1001164207750, limit=30)
for message in result:
    for word in words:
        if re.search(word, str(message)):
            client.send_message(-1001329672585, str(message.text))
                
    



