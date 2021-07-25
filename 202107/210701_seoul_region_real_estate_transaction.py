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
print(type())
# import pandas as pd

# df=pd.DataFrame(avg_lst)
# df


# d_name1 = [lst[1] for lst in d_lst if lst[1] not in d_name1 ]
# #print(d_name1)

# d_name2 = [lst[1] for lst in d_lst if lst[1] in d_name2 ]
# #print(d_name1)

# if d_name1 == d_name2:
#     print('1')

# -

# ### 동별 평균 계산값을 그래프를 이용해 비교 분석
#
# - pandas 모듈을 이용한 데이터 관리
# - 꺽은선 그래프
# - 막대 그래프
# - bocplot 그래프

# +
df1 = df[df['평균판매가']!= 0]
df1.sort_values(by = ['평균판매가'], ascending = False) 

# .sort_values(by = ['평균판매가'])데이터 프레임 구조에서만 사용이 가능
# 기본은 오름차순 
# .sort_values(by = ['평균판매가'], ascending = False) 내림차순
# True = 1, False = 0 을 의미한다
# -

# 정렬한 결과 값을
df1 = df1.sort_values(by = ['거래건수'], ascending = False)# 와 같은 내용
#df1.sort_values(by = ['평균판매가'], ascending = False, inplace = True)
df1

# +
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name) 

df1['평균판매가'].plot()
plt.show()
# -

#index 가 기준값으로 들어가기 때문에 index로 정렬해줘야함
df1=df1.sort_index()
df1['평균판매가'].plot()
plt.show()

plt.figure(figsize=(15, 4))
plt.xticks(size = 10, rotation = 45 )
plt.plot(df1['동이름'], df1['거래건수'])
plt.show()

# ### 막대그래프 그리기

# +
plt.style.use('ggplot') # 그래프 예쁘게 표현하기

plt.figure(figsize=(15, 4))
plt.xticks(size = 10, rotation = 45 )
plt.bar(df1['동이름'], df1['평균판매가'])#막대 그래프 표현


plt.title(g_name + ' 동별 아파트 평균 판매가 분석', size = 23)

plt.show()
# -

print(plt.style.available) # 사용할 수 있는 스타일

# ### boxplot 그래프
#
# - 연속형 변수에서 최소값/최대값/ 제 1사분위수(Q1), 중앙값, 제 3사분위수(Q3)과 같은 통계량을 계산하기 위해 사용
# - 제 1사분위수(Q1)

plt.boxplot(df1['평균판매가'])
plt.show()


