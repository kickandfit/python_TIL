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

# #### 재귀함수, 스택, 큐(feat.우선 순위 큐)
#
# - 큐는 collections 의 deque를 활용
# - 우선 순위 큐는 heapq을 활용

# +
def f(n):
    if n<1: 
        return
    f(n-1) 
    f(n-1)
    f(n-1) 

# 가지는 의미만 가지고 가면된다. 2 번 호출하면, 가지가 2개씩늘어난다. 근데 결국에는 그 '모든 가지를 방문'한다
# 재귀를 쓰면 비효율적이다. (메모리 조건, 시간 조건) 


# +
# 큐 자료구조
from collections import deque

queue = deque([1, 2, 3, 4, 5])
print(queue)
queue.append(6)
print(queue)
queue.appendleft(0)
print(queue)
b = queue.pop() #6이라는 값을 가진다

a =queue.popleft() # 0값을 가지고 있다
print( a, b)

# +
# 우선순위 큐 : 작은 순으로 배열
# 가치에 따라서 배열해서 넣는다?
# 파이썬에서는 작은 값을 기준으로 넣어요 최소 힙.
import heapq

data = [2,3,1,5,6,8,0,2]

h= []
result = []
for value in data:
    heapq.heappush(h, value)
# h에 들어가는 것만으로는 의미갖지 않아요
# 근데 h에서 빼오면 , 작은 순으로 정렬이 되요.

for i in range(len(h)):
    result.append(heapq.heappop(h))
result



# +
# 큰순서대로
import heapq

data = [2,3,1,5,6,8,0,2]

h= []
result = []
for value in data:
    heapq.heappush(h, -value)
# h에 들어가는 것만으로는 의미갖지 않아요
# 근데 h에서 빼오면 , 작은 순으로 정렬이 되요.

for i in range(len(h)):
    result.append(-heapq.heappop(h))
result

# -

# #### dfs, bfs
# - dfs는 스택 , 재귀함수를 이용한다.
# - bfs는 큐 활용, 반복문을 이용한다.

# ####  keyidea(dfs)
#     1.탐색 시작 노드를 스택에 넣고 방문 처리한다
#     2. 스택의 최상단 노드에서 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다
#     3. 2번의 과정을 반복한다

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
visited = [False] * (8+1)
# Fasle 면 방문을 하지 않은 놈, True 방문을 했다를 의미함
def dfs(graph, s, visited):
    visited[s] = True
    print( s, end = ' ')
    for i in graph[s]:
        if not visited[i]: # if 문이 작동할라면 안에 조건이 참이어야 되죠
            # visited 초기에 False 들어가있어요
            # not False = True 가 되니까, 방문하지 않았다면 이라는 뜻가지게 되요
            # 조건문이 True이면은 조건문 아래 코드를 실행하지 않을꺼에요. 즉 방문하지 않았을때만 실행할거에요
            dfs(graph, i, visited)
dfs(graph, 1, visited)

# #### keyidea(bfs)
#     1. 탐색 시작 노드를 큐에 놓고 방문처리할거에요
#     2. 큐에서 노드를 꺼내서 인접 노드 확인 후 방문 하지 않은 놈을 방문 처리
#     3, 더이상 수행할 수 없을 때가지

from collections import deque
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
visited =[False] * 9
visited
def bfs(graph, visited, s):
    que = deque([s])# deque( 변수 ) 변수는 iterable한 객체가 들어가야되는데, iterable, list구조, 튜플
    #deque({s})? 인덱싱을 못해요.
    visited[s] = True
    while que: # que 안에 값이 있으면 True, 없으면 False, while문은 que가 다 빌때까지 해라라는 의미를 가짐
        v = que.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i]= True
                que.append(i)
bfs(graph, visited, 1)


# #### dfs, bfs
#
# - 완전 탐색 문제에 사용이 되요. 모든 노드를 다 방문해야되는 상황에서 사용될 수 있다
# - 문제 상황을 그래프로 나타낼 수 있을 때, 이차원 배열이 나왔을때

