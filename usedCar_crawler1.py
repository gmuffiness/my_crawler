import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen
import re
searchUrl = 'http://www.insunmotors.com/goods/list.do?part2=050901003011&menu=menu3&rows=10&cpage='

searchList = []

# i 는 페이지 넘버
for i in range(43):
    try:
        # detailUrl 들어가서 텍스트 같은 종류끼리 분류 / 이미지 여러장 저장.
        detailUrl = searchUrl + str(i+1)

        html = urllib.request.urlopen(detailUrl).read()
        soup = BeautifulSoup(html, 'html.parser')

        # title = soup.find('p', id='price')
        infoCard = soup.select('td > a > span')
        price = soup.select('td > p')
        temp = []
        count = 0
        print(len(infoCard))
        for j in range(len(infoCard)):
            print(j)
            text = infoCard[j].text.replace('\t','').replace('\n','').replace('\r','')
            priceValue = price[count].text
            print(text)
            print(priceValue)
            if j % 4 == 0:
                if j == 0:
                    continue
                temp.insert(0, str(j//4 + 10 * i))
                temp.append(priceValue.strip()[:-1])
                searchList.append(temp)
                count += 1
                temp = []
                continue
            elif (j+3) % 4 == 0:
                for k, char in enumerate(text):
                    if char == ":":
                        cname_and_year = text[k+1:].strip()
                        for m, char2 in enumerate(cname_and_year):
                            if char2 == "(":
                                cname = cname_and_year[:m].strip()
                                year = cname_and_year[m+1:-3].strip()
                                temp.append(cname)
                                temp.append(year)
            else:
                for k, char in enumerate(text):
                    if char == ":":
                        temp.append(text[k+1:].strip())
            if (j+1) % 40 == 0:
                temp.insert(0, str((j+1)//4 + 10 * i))
                temp.append(priceValue.strip()[:-1])
                searchList.append(temp)
                count += 1
                temp = []
    
        # searchList.append(temp)
    except Exception as e:
        print('예외 발생', e)

print(searchList)

f = open(f'muffler_price_from_site1.csv', 'w', encoding='ANSI', newline='')
csvWriter = csv.writer(f)
csvWriter.writerow(['단가id','차량명','연식','부품명','부품등급','판매가격'])
for postObject in searchList:
    csvWriter.writerow(postObject)
f.close()

print('complete')
