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
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm
font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

df1=pd.read_csv('./data/서울시 인구현황_구.txt', sep='\t', header=1)
df1=df1.iloc[:, [0,1,6,7,9,10]]
df1.drop(0, inplace=True)

### 컬럼 이름 변경하기
col_name=['년도', '자치구', '내국인(남)', '내국인(여)','외국인(남)','외국인(여)']
for i in range(len(col_name)):
    df1.rename(columns={df1.columns[i]:col_name[i]}, inplace=True)

### 데이터 중 "…" 값 제거하기 / 1991년 데이터 삭제
df1=df1[df1['내국인(남)']!="…"]

### 콤마(,) 제거하기
df1['내국인(남)']=df1['내국인(남)'].str.replace(",","")
df1['내국인(여)']=df1['내국인(여)'].str.replace(",","")
df1['외국인(남)']=df1['외국인(남)'].str.replace(",","")
df1['외국인(여)']=df1['외국인(여)'].str.replace(",","")

### 숫자형 데이터 변경하기
df1=df1.astype({'내국인(남)':'int64','내국인(여)':'int64','외국인(남)':'int64','외국인(여)':'int64'})
#print(df1.dtypes)
cho=input('출력 조건 입력(년도별:1, 자치구별:2): ')

plt.style.use('ggplot')

fig=plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

if cho == "1":
    ### 년도별 조회(합계 제외)
    
    inYear=input('조회 년도 입력: ')
    df2 = df1[(df1['년도'] == inYear) & (df1['자치구'] != '합계')]  # 합계 제외
    df2['외국인']=df2['외국인(남)']+df2['외국인(여)']
    x=df2['자치구'], y=df2[['외국인(남)', '외국인(여)']]
    df2.plot(kind='bar', x='자치구', y=['외국인(남)', '외국인(여)'], ax=ax1)
    df2.plot(kind='bar', x='자치구', y='외국인', ax=ax2)
    
# plot()에서 ax는 위치값을 나타내주는 옵션, 단 add_subplot를 이용한 상태에서만
# 사용가능한 옵션이다
elif cho=="2":
    ### 자치구별 조회
    ingu = input('조회 자치구 입력: ')
    df2=df1[df1['자치구'] == ingu]
    df2.plot(kind='bar', x='년도', y=['외국인(남)', '외국인(여)'], figsize=(10, 4), ax=ax1)
    df2.plot(kind='bar', x='년도', y=['내국인(남)', '내국인(여)'], figsize=(10, 4), ax=ax2)
else:
    print('1과 2중 하나만 입력하세요.')
    exit()

#plt 안의 데이터를 저장해
plt.savefig('./Data/image_1.png')
    
plt.show()
# show 한 이후에는 저장이 되지 않는다.
# show 이후에는 메모리가 날라간다
# -