# ####  실전문제
#
# #### 문제1
# n * m 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리, 상하좌우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 이때얼음 틀의 모양이 주어졌을 떄 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 다음의 4 *5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.
#
# 입력 조건 : 첫번째 줄에 얼음 틀의 세로길이 n과 가로 길이 m이 주어진다(1<=N , M<=1000)
# 두번 째 줄부터 n + 1번째 줄까지 얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지않은 부분은 1이다
#
# 출력 조건 : 한 번에 만들 수 있는 아이스크림의 개수를 출력한다
# - 입력
# - 4 5
# - 00110
# - 00011
# - 11111
# - 00000
#
#
# - 출력 : 3
#
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

# ####  문제 1번 풀이 keyidea
#
#     1. 주어진 입력조건을 받아보자
#     1-1. 입력받은 정보를 활용해서 아이스크림 통을 생성하자
#     2. 1이라는 것은 방문했다라고 생각하고, 0이라는 부분은 방문을 하지 않았다라고 생각을 하자 (visited를 안쓰겠다)
#         - 방문을 하면 그 값은 0일 것이다.
#         - 아 그러면 0이라는 부분을 1로 바꿔버리겠다
#         - 가정은 0이면 노방문 1이면 방문 이 되겠다
#     3. dfs 로 구분을 할껀데 0부분만 떼와보자
#     4. 떼온 부분에 음료수를 채우자 그리고 그 채운 음료수 개수를 세보자
#  

# +
n, m  = map(int, input().split()) # n행 m열 정보 받기
graph = [] #아이스크림 통
for i in range(n):
    graph.append(list(map(int, input())))
def dfs(x,y):
    # 범위를 벗어나게 되면 종료해라
    if x>=n or y>=m or x<=-1 or y<=-1:
        return False # 덩어리 구문 하기위해서 True/ False를 쓸꺼에요
#     print(x,y)
    # 노드를 방문하고, 방문하지 않았다면, 연결된 노드들 확인하고, 다시 꺼내서 연결된 노드 방문하고, 인접노드 확인하고
    if graph[x][y] == 0:
        #방문처리하기
        graph[x][y] = 1
        # 인접노드 확인
        dfs(x-1,y) #현재 기준으로 위로 다 탐색해봐( 방문 했는지 안했는지 체크하고 안했으면 방문 처리해)
        dfs(x+1,y) #현재 기준으로 아래로 가봐
        dfs(x,y-1) #현재 기준으로 왼쪽으로 가봐
        dfs(x,y+1) #현재 기준으로 오른쪽으로 가봐
        
        return True

    return False


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
            print(count, i, j) # i j 가 처음 방문 했을 때 그 덩어리가 0 즉 방문하지 않았던 위치값
print(count)

# +
dfs(0,0) -> True
11110
11111
11111
00000

True 

dfs(0,1)
11110
11111
11111
00000
True False 

dfs(0, 2)
11110
11111
11111
00000
True False False

dfs(0, 3)
11110
11111
11111
00000
True False False False

dfs(0,4)
11111
11111
11111
00000
True False False False True


True  False False False True
False False False False False
False False False False False
False False False False False

dfs(3,0)

True

11111
11111
11111
11111

True  False False False True
False False False False False
False False False False False
False False False False False
True  False False False False


# +
# bfs 구현 문제 1번
from collections import deque

def bfs (x, y):
    
    if x<=-1 or y<=-1 or x>=n or x>=m:
        return False
    if graph[x][y]== 1:
        return False
    que = deque([[x,y]])
    graph[x][y] = 1
    while que:
        x, y = que.popleft()
        if x+1 < n:
            x += 1
            if graph[x][y] == 0:
                graph[x][y] = 1
                que.append([x,y])
            x -= 1
        if y+1 < m:
            y += 1
            if graph[x][y] == 0:
                graph[x][y] = 1
                que.append([x,y])
            y -= 1
    return True
    


