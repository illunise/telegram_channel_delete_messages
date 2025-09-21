from telethon import TelegramClient, events

api_id = 23415122
api_hash = '99031ccaece715486c96b1a2193032d4'
session_name = 'ManishForward'
channel = -1001985769215

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    async for message in client.iter_messages(channel):
        try:
            await client.delete_messages(channel, message.id)
            print(f"Deleted message: {message.id}")
        except Exception as e:
            print(f"Could not delete message {message.id}: {e}")

with client:
    client.loop.run_until_complete(main())
