#input 태그정보 받아오기
import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.naver.com/')
soup = BeautifulSoup(url.content, 'html.parser')

soup.find('input')



input = soup.select('input')[0]
print(input)
#print(input.get_text())