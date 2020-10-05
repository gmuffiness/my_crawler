import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

# Basic Settings
baseUrl = 'https://www.google.com/search?q='
plusUrl = input('검색어를 입력하세요: ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome('/Users/max53/Downloads/chromedriver')
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, features='html.parser')

# Start Crawling

r = soup.select('.r')
print(type(r)) # list

for i in r:
    # print(i.select_one('.ellip').text) # select는 리스트라 오류남.
    # print(i.select_one('.iUh30.bc').text)
    # print(i.a.attr['href'])
    print(i)

driver.close()