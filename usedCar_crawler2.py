import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen
import re
import json
from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/max53/OneDrive/Documents/chromedriver')
driver.implicitly_wait(20)

driver.get('http://www.gparts.co.kr/display/showSearchDisplayList.do')

search_keyword = driver.find_element_by_id("searchKeyword1")
search_keyword.send_keys('머플러')

search_btn = driver.find_element_by_class_name("btnTopSrch")
search_btn.click()

driver.implicitly_wait(20)


# title = driver.find_element_by_class_name("tit")
# print(title.text)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all('div', {'class':'tit'})
title = title[:30]
price = soup.find_all('div', {'class':'price'})
price = price[:30]
tmp_list = []
searchList = []


# page 1 스크래핑
for i in range(len(title)):
        tmp_title = title[i].text.split(' ')
        tmp_price = price[i].text
        # tmp_title[1] = 회사명, tmp_title[3:-1] = 차종, tmp_title[-1] = 연식
        tmp_list.append(i+1)
        tmp_list.append(tmp_title[1])
        tmp_list.append(' '.join(tmp_title[3:-1]))
        tmp_list.append(tmp_title[-1][1:-3])
        tmp_list.append(tmp_price[1:-2])
        searchList.append(tmp_list)
        tmp_list = []

# page 2~ 스크래핑
for j in range(1,69):
#     driver.execute_script("fnPaginate({j});")
        next_btn = driver.find_element_by_css_selector('span.right > a')
        next_btn.click()
        driver.implicitly_wait(40)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find_all('div', {'class':'tit'})
        title = title[:30]
        price = soup.find_all('div', {'class':'price'})
        price = price[:30]

        for i in range(len(title)):
                tmp_title = title[i].text.split(' ')
                tmp_price = price[i].text
                # tmp_title[1] = 회사명, tmp_title[3:-1] = 차종, tmp_title[-1] = 연식
                tmp_list.append(j*30 + i+1)
                tmp_list.append(tmp_title[1])
                tmp_list.append(' '.join(tmp_title[3:-1]))
                tmp_list.append(tmp_title[-1][1:-3])
                tmp_list.append(tmp_price[1:-2])
                searchList.append(tmp_list)
                tmp_list = []
        driver.implicitly_wait(40)
        
print(searchList)
print(len(searchList))


f = open(f'muffler_price_from_site2.csv', 'w', encoding='ANSI', newline='')
csvWriter = csv.writer(f)

csvWriter.writerow(['단가id','회사','차량명','연식','판매가격'])
for postObject in searchList:
    csvWriter.writerow(postObject)

f.close()

print('complete')
