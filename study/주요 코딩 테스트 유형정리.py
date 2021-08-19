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

# # 카카오
#
#
# - 20년 카카오
#     - 구현, 브루트 포스, 투 포인터, BFS
# - 19년 카카오 
#     - 구현, 다이나믹 프로그래밍, 자료구조
# - 18년 카카오
#     - 그리디, 구현
# - 17년 카카오
#     - 그리디, 구현

# # 라인
# - 20년
#     - 완전 탐색, 문자열, 자료구조
# - 19년 하반기
#     - 자료구조, 완전 탐색, 구현
# - 19년 상반기
#     - 탐색, 구현
# - 18년 하반기
#     - 탐색, 그리디, 다이나믹 프로그래밍, 
# - 18년 상반기
#     - 탐색, 그리디, 다이나믹 프로그래밍

# # 1주차
# - 탐색 5문항 (브루드 포스 부분 위에서 5문항)
#

# ####  한수

# +
N = int(input())
result = 0

for i in range(1,N+1):
    if i <= 99 :
        result += 1
    else:
        N = str(i)
        if int(N[0])-int(N[1]) == int(N[1])-int(N[2]):
            result += 1
print(result)
# -

# #### 블랙잭

# +
# 이건 왜 틀린걸까 도대체가... ㅎㅎㅎ
from itertools import combinations

# n, m = map(int, input().split())
n, m = 5, 21
# N = list(sys.stdin.readline())
# N = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
N = [5, 6, 7, 8, 9]
M = combinations(N, 3)
sum = 0
min = 10000
for a, b, c in M:
    sum = a+ b+ c
   
    if sum <= m and (m-sum)<min:
        min = m - sum
        result = sum
        
print (result)



# +
from itertools import combinations

n, m = map(int, input().split())

N = map(int, input().split())

sum = 0
result = 0
for a, b, c in combinations(N, 3):
    sum = a+ b+ c
    if result < sum <=m:
        result = sum 
    sum = 0
    
print (result)

# -
# #### 분해합


# +
from itertools import product
n = int(input())
result = 1000
num = [i for i in range(10)]

        

# -


