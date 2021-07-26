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

# +
#1로 만들기 : 다이나믹 프로그래밍 필요없음(메모리를 반복해서 쓰지 않음), my solution
def make_num_1(num):
    global div_lst , cnt , d

    if num ==1.0:
        return 1
    if d[int(num)] != 0 :
        return d[int(num)]
    for i in div_lst:
#         print(num)
        if num % i == 0:
            num = num / i
           
            make_num_1(num)
            cnt+= 1
            d[int(num)] = cnt
            return d[int(num)]     
    num -=1
            
#             print(cnt)

    make_num_1(num)
    cnt += 1
    d[int(num)] = cnt
    return d[int(num)]
div_lst = [5, 3, 2]
cnt = 0
d = [0]*3001
make_num_1(300)


# +
#다이나믹 프로그래밍 예시)
def pibo(x):
    if x > 2:
        print(x)
    elif x == 2 or x == 1:
        return 1
    if d[x] != 0 :
        return d[x]
    d[x] = pibo(x-1)+pibo(x-2)
  
    return d[x]
  
pibo(9)


# +
#another solution
def a(n):
    global d_lst, cnt
    if n >1:
        
        for i in d_lst:
            if n % i == 0:
                n = n/i
                print(n)
                a(n)
                cnt += 1
                return cnt

        n -= 1
        print(n)
        a(n)
        cnt += 1
        return cnt
                    
n = 300
cnt = 0
d_lst = [2 , 3, 5]
d = [0]*(n+1)
a(n)
# -

#풀이 for문 이용
d_lst = [2, 3, 5]
n = 300
new_lst = [0]*(n+1)
for i in range(2, n+1):
    new_lst[i] = new_lst[i-1]+1
    for j in d_lst:
        if i % j ==0:
            new_lst[i] = min(new_lst[i], new_lst[i//j]+1 )
new_lst[300]




