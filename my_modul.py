from bs4 import BeautifulSoup
import requests


def get_news():
    url = 'https://lenta.ru/'
    r = requests.get(url, )
    soup = BeautifulSoup(r.text, 'html.parser')
    div = soup.find('main', class_='layout__content js-site-container').find_all('a', class_='card-mini _topnews')
    d = soup.find('main', class_='layout__content js-site-container').find_all('a', class_='card-big _longgrid')
    e = soup.find('main', class_='layout__content js-site-container').find_all('a', class_='card-mini _longgrid')
    data = []
    for t in div:
        news = t.text
        news_href = 'https://lenta.ru/' + t['href']
        data.append(news)
        data.append(news_href)
    for j in e:
        news = j.text
        news_href = 'https://lenta.ru/' + j['href']
        data.append(news)
        data.append(news_href)

    for i in d:
        news = i.text
        news_href = 'https://lenta.ru/' + i['href']
        data.append(news)
        data.append(news_href)
    for o in range(1, 21):
        url = f'https://lenta.ru/parts/news/{o}/'
        r = requests.get(url=url)
        soup = BeautifulSoup(r.text, 'lxml')
        main = soup.find('main', class_='layout__content js-site-container').find_all('a',class_='card-full-news _parts-news')
        for z in main:
            news = z.text
            news_href = 'https://lenta.ru/' + z['href']
            data.append(news)
            data.append(news_href)
    return data

