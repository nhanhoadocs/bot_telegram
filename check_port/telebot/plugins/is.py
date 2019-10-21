import requests
import validators
from telegram import ParseMode


def handle(bot, update, args):
    if args:
        domain = args.pop(0)
        if validators.domain(domain):
            try:
                data = requests.get("https://{}".format(domain))
                time = data.elapsed.total_seconds()
                code = data.status_code
                msg = "Website ***https://{}*** voi status code la `{}` trong `{}s`".format(domain,
                                                                         code,
                                                                         time)
                update.message.reply_text(
                             text=msg,
                             parse_mode=ParseMode.MARKDOWN)
            except requests.exceptions.ConnectionError:
                update.message.reply_text(
                             text='***Ket noi that bai toi website*** '
                                  '`https://{}`'.format(domain),
                             parse_mode=ParseMode.MARKDOWN)

        else:
            update.message.reply_text(
                         text='***Ten domain khong hop le***\n'
                              'VD: /is minhkma.com',
                         parse_mode=ParseMode.MARKDOWN)
    else:
        update.message.reply_text(
                         text='***Nhap domain ban muon check***\n'
                              'VD: /is minhkma.com',
                         parse_mode=ParseMode.MARKDOWN)