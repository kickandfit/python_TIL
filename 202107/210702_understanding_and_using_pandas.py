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

import pandas as pd
from numpy import random
import matplotlib.pyplot as plt

# #### pandas.Series 구조
#
# - 1차원(1D) 구조를 가지고 있음

# Series 구조로 생성하는 경우는 아주 드물다
df1 = pd.Series(['aaa', 'bbb', 'ccc', 'ddd'], name = "Name")
print(df1)
print(type(df1))

df2 = pd.Series([13, 24, 31, 29], name = "Age")
print(pd.DataFrame(df2))
print()
print(df2)


# +
# 시리즈로 만들어진 데이터 하나로 합치기
# 단 데이터 프레임 구조라도 데이터 개수만 같으면 사용할 수 있다
# 두 개 이상의 데이터프레임 또는 시리즈 구조의 데이터를 병합할 때 사용
# 병합방법 : 행병합(행추가) -> axis = 0, 열병합(열추가) -> axis = 1


df0 = pd.concat([ df1, df2 ], axis = 1)
print(df0)
print(type(df0))
# -

# ### pandas.DataFrame 구조

# +
# pandas.DataFrame 생성 : 딕셔너리 구조 이용

df1 = pd.DataFrame({'Name' : ['aaa', 'bbb', 'ccc', 'ddd'],
                   'Age' : [33, 28, 45, 41],
                   'Sex' : ['male', 'female', 'male', 'female']})
df1

# +
# pandas.DataFrame 생성 : 리스트 구조 이용
# pandas.DataFrame([리스트 값], columns = [열이름 정의])


df1 = pd.DataFrame([['AAA', 33, 'male'], 
                   ['BBB', 28, 'female'], 
                   ['CCC', 45, 'male'], 
                   ['DDD', 41, 'female']], columns = ["Name" , 'Age', 'sex'])
print(df1)


# +
# pandas.DataFrame 생성 : 리스트와 딕셔너리가 같이 있는 경우
#pandas.DataFrame( [ {딕셔너리1}, {딕셔너리2}, {딕셔너리3}, {딕셔너리4} )

df1 = pd.DataFrame( [{'Name' : 'aaa', 'Agee' : 33, 'sex' : 'male'},
                    {'Name' : 'bbb', 'Agee' : 28, 'sex' : 'female'},
                    {'Name' : 'ccc', 'Agee' : 45, 'sex' : 'male'},
                    {'Name' : 'ddd', 'Agee' : 41, 'sex' : 'female'},])
df1
# -

# ### Pandas 에서 NaN( 결측치 ) 처리

#csv 파일 가져오기 : pd.read_csv('디렉토리 경로 및 파일명' , encoding='형태에 맞춰서')
# encoding 옵션 : 기본 utf-8, 상황에 따라, cp949, ansi, utf-16
df1=pd.read_csv('./Data/성적표.csv', encoding = 'cp949')
print(df1)

# NaN 값 확인 DataFrame.isnull().sum() -> 각 열단위 NaN 확인
df1.isnull().sum()

# +
# NaN 값 처리 : 모든 데이터 NAN 인 데이터 행 삭제: DataFrame.dropna()
# dropna() 옵션 : default(생략시) -> how = 'any' : NaN이 있는 모든 행 삭제
# dropna() 옵션 : how = 'all' -> 행 전체가 NaN 일 때 삭제
# dorpna() 옵션 : thresh = 3 (thresh = 결측치 개수) -> NaN 이 3개 이상인 행 전체 삭제 

#df1.dropna(how = 'all')
df1.dropna(thresh = 3) # NaN이 3개 이상이면 제거
# -

# dropna() 옵션 , axis = 1 열 전체가 NaN인 값 삭제
# defualt axis = 0
df1.dropna(how = 'all', axis = 1)


# +
# 결측치를 수정한 데이터 적용하기

#df1.dropna(thresh = 3, inplace = True)
df1 = df1.dropna( thresh = 3)
df1
# -

# ### pandas 모듈을 이용한 데이터 편집 및 관리

# +
#실기 이론 점수 60-100 점 사이의 값으로 

df1['이론'] = random.randint(60, 101, size = len(df1))
df1['실기'] = random.randint(60, 101, size = len(df1))
print(df1.head(3))
display(df1.tail(3))
# -

# ### [요구사항]
#
# - "남/여" 열의 값을 남자 -> 1  여자-> 2 변경해서 새로운 열을 추가해보기
# - 열 이름 - > 성별 코드
# - df1 열 순서 : 순서, 이름, 성별, 성별코드, 학과, 학년, 이론, 실기

# +
#df1['성별코드'] = [1 if xy == '남자' else 2 for xy in df1['남/여']]

성별코드 = []
for xy in df1['남/여']:
    if xy == "남자":
        성별코드.append(1)
    else:
        성별코드.append(2)

df1['성별코드'] = 성별코드 
# df1에 새로운 열 생성 후 데이터 입력()
# 단, csv 파일에 영향을 주지 않음
# 메모리에서 활용되고 있는 내용임
# -

df1 = df1[['순번', '이름', '남/여','성별코드','학과','학년', '이론', '실기']]
df1

df1['합계'] = df1['이론'] + df1['실기']
df1['평균'] = df1['합계'] / 2
df1.head(3)

