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
# 사용자로부터 구명, 동명 입력받아 데이터 조회
# 출력값 : '자치구명', '법정동명', '건물주용도', '건축년도', 
#              3            5          15            17     
#'건물면적' ,'층정보', '물건금액', '건물명'
#    11         13        16         18

import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


g_name = input('조회 구 이름 입력하세요.')
d_name = input('조회 동 이름 입력하세요.')
f = open('./Data/서울특별시_부동산_실거래가_정보_2020년.csv', encoding = 'cp949')
raw_data = csv.reader(f)
header = next(raw_data)

print(header)
data_lst=[]

for row in raw_data:   
    
    if g_name in row[3] and d_name in row [5]:
        
        
            #print([row[3],row[5],row[15],row[17],row[11],row[13],row[16],row[18]])
            data_lst.append([row[3],row[5],row[15],row[17],row[11],row[13],row[16],row[18]])
            
f.close()

#print(data_lst)
#print(type(data_lst))

# -

# ### 미션 : 구별 동단위 건물주용별 평균 시세
#
# - 1. 구단위 데이터 조회
# - 2. 조회구의 동별 아파트 평균 가격 계산
#

# +
import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


g_name = input('조회 구 이름 입력하세요.')

f = open('./Data/서울특별시_부동산_실거래가_정보_2020년.csv', encoding = 'cp949')
raw_data = csv.reader(f)
header = next(raw_data)

#print(header)

d_lst = []

for row in raw_data:   
    
    if g_name in row[3] :
            d_lst.append([row[3],row[5],row[15],row[17],row[11],row[13],row[16],row[18]])

d_name = []


for lst in d_lst:
    if lst[1] not in d_name:
        d_name.append(lst[1])
#print(d_name)

# 동별 평균값 계산
d_avg = 0
avg_lst = []

for dong in d_name:
    tot = 0
    cnt = 0
    for lst in d_lst:
        if dong == lst[1] and "아파트" == lst[2]:
            tot += int(lst[-2])
            cnt += 1
    
    if cnt == 0:
        avg_lst.append({"동이름":dong, "평균판매가":0, "거래건수":cnt})
    
    else:
        d_avg = tot/cnt
        avg_lst.append({"동이름":dong, "평균판매가":int(d_avg), "거래건수":cnt})

        
#print(avg_lst)
f.close()

import pandas as pd

df=pd.DataFrame(avg_lst)
df


# d_name1 = [lst[1] for lst in d_lst if lst[1] not in d_name1 ]
# #print(d_name1)

# d_name2 = [lst[1] for lst in d_lst if lst[1] in d_name2 ]
# #print(d_name1)

# if d_name1 == d_name2:
#     print('1')

# -




