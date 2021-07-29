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

# ### NumPy 특징
#
# - 과학 기술 계산을 위한 라이브러리 제공
# - 백터/행렬/배열 처리 및 연산, 난수 발생
# - 파일관리(txt, csv 등 파일 읽기/쓰기)
# - 리스트(list) 형 데이터와 유사하지만 Numpy는 배열의 특징을 가짐
# - 모든 원소는 동일한 자료형이어야 한다.
# - 원소들 중 다른 자료형이 있다면 가장 큰 자료형으로 변경됨
# - 계산 속도가 빠르다
# - 벡터/연산, 배열 인덱싱 등을 통해 질의 가능

import numpy as np

lst = [1, 2, 3, 4, 5]
s = [i*2 for i in lst]

arr_lst = np.array(lst)
arr_lst*2

# #### numpy 연산
# - 행렬 연산이라고 생각해라
#      - 즉 데이터의 개수가 맞지 않으면 연산할 수 없다

#1차원 배열 구조, 즉 벡터 구조
arr1 = np.array([1,2,3])
arr2 = np.array([10, 20, 30])
print(arr1+arr2)
print(arr2>=20)

# #### 넘파이를 두 벡터 연산시자료의 갯수는 동일해야 한다

# +
arr1 = np.array([1,2,3,4])
arr2 = np.array([10, 20, 30])

arr1 + arr2
#에러가 나온다 왜? 개수가 맞지 않으니까
# -

# #### 2차원 배열 구조

lst = [[0,0,1], [8, 12, 33]]
arr = np.array(lst)
print(lst)
print(arr)

# +
print(len(lst))  # lst의 전체 데이터 개수
print(len(arr))  # arr의 행의 개수

print(len(lst[0])) # lst의 첫번째 데이터의 갯수
print(len(arr[0])) # arr의 열의 갯수
# -

# - numpy에서 움직이는 데이터는 갯수를 맞춰준다
# - 그렇지 않으면 object를 받아와 버린다. 즉 list면 array([],[])

lst = [[0,0,1,1],[8, 12, 33]]
arr = np.array(lst)
arr

# #### 3차원 배열

lst = [[[10, 20, 30]]]
arr = np.array(lst)
print(arr.shape) # arr의 모양을 보는 방법 (차원)
#(면, 행, 열)
print(arr)

lst = [[[10, 20, 30],[15, 25, 35]]]
arr = np.array(lst)
print(arr.shape) # arr의 모양을 보는 방법 (차원)
#(면, 행, 열)
print(arr)

# - 배열을 만들려면 구조가 똑같아야한다

lst = [[[10, 20, 30], [15, 25, 35]],[[1.,2.,3.],[12, 13., 15]]]
arr = np.array(lst)
print(arr.shape) # arr의 모양을 보는 방법 (차원)
#(면, 행, 열)
print(arr)

# - 가장 큰 자료형으로 바꿔준다

lst = [[[10, 20, 30], [15, 25, 35]],[[1.,2.,3.],[12, 13., '15']]]
arr = np.array(lst)
print(arr.shape) # arr의 모양을 보는 방법 (차원)
#(면, 행, 열)
print(arr)

# ####  파이썬 자료형
# - NoneType / bool/ int / float / complex / str / tuple / list / dict/ fuction

# +
from sys import getsizeof

a=1;b=1.;c='1'
print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(c))
# -

# #### 배열 구조 데이터 인덱싱

arr = np.array([10, 20, 30, 40, 50])
print(arr[0])

# +
# 2차원 배열의 인덱싱

arr = np.array([[10, 20, 30, 40, 50],[15, 25, 35, 45, 55]])
print(arr[0])    # 첫번째 행 전체 출력해
print(arr[-1])   # 마지막 행 전체 출력해
print(arr[0][0]) #우리가 리스트에서 데이터 불러왔던 구조,
                 #0번째 행가져오고 0번쨰 열 데이터 가져와
print(arr[0, 0]) # 0번째 행 0번째 열 데이터 가져와

# +
# 3차원 배열의 인덱싱

lst = [[[10, 20, 30], [15, 25, 35]],[[1.,2.,3.],[12, 13., 15]]]
arr = np.array(lst)
print(arr.shape)
print(arr)
# -

# ####  불리언(Boolean) 배열 방식을 이용한 인덱싱

arr = np.arange(1, 11)
arr

atf = np.array([False, True, False, True, False, True, False, True,False, True])
print(arr[atf]) # Ture인 값만 매칭해서 출력
anum = np.array([0,2,4,6,8])
print(arr[anum]) # anum을 위치값으로 사용해 출력

print(arr[arr%2==1])
print(arr[arr%2==0])

arr = np.array([[10, 20, 30],[15, 25, 35],[1.,2.,3.],[12, 13., 15]])
arr

