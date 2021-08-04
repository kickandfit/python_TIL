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

# 문자 재정렬
a = list( 'a1bds42d')
a.sort()
b = []
c = []
for i in a:
    try:
        b.append(int(i))
    except:
        c.append(i)
d= ""
tot = 0
for i in c:
    d += i
for i in b:
    tot +=i
print(d+str(tot))

# +
# 모범답안
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()
if value != 0:
    result.append(str(value))
print(''.join(result))
    
# -

#문자열 압축
s= 'ababcdcdababcdcd'
def solution(s):
    answer = len(s)
    for step in range(1,len(s)//2 + 1):
        compressed=''
        prev = s[0:step]
        count = 1
        for j in range(step,len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer


# +
#연구소 답은 나오는데..100퍼 시간초과다 이거

from itertools import combinations
import copy
n , m = 7 , 7


board = [[2, 0, 0, 0, 1, 1, 0],
 [0, 0, 1, 0, 1, 2, 0],
 [0, 1, 1, 0, 1, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 1],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0]]
temp = copy.deepcopy(board)
space = [(0, 1), (0, 2), (0, 3), (0, 6), (1, 0), (1, 1), (1, 3), (1, 6), (2, 0), (2, 3),
 (2, 5), (2, 6), (3, 0), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 0), (4, 1), (4, 2),
 (4, 3), (4, 4), (5, 0), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 0), (6, 2), (6, 3),
 (6, 4), (6, 5), (6, 6)]
virus = [[(0, 0), (1, 5)]]
# space = []
# virus = []
# for i in range(n):
#     i = list(map(int, input().split()))
#     board.append(i)
    
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append((i,j))
        if board[i][j] == 0:
            space.append((i,j))
dx = [-1, 0, 1, 0]            
dy = [0, 1, 0, -1]      
#바이러스 퍼지기
def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx>=0 and nx<n and ny>=0 and ny <m:

            if board[nx][ny] == 0:
                board[nx][ny] = 2
                dfs(nx,ny)

            
#벽 설치하기
cnt = 0
result = 0

for data in combinations(space, 3):
    cnt = 0
    for x,y in data:
        board[x][y] = 1
    for i in range(n):
        for j in range(m):
            if board[i][j]== 2:
                dfs(i,j)
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                cnt += 1
    for x,y in data:
        board[x][y] = 0           
    
    board = copy.deepcopy(temp)
     
    result = max(result ,cnt)
    
print(result)

# -

# #### 경쟁적 전염
#
# mysolution keyidea
#
# 1. 숫자가 있다면, 숫자 없다면 0으로 board 입력
# - 방법1. 보드 탐색 ->바이러스 숫자 탐색 -> 찾았다면 상하좌우 범위내에서 한칸 전염

# +
#뭔가 조금씩아쉬워..
from collections import deque

n,k = map(int, input().split())
graph = []
data = []
for i in ragne(n):
    graph.append(list(map(int,input().split())))
    
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j))
data.sort()
q = deque(data)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

target_s, target_x, target_y = map(int, intput().split())
# 핵심코드 bfs
while q:
    virus, s, x, y = q.popleft()
    
    if s == target_s:
        break
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx and nx <n and 0 <= ny and ny < n:
            
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))
# -




