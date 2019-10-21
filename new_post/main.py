import requests
import time
import configparser
import mysql
import beauti
import beauti_do

from send_message import send
from bs4 import BeautifulSoup

def get_config(file):
    config = configparser.ConfigParser()
    config.read(file)
    return config

def m_new(myConnection, sql):
    config = get_config("setting")
    url_new = config['sites']['url']
    data_new = beauti.getData(url_new)
    list_id_new = beauti.getId(data_new)
    values_new = sql.query(myConnection, 'new')
    for ids in list_id_new:
        if ids[0] not in values_new:
            sql.insert(myConnection, 'new', ids[0])
            send(config["telegram"]["token"], config["telegram"]["chat_id"], ids[1])

def m_do(myConnection, sql):
    config = get_config("setting")
    url_do = config['sites']['url_do']
    data_do = beauti_do.getData(url_do)
    list_id_do = beauti_do.getId(data_do)
    values_do = sql.query(myConnection, 'do')
    for ids in list_id_do:
        if ids[0] not in values_do:
            sql.insert(myConnection, 'do', ids[0])
            send(config["telegram"]["token"], config["telegram"]["chat_id"], ids[1])

def main():
    config = get_config("setting")
    sql = mysql.mysql(config["mysql"]["hostname"], config["mysql"]["username"],
                      config["mysql"]["password"], config["mysql"]["database"])
    myConnection = sql.connection()
    m_new(myConnection, sql)
    m_do(myConnection, sql)
    sql.close(myConnection)


main()