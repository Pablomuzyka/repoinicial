from bs4 import BeautifulSoup
import requests
import pandas as pd


url= 'https://mystake.bet/es/casino/gamepage?gameid=12489'
page= requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')

dato0=soup.find_all('span',class_='low')
dato1=soup.find_all('span',class_='medium')
dato2=soup.find_all('span',class_='high')

print(dato0)
