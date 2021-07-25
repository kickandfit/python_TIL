# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ### 벅스뮤직 실시간 차트 데이터 가져오기
# - 웹 크롤링 기본적인 방법으로 데이터 연결(requests)

import requests
from bs4 import BeautifulSoup as bs
import sys
import pandas as pd

# +
url = 'https://music.bugs.co.kr/chart/track/realtime/total' #realtime

bugs_html = requests.get(url)

if bugs_html.status_code != 200:
    sys.exit('웹 페이지 정보를 가져올 수 없습니다.')
    
bugs_soup = bs(bugs_html.content, "html.parser")
bugs_soup =bugs_soup.find('tbody')
#print(bugs_soup)
tr_soup = bugs_soup.find_all('tr') #리스트형 구조로 'tr' 태크 전체 찾아옴


bugs_list=[]
# 순위, 곡명, 아티스트, 앨범
for tr in tr_soup:
    
    rank = tr.find('strong').text # 순위 값 추출
    title = tr.find('p', class_='title').text.replace("\n","")
    artist = tr.find('p', class_='artist').text.replace("\n","")
    album = tr.find('a', class_='album').text.replace("\n","")
    
    bugs_list.append({"순위" : rank, "곡명" : title, '아티스트' : artist, '앨범' : album})
    
df1=pd.DataFrame(bugs_list, columns = ['순위','앨범','곡명','아티스트'])
df1
# -

# ###  멜론 차트 정보 가져오기
#
# - selenium 모듈 사용
# - selenuium 모듈은 chromedriver.exe를 이용해 크롬 브라우저 직접 컨트롤
#

# +
# #!pip install selenium
# -

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import sys
import pandas as pd
import time

# +
driver = webdriver.Chrome('c:/pydata/chromedriver.exe')
time.sleep(2) # time.sleep() :대기시간(초) 무조건 기다림(실행전)

url = 'https://www.melon.com/chart/index.htm' # chart1, /day, / week,/ month
driver.get(url) # 실행된 chromedriver 주소창에 url 입력 후 이동
driver.implicitly_wait(10) # 사이트 화면이 나타날때까지 기다림(최대 10초)
# 만약 10초가기다리면 error 발생

melon_html = driver.page_source # chromedriver 화면 전체 소스 코드 가져오기


    

# +
#driver.get('https://www.naver.com') #네이버로 이동하고 싶은데

# +
melon_soup = bs(melon_html ,  "html.parser")
melon_soup =melon_soup.find('tbody')
#print(bugs_soup)
tr_soup = melon_soup.find_all('tr') #리스트형 구조로 'tr' 태크 전체 찾아옴

melon_lst = []
cnt = 0       # 순위 표기
for tr in tr_soup:
    cnt += 1
    rank = cnt
    title = tr.find('div', class_='ellipsis rank01').get_text().replace('\n',"")
    artist = tr.find('span', class_='checkEllipsis').get_text().replace('\n',"")
    album = tr.find('div', class_='ellipsis rank03').get_text().replace('\n',"")
    starcnt = int(tr.find('span', class_='cnt').get_text().replace('\n총건수\n',"").replace(',',""))
    
    melon_lst.append([ rank, title, artist, album, starcnt])

df2 = pd.DataFrame(melon_lst, columns = ['순위', '곡명', '아티스트', '앨범', '좋아요'])
df2
# -

tr.find('div',class_='ellipsis rank01').get_text().replace('\n','')




