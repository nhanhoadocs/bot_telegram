import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler,\
    ConversationHandler, RegexHandler, MessageHandler, Filters


from telebot.plugins import mapping


CHOOSING, FIRST, SECOND, THIRD, FOURTH, FIFTH  = range(6)
data = {}


def handle(bot, update):
    keyboard = [[InlineKeyboardButton("Ram 2GB, vCPU 1, Disk 10G",
                                      callback_data='package1'),
                 InlineKeyboardButton("Ram 2GB, vCPU 2, Disk 20G",
                                      callback_data='package2')],
                [InlineKeyboardButton("Ram 4GB, vCPU 4, Disk 40G",
                                      callback_data='package3')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(u"Create VM, select flavor",
                              reply_markup=reply_markup)
    return FIRST

def first(bot, update):
    query = update.callback_query
    data['package'] = query.data
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"Select OS"
    )
    keyboard = []
    for os in mapping.OSs:
        keyboard.append([InlineKeyboardButton( mapping.OSs[os]['name'],
                                      callback_data=os)])
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=reply_markup
    )
    return SECOND

def second(bot, update):
    query = update.callback_query
    data['os'] = query.data
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"Select network"
    )
    keyboard = []
    for network in mapping.networks:
        keyboard.append([InlineKeyboardButton(network['name'],
                                      callback_data=network['device'])])
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=reply_markup
    )
    return THIRD

def third(bot, update):
     query = update.callback_query
     data['network'] = query.data
     bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"Select network"
     )
     keyboard = [[InlineKeyboardButton("Add a network",
                                      callback_data='add'),
                 InlineKeyboardButton("Skip",
                                      callback_data='skip')]]
     reply_markup = InlineKeyboardMarkup(keyboard)
     bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=reply_markup
     )
     return FOURTH

def choose_name(bot, update):
    query = update.callback_query
    if query.data == 'skip':
        update.callback_query.message.reply_text(
            "Alright, a new VM. Please choose a name for your VM.")
        return FIFTH
    elif query.data == 'add':
        bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u"Add a network or Skip"
        )
        keyboard = []
        for network in mapping.networks:
            keyboard.append([InlineKeyboardButton(network['name'],
                                          callback_data=network['device'])])
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.edit_message_reply_markup(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            reply_markup=reply_markup
        )

def create_vm(bot, update):
    name_vm = update.message.text
    data['name_vm'] = name_vm
    package = mapping.packages[data['package']]
    # print(package)
    cmd = mapping.OSs[data['os']]['cmd']
    print(cmd)
    # outut = os.open(cmd.format(data['name_vm'],
    #                  package['ram'],
    #                  package['vcpu'],
    #                  data['name_vm'],
    #                  package['disk'],
    #                  mapping.OSs[data['os']]['location'],
    #                  data['network'],
    #                  mapping.network_PXE['device'],
    #                  mapping.OSs[data['os']]['ks_dir']
    #                  )).read()
    # print(outut)
    update.message.reply_text('Create VM: {}.'
                              '\nPlease go to dashboard to view'
                              '\nBye Bye'.format(name_vm))


def create_vm_nics(bot, update):
    name_vm = update.message.text
    data['name_vm'] = name_vm
    package = mapping.packages[data['package']]
    # print(package)
    cmd = mapping.OSs[data['os']]['cmd']
    print(cmd)
    # outut = os.open(cmd.format(data['name_vm'],
    #                  package['ram'],
    #                  package['vcpu'],
    #                  data['name_vm'],
    #                  package['disk'],
    #                  mapping.OSs[data['os']]['location'],
    #                  data['network'],
    #                  mapping.network_PXE['device'],
    #                  mapping.OSs[data['os']]['ks_dir']
    #                  )).read()
    # print(outut)
    update.message.reply_text('Create VM: {}.'
                              '\nPlease go to dashboard to view'
                              '\nBye Bye'.format(name_vm))

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('create', handle)],
    states={
        FIRST: [CallbackQueryHandler(first)],
        SECOND: [CallbackQueryHandler(second)],
        THIRD: [CallbackQueryHandler(third)],
        FOURTH: [CallbackQueryHandler(choose_name)],
        FIFTH: [MessageHandler(Filters.text, create_vm)],
    },
    fallbacks=[CommandHandler('create', handle)],
)