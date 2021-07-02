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
from numpy import random as rd
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

# ### 성적표.csv 파일을 이용한 데이터 추가/수정/삭제 등 관리

#csv 파일 가져오기 : pd.read_csv('디렉토리 경로 및 파일명' , encoding='형태에 맞춰서')
# encoding 옵션 : 기본 utf-8, 상황에 따라, cp949, ansi, utf-16
df1=pd.read_csv('./Data/성적표.csv', encoding = 'cp949')
print(df1)


