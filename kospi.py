#네이버 증시 페이지에 대신 접속해서,
# 현재 코스피 지수를 가져오는 프로그램
#pip는 python이 제공하는 모듈시스템

import requests
import bs4
#이 주소로 요청을 보내면 응답으로 HTML 파일이 도착할 것
html = requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')


#텍스트뿐인 html 파일을 내가 보기 좋게 접근할 수 있도록 변경. bs4의 BeutifulSoup이 도와줌
soup = bs4.BeautifulSoup(html.text, 'html.parser')
#css selector로 내가 원하는 태그를 가져 오겠다
kospi = soup.select_one('#now_value')

print(kospi.text)

##now_value#now_value