# -

# #### 다음 시간 다이나믹 프로그래밍
#
# - 재귀 확실 복습하셔야되요
# - 탑다운 : 메모이제션 , 바텀업 : DP 테이블
# - 다이나믹 프로그래밍의 목적 : 중복된 계산을 줄이기 위함
#     - 사용하는 경우 : 큰 쿤제를 작은 문제로 나누고, 작은 문제로 푼 답이 큰 문제로 풀 떄 변하지 않는 경우

# ####  call by assignment
#
# - int, str, boolen, tuple 등은 call by value 형식으로 받아옴
# - list, dict 등은 call by referece 형식으로 받아옴
# - 즉 Mutable 갑과 immutable 값이 존재하는데, mutable은 copy를 해줘야만, 따로 메모리에 저장 되기 때문에 서로의 간섭에서 벗어날 수 있음
# - immutable은 서로 간섭하지 않음
# - 사용자가 만든 class는 기본적으로 mutable임
# - 때문에 판다스, 넘파이 등의 형식은 mutable 이라 똑같은 데이터셋, 배열 등을 활용하고 싶을 때는 copy해줘야함
# - 또한 mutable의 mutable이 있을 경우, deep copy를 해줘야함

# #### 문제 4번 풀이 idea(왤케 어렵냐..이걸 50분이라..)
#
#     1. 문제 조건 입력받기
#     2. 움직임 구현하기(회전으로 움직임 + 직선 움직임) ( 조건 : 회전하는 축 대각선기준 1 이 있으면 불가)
#     3. 움직임 한번에 1초
#     4. bfs 구현해서 가장 마지막칸에 +1로 구현해보자

# ####  다이나믹 프로그래밍 문제 1.
#
# 정수 x가 주어질 떄 정수 x 에 사용할 수 있는 연산은 다음과 같이 4가지다. x가 5로 나누어 떨어지면, 5로 나눈다. x가 3으로 나누어 떨어지면 3으로 나눈다 2로 나누어 떨어지면 2로 나눈다. x 에서 1을 뺀다.
#
# 정수 x가 주어졌을때, 4개의 연산을 적절히 사용해서 1로 만들려고 한다. 연산을 사용하는 최솟값을 출력해라

n = 267
d = [0]*(n+1)
for i in range(2, n+1):
    d[i] = d[i-1] + 1
    
    if i % 2== 0 :
        d[i] = min(d[i],d[i//2]+1)
    if i % 3== 0 :
        d[i] = min(d[i],d[i//3]+1)
    if i % 5== 0 :
        d[i] = min(d[i],d[i//5]+1)
print(d[n])
cnt = 0
def d(n):
    global cnt
    
    if n <=2:
        return 1
    
    for i in (5, 3, 2):
        if n%i == 0:
            d(int(n/i))
            cnt += 1
            break
        else : 
            d(n-1)
            cnt += 1
            break
    return cnt
print(d(n))


# +
# 피보나치 구현 및 다이나믹 프로그래밍
# 피보나치 수열 구현
def fibo(n):
    if n ==1 or n ==2:
        return 1
    return fibo(n-1) + fibo(n-2)
    
# 다이나믹 프로그래밍 적용
d = [0]*(n+1)
def fibo_D(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo_D[n-1]+fibo_D[n-2]
    return d[n]
print(fibo_D(6))
    
# -



def d(n):
    print(n)
    if n <=2:
        return 1
    d(n-1)
d(10)

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
visited=[False]*9
def dfs_1(graph, v, visited):
    visited[v] = True
    print(v)
    for i in graph[v]:
        if not visited[i]:
            dfs_1(graph,i,visited)
            break # 1path의 역할을 하겠네 최대 깊이 1 path
dfs_1(graph ,1 ,visited)


