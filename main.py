from telegram.ext import Updater, MessageHandler, Filters
from telegram import ChatMemberUpdated
import time

TOKEN = "8452416399:AAFOguo97PwEmXQJie6Q8PT11Ykuh0qCs2w" 

RULES = """
👋 ¡Bienvenid@ al grupo!

📌 Reglas básicas:
1. Respeto entre todos.
2. Prohibido spam.
3. No enviar contenido ilegal.
4. Mantener los temas del grupo.

¡Disfruta el chat!
"""

def greet(update, context):
    # Detectar si el evento es entrada de un nuevo usuario
    for member in update.message.new_chat_members:
        msg = update.message.reply_text(f"Bienvenido {member.full_name}!\n\n{RULES}")
        
        # Esperar unos segundos antes de borrar
        time.sleep(15)

        # Eliminar el mensaje del bot
        context.bot.delete_message(chat_id=update.message.chat_id, message_id=msg.message_id)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Detectar nuevos miembros
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, greet))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
