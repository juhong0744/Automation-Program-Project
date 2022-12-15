# 네이버 검색 API 예제 - 블로그 검색

import requests
from urllib.parse import urlparse

keyword = "서현역"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=100"# JSON 결과
result = requests.get(urlparse(url).geturl(),headers={"X-Naver-Client-Id":"stFxwfIj36BGAyE2W5cv",
        "X-Naver-Client-Secret":"yg8A9uKbgI"})
#print(result.json())
json = result.json()
json['display'] = 100
#print(json['lastBuildDate'])
#print(json['total'])
#print(json['start'])
#print(json['display'])
#print(json['items'])

i=1
for item in json['items']:
    print(str(i)+") " + item['title'].replace("<b>","").replace("</b>",""),item['link'])
    i +=1