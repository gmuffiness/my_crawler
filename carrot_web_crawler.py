import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen
import re
baseUrl = 'https://www.daangn.com'
plusUrl = input('검색어를 입력하세요: ')
searchUrl = baseUrl + '/search/' + quote_plus(plusUrl)

html = urllib.request.urlopen(searchUrl).read()
soup = BeautifulSoup(html, 'html.parser')

# 전체 container
card = soup.find_all(class_='flea-market-article-link')

# [text, detail href] 순서로 리스트로 들어가게 될 예정.
searchList = []

for i in range(len(card)):
    try:
        # detailUrl 들어가서 텍스트 같은 종류끼리 분류 / 이미지 여러장 저장.
        detailUrl = baseUrl + card[i].attrs['href']

        html2 = urllib.request.urlopen(detailUrl).read()
        soup2 = BeautifulSoup(html2, 'html.parser')

        title = soup2.find('h1', id='article-title')
        category = soup2.find('p', id='article-category')
        price = soup2.find('p', id='article-price')
        description = soup2.find('div', id='article-detail')
        counts = soup2.find('p', id='article-counts')

        # test = re.sub(r"[\n]", "", counts.text) 
        # print(test)
        
        temp = []
        temp.append(str(i+1))
        temp.append(title.text)
        temp.append(re.sub(r"[ \n]", "", category.text))
        temp.append(re.sub(r"[ \n]", "", price.text))
        temp.append(description.text)
        temp.append(re.sub(r"[ \n]", "", counts.text))

        searchList.append(temp)
    except Exception as e:
        print('예외 발생', e)

print(searchList)

f = open(f'{plusUrl}.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)

csvWriter.writerow(['id','title','category','price','description','counts'])
for postObject in searchList:
    csvWriter.writerow(postObject)

f.close()

print('complete')



# img file save into carrot_img folder

# img = soup2.find_all(class_='landscape')
# print(img)

# n = 1
# for i in img:
#     imgUrl = i['data-lazy']
#     with urlopen(imgUrl) as f:
#         with open('./carrot_img/' + plusUrl + str(n) + '.jpg', 'wb') as h:
#             img = f.read()
#             h.write(img)
#     n += 1
#     print(imgUrl)

# print('다운로드 완료')