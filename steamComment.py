# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import json

headers = {    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'}
file = open('onlycomment.txt', 'w+', encoding='utf-8')
for i in range(1, 100):
    url = 'http://steamcommunity.com/app/1102130/homecontent/?userreviewsoffset=' + str(10 * (i - 1)) + '&p=' + str(
        i) + '&workshopitemspage=' + str(i) + '&readytouseitemspage=' + str(i) + '&mtxitemspage=' + str(
        i) + '&itemspage=' + str(i) + '&screenshotspage=' + str(i) + '&videospage=' + str(i) + '&artpage=' + str(
        i) + '&allguidepage=' + str(i) + '&webguidepage=' + str(i) + '&integratedguidepage=' + str(
        i) + '&discussionspage=' + str(
        i) + '&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid=1102130&appHubSubSection=10&l=schinese&filterLanguage=default&searchText=&forceanon=1'
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')  
    reviews = soup.find_all('div', {'class': 'apphub_Card'})    
    for review in reviews:
        nick = review.find('div', {'class': 'apphub_CardContentAuthorName'})
        title = review.find('div', {'class': 'title'}).text
        hour = review.find('div', {'class': 'hours'}).text.split(' ')[0]
        link = nick.find('a').attrs['href']
        comment = review.find('div', {'class': 'apphub_CardTextContent'}).text.split('\n')[2].strip('\t')

        file.write(
            comment + '\n')
file.close()