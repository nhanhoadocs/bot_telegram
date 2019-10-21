import whois
import socket
import validators
from telegram import ParseMode
import requests
from bs4 import BeautifulSoup


def handle(bot, update, args):
    if args:
        action = args.pop(0)
        if validators.domain(action):
            domain_split = action.split('.')
            if domain_split[len(domain_split) - 1] == 'vn':
                if domain_split[0] == 'www':
                    domain_split = list(set(domain_split) - set(['www']))
                    if len(domain_split) == 2:
                        domain_split = list(set(domain_split) - set(['vn']))
                        headers = {
                            'Accept-Language': 'en',
                        }

                        params = {"domain": domain_split[0], "ext": '.vn',
                                  "type": '1'}

                        response = requests.get('https://nhanhoa.com/whois/',
                                                headers=headers, params=params)
                        if response:
                            parsed_html = BeautifulSoup(response.text)

                            keys = parsed_html.findAll('div', {"class": "flleft"})
                            values = parsed_html.findAll('div',
                                                         {"class": "flright"})
                            data_keys = []
                            data_values = []
                            for key in keys:
                                if str(key.text).startswith('DNS'):
                                    key = key.text.split(":")[0]
                                    data_keys.append(key)
                                else:
                                    data_keys.append(key.text)
                            for value in values:
                                data_values.append(value.text)
                            data = {}
                            for i, j in list(zip(data_keys, data_values)):
                                data[i] = j
                            s = "Tên miền : ***{}***\n" \
                                "Nhà đăng kí : ***{}***\n" \
                                "Trạng thái : ***{}***\n" \
                                "Ngày đăng kí : ***{}***\n" \
                                "Ngày hết hạn : ***{}***\n" \
                                "Nameservers : ***{}***\n" \
                                "DNSSEC : ***{}***".format(data['Domain:'],
                                                           data['Registrar Name'],
                                                           data['Status'],
                                                           data['Issue Date'],
                                                           data['Expired Date'],
                                                           data['DNS'],
                                                           data['DNSSEC']
                                                           )
                            if data['Domain:'] != '' and\
                                    data['Registrar Name'] != ''\
                                    and data['Status'] != ''\
                                    and data['Issue Date'] != ''\
                                    and data['Expired Date'] != ''\
                                    and data['DNS'] != ''\
                                    and data['DNSSEC'] != '':
                                update.message.reply_text(
                                                 text=s,
                                                 parse_mode=ParseMode.MARKDOWN)
                            else:
                                update.message.reply_text(
                                                 text='***Khong tim thay thong tin domain*** ```{}```'.format(action),
                                                 parse_mode=ParseMode.MARKDOWN)
                        else:
                            update.message.reply_text(
                                             text='***Khong tim thay thong tin domain*** ```{}```'.format(action),
                                             parse_mode=ParseMode.MARKDOWN)
                    elif len(domain_split) == 3 and 'com' in domain_split:
                        domain_split = list(set(domain_split) - set(['com', 'vn']))
                        headers = {
                            'Accept-Language': 'en',
                        }

                        params = {"domain" : domain_split[0], "ext" : '.com.vn', "type" : '1'}

                        response = requests.get('https://nhanhoa.com/whois/', headers=headers, params=params)
                        if response:
                            parsed_html = BeautifulSoup(response.text)

                            keys = parsed_html.findAll('div', {"class": "flleft"})
                            values = parsed_html.findAll('div', {"class": "flright"})
                            data_keys = []
                            data_values = []
                            for key in keys:
                                if str(key.text).startswith('DNS'):
                                    key = key.text.split(":")[0]
                                    data_keys.append(key)
                                else:
                                    data_keys.append(key.text)
                            for value in values:
                                data_values.append(value.text)
                            data = {}
                            for i,j in list(zip(data_keys,data_values)):
                                data[i] = j
                            s = "Tên miền : ***{}***\n" \
                                "Nhà đăng kí : ***{}***\n" \
                                "Trạng thái : ***{}***\n" \
                                "Ngày đăng kí : ***{}***\n" \
                                "Ngày hết hạn : ***{}***\n" \
                                "Nameservers : ***{}***\n" \
                                "DNSSEC : ***{}***".format(data['Domain:'],
                                                           data['Registrar Name'],
                                                           data['Status'],
                                                           data['Issue Date'],
                                                           data['Expired Date'],
                                                           data['DNS'],
                                                           data['DNSSEC']
                                                           )
                            if data['Domain:'] != '' and\
                                    data['Registrar Name'] != ''\
                                    and data['Status'] != ''\
                                    and data['Issue Date'] != ''\
                                    and data['Expired Date'] != ''\
                                    and data['DNS'] != ''\
                                    and data['DNSSEC'] != '':
                                update.message.reply_text(
                                                 text=s,
                                                 parse_mode=ParseMode.MARKDOWN)
                            else:
                                update.message.reply_text(
                                                 text='***Khong tim thay thong tin domain*** ```{}```'.format(action),
                                                 parse_mode=ParseMode.MARKDOWN)
                        else:
                            update.message.reply_text(
                                             text='***Khong tim thay thong tin domain*** ```{}```'.format(action),
                                             parse_mode=ParseMode.MARKDOWN)
                    else:
                        update.message.reply_text(
                                         text='***Chi ho tro domain co dang minhkma.vn***',
                                         parse_mode=ParseMode.MARKDOWN)
                else:
                    if len(domain_split) == 2:
                        headers = {
                            'Accept-Language': 'en',
                        }

                        params = {"domain": domain_split[0], "ext": '.vn',
                                  "type": '1'}

                        response = requests.get('https://nhanhoa.com/whois/',
                                                headers=headers, params=params)
                        if response:
                            parsed_html = BeautifulSoup(response.text)

                            keys = parsed_html.findAll('div', {"class": "flleft"})
                            values = parsed_html.findAll('div',
                                                         {"class": "flright"})
                            data_keys = []
                            data_values = []
                            for key in keys:
                                if str(key.text).startswith('DNS'):
                                    key = key.text.split(":")[0]
                                    data_keys.append(key)
                                else:
                                    data_keys.append(key.text)
                            for value in values:
                                data_values.append(value.text)
                            data = {}
                            for i, j in list(zip(data_keys, data_values)):
                                data[i] = j
                            s = "Tên miền : ***{}***\n" \
                                "Nhà đăng kí : ***{}***\n" \
                                "Trạng thái : ***{}***\n" \
                                "Ngày đăng kí : ***{}***\n" \
                                "Ngày hết hạn : ***{}***\n" \
                                "Nameservers : ***{}***\n" \
                                "DNSSEC : ***{}***".format(data['Domain:'],
                                                           data['Registrar Name'],
                                                           data['Status'],
                                                           data['Issue Date'],
                                                           data['Expired Date'],
                                                           data['DNS'],
                                                           data['DNSSEC']
                                                           )
                            if data['Domain:'] != '' and\
                                    data['Registrar Name'] != ''\
                                    and data['Status'] != ''\
                                    and data['Issue Date'] != ''\
                                    and data['Expired Date'] != ''\
                                    and data['DNS'] != ''\
                                    and data['DNSSEC'] != '':
                                update.message.reply_text(
                                                 text=s,
                                                 parse_mode=ParseMode.MARKDOWN)
                            else:
                                update.message.reply_text(
                                                 text='***Khong tim thay thong tin domain*** ```{}```'.format(action),
                                                 parse_mode=ParseMode.MARKDOWN)
                        else:
                            update.message.reply_text(
                                             text='***Khong tim thay thong tin domain*** ```{}```'.format(action),
                                             parse_mode=ParseMode.MARKDOWN)
                    elif domain_split[len(domain_split) - 2] == 'com':
                        headers = {
                            'Accept-Language': 'en',
                        }

                        params = {"domain" : domain_split[0], "ext" : '.com.vn', "type" : '1'}

                        response = requests.get('https://nhanhoa.com/whois/', headers=headers, params=params)
                        if response:
                            parsed_html = BeautifulSoup(response.text)

                            keys = parsed_html.findAll('div', {"class": "flleft"})
                            values = parsed_html.findAll('div', {"class": "flright"})
                            data_keys = []
                            data_values = []
                            for key in keys:
                                if str(key.text).startswith('DNS'):
                                    key = key.text.split(":")[0]
                                    data_keys.append(key)
                                else:
                                    data_keys.append(key.text)
                            for value in values:
                                data_values.append(value.text)
                            data = {}
                            for i,j in list(zip(data_keys,data_values)):
                                data[i] = j
                            s = "Tên miền : ***{}***\n" \
                                "Nhà đăng kí : ***{}***\n" \
                                "Trạng thái : ***{}***\n" \
                                "Ngày đăng kí : ***{}***\n" \
                                "Ngày hết hạn : ***{}***\n" \
                                "Nameservers : ***{}***\n" \
                                "DNSSEC : ***{}***".format(data['Domain:'],
                                                           data['Registrar Name'],
                                                           data['Status'],
                                                           data['Issue Date'],
                                                           data['Expired Date'],
                                                           data['DNS'],
                                                           data['DNSSEC']
                                                           )
                            if data['Domain:'] != '' and\
                                    data['Registrar Name'] != ''\
                                    and data['Status'] != ''\
                                    and data['Issue Date'] != ''\
                                    and data['Expired Date'] != ''\
                                    and data['DNS'] != ''\
                                    and data['DNSSEC'] != '':
                                update.message.reply_text(
                                                 text=s,
                                                 parse_mode=ParseMode.MARKDOWN)
                            else:
                                update.message.reply_text(
                                                 text='***Khong tim thay thong tin domain*** ```{}```'.format(action),
                                                 parse_mode=ParseMode.MARKDOWN)
                        else:
                            update.message.reply_text(
                                             text='***Khong tim thay thong tin domain*** ```{}```'.format(action),
                                             parse_mode=ParseMode.MARKDOWN)
                    else:
                        update.message.reply_text(
                                         text='***Khong tim thay thong tin domain*** ```{}```'.format(action),
                                         parse_mode=ParseMode.MARKDOWN)
            else:
                try:
                    w = whois.whois(action)
                    if w:
                        if w.domain_name:
                            if type(w.domain_name) is list:
                                domain_name = w.domain_name[0]
                            else:
                                domain_name = w.domain_name
                        else:
                            domain_name = None
                        if w.status:
                            if type(w.status) is list:
                                status_domain = []
                                for i in w.status:
                                    status_domain.append(i.split()[0])
                                status = " | ".join(status_domain)
                            elif type(w.status) is str:
                                status = w.status.split()[0]
                            else:
                                status = None
                        else:
                            status = None
                        if w.creation_date:
                            if type(w.creation_date) is list:
                                creation_date = w.creation_date[0]
                            else:
                                creation_date = w.creation_date
                        else:
                            creation_date = None
                        if w.expiration_date:
                            if type(w.expiration_date) is list:
                                expiration_date = w.expiration_date[0]
                            else:
                                expiration_date = w.expiration_date
                        else:
                            expiration_date = None
                        if w.updated_date:
                            if type(w.updated_date) is list:
                                updated_date = w.updated_date[0]
                            else:
                                updated_date = w.updated_date
                        else:
                            updated_date = None
                        if w.dnssec:
                            if type(w.dnssec) is list:
                                dnssec = w.dnssec[0]
                            else:
                                dnssec = w.dnssec
                        else:
                            dnssec = None
                        if w.name_servers:
                            if type(w.name_servers) is list:
                                name_servers = " | ".join(w.name_servers)
                            elif type(w.name_servers) is str:
                                name_servers = w.name_servers
                            else:
                                name_servers = None
                        else:
                            name_servers = None
                        s = "Tên miền : ***{}***\n" \
                            "Nhà đăng kí : ***{}***\n" \
                            "Trạng thái : ***{}***\n" \
                            "Ngày đăng kí : ***{}***\n" \
                            "Ngày cập nhập : ***{}***\n" \
                            "Ngày hết hạn : ***{}***\n" \
                            "Nameservers : ***{}***\n" \
                            "DNSSEC : ***{}***".format(
                            domain_name,
                            w.registrar,
                            status,
                            creation_date,
                            updated_date,
                            expiration_date,
                            name_servers,
                            dnssec
                        )
                        if s:
                            update.message.reply_text(
                                             text=s,
                                             parse_mode=ParseMode.MARKDOWN)
                        else:
                            update.message.reply_text(
                                             text='***Khong tim thay thong tin domain*** '
                                                  '`{}`'.format(action),
                                             parse_mode=ParseMode.MARKDOWN)
                    else:
                        update.message.reply_text(
                                         text='***Khong tim thay thong tin domain*** '
                                              '`{}`'.format(action),
                                         parse_mode=ParseMode.MARKDOWN)
                except socket.gaierror:
                    update.message.reply_text(
                                     text='***Khong tim thay thong tin domain*** '
                                          '`{}`'.format(action),
                                     parse_mode=ParseMode.MARKDOWN)
                except:
                    update.message.reply_text(
                                     text='***Khong tim thay thong tin domain*** '
                                          '`{}`'.format(action),
                                     parse_mode=ParseMode.MARKDOWN)
        else:
            update.message.reply_text(
                             text='***Ban phai nhap mot domain***\n'
                                  'VD: minhkma.com',
                             parse_mode=ParseMode.MARKDOWN)
    else:
        update.message.reply_text(
                         text='***Nhap domain ban muon check***\n'
                              'VD: /whois minhkma.com',
                         parse_mode=ParseMode.MARKDOWN)
