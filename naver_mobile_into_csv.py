import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import csv

baseUrl = 'https://m.search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요: ')
url = baseUrl + quote_plus(plusUrl)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

total = soup.select('.api_txt_lines.total_tit')

print(total[0])
searchList = []

for i in total:
    # print(i.text)
    # if 'href' in i.attrs:
    #     print(i.attrs['href'])
    # print()
    temp = []
    temp.append(i.text)
    if 'href' in i.attrs:
        temp.append(i.attrs['href'])
    else:
        temp.append('no link')
    searchList.append(temp)

f = open(f'{plusUrl}.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)

for i in searchList:
    csvWriter.writerow(i)

f.close()

print('complete')