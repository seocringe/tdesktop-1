from telethon import TelegramClient

# Используйте свои значения api_id и api_hash здесь
api_id = 13481076
api_hash = '38eae581b24be85cb7c4e69c619f852b'

# Создайте экземпляр клиента
client = TelegramClient('session_name', api_id, api_hash)

# Асинхронно запустите клиент
async def main():
    # Подключитесь к серверам Telegram
    await client.start()
    
    # Теперь вы можете вызывать методы API через объект client
    
    # Например, отправим сообщение самому себе
    await client.send_message('me', 'Привет! Клиент MTProto успешно инициализирован.')

# Выполните функцию main
with client:
    client.loop.run_until_complete(main())
