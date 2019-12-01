from datetime import timedelta, datetime



# Message(mentioned=False, message='The first thing', fwd_from=None, reply_markup=None, id=103225, legacy=None, media_unread=False, via_bot_id=None, date=datetime.datetime(2019, 11, 23, 9, 12, 38, tzinfo=datetime.timezone.utc), media=None, to_id=PeerChat(chat_id=376737263), silent=False, post_author=None, post=None, grouped_id=None, from_scheduled=None, entities=[], views=None, edit_date=None, reply_to_msg_id=None, edit_hide=None, out=True, restriction_reason=[], from_id=168343328)

user_mess = 'Что-то прилетело сюда'
mess_dat = (datetime.utcnow() + timedelta(hours=3)
            ).strftime("%d.%m.%Y\n%H:%M\n")
full_msg = f'**{mess_dat}**\n{user_mess}'
print(full_msg)
