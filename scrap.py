from bs4 import BeautifulSoup

import requests
import pandas as pd
from pprint import pprint

#
# class BeautifulSoup_:
#     def __init__(self, link,search):
#         self.link = link
#         self.search = search
#         self.result = pd.DataFrame()
#     def get_soup(self):
#         resp = requests.get(self.link)
#         soup = BeautifulSoup(resp.text, 'html.parser')
#         # return soup
#
#
#         posts = soup.find_all('div', class_='posts__item')
#         # print(posts)
#         for post in posts:
#             title = post.find('h2', class_='posts__title').text
#             print(title)
#             date = post.find('div', class_='posts__date').text
#             print(date)
#             link = post.find('a').get('href')
#             print(link)
#     def netology_search(self):
#         url = self.link
#         params = {'s': self.search}
#         res = pd.DataFrame()
#         resp = requests.get(url, params)
#         soup = BeautifulSoup(resp.text, 'html.parser')
#         # print(soup)
#         posts = soup.find_all('article', class_='status-publish')
#         print('POST',posts)
#         for post in posts:
#             title = post.find('h2', class_='entry-title').text
#             print(title)
#             date = post.find('span', class_='posted-on').text
#             print(date)
#             link = post.find('a').get('href')
#             print(link)
#             self.result = self.result._append({'title': title, 'date': date, 'link': link}, ignore_index=True)
#         print(self.result)
#         self.result.to_csv('netology.csv', index=False)
#
#
#     def under_link(self,link):
#         link = f'{self.link2}/{link.strip("/")}/'
#         # print(self.list[0]['link'])
#         print(link)
#         resp = requests.get(link)
#         soup = BeautifulSoup(resp.text, 'html.parser')
#         #print(soup)
#         d = soup.find_all('div',class_='content')
#         # print(d)
#         n = 0
#         for i in d:
#             if n == 1:
#                 #print(i)
#                 cont = i.find_all('p')
#                 #print('content',cont)
#                 for c in cont:
#                     print(c.text)
#             n += 1
#
#             print('-------------------')
#         # print(cont)
#         # for c in cont:
#         #     print(c)
#         #     print('-------------------')
#
#
#     def create_link_list(self):
#         print(self.list)
#         for item in self.list:
#             print(item['link'])
#             self.under_link(item['link'])
#     def coscmos_search(self,link_):
#         self.link2 = link_
#         resp = requests.get(link_)
#         soup = BeautifulSoup(resp.text, 'html.parser')
#         # print(soup)
#         row = soup.find_all('a', class_='news watermark-hover')
#         # print('_______________')
#         # print(row[0].text)
#         # print(len(row))
#         self.list = []
#         for item in row:
#             dict = {}
#             #print(item.get('href'))
#             dict['link'] = item.get('href')
#             #print(item.text)
#             #print(item.find('h3').text)
#             dict['title'] = item.find('h3').text
#             #print(item.find('img').get('src'))
#             dict['img'] = item.find('img').get('src')
#             self.list.append(dict)
#         #pprint(self.list)
#         self.create_link_list()




# s = BeautifulSoup_('http://netology.ru/blog','python')
# # s.get_soup()
# print('=======================================================================')
# l = 'https://cosmos.vdnh.ru'
# # s.netology_search()
# s.coscmos_search(l)
# https://www.astronews.ru/

class Astronews:
    def __init__(self, link):
        self.link = link

    def get_soup_obj(self):
        resp = requests.get(self.link)
        soup = BeautifulSoup(resp.text, features='lxml')
        return soup

    def get_info(self):
        obj = self.get_soup_obj()
        # print(obj)
        news = obj.find_all('div', class_='col')
        for n in news:

            print(n)
            print('-------------------')

a = Astronews('https://www.astronews.ru/')
print(a.get_info())