import shodan
import json
import time
import requests
import shodan
from telegram import ParseMode
import validators

def get_port(hostname):
    api_key = "WSfoblrpUWNh3LA9eXqdNXuHJPco9ozJ"
    api = shodan.Shodan(api_key)
    try:
        info = api.host(hostname)
        datas = info["data"]
        ports = "Port đang sử dụng\n"
        for data in datas:
            port = str(data["port"])
            service = str(data["_shodan"]["module"])
            port_1 = "`" + port + ":" + service + "`"
            ports = ports + "\n" + port_1
    except:
        ports = "Not found"
    return ports

def handle(bot, update, args):
    if args:
        if len(args) < 2:
            ip = args.pop(0)
            if validators.ipv4(ip):
                data = get_port(ip)
                print(data)
                if data:
                    update.message.reply_text(text='{}'.format(data), parse_mode=ParseMode.MARKDOWN)
                else:
                    update.message.reply_text(text='***Not Found***', parse_mode=ParseMode.MARKDOWN)
            else:
                update.message.reply_text(text='***you must enter a IP***', parse_mode=ParseMode.MARKDOWN)
        else:
            update.message.reply_text(text='***you must enter a IP***', parse_mode=ParseMode.MARKDOWN)
    else:
        update.message.reply_text(text='***you must enter a IP***', parse_mode=ParseMode.MARKDOWN)
