from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba! Bana bir URL gönderin, ben de dosyayı indirip sizin için yükleyeceğim.")

def upload_file(update, context):
    url = update.message.text
    file = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as f:
        f.write(file.content)
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_name, "rb"))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Dosya yüklendi.")

def main():
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, upload_file))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

Bu kod, `python-telegram-bot` kütüphanesini kullanarak bir Telegram botu oluşturur. `start` fonksiyonu, botunuzu başlatmak için bir komut işleyicisidir. `upload_file` fonksiyonu, kullanıcının gönderdiği URL'i alır, dosyayı indirir ve kullanıcının sohbetine dosyayı yükler. Bot token'inizi `YOUR_BOT_TOKEN` ile değiştirin.
