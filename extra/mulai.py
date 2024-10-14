import os
import sys
from telebot import TeleBot

def restart(bot: TeleBot, message) -> None:
    chat_id = message.chat.id
    message_id = message.message_id
    bot.send_message(chat_id=chat_id, text="Bot berhasil dinyalakan ulang.")

    # Save the chat and message ID to a file for post-restart actions (optional)
    with open(".restartmsg", "w") as f:
        f.write(f"{chat_id}\n{message_id}\n")

    # Restart server by first running update.py then main.py
    os.execl(sys.executable, sys.executable, "-c", "import os; os.system('python update.py'); os.execl(sys.executable, sys.executable, 'main.py')")
