import requests
from bs4 import BeautifulSoup


def getData(url):
    datas = requests.get(url)
    soup = BeautifulSoup(datas.text, "lxml")
    data = soup.find(class_="posts")
    data1 = data.find_all(class_="post-preview")
    return data1


def getId(datas):
    lists = []
    for data in datas:
        id = data.get('id')
        links = data.find('a').get('href').strip()
        a = (id, links)
        lists.append(a)
    return lists