# #### Pandas.DataFrame 저장
#
# - csv: DataFrame.tp_csv('디렉토리 경로 및 파일명.csv', index = False) # 구분자 기본 콤마(,), 인덱스 = 저장하지 않음
# - txt: DataFrame.tp_csv('디렉토리 경로 및 파일명.txt', sep="\t", index = False) #구분자(sep)을 tab(\t)으로 설정
# - xlsx: DataFrame.tp_excel('디렉토리 경로 및 파일명.xlsx', index = False, sheet_name = 'new_name')
# -        엑셀 추가 모듈 설치해야 사용 가능 : 2003버전 = xlrd 설치
# -        엑셀 추가 모듈 설치해야 사용 가능 : 2007버전이후 = openpyxl 설치
# - html: DataFrame.tp_html('디렉토리 경로 및 파일명.html', index = False)
# - csv: DataFrame.tp_csv('디렉토리 경로 및 파일명.csv', index = False, header = False) # 제목도 제거하고 저장할게요

# +
# 기본 형식으로 저장 -> csv
# #!pip install openpyxl

df1.to_csv('./data/성적1.csv')
df1.to_csv('./data/성적2.txt', sep = '\t', index = False)
df1.to_excel('./data/성적3.xlsx', header = False)
df1.to_html('./data/성적4.html', index = False)
# -

# ### pandas.DataFrame 행/열 값 출력하기
#
# - DataFrame.loc[indexr값, '열이름']
# - DataFrame.loc[[index값1,index값2], ['열이름1', '열이름2]]
#
# - DataFrame.iloc[행위치, 열위치]
# - DataFrame.iloc[행시작위치:행종료위치, 열시작위치:열종료위치]
#

# 열 이름
df1.columns

df1[[ '이름','성별코드','학년', '평균']]

df1[df1['남/여']=='여자']

# #### 데이터의 index 값을 이용해 출력하는 방법
# - DataFrame.loc[index 값] -> 단일 행 출력
# - DataFrame.loc[index 시작값 : index종료값] -> 시작 ~종료값 다중 행 출력
# - DataFrame.loc[index 시작값 : index종료값,''열이름', '열이름']] -> 시작값~종료값 다중 행에서 열이름 정보만 가져오기

# 1개의 행 데이터 출력
df1.loc[1]

# +
# index 값이 1~6인 데이터 출력
# 리스트 인덱싱이 아니다
# 메모리 주소값이 아니라, 메모리를 찍어준 데이터 자체다

df1.loc[1:6]
# -

df1.loc[1:6, ['이름', '학과', '이론', '실기']] # 1번에서 6번 인덱스의 이름만 보고 싶다

df1.loc[[1, 3, 4, 10], ['이름', '학과', '이론', '실기']]

# ### 데이터 위치값을 이용한 행/열 출력
#
# - DataFrame.iloc -> index값, columns:열 이름값은 없다 라고 생각해라
# - DataFrame.iloc[행위치, 열위치]
# - DataFrame.iloc[행시작위치: 행종료위치, 열시작위치 : 열종료위치]

df1.iloc[1:6] # 행 위치가 1 부터 6 전까지

# +
# 행위치가 1부터 6 전까지 '이름', '남/여', '학년' 데이터 출력

df1.iloc[1:6, [1,2,5]]
# -

df1.iloc[5:11, 1:6]

# ### DataFrame.sort_values()/DataFrame.sort_index()

# +
# DataFrame의 값을 기준으로 정렬 : DataFrame.sort_values(by=['열이름'], ascending = True/False)
# 기본값 오름차순

df1=df1.sort_values(by=['학년'])
display(df1.head()) #display는 ipython에서 만 지원

df1.sort_values( by = ['평균'], ascending = False, inplace = True ) # 평균을 기준으로 내림차순
display(df1.head())

# +
# 정렬 대상이 2개 이상인 경우
# 학년을 기준으로 1차 오름 차순 정리하고 
# 평균을 기준으로 2차 내림차순 정리해라

df1.sort_values(by = ['학년', '평균'], ascending = [True, False], inplace = True)
df1.iloc[0:9]
# -

df1.loc[29:33] 
df1
#데이터 1번과 9번 사이의 값을 뽑아라
#정렬 시에 그 사이의 데이터는 몇개가 될줄 몰라

df1= df1.sort_index() # 기본값은 ascending = True
df1

# index 값 재 설정
df1.reset_index() # 기존 index 값을 유지하면서 새로운 인덱스 추가 적용

# index 값 재 설정
df1.reset_index(drop = True) # 인덱스 값을 제거하고 새로운 인덱스 추가 적용

# ### DataFrame 행/열 삭제
#
# - DataFrame.drop(index = 숫자, axis = 0 ) # index 값이 숫자인 행 1개 전체 삭제
# - DataFrame.drop(index = [숫자, 숫자, 숫자], axis = 0 ) # 여러개의 행 삭제
# - DataFrame.drop(DataFrame[DataFrame['열이름'] <= 69].index) 열이름이 69보다 같거나 작다면 삭제해
# - DataFrame.drop(DataFrame[['열이름1', '열이름2]], axis = 1) # 정의한 열을 삭제해

df1.drop(0) # index값이 0인 행삭제
df1.drop([0,2,4,6]) #index값이 0,2,4,6 인 데이터 행 삭제


df1.drop(df1[df1['평균'] < 90].index)

# +
#drop()으로 열을 삭제하는 이유 : 확인 후 데이터 적용이 가능
# 즉 inplace가 아닌 상태라서 쓰는 것이다 cpu에서만 놀기 때문에

df1.drop(['순번', '성별코드'], axis = 1) # 열 삭제
df1.drop(columns = ['학과', '합계'])

# +
# 삭제 후 적용까지 한것
# 즉 메모리에서 직접 해버려, 메모리에서 완전히 제거

del df1['합계']
df1.head()
