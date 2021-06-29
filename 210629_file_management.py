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

# ### CSV 형식의 파일 읽어오기
#
# - csv 모듈 이용, open("파일경로 및 파일명", 오픈형식, encoding=)
# - 오픈형식 : r = 읽기전용, w = 파일생성 및 쓰기, a = 기존파일에 데이터 추가
# - encoding -> cp949: 마이크로소프트에서 한글처리 방법(아스키코드), utf-8: 범용 보통 (유니코드)
# - pandas 모듈 이용

# +
import pandas as pd
import csv

f=open('./Data/seoul.csv','r', encoding='cp949') 

data = csv.reader(f, delimiter=",") # 안에 있는 데이터를 , 단위로 구분해서 가져와라

print(data)
f.close()

# 파일을 메모장으로 열고 우측 하단에 ANSI 면 아스키코드, UTF면 utf-8
# \t는 tqb키를 의미함

# +
f=open('./Data/seoul.csv','r', encoding='cp949') 
# 엑셀을 열었는데 한글이 보이면 cp949
# 엑셀을 열었는데 깨지는데 메모장으로 열면 보인다? UTF-8 or UTF-16
data = csv.reader(f, delimiter=",") # 안에 있는 데이터를 , 단위로 구분해서 가져와라

header=next(data) # next() : 첫행을 제목행으로 처리 다음줄부터 읽어라
print(header)
print()

for row in data:
    print(row)
    
f.close()

# +
f=open('./Data/seoul.csv','r', encoding='cp949') 

data = csv.reader(f, delimiter=",") 

header=next(data) 

temp_Max=["",0]
for row in data:
    if row[5] != "":
        if float(row[5]) > temp_Max[1]:
            temp_Max[0] = row[6]
            temp_Max[1] = float(row[5])

f.close()

print(temp_Max)
# -

# ### 미션: 최고 기온이 가장 높은 날짜와 최고기온 출력

# +
f=open('./Data/seoul.csv','r', encoding='cp949') 

data = csv.reader(f, delimiter=",") 

header=next(data) 

temp_Max=["",0]
temp_Min=["",100]# 0으로 초기화하면 0도보다 낮은 온도가 없으면 초기값이 결과값이 됨
temp_rage=["",0]

for row in data:
    if row[5] != "":
        if float(row[5]) > temp_Max[1]:
            temp_Max[0] = row[6]
            temp_Max[1] = float(row[5])
    if row[8] != "":
        if float(row[8]) < temp_Min[1]:

            temp_Min[0] = row[9]
            temp_Min[1] = float(row[8])


f.close()

print(temp_Max)
print(temp_Min)

# +
f=open('./Data/seoul.csv','r', encoding='cp949') 

data = csv.reader(f, delimiter=",") 

header=next(data) 

temp_Max=["",0]
temp_Min=["",100]# 0으로 초기화하면 0도보다 낮은 온도가 없으면 초기값이 결과값이 됨
temp_range=[]
temp_Mrange=["",0]
for row in data:
    
    if row[5] != "" and row[8] != "" :
        
        temp_range.append(float(row[5])-float(row[8]))
        
        if float(row[5]) > temp_Max[1]:
            temp_Max[0] = row[6]
            temp_Max[1] = float(row[5])
    
        if float(row[8]) < temp_Min[1]:

            temp_Min[0] = row[9]
            temp_Min[1] = float(row[8])

# 사실 아래 for 는 약간 비효율 적이나 효율적인 방법이 생각나지 않음
    for dt in temp_range:
        if dt > temp_Mrange[1]:
            temp_Mrange[1] = dt
            temp_Mrange[0] = row[9]

        
f.close()

# 최고 기온, 최저기온, 최대 기온차
print(temp_Max)
print(temp_Min)
print(temp_Mrange)
# -

import pandas as pd

df=pd.read_csv('./Data/seoul.csv',encoding="cp949")
df

df[df['최고기온(℃)']==df['최고기온(℃)'].max()] 
# 최고기온(℃) 키는 목록에 있는 키를 가져와야 한다 그리야 keyerror가 나지 않음

df['최고기온(℃)'].max()

df[df['최저기온(℃)']==df['최저기온(℃)'].min()]

df.info()

df.columns # 열이름 들만 추출해 내기

# ## 직장인들을 위한 책은 판다스
# ## 모두의 데이터 분석은 데이터 활용

df[['지점명', '일시', '평균기온(℃)','최고기온(℃)', '최저기온(℃)']]
# pandas는 편하지만, tensorflow 와 같은 곳에서 읽어내지 못함
# 때문에 추가 작업이 필요함
# 참고 페이지 pandas 검색해서 홈페이지에 들어가면 설명서 나와있음
# Pandas documentation pdf 다운로드 하면 알 수 있음

# #### [미션] 자신의 생일과 일치하는 날짜에 대한 날짜/평균기온/최고/최저 출력하는 데이터
#
# - 생일일치: 월, 일 두개가 일치하면 나머지 데이터 리스트 변수에 리스트형으로 추가

# +
import csv
f=open('./Data/seoul.csv','r', encoding='cp949') 

data = csv.reader(f, delimiter=",") # 안에 있는 데이터를 , 단위로 구분해서 가져와라
header=next(data) # next() : 첫행을 제목행으로 처리 다음줄부터 읽어라
print(header)
print()

my_birth = ["1993-05-01"]

result_data = []
for row in data:
    target_data=["", 0, 0, 0]
    if row[-1] != "":
        if int(row[-1][:4])>=1993 and row[-1][5:7]=="05" and row[-1][-2:]=="01" :
            target_data[0] = row[-1]
            target_data[1] = row[3]
            target_data[2] = row[-2]
            target_data[3] = row[5]
            
            result_data.append(target_data)

f.close()
print(result_data)

# +
import csv
f=open('./Data/seoul.csv','r', encoding='cp949') 

data = csv.reader(f, delimiter=",") # 안에 있는 데이터를 , 단위로 구분해서 가져와라
header=next(data) # next() : 첫행을 제목행으로 처리 다음줄부터 읽어라
print(header)
print()

my_birth = ["1993-05-01"]


for row in data:
    if row[-1] != "":
        if int(row[-1][:4])>=1993 and row[-1][5:7]=="05" and row[-1][-2:]=="01" :
            result_data.append([row[-1],row[3],row[-2],row[5]])

f.close()
print(result_data)
# -


