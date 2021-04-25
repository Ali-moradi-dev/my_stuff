from telethon.sync import TelegramClient
from telethon import events
from enviorment import phone, api_id, api_hash, host, port
import socks

#define proxy
proxy = (socks.SOCKS5, host, port)

#set client
client = TelegramClient(phone, api_id, api_hash,proxy=proxy)

client.connect()

if not client.is_user_authorized():
    print('\n--------Loggin Need Authorizing .....')
    client.send_code_request(phone)
    print("Code Sent to  ==>",phone)
    client.sign_in(phone, input('\nEnter the code: '))

# -1001393611796


@client.on(events.NewMessage(incoming=True,func=lambda e: e.is_private))
async def my_event_handler(event):
    chat_id = event.chat_id
    text = event.raw_text
    chat_id = 1001393611796
    await client.send_message(chat_id,text)
    print(chat_id)
    print(text)





if __name__ == '__main__':
    client.start()
    print("Client is Starting ...")
    try:
        client.run_until_disconnected()
    except (KeyboardInterrupt, SystemExit):
        pass
