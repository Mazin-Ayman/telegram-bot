import telebot
from telebot import types, util
BOT_TOKEN = "5878480583:AAGipE9ZQgt7Ld6KUqo9Pr2YWpaR7JZotvM"

bot = telebot.TeleBot(BOT_TOKEN)
text_messages = {
    "greeting":u"اهلا {name} مرحبا بك في مجموعتنا☺️",
    "goodbye":u"لقد غادر {name} المجموعه😥",
    "leave":u"لقد تمت إضافتي الى مجموعة لم يتم التعرف عليها لذلك باي👋",
    "call":"مرحبا كيف يمكنني مساعدتك🤔؟ ",
    "bot-info":'''مرحبا👋👋
    انا بوت تم برمجتي بواسطه @Mazin_Ayman'''
}
@bot.message_handler(commands=['start'])
def hello(msg):
    bot.send_message(msg.chat.id, f'Hello @{msg.from_user.username}')
@bot.chat_member_handler()
def handle(message:types.ChatMemberUpdated):
    newResponse = message.new_chat_member
    if newResponse.status == 'member':
        bot.send_message(message.chat.id,
        text_messages['greeting'].format(name=newResponse.user.first_name))
    if newResponse.status == 'left':
        bot.send_message(message.chat.id,
        text_messages['goodbye'].format(name=newResponse.user.first_name))


# exits
@bot.my_chat_member_handler()
def leave(message:types.ChatMemberUpdated):
    update = message.new_chat_member
    if update.status == 'member':
        bot.send_message(message.chat.id, text_messages['leave'])
        bot.leave_chat(message.chat.id)


# listening to all messages
@bot.message_handler(func=lambda m:True)
def reply(msg):
    text = msg.text.split()
    if text[0] == "bot":
        bot.reply_to(msg, text_messages['call'])
    elif text[0] == "bot-info":
        bot.reply_to(msg, text_messages['bot-info'])
bot.infinity_polling(allowed_updates=util.update_types)
