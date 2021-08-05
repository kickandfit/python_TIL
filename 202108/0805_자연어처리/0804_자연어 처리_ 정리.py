# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## pandas
#
# - 일반적으로 세가지 구조
#     - 시리즈(Series) ( 1차원 배열에 대응 되는 구조 )
#     - 데이터 프레임)DataFrame) ( 2차원 배열에 대응 되는 구조 )
#     - 패널(Panel)

import pandas as pd

# 시리즈(Series)
# - 시리즈 클래스는 1차원 배열의 값(values)에 값에 대응되는 인덱스(index)를 부여할 수 있는 구조
# - index와 value

sr = pd.Series([17000, 18000, 1000, 5000],
       index=["피자", "치킨", "콜라", "맥주"])
print(sr)


sr.values #시리즈는 값만 출력할 때 배열 구조로 나옴

sr.index

sr[0] #sr.iloc[0]

sr['피자'] #sr.loc['피자']

# 데이터프레임(DataFrame)
# - 2차원 리스트를 매개변수로 전달
# - 2차원이므로 행방향 인덱스(index)와 열방향(columns)가 존재하는 자료구조
# - 열(columns), 인덱스(index), 값(values)으로 구성

# +
# index와 columns 를 넣어주지 않으면 숫자로 들어감

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values)
print(df)


# +
# index와 column를 넣어준다면 정해준 값을 기준으로 들어감

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)
print(df)

# +
import numpy as np

# 데이터 프레임을 np로 넘기는 부분
# tensorflow 와 keras 에서 기본적으로 배열을 가지고 들어감

# +
# 방법 1
# np.array에 데이터 프레임을 넣으면 기본적으로 value만 가져감

np.array(df)

# +
# 방법 2
# 마찬가지로 index와 columns를 제외시킴

df.to_numpy()
# -

print(df.index) 
print(df.columns) # columns is index of axis
print(df.values) # values is array like np.array

# 리스트로 생성하기
data = [
    ['1000', 'Steve', 90.72], 
    ['1001', 'James', 78.09], 
    ['1002', 'Doyeon', 98.43], 
    ['1003', 'Jane', 64.19], 
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]
df = pd.DataFrame(data)
print(df)
print(df.info())

# +
# 딕셔너리로 생성하기

# dictionary의 key가 columns로 간다

