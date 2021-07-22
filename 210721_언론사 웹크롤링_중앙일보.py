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

# ### request Vs urlib.request
#
# - 데이터를 보낼때 requests는 딕셔너리 형태, urlib는 인코딩하여 바이너리 형태로 전송
# - requests는 요청 메소드 (get,post)를 명시하지만 urlib는 데이터 여부에 따라 get과 post요청을 구분
# - 없는 페이지 요청시 requests는 에러는 띄우지 않지만 urllib는 에러를 띄움

import requests
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
import re   # 데이터에 대한 정규형 표현
import pandas as pd


# +
def news_parser(keyword,spage = 1, epage = 2):
    
    
    news_list=[]
    for page in range(int(spage), int(epage)+1):
        url = 'https://news.joins.com/Search/JoongangNews?page='+str(page)
        url = url +"&Keyword="+quote(keyword) #바이너리 코드 변경
        url = url + '&SortType=New&SearchCategoryType=JoongangNews'
    
        news_html = requests.get(url)
        if news_html.status_code != 200:
            print('url을 받아오지 못했습니다')
        news_soup = bs(news_html.text, 'html.parser')
    
    #방법 1 : select는 find_all과 같음
        li_text_tag = news_soup.select('div.bd>ul.list_default>li')
    
    #방법 2
#     ul_text_tag = news_soup.find('ul', class_="list_default")
#     li_text_tag = ul_text_tag.find_all('li')
    #print(li_text_tag)
    
        for li in li_text_tag:
            title = li.find('h2').get_text()
            new_url = li.find('a')['href']
            body= body_text(new_url)
            day = li.select('span.byline>em')[-1].get_text()

            news_list.append([title, day, body])

    df1 = pd.DataFrame(news_list, columns = ['제목', '날짜', '상세내용'])
    return df1



# -

def body_text(url):
    html = urlopen(url)
    soup = bs(html,'html.parser')
    
    try: 
        body = soup.find('div', id='article_body').text
    except:
        body=""
        
    #숫자/영문/한글 모두 ""로 변환
    body = re.sub("[^0-9ㄱ-ㅣ가-힣a-zA-z]","",body)
    return body



# +
keyword = input('조회 키워드 입력:')
spage = input('시작 페이지 번호:')
epage = input('종료 페이지 번호:')

df1 = news_parser(keyword, spage, epage)
# -

df1



for df_url in df1['상세_url']:
                  
    html = urlopen(df_url)
    soup = bs(html, 'html.parser')

    title = soup.find('h1', class_='headline mg').text
    #print(title,"\n\n")
    body = soup.find('div', id='article_body').text
    #print(body)

# +
title_list=[]
body_list=[]

for df_url in df1['상세_url']:
                  
    html = urlopen(df_url)
    soup = bs(html, 'html.parser')

    title = soup.find('h1', class_='headline mg').text
    #print(title,"\n\n")
    try: 
        body = soup.find('div', id='article_body').text
    except:
        body=""
        
    #숫자/영문/한글 모두 ""로 변환
    #title_list.append(re.sub("[0-9ㄱ-ㅣ가-힣a-zA-z]","",title))
    title_list.append(re.sub("[^0-9ㄱ-ㅣ가-힣a-zA-z]","",title))
    #print(body)
# -

txt = '''
안녕하세요~~
반갑습니다ㅋㅋㅋㅋ
body, html, H1, 1234'''

print(re.sub('[a-zㄱ-ㅣ]',"",txt)) #제거
print(re.sub('[^a-z가-힣]',"",txt)) #남김


