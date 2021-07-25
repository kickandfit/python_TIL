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

import numpy as np
#np.random.randint(10,20)
#10 이상 20미만 range에서 랜덤수를 출력해라

#실습 1 - 0~50 랜덤한 숫자를 뽑아서, 리스트에 10개의 수를 넣어라
l1 = []
for num in range(10):
    num=np.random.randint(0,51)
    l1.append(num)
print(l1)

# +
#강사님 예시
rd_lst=[]

for i in range(10):
    rd_lst.append(np.random.randint(0,51))

print(rd_lst)

# +
#같은 방법 데이터 한줄쓰기

rd_lst = [np.random.randint(0,51) for i in range(10)]
print(rd_lst)

# lst = [ 리스트에 추가하고자하는 데이터를 발생시키는 부분 for 문 ]

# +
# 한줄쓰기 예시 2.
# words 데이터에서 글자수가 4개 이상인 데이터를 찾아 new_words에 리스트로 저장
words = ["멀티캠퍼스","티스토리", "블로그", "파이썬", "for", "프로그래밍", "반복"]

new_words = []

for word in words:
    if len(word)>3:
        new_words.append(word)

print(new_words)

# +
# 강사님 코딩

new_words1 = [word for word in words if len(word) > 3]
print(new_words1)

# 리스트 구조가 리스트로 연결될 때 사용
# 단 문법이 복잡하지 않을 때 사용

# +
# 이중구조 리스트
# 리스트에 단어 추가하기 한줄쓰기
words = [ [ "이중 for문", "파이썬", "프로그래밍", "스터디" ], 
          [ "Python", "NLP", "ML", "DL" ], 
          [ "leetCode", "BaekJoon", "HackerRank" ], 
          [ "멀티캠퍼스", "COMPAS", "DACON", "Kaggle" ] ]

wd_lst=[ j for i in words for j in i if len(j)>3 ]
print(wd_lst)
# -

# ### 문제 예시)random 모듈을 이용한 리스트 발생
#
# - 기준 : 0-50의 난수
# - 1세드당 인수가 10-20 개의 값을 갖게하라
# - 젠체 세트가 5세트
#
#

import numpy as np

print(np.random.randint(51))
print(np.random.randint(25, 51))
print(np.random.randint(0, 51, 10))
print(np.random.randint(51, size=10))

# +
int_lst = []

for num in range(5):
    int_lst.append(list(np.random.randint(0,51, size= np.random.randint(10,21))))
int_lst

# -

#한줄 쓰기
rd_lst=[list(np.random.randint(51,size=np.random.randint(10,21))) for i in range(5)]
rd_lst
#list는 구조 변경이 안된다. array는 차원 구조를 바꿀수 있다
#list는 1차원 구조다, array는 다차원 구조다

# ### (요구사항)입력된 숫자 데이터에서 최대값/최소값/합계 계산
# - 1. data에 입력된 값을 기준으로 계산
# - 2. 위에서 생성된 rd_lst 데이터를 이용해 계산
#
# ### 제한조건
# - sum(),max(),min() 함수 사용 금지

data1=[43, 19, 31, 5, 3, 32, 23, 38, 5, 18, 39, 36, 13, 23, 23, 41, 47, 13, 41]
max1 = data1[0]
min1 = data1[0]
sum1 = data1[0]
for num in data1:
    if num > max1:
        max1=num
    if num < min1:
        min1=num
    sum1 += num
print(max1)
print(min1)
print(sum1)

# +
#전체에서 최대값/최소값/합계 + 그룹내 최대값/최소값/합계
rd_lst=[list(np.random.randint(51,size=np.random.randint(10,21))) for i in range(5)]

tot_max2= [(rd_lst[0][0])]
tot_min2= [(rd_lst[0][0])]
tot_sum2= [(rd_lst[0][0])]
par_max2=[(rd_lst[0][0])]
par_min2=[(rd_lst[0][0])]
pre_sum = [(rd_lst[0][0])]
par_sum2=[]
for num in rd_lst:
    for i in num:
        if i > tot_max2:
            tot_max2 = i
    
        
        if i < tot_min2:
            tot_min2 = i
   
        tot_sum2 += i
        pre_sum += i
    par_max2.append(tot_max2)
    par_min2.append(tot_min2)
    par_sum2.append(pre_sum)
        
        
    pre_sum = 0
        
print(rd_lst)
print(f'전체 최대값:{tot_max2}, 전체 최소값:{tot_min2}, 전체 합계:{tot_sum2}')

print(f'그룹별 최대값:{par_max2}, 그룹별 최소값:{par_min2}, 그룹별 합계:{par_sum2}')

# +
rd_lst=[list(np.random.randint(51,size=np.random.randint(10,21))) for i in range(5)]

T_lst = [0, rd_lst[0][0], rd_lst[0][0]] #전체 값 계산
G_lst = []
G_num = 0
for lst in rd_lst:
    tem_lst=[0, lst[0], lst[0]]
    G_num += 1
    for Glst in lst:
        
        if Glst> tem_lst[1]:
            tem_lst[1] = Glst
        
        if Glst< tem_lst[2]:
            tem_lst[2] = Glst
        
        tem_lst[0] += Glst
    
    G_lst.append(tem_lst)
    print(f'{G_num}그룹 합계:{tem_lst[0]} 최대:{tem_lst[1]} 최소:{tem_lst[2]}')
    
    T_lst[0] = T_lst[0] + tem_lst[0]
    
    if tem_lst[1] > T_lst[1]:
        T_lst[1] = tem_lst[1]
    
    if tem_lst[2] < T_lst[2]:
        T_lst[2] = tem_lst[2]
print(f'전체 합계:{T_lst[0]} 최대:{T_lst[1]} 최소:{T_lst[2]}')

#list 는 어떤 배열이든 마구 때려넣을 수 있어, array는 데이터의 개수가 맞아야되
# -














