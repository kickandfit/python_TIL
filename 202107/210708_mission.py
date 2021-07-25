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

from tqdm import tqdm
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import requests
from bs4 import BeautifulSoup as bs
from datetime import timedelta

# +
#http://openapi.seoul.go.kr:8088/(인증키)/xml/CardSubwayPayFree/1/5/201501/
uRow  = 5
tdate = 201501
def url_parser(tdate, uRow = 5):
    uKey = "4f617954766d6f6f37354448475961"
    url_gibon = 'http://openapi.seoul.go.kr:8088/' + uKey
    url_obj = "/xml/CardSubwayPayFree/"
    url_row = "1/"+ str(uRow) + "/"
    url_date = str(tdate)+"/"

    url = url_gibon + url_obj + url_row + url_date
    url_soup = url_parser(url)
    return url_soup

def url_parser(url):
    url_xml = requests.get(url)

    if url_xml.status_code != 200:
        print('데이터를 가져오지 못했습니다')
        exit()

    soup = bs(url_xml.content, 'html.parser')
   
    return soup
def seoul_sw_pandas(seoul_sw_soup):
    xml_row = seoul_sw_soup.find_all('row')
    xml_txt = []
    for row in xml_row:
        dt = row.find('use_mon').text               # 사용일자
        line = row.find('line_num').text           # 호선(라인)
        sub_sta = row.find('sub_sta_nm').text      # 역이름
        pay_ride = row.find('pay_ride_num').text     # 승차총인원
        free_ride = row.find('free_ride_num').text # 하차총인원
        pay_alight = row.find('pay_alight_num').text
        free_alight = row.find('free_alight_num').text
        
        xml_txt.append({'사용원': dt, '호선명': line, '지하철역': sub_sta, '유임승차인원': pay_ride, 
                        '무임승차하차': free_ride,'유임승차총인원' : pay_alight,'무임승차총인원' : free_alight})

    #print(xml_txt)
    df = pd.DataFrame(xml_txt)
    return df

def date_range(sDt, eDt):
    tdate = []
    for i in range(int(sDt),int(sDt)+1+((int(eDt[:4])-int(sDt[:4]))*12+int(eDt[4:]))-int(sDt[4:])):

        for j in range(4):
            if j*12 <(i-int(sDt[:4])*100)<12*(j+1)+1:
                if j == 0 :
                    tdate.append(i)
                    continue
                else : 
                    tdate.append(str((int(sDt[:4])+(j))*100+(i-12*j)-100*(int(sDt[:4])))) 
    return tdate

def main_api(sDt, eDt):
    df0 = pd.DataFrame()
    dt_range = date_range(sDt,eDt)
    # 데이터 없는 월 처리하기
    for tdate in dt_range:
        if seoul_sw_soup.find('code').text=="INFO==200":
            continue
        
        url=url_parser(tdate)    # 한페이지에 5개의 데이터가 출력된 url 정보 가져오기
        uRow=url.find('list_total_count').text   # 조회된 전체 데이터 개수 추출하기
        seoul_sw_soup=url_parser(tdate, uRow)    # 한페이지에 추출한 전체 데이터 출력 url 정보 가져오기
        df=seoul_sw_pandas(seoul_sw_soup)   # 요청 데이터에 대한 DataFrame 형식으로 변경하기
        
        df0 = pd.concat([df0,df], ignore_index = True)
    print(df0)
    return df0

# +



# -

if __name__ == "__main__":
    
    sDt = input('조회 시작일 입력 (예 : 202101) : ')
    eDt = input('조회 종료일 입력 (예 : 202105) : ')

    
    df0 = main_api(sDt, eDt)
    print('==============작업종료=================')


# +
# for i in range(int(sDt),int(sDt)+1+((int(eDt[:4])-int(sDt[:4]))*12+int(eDt[4:]))-int(sDt[4:])):
    
#     if (i-int(sDt[:4])*100)<13:
#         print(i)
#     elif 13<=(i-int(sDt[:4])*100)<25:
#         print((int(sDt[:4])+1)*100+(i-12)-100*(int(sDt[:4])))
# -

def url_print(tdate, uRow = 5):
    uKey = "4f617954766d6f6f37354448475961"
    url_gibon = 'http://openapi.seoul.go.kr:8088/' + uKey
    url_obj = "/xml/CardSubwayPayFree/"
    url_row = "1/"+ str(uRow) + "/"
    url_date = str(tdate)+"/"

    url = url_gibon + url_obj + url_row + url_date
    url_soup = url_parser(url)
    return url_soup
print(url_print(202105))



# +
# def date_range(sDt, eDt):
#     tdate = []
#     for i in range(int(sDt),int(sDt)+1+((int(eDt[:4])-int(sDt[:4]))*12+int(eDt[4:]))-int(sDt[4:])):

#         for j in range(4):
#             if j*12 <(i-int(sDt[:4])*100)<12*(j+1)+1:
#                 if j == 0 :
#                     tdate.append(i)
#                     continue
#                 else : 
#                     tdate.append(str((int(sDt[:4])+(j))*100+(i-12*j)-100*(int(sDt[:4])))) 
#     return tdate
# date_range("202005","202107")
# -


