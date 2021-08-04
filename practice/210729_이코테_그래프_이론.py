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
#기본적인 서로소 집합 알고리즘 구현

def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을때 까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0]*(v+1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i
    
#union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    
#각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end = ' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end= ' ')
print()

#부모 테이블 내용 출력
print('부모 테이블: ', end = ' ')
for i in range(1, v+1):
    print(parent[i], end = ' ')
    


# +
# 고찰
def find_parent(parent, x):
    # 야, parent table 불러오고 x가져와봐
    if parent[x] != x : # parent 테이블에 표시된 값이 x야?
        # 그럼 parent테이블 블러오는데, x 값을 업데이트시켜
        # parent[x]는 연결된 놈을 뜻하니까  그 놈이 끝까지 가서
        # 만날때까지 불러오고 불러옴과 동시에 넌 종료해
        return find_parent(parent, parent[x])
    #같어? 그러면 그 비교한 값이 니 루트노드 값이야
    return x

def union_parent(parent, a, b):
    # 야 a,b 부모가 누구야?
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    #합칠꺼라며, 그럼 부모끼리 비교해
    # 큰놈의 부모가 작은놈이야 알겠어?
    if a>b:
        parent[a] = b
    else:
        parent[b] = a


# -

# 경로압축
def find_parent(parent,x):
    if parent[x] != x:
        # 아 일일이 경로 찾기 귀찮어
        # 그냥 루트 노드만 데리구와 그냥 경로 필요없이
        # 다 그냥 루트노드 가리켜 알겠어?
        # if 종료 조건 만족할라면 , 부모까지 올라가야되자너?
        # 올라가서 그넘을 그냥 처음 parent[x]에 넣어
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# +
#review dfs
def dfs(graph, v, visited):
    visited[v]= True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
#             return dfs(graph, i, visited) # 깊이로 하나의 경로 탐색
            dfs(graph, i, visited) # 깊이로 다 탐색
        
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
# -
# #### 신장트리
# - 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
#
# ##### 크루스칼 알고리즘(최소 신장트리 알고리즘)
# - 다양한 문제 상황에서 가능한 최소한의 비용으로 신장 트리를 찾아야할때
#
# - keyidea(크루스칼 알고리즘 - 그리디의 일종)
#     1. 간선 데이터를 비용에 따라 오름차순으로 정렬
#     2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
#         - 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다
#         - 사이클이 발생하는 경우 최소 신장트리에 포함시키지 않는다
#     3. 모든 간선에 대하여 2번의 과정을 반복한다


# +
# 크루스칼 알고리즘

# 특정 원소 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a>b:
        parent[a] = b
    else b>a:
        parent[b] = a
#노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0]*(v+1)

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이상에서, 부모를 자기 자신으로 초기화
for i in ragne(1, v+1):
    parent[i] = i
# 모든 간선에 대한 정보 입력받기

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += cost


# -

# #### 서로소 집합을 활용한 사이클 판별
#
# - 간선에 방향성이 없는 무향 그래프에 대해서만 적용가능
#     1. 각 간선을 확인하며 두 노드의 루투 노드를 확인한다.
#         - 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산
#         - 루트노드가 서로 같다면 사이클이 발생
#     2. 그래프에 포함되어 있는 모든 간선에 대하여 반복

# +
# 서로소 집합을 활용한 사이클 판별 소스코드

def find_parent(parent , x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        
    return parent[x]


def union_parent(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a>b:
        parent[a] = b
    else b>a:
        parent[b] = a
#노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0]*(v+1)

# 부모 테이상에서, 부모를 자기 자신으로 초기화
for i in ragne(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    #사이클이 발생한 경우 종료
    if find_parent(parent,a)  == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)
# -

# #### 위상 정렬
#
# - 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 고자할때 사용
#     ex) 선수 과목을 고려한 학습 순서 설정
# - 진입 차수 : 들어오는 간선의 개수
#
# keyidea(위상 정렬)
#
# 1. 진입 차수가 0인 노드를 큐에 넣는다
# 2. 큐가 빌 때까지 다음의 과정을 반복한다
#
# - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
# - 새롭게 진입차가 0이 된 노드를 큐에 넣는다
#
#
# 참고 : 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단

# +
from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e= map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0]*(v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    
    # 진입차수 1 증가
    indegree[b] += 1
    
# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i]==0:
            q.append(i)
    
    # 큐가 빌때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        
        now = q.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1
            
            if indegree[i] ==0:
                q.append(i)
for i in result:
    print(i, end = ' ')


# -
# 재귀로 보는 트리 : 전위 순위
def a(n):
    if n<1:
        return 1
    print(n, end = ' ')
    a(n-1)
    a(n-1)
    a(n-1)
a(3)


# ![image.png](attachment:image.png)

# 재귀로 보는 트리 : 중위 순회 -1
# 코드의 위치에 따라 탐색 순서가 달라짐 ( print 위치 2 따라서 아래 한개 탐색 후 위 찍고 다시 아래 세개)
def a(n):
    if n<1:
        return 1
    
    a(n-1)
    print(n, end = ' ')
    a(n-1)
    a(n-1)
    a(n-1)
a(4)


# ![image.png](attachment:image.png)

# 재귀로 보는 트리 : 중위 순회 -2
# 코드의 위치에 따라 탐색 순서가 달라짐 ( print 위치 3 따라서 아래 두개 탐색 후 위 찍고 다시 아래 두개)
def a(n):
    if n<1:
        return 1
    
    a(n-1)
    a(n-1)
    print(n, end = ' ')
    a(n-1)
    a(n-1)
a(4)


# ![image.png](attachment:image.png)

# +
#재귀로 보는 회귀 : 후위순회
def a(n):
    if n<1:
        return 1
    
    a(n-1)
    a(n-1)
    a(n-1)
    a(n-1)
    print(n, end = ' ')
    
a(4)
# -

# ![image.png](attachment:image.png)

# +
#재귀로 보는 순회 응용
cnt = 0
def a(n):
    global cnt
    print(n, end = ' ')
    if n<=1: # <= 와 < 의 차이 내가 코드를 작성하고 위에서 종료조건 위에서 빠져나오게 할때는 =을 써줘야함
        cnt += 1
        return cnt
    
    a(n-1)
    a(n-1)
    return a(n-1)

print(a(3))

# +
#재귀로 보는 순회 응용2
cnt = 0
def a(n):
    global cnt
    print(n, end = ' ')
    if n<1: # <= 와 < 의 차이 내가 코드를 작성하고 종료조건 아래에서 빠져나오게 할때는 =을 빼줘야함. 
            #그러나 메모리의 비효율성이 발생함 ( 바로 위의 코드와 결과는 같으나, 사실은 0까지 메모리가 부여됨)
            #낭비된 메모리 개수 =27(cnt개)
        cnt += 1
        return cnt
    
    a(n-1)
    a(n-1)
    return a(n-1)

print(a(3))
# -

#재귀로 보는 순회 응용3
cnt = 0
def a(n):
    global cnt
    print(n, end = ' ')
    if n<1: # <= 와 < 의 차이 내가 코드를 작성하고 종료조건 아래에서 빠져나오게 할때는 =을 빼줘야함. 
            #그러나 메모리의 비효율성이 발생함 ( 바로 위의 코드와 결과는 같으나, 사실은 0까지 메모리가 부여됨)
            #낭비된 메모리 개수 =27(cnt개)
            # 낭비된 메모리수 a(n-1)개의 호출 개수를 n개라 하면 n의 3승개
        cnt += 1
        return cnt
    
    a(n-1)
    a(n-1)
    a(n-1)
    return a(n-1)
print(a(3))

#재귀로 보는 순회 응용4
cnt = 0
def a(n):
    global cnt
    
    if n<1: # <= 와 < 의 차이 내가 코드를 작성하고 종료조건 아래에서 빠져나오게 할때는 =을 빼줘야함. 
            #그러나 메모리의 비효율성이 발생함 ( 바로 위의 코드와 결과는 같으나, 사실은 0까지 메모리가 부여됨)
            #낭비된 메모리 개수 =27(cnt개)
        cnt += 1
        return 1
    print(n, end = ' ')
#     a(n-1)
#     a(n-1)
#     a(n-1)
    return a(n-1) + a(n-1)+ a(n-1)# 이건 규칙모르겠다 솔직히
print(a(3))

1 36 378 2080 // 6*6 / 6*7*9 / 10*4*4*13
