import socket
import ssl
import sys
import validators

from telegram import ParseMode


def handle(bot, update, args):
    if args:
        hostname = args.pop(0)
        print(hostname)
        if validators.domain(hostname):
            try:
                port = '443'
                context = ssl.create_default_context()
                sock = socket.create_connection((hostname, port))
                ssock = context.wrap_socket(sock, server_hostname=hostname)
                data = ssock.getpeercert()
                print(data)
                s = """
                Domain : ***{}***\nissuer : ***{}***\nnotAfter : ***{}***\nnotBefore : ***{}***
                """.format(hostname,
                           data['issuer'][4][0][1],
                           data['notAfter'],
                           data['notBefore'])
                bot.send_message(chat_id=update.message.chat_id,
                                 text='{}'.format(s),
                                 parse_mode=ParseMode.MARKDOWN)
            except ssl.SSLError as e:
                bot.send_message(chat_id=update.message.chat_id,
                         text='***{}***'.format(e),
                         parse_mode=ParseMode.MARKDOWN)
            except:
                bot.send_message(chat_id=update.message.chat_id,
                                 text='***{}***'.format(sys.exc_info()),
                                 parse_mode=ParseMode.MARKDOWN)
        else:
            bot.send_message(chat_id=update.message.chat_id,
                         text='***Ten domain khong hop le***\n'
                              'VD: /ssl minhkma.com',
                         parse_mode=ParseMode.MARKDOWN)
    else:
        bot.send_message(chat_id=update.message.chat_id,
                         text='***Nhap domain de check***\n'
                              'VD: /ssl minhkma.com',
                         parse_mode=ParseMode.MARKDOWN)