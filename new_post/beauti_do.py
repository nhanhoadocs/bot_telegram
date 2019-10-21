import requests
from bs4 import BeautifulSoup


def getData(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "lxml")
    datas = soup.find_all(class_="tutorial")
    return datas


def getId(datas):
    lists = []
    for data in datas:
        id = data.get('data-id')
        link = data.find('a').get('href').strip()
        links = "https://www.digitalocean.com" + link
        a = (id, links)
        lists.append(a)
    return lists

