import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from urllib.request import urlopen

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요: ')
url = baseUrl + quote_plus(plusUrl)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

img = soup.find_all(class_ = '_img')

# 꼭 출력을 해보자. 자바스크립트 다 거쳐서 나오는 게 크롬 개발자 상의 명이기 때문에, 실제 class명과 다를 수 있기 때문!
print(img[0])

n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)

print('다운로드 완료')