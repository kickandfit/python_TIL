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

# +
import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
from tqdm import tqdm
import matplotlib.font_manager as fm

def font():
    font_name = fm.FontProperties(fname = 'C:/Windows/Fonts/malgun.ttf').get_name()
    plt.rc('font', family = font_name)
    
def url_print(uRow = 5):
    idate = '2021'
    url_basic = 'http://openAPI.seoul.go.kr:8088/'
    uKey = '4f617954766d6f6f37354448475961'
    url_obj = '/xml/TbCorona19CountStatusJCG/1/'+str(uRow)+'/'


    url = url_basic + uKey + url_obj
    
    url_soup = url_parser(url)
    return url_soup

def url_parser(url):
    xml_url = requests.get(url)
    if xml_url.status_code == 200:
        pass
        #print('정상적으로 데이터를 받아왔습니다')
    else:
        print('데이터를 가져오지 못했습니다.')
    xml_soup = bs(xml_url.content , 'html.parser')
    #print(xml_soup)
    return xml_soup

#index 만들기
def df_columns():
    data = pd.read_csv('c:/pydata/서울특별시 코로나19 자치구별 확진자 발생동향.csv', encoding = 'cp949')
    df_index = list(data.columns)
    
    return df_index

#전체데이터 받아오기
def tot_data_save():
    df_index = df_columns()
    df1 = pd.DataFrame()
    uRow = url_print().find('list_total_count').text
    xml_soup = url_print(uRow)
    for num in tqdm(range(int(uRow)), desc = '진행률'):
        soup_data = xml_soup.select('row')[num].text
        pre_data_lst=[]
        data_lst= [] 
        text = ""
        
        #예외처리 '수집일'이 없는 경우 Nan으로 받아서 처리
        try:
            for i in soup_data:
                if i != '\n':
                    text += i
                else:
                    pre_data_lst.append(text)
                    text = ""
            for i in range(len(pre_data_lst)):
                if pre_data_lst[i] != "":
                    data_lst.append(pre_data_lst[i])
            # print(len(df_data_lst))
            df = pd.DataFrame( [data_lst], columns = df_index)
            df1 = pd.concat([df1,df], ignore_index = True)
        except:
            if len(data_lst) != 1: #마지막 데이터 20이 들어간 자리 처리
                df = pd.DataFrame( [data_lst], columns = df_index[:-1])
                df1 = pd.concat([df1,df], ignore_index = True)
    df1.to_csv('c:/pydata/seoul_covid19_info.csv', index = False, encoding = 'cp949')

#최신 자료 업데이트
def update_data():
    df = pd.read_csv('c:/pydata/seoul_covid19_info.csv', encoding = "cp949")
    url= url_print()
    #print(url)
    today_date = url.find('jcg_dt').text
    #print(today_date)
    df_index = df_columns()
    if df.loc[0][0] == today_date:

        print('최신 데이터 자료입니다')

    else:

        soup_data = url.select('row')[0].text
        pre_data_lst=[]
        data_lst= [] 
        text = ""
        df1 = pd.DataFrame()
        for i in soup_data:
            if i != '\n':
                text += i
            else:
                pre_data_lst.append(text)
                text = ""
        for i in range(len(pre_data_lst)):
            if pre_data_lst[i] != "":
                data_lst.append(pre_data_lst[i])
        # print(len(df_data_lst))
        df1 = pd.DataFrame( [data_lst], columns = df_index)
        df = pd.concat([df1,df], ignore_index = True)
        df.to_csv('c:/pydata/seoul_covid19_info.csv', index = False, encoding = 'cp949')

#프로그램 스타트
def start():
    num = int(input('데이터 자료를 가지고 있습니까? 데이터가 없다면 "1"을 기존 데이터를 가지고 있다면 "2"를 눌러주세요.'))
    data = pd.DataFrame()
    if num == 1:
        tot_data_save()
    elif num == 2: 
        data = update_data()
    else:
        print('숫자를 잘못 입력하셨습니다')
        exit()

# 기준일 날짜 처리(년월일 처리) + 일별 정리(지역구별 일별 추가 발생자)
#df['자치구 기준일'].loc[0].replace(".","")[:-2] : 문자열 처리후 날짜까지만
def daily_data(df):
    df_index = df_columns()
    new_index = []
    for i in range(len(df)):
        df['자치구 기준일'].loc[i] =  df['자치구 기준일'].loc[i].replace(".","")[:-2]
    #columns 이름 변경
    df1 = df.rename(columns = {'자치구 기준일' : '발생년월일'})
    for i in df_index:
        if i[-2:] == '추가' :
            new_index.append(i)
    new_index.insert(0,"발생년월일")

    df3 = df1[new_index] # 지역별 추가 발생자 데이터
    df3.sort_values(by = '발생년월일', ascending = True, inplace = True)
    df3.reset_index(inplace = True)
    return df3

#월별 데이터 처리(지역구별 추가 발생자)
def month_data(df):
    df_index = df_columns()
    new_index = []
    for i in range(1):
        for i in range(len(df)):
            df['자치구 기준일'].loc[i] =  df['자치구 기준일'].loc[i].replace(".","")[:-2]
    df2 = df.rename(columns = {'자치구 기준일' : '발생년월일'})
    for i in df_index:
        if i[-2:] == '추가' :
            new_index.append(i)
    new_index.insert(0,"발생년월일")
    df4 = df2[new_index]
    df4 = df4.rename(columns = {'발생년월일' : '발생년월'})
    df4 = df4.groupby('발생년월').sum()
    df4.sort_values(by = '발생년월', ascending = True, inplace = True)
    df4.reset_index(inplace = True)
    return df4


# +
start()
font()
df = pd.read_csv("c:/pydata/seoul_covid19_info.csv", encoding = 'cp949')
df.drop('수집일', axis =1, inplace = True )
df1 = daily_data(df)
df2 = month_data(df)

#자치구 조회
gu = input('조회할 구 입력:')
plt.style.use('ggplot')
df2.plot(kind = 'bar', x = '발생년월', y = gu+' 추가')
plt.xlabel('발생년월', size = 13)
plt.ylabel('추가 확진자수', size = 13)
plt.title('월별 조회 해당구 추가 확진자 현황')
plt.show()
# -
df1

df2













