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
# dfs 구현
def dfs(graph, v, visited):
    
    visited[v] = True
    print(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]  
visited = [False]*9
dfs(graph, 1, visited)

# +
# bfs 구현
from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v)
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]  
visited = [False]*9
bfs(graph, 1, visited)
# -

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
graph

# +
# 모범 답안 dfs 구현
graph = [[0, 0, 1], [0, 1, 0], [1, 0, 1]]
n, m = 3,3

def dfs(x, y):
    
    if x<= -1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y] ==0:
        
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1
            print(result, i ,j)
print(result)


# +
from collections import deque

graph = [[0, 0, 1], [0, 1, 0], [1, 0, 1]]
n, m = 3,3

result = 0

def bfs(x,y):
    if graph[x][y] == 1:
        return False
    # 방문하지 않은 상황이면 que에 넣어
    que = deque([[x,y]])
    while que:
        x, y = que.popleft()
        #방문 처리
#         print(graph[x][y],'-------',x,y)
        if graph[x][y] == 0:
            graph[x][y] = 1
            #연결된 다른 노드 확인
            if x+1<n:
                x = x+1
                que.append([x,y])
                x = x-1 #다시 제자리로 돌려야함
                
            if y+1<m:
                y = y+1
                que.append([x,y])
                y = y-1 
    return True

for i in range(n):
    for j in range(m):
        if bfs(i,j) == True:
            result +=1
            print(result, i ,j)
print(result)
        
    
        


# +
from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or ny< 0 or nx>=n or ny>=m:
                continue
                
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
# -

graph

# #### 문제1
# n * m 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리, 상하좌우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 이때얼음 틀의 모양이 주어졌을 떄 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 다음의 4 *5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.
#
# 입력 조건 : 첫번째 줄에 얼음 틀의 세로길이 n과 가로 길이 m이 주어진다(1<=N , M<=1000)
# 두번 째 줄부터 n + 1번째 줄까지 얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지않은 부분은 1이다
#
# 출력 조건 : 한 번에 만들 수 있는 아이스크림의 개수를 출력한다
# - 입력
# - 00110
# - 00011
# - 11111
# - 00000
# - 출력 : 3
# #### 문제2
# 동빈이는 N * M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 동빈이의 위치는 (1,1) 이고 미로의 출구는 (N,M)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있다. 이떄 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시한다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
#
# 입력조건 : 첫째 줄에 N,M(4<=N, M<=200) 이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수 (0 or 1)로 미로의 정보가 주어집니다. 각각의 수들은 공백 없이 붙어서 입력으로 제시됩니다. 또한 시작 칸과 마지막 칸은 항상 1이다.
#
# 출력 조건 : 첫째 줄에 최소 이동 칸의 개수를 출력해라
# ex)
# - 입력
# - 5 6
# - 101010
# - 111111
# - 000001
# - 111111
# - 111111
#
# - 출력 = 10
#
#
# #### 문제3
# - https://www.acmicpc.net/problem/18428
# - 제한 시간 60분
#
#
# #### 문제4
# - https://programmers.co.kr/learn/courses/30/lessons/60063
# - 제한 시간 50분

# +
# 문제 3
from itertools import combinations
n = int(input())
board = []
teachers = []
spaces = []
for i in range(n):
    board.append(list(map(str, input().split())))
    for j in range(n):
        if board[i][j] == 't':
            teachers.append((i,j))
        # obstacle을 설치할 수 있는 공간 저장
        if board[i][j] == 'x':
            spaces.append((i,j))

        
def look(board,x,y):
    if board[x][y] == 't':
        #왼쪽 탐색
        if direction == 0:
            while y >=0:
                y -= 1

                if board[x][y] == s:
                    return True
                if board[x][y] == o:
                    return False
            
         #오른쪽 탐색
        if direction == 1:
            while y < n:
                y +=1
                if board[x][y] == 's':
                    return True
                if board[x][y] == 'o':
                    return False
        #위쪽탐색
        if direction == 2:
            while x>=0:
                x -=1
                if board[x][y] == 's':
                    return True
                if board[x][y] == 'o':
                    return False
        #아래 탐색
        if direction == 3:
            while x<n:
                x +=1
                if board[x][y] == 's':
                    return True
                if board[x][y] == 'o':
                    return False

def process():
    
    for x,y in teacher:
        for i in range(4):
            if look(x,y,i):
                return True
        return False
    
    find = False
    
    for data in combinations(spaces, 3):
        
        for x,y in data:
            board[x][y] = 'o'
        
        if not process():
            
            find = True
            break
            
        for x,y in data:
            board[x][y] = 'x'
            
            
if find:
    print('YES')

else:
    print('NO')
# -