data = { '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
'이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
         '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]}

df = pd.DataFrame(data)
print(df)

# -

data = [{'학번' : '1000', '이름' : 'Steve', "점수" : 90.72},
       {'학번' : '1001', '이름' : 'Jamees', "점수" : 78.09},
       {'학번' : '1002', '이름' : 'Doyeon', "점수" : 98.43},]
df = pd.DataFrame(data)
print(df)
print()
print(np.array(data))#data를 넘파이로 가져오면 딕셔너리 자체로 들어감
print()
print(np.array(df))

np.array(df[['학번']]) # 판다스와 넘파이 변형 후 응용 열떼내기

np.array(df[['학번', '점수']]) # 판다스 넘파이 응용2

# #### 외부데이터 읽기
#
# - Pandas는 CSV, 텍스트, Excel, SQL, HTML, JSON 등 다양한 데이터 파일을 읽고 데이터 프레임 생성
# - df = pd.read_csv()(csv 또는 txt), df=pd.read_excel(엑셀파일), df=pd.read_html(url), df=pd.read_json(json파일)

# ## Numpy
#
# - 수치 데이터를 다루는 파이썬 패키지
# - 핵심 : 다차원 행렬 자료구조인 ndarray를 통해 벡터 및 행렬을 사용하는 선형 대수 계산에서 주로 사용

import numpy as np

# #### numpy의 주요 모듈
# 1. np.array() # 리스트, 튜플, 배열로 부터 ndarray를 생성
# 2. np.asarray() # 기존의 array로 부터 ndarray를 생성
# 3. np.arange() # range와 비슷
# 4. np.linspace(start, end, num) # [start, end] 균일한 간격으로 num개 생성
# 5. np.logspace(start, end, num) # [start, end] log scale 간격으로 num개 생성
#

a = np.array([1, 2, 3, 4, 5]) #리스트를 가지고 1차원 배열 생성
print(type(a))
print(a)


b = np.array([[10, 20, 30], [ 60, 70, 80]]) 
print(type(b))
print(b) #출력


print(b.ndim) #차원 출력 : ......면 행 열
print(b.shape) #크기 출력 (구조) : 2행 3열


# #### ndarray의 초기화
# - zero() : 해당 배열에 모두 0을 삽입
# - ones() : 해당 배열에 모두 1을 삽입
# - full() : 배열에 사용자가 지정한 값을 넣는데 사용
# - eye() : 대각선으로 1이고 나머지는 0인 2차원 배열을 생성

a = np.zeros((2,3)) # 모든값이 0인 2x3 배열 생성.
print(a)


a = np.ones((2,3)) # 모든값이 1인 2x3 배열 생성.
print(a)


a = np.full((2,3), 7) # 모든 값이 특정 상수인 배열 생성
print(a)

a = np.eye(3) # 대각선으로는 1이고 나머지는 0인 2차원 배열을 생성
print(a)      # 숫자가 3 이면 3x3 행렬 , 5이면 5x5

# #### np.arange()
# - 지정해준 범위에 대해서 배열을 생성
# - numpy.arange(start, stop, step, dtype)
# - a = np.arange(n) # 0 , ....., n-1 까지 범위의 지정
# - a = np.arange(i, j, k, dtype = None) # i부터 j-1까지 k 만큼 증가하는배열 dtpye = None 생략(int 32/int64)
# - a = np.arange(i, j, k, dytpe = np.int32)# i부터 j-1까지 k 만큼 증가하는배열(int32)
#

a = np.arange(5.0)
print(a.dtype)
a

a = np.arange(5)
print(a.dtype)
a

# #### NumPy의 dtype
#
# unit : 0과 양수 int : 음수 0 정수
# - np.int8: 8-bit signed integer (from -128 to 127)
# - np.uint8: 8-bit unsigned integer (from 0 to 255)
# - np.int16: 16-bit signed integer (from -32768 to 32767)
# - np.uint16: 16-bit unsigned integer (from 0 to 65535)
# - np.int32: 32-bit signed integer (from -231 to 231-1)
# - np.uint32: 32-bit unsigned integer (from 0 to 2**32-1)
# - np.int64: 64-bit signed integer (from -263 to 263-1)
# - np.uint64: 64-bit unsigned integer (from 0 to 2**64-1)
#

# #### reshape()
#
# - 배열 구조 변경

a = np.array(np.arange(30))
print(a)
print()
print(a.reshape((5,6)))


a = np.array(np.arange(30)).reshape((5,6))
print(a)

# #### Numpy 슬라이싱
#
# - ndarray를 통해 만든 다차원 배열은 파이썬의 리스트처럼 슬라이스(Slice) 기능을 지원
# - 원소들 중 복수 개에 접근할 수 있음
#

a = np.array([[1, 2, 3], [4, 5, 6]])
a

a[0:2, 1:2] # 행: 0부터 2전(0,1) 열 1부터 2전까지(1)

a.reshape(-1)

# shwallow copy
b = a[0, :] # 첫번째 행 출력
print(b)
print(b.shape)
print(b.ndim)

# #### Numpy 정수 인덱싱 (integer indxing)
# - 원본 배열로부터 부분 배열을 구함

a = np.array([[1,2], [4,5], [7,8]])


b = a[[2, 1],[1, 0]] # a[[row2, row1],[col1, col0]]을 의미함.
                     # a[[행1],[행2]], [열1,열2]]
print(b)
# b = [value1, value2] =[(row2, col1), (row1,col0)]
# 뭐 이딴식으로 해놨지?

# #### Numpy 연산
#
# - Mumpy를 사용하면 배열간 연산을 손쉽게 수행
# - +,-, *, /의 연산자를 사용할 수 있음(산술연산)
# - add(), subtract(), multiply(), divide() 함수 사용 가능
# - 벡터와 행렬의 곱 또는 행렬곱을 위해서는 dot()을 사용

# +
x = np.array([1,2,3])
y = np.array([4,5,6])

print(x)
print()
print(y)

# -

b = x + y # 각 요소에 대해서 더함
# b = np.add(x, y)와 동일함
print(b)

b = x - y # 각 요소에 대해서 빼기
a= b
# b = np.subtract(x, y)와 동일함
print(b)


# 행렬자체가 들어가는 것은 재할당의 의미로 들어감
# 주소가 바뀌지 않음
b = y * x # 각 요소에 대해서 곱셈
# b = np.multiply(y, x)와 동일함
print(b)


b = y / x  # 각 요소에 대해서 나눗셈
# b = np.divide(y, x)와 동일함
print(b)


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a)
print()
print(b)

# +
c = np.dot(a, b)
print(c)
# a의 행과 b의 열
# ([1*2 + 2+7, 1*4 + 2*8],
#  [5*3 +4*7, 3*6+4*8])

#([a행1*b열1, a행1*b열2],
# [a행2*b열1, a행2*b열2])
# -

a = np.array([[1,2],[3,4],[5,6]])
b = np.array([[5,6,7],[8,9,10]])
c = np.array([[2,2],[3,3],[4,4]])
print(a);print(b);print(c)
print(a.shape);print(b.shape);print(c.shape)

d = np.dot(a,b)
print(d)

e = np.dot(d,c)
print(e)


