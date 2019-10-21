def handle(bot, update, args):
    action = args.pop(0)
    bot.send_message(chat_id=update.message.chat_id,
                     text=action)