arr[[1,3], :] # 1행이랑 3행 가져오고 열은 다가져와

# #### 배열 생성/구조 변경

arr = np.array([15, 25, 35 ,45])
arr.dtype

arr = np.array([15, 25, 35 ,45], dtype = 'd')
arr.dtype

arr[1] = 28
arr

arr = np.arange(1, 10 ,2)
arr

arr = np.arange(10,1, -1)
arr

arr = np.logspace(0,1, 10) #10^0승부터 10^1승까지 10개 구간으로 나눈다
# np.logspace(a,b, c) 10^a부터 10^b 승까지 c 개의 구간으로 나눠라
arr

arr = np.linspace(0, 100, 5, endpoint = False) # 0 부터 100까지 실수범위 5구간으로 나눠라 마지막 값은 제거한다
arr

# #### 배열 데이터 변경

arr = np.array([1,2,3,4,5,6,7,8,9,10])
arr_res = arr.reshape(5, 2)
arr_res


arr = np.ones(50) # 50개의 데이터를 다 0로
len(arr)
arr = np.zeros(50) # 50개의 데이터를 다 0 으로
arr_res = arr.reshape(10, -1)
# 행또는 열 위치에 -1를 넣으면 자동 생성
# 다만 arr.reshape(-1,-1)은 에러
arr_res

arr_res.reshape(-1,5,2) # 3차원 구조로도 변경가능
# 즉 차원도 마음데로 바꿀수 있음

arr_res.reshape(-1) # 즉 1차원으로도 다시변경 가능

arr = np.arange(1, 61)
arr_res = arr.reshape(-1, 6)
arr_res

arr_res[0] = 0
arr_res

arr_res[0,2] = 10
arr_res

# ####  브로드캐스팅(broad casting) & 마스킹(masking)
#  - 하나의 배열 or 요소가 어떤 특정 배열에 영향을 미칠때 배열간의 형상을 맞추는 것을 브로드 캐스팅이라고함

#arr_res 배열에서 값을 나누고 남은 나머지가 0이면 True 반환
#idx 변수를 만들어(=masking을 만듬) True/False로 변환된 데이터 저장
idx = arr_res%2==0
idx

# 만들어진 idx의 마스킹 값을 기준으로 True인 값만 출력
arr_res[idx] = 100
arr_res
#True 값만 뽑아서 100으로 바꿔라

# #### NumPy에서 파일 읽고/쓰기

with open('c:/pydata/test.csv', encoding='utf-8') as f:
    csv_data = []
    for line in f.readlines():
        line = line.replace('\n',"")
        csv_data.append(line.split(','))
print('csv_data','\n',csv_data)
print(type(csv_data[0][1]))

import pandas as pd
df = pd.read_csv('c:/pydata/test.csv', encoding='utf-8', names=['이름','값'])
#제목이 없을때는 names를 줘서 columns를 넣어주면 된다
df.info()

np_data=np.loadtxt('c:/pydata/test.csv', encoding='utf-8', 
                   delimiter = ',', dtype = str)
np_data
# delimiter : 구분자 입력, dtype : 데이터 타입 설정

# +
# idx= []
# for i in np_data:
#     i[1]=i[1].replace(" ","")
#     idx.append(int(i[1]))
# arr_res = np.array(idx)
# arr_res
# -

idx = np_data==""
np_data[idx] = 0
np_data

# #### NaN 변경하기

arr = np.array([5, 6, np.NaN])
arr

np.isnan(arr) # pandas.isna

np.nan_to_num(arr)

arr[np.isnan(arr)] = 5.5


arr = np.array([5, 6, np.NaN])
arr[np.isnan(arr)]=np.mean(np.nan_to_num(arr))
arr

arr = np.array([5, 6, np.NaN])
arr[np.isnan(arr)]=sum(np.nan_to_num(arr))/sum(np.isnan(arr)==False)
arr


arr = np.array([5, 6, np.NaN])
print(np.max(arr))
print(np.min(arr))

arr = np.array([5, 6, np.NaN])
arr[np.isnan(arr)]=np.max(arr[np.isnan(arr)==False])
arr

arr = np.array([5, 6, np.NaN])
( arr[np.isnan(arr) == False] )


# #### 행렬 데이터 결합, concatenate 함수

arr1 = np.random.randint(10, size=(2, 3)) # 0-9 사이의 정수를 이용해 2행 3열 구조 데이터 생성
arr2 = np.random.randint(10, size=(2, 3))
arr3 = np.random.randint(10, size=(2, 3))
print(arr1)
print(arr2)
print(arr3)

# #### concatenate : 기본 세로결합
# - np.concatenate

np.concatenate((arr1, arr3))

# #### 가로결합
# - 옵션에 axis = 1 추가

np.concatenate((arr2, arr3), axis = 1)


