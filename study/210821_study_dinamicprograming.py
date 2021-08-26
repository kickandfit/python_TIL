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

# #####  call by assignment
#
# - int, str, boolen, tuple 등은 call by value 형식으로 받아옴
# - list, dict 등은 call by referece 형식으로 받아옴
# - 즉 Mutable 갑과 immutable 값이 존재하는데, mutable은 copy를 해줘야만, 따로 메모리에 저장 되기 때문에 서로의 간섭에서 벗어날 수 있음
# - immutable은 서로 간섭하지 않음
# - 사용자가 만든 class는 기본적으로 mutable임
# - 때문에 판다스, 넘파이 등의 형식은 mutable 이라 똑같은 데이터셋, 배열 등을 활용하고 싶을 때는 copy해줘야함
# - 또한 mutable의 mutable이 있을 경우, deep copy를 해줘야함

# #### 오늘!
# - 재귀 확실 복습하셔야되요
# - 탑다운 : 메모이제션 , 바텀업 : DP 테이블
# - 다이나믹 프로그래밍의 목적 : 중복된 계산을 줄이기 위함
#     - 사용하는 경우 : 큰 쿤제를 작은 문제로 나누고, 작은 문제로 푼 답이 큰 문제로 풀 떄 변하지 않는 경우

# +
# 피보나치수열
#      1, 1, 2, 3, 5, 8 ,13 , 21  --> a(n-2) + a(n-1) = a(n)
                                #  --> b[] 리스트에 저장을 하는거요

def fibo(n):
    if n == 1 or n == 2:
        return 1
    print(n, end = ' ')
    return fibo(n-1)+fibo(n-2)
print(fibo(8))

# 반복이 많은데, 같은 값에 대해서 반복을 하고 있는거에요
# 굉장히 비효율적이고 메모리도 많이 쓰고 시간도 오래걸려
# 21을 구하는데 원래는 6번에 구할수 있는데 위 처럼 짜면 기하급수적으로 늘어나요
# n = 100 만되도 못구해
# -

def a(n):
    if n< 1:
        return
    print(n, end = ' ')
    a(n-1)
    a(n-1)
a(3)

# +
#아이디어 -> 같은 값들을 계속구하는 게 문제
#a(n-2) + a(n-1) = a(n) 한번만 구하고 싶은거에요
                                #  --> b[] 리스트에 저장을 하는거요

#한번 구하잖아요? 그거를 다른데다가 저장을해
#저장 후에 다음번에 그값을 토대로 계산을해

# 5*5*5,5*5*5,5*5*5
# b[5] = 5, b[25]=25 , b[25]*5 = > b[125]=125
# b[1---->100] b[23]-->23 --> dp 테이블이라고 일컬음
# 탑다운 , 바텁업 ---> 재귀로 구현하면 보통 탑다운(dp->메모이제이션), 바텀은 아래서 위로 올라가(dp테이블)

# 피보나치 수열을 저장하는 테이블
d = [0] * 101

def fibo(x):
    if x == 1 or x ==2:
        return 1
    # dp테이블에 값이 있어?
    if d[x] != 0:
        return d[x]
    
    print(x, end = ' ')
    d[x] = fibo(x-2) + fibo(x-1)
    return d[x]

fibo(8)


# +
# dp테이블 이해
# 1로 만들기
# 5, 3, 2 ---> 어떤 수 5, 3, 2로 나눌 수 있으면 나눌거에요, 
# 못나누면 그수 -1을 하고 다시 2 ,3 ,5 중에 나눌수 있는지 볼거에요
# 결과 적으로는 1로 만들거에요, 최소횟수를 구하고 싶어요

# 26 -> 13 -> 12 ->6 ->3 ->1 (5번) ////////////// 26 ->25->5->1 (3번)

# a(n) = max( 방법 1 a(n-1),방법 2 a(n-1)) /////힌트
# a(n) = min(a(n//5),a(n//3),a(n//2),a(n)-1) +1

# 바텁 업
x = int(input())
d = [0] *(x+1)

# 1--->2 ,1--->3,1---5
for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2]+1) # 오른쪽 항 d[i]는 i-1에서 +1 해준거에요
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i],d[i//5]+1)
        
print(d[x])
# -

# #### 바닥 공사
# 가로 길이가 N, 세로 길이가 2인 직사각형 형태의 얇은 바닥이 있다. 태일이는 이 얇은 바닥을 1 X 2의 덮개, 2 X 1의 덮개, 2 X 2의 겊개를 이용해 채우고자 한다. 이 때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오. 예를 들어 2 X 3 크기의 바닥을 채우는 경우의 수는 5 가지다

# +
# a(n) = a(n-1) + a(n-2)*2

n = int(input())
d = [0]*(n+1)

d[1] = 1
d[2] = 3

for i in range(3,n+1):
    d[i] = d[i-1] +2*d[i-2]
    
print(d[n])
# -

# # 개미 전사
# - 개미 저사는 부족한 식량을 충당하고자 메뚜기 마을의 식량 창고를 몰래 공격하려고 한다. 메뚜기 마을에는 여러 개의 식량창고가 있는데, 식량창고는 일직선으로 이어져 있다. 각 식량 창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정이다. 이때 메뚜기 정찰병들은 일직선상에 존재하는 식량 창고 중에서 서로 인접한 식량 창고가 공격받으면 바로 알아챌 수 있다. 따라서 개미 전사가 정찰병에게 들키지 않고 식량 창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량 창고를 약탈해야 한다. 예를 들어 시걍 창고가 4개가 다음과 같이 존재한다고 가정하자 [1, 3, 1, 5] 이때 개미전사는 두 번째 식량창고와 네 번째 식량창고를 선택 했을 때 최댓값인 총 8개의 식량을 빼앗을 수 있다. 개미 전사는 식량창고가 이러헥 일직선상일 때 최대한 맣은 식량을 얻기를 원한다. 개미 전사를 위해 식량 창고 N개에 대한 정보가 주어 졌을때 얻을 수 있는 식량의 최대값을 구하느 프로그램을 작성하라
#
# 입력 조건 : 첫째 줄에 식량 창고의 개수 N이 주어진다
# 둘째 줄에 공백으로 구분되어 각 식량 창고에 저장된 식량의 개수 k가 주어진다.
#
# 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력해라

# +
# a(n) = max(a(n-1),a(n-2)+k(n))

n = int(input())
array = list(map(int, input().split())) # 1 2 3 4 5 6 7 , 공백으로 구분해서 1,2,3,4,5 를 리스트에 넣어 뭘로? int로
d = [0]*(n+1)

# 식량의 최대개수를 담는 배열 -> d 가 되는 거에요

d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2, n):
    d[i] = max(d[i-1],d[i-2]+array[i])
    
print(d[n-1])
# -


