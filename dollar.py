import bs4
import requests

html = requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')

soup = bs4.BeautifulSoup(html.text, 'html.parser')
#css selector로 내가 원하는 태그를 가져 오겠다
dollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

#소스코드에 가서 카피 - 카피 셀렉터 #exchangeList > li.on > a.head.usd > div > span.value

print(dollar.text)
