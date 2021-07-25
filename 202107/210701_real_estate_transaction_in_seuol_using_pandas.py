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

df1=pd.read_csv("./Data/서울특별시_부동산_실거래가_정보_2020년.csv", encoding='cp949')

df1[df1['자치구명']=='성북구']
# -

type(df1['자치구명']) # 시리즈는 필드를 그냥 나열해 놓은 구조, 따로따로 분리

type(df1[['자치구명','건물주용도']]) # dataframe 은 행과 열이 있는구조

df1.columns

# +
# dataframe 구조에서 원하는 필드값만 가져와 재졍의 하기
df1=df1[['자치구명', '법정동명',
     '건물주용도',
    '건축년도', '건물면적', '층정보', '물건금액', '건물명']]

df1.info() # 데이터프레임의 데이터 정보 확인하기

# object 객체형 데이터 : 문자형 데이터를 의미
# index의 개수와 데이터 수가 다르면 null 값이 있다
# null 값을 어떻게 처리해야하는 가를 고민해야함
# numpy로 넘어갈 때 배열 구조로 바꿔야함

# +
# 결측치 찾기

df1.isnull() # 결측치는 false로 나머지는 true로 뿌려줘

# -

df1.isnull().sum() # 열 단위 NaN 값의 갯수 확인하기

# +
df1[df1['건축년도'].isnull()] # 건축년도가 NaN 값만 화면에 보여줘

#notnull() 은 정상 값만 보여줘
# -

df1[df1['층정보'].isnull()].head(3) # 층정보가 NaN 값인 정보를 위에서 3개만 보여줘

df1[df1['층정보'].isnull()].tail(3) # 밑에서 3개만 볼까?

# +
#df1.fillna(1) # 전체 null 값을 .fillna() 를 활용해 () 속의 데이터로 바꾸겠다

df1 = df1.fillna({'층정보':1, '건물명':'단독', '건축년도':0})
df1.isnull().sum()
# NaN 값 중 층정보는 1로 바꿔줘, 건물명은 단독으로 바꿔줘
# 특정 열의 정보를 특정 정보로 변경하기

# +
# NaN 데이터 삭제 : dropna() 함수 사용
# 옵션 : how="any" -> 기본옵션, NaN이 하나라도 존재하면 삭제
# 옵션 : how="all" -> 데이터 전체( 행 전체 )가 NaN인 데이터만 삭제

df1.dropna(how="all")
# -

# ###  pandas.DataFrame 데이터 관리
# #### 데이터 검색
#
# - 단일조건 : df[df['열이름']==조건]
# - 다중조건 : df[ (df['열이름']==조건1 ) & (df['열이름']==조건2 ) -> AND 연산
# - 다중조건 : df[ (df['열이름']==조건1 ) | (df['열이름']==조건2 ) -> OR 조건

df1['자치구명'].unique() # unique() 고유값 뽑아 주기, array로 받아줌

df1[df1['자치구명']=='성북구']['법정동명'].unique() #단일조건 활용하기
# 자치구명이 성북구인 데이터에서 법정동명을 가져와 고유값(제거) 후 출력

# 자치구명이 성북구인 데이터에서 법정동명을 가져와 동별 개수를 체크해서 출력해
df2 = df1[df1['자치구명']=='성북구']['법정동명'].value_counts()
type(df2)
df2
# 정릉동, 장위동 등이 index 값이 됨 타입이 series 이기 때문

# +
# 자치구가 성북구이면서 건물주용도가 아파트인 데이터에 대한 법정동명 거래 건수 출력
df1[(df1['자치구명']=='성북구') & (df1['건물주용도']=='아파트')]['법정동명'].value_counts()

#고유값에서 데이터 값이 0이면 안보여주는구나

# +
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name) 

# series 일 때는 plot은 되는데 bar 는 안되는 구나
# 아 그럼 plot 에서 옵션을 주자

df2.plot(kind = 'bar', figsize=(10,3))
#df2.plot(kind = 'barh') #세로형 바 그래프

plt.show()

# +
# kind= "" : bar, pie, hist, ked, box, scatter, area

df2.plot(kind='box', figsize=(5,3 ))
plt.show()

df2.plot(kind='pie', figsize=(5,3 ))
plt.show()

df2.plot(kind='area', figsize=(5,3 ))
plt.show()

# +
# 평균 판매가가 자동으로 들어간다 그러나 차이점은 0이라는 숫자들은 자동으로 제거된다

df2 = df1[(df1['자치구명']=='성북구') & (df1['건물주용도']=='아파트')].groupby('법정동명').mean()
df2['물건금액'].plot(kind='bar', figsize=(10, 5))

# -

# ### [미션] 구단위 동별 '물건금액'  평균을 차트로 시각화 해주세요
#
# - 구이름, 건물주용도는 사용자에게 입력받아 진행
#

# +
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

df=pd.read_csv("./Data/서울특별시_부동산_실거래가_정보_2020년.csv", encoding='cp949')

g_name = input(str(""))
b_using = input(str(''))
df3 = df[(df['자치구명']==g_name) &(df['건물주용도']==b_using)][['법정동명', '물건금액']].groupby('법정동명').mean()
df3['물건금액'].plot(kind='bar', figsize=(10, 5))
plt.show()

#plt.savefig() 에 대해서 알아보기
# -


