import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='
plusUrl = input('검색어를 입력하세요: ')
url = baseUrl + quote_plus(plusUrl)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_ = 'sh_blog_title')

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()