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


