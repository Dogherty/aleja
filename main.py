from telethon import TelegramClient, sync, events
from googletrans import Translator

translator = Translator()


INPUT_CHANNEL = 'dogherty_post_test'
OUTPUT_CHANNEL = 'sfdvdbdbfjcjvhhfhrvwv'

api_id = 20036480
api_hash = '042a09688357da2892b975c79a724f27'

client = TelegramClient('sad', api_id, api_hash)

@client.on(events.NewMessage(chats=(INPUT_CHANNEL)))
async def normal_handler(event):
    await client.send_message(OUTPUT_CHANNEL, event.message)
    await client.send_message(OUTPUT_CHANNEL, translator.translate(event.message.text, dest='es').text)

client.start()
client.run_until_disconnected()