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
#문자열 빠르게 입력받기

import sys

input_data = sys.stdin.readline().rstrip()

print(input_data)

# +
# 간단하지만 느린 다익스트라알고리즘
import sys
# input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수 입력받기
n, m  = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
#방문처리
visited = [False]*(n+1)
#최단 거리 테이블 모두 초기화
distance = [INF] *(n+1)

for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    # 초기 노드에서 이어진 노드와 코스트 업데이트
    
    for j in graph[start]:
        distance[j[0]] = j[1]
        
    
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        visited[now] = True
        
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost< distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INF)라고 풀력
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

# +
# 우선순위큐를 활용한 다익스트라 알고리즘
import sys
import heapq
#input = sys.stdin.readline
INF = int(1e9)

n , m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼낵
        dist, now = heapq.heappop(q)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # 우선순위 큐를 사용했기 때문에 가능하다
        # 앞에서 이미 처리해 테이블을 갱신한 상태다
        # 때문에 다음 순위에서는 무조건 cost가 클수 밖에 없다
        if distance[now] < dist: # 이 부분이 약간 이해가 안가네..
            continue
        
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INF)라고 풀력
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

# +
# 폴로이드 워셜 알고리즘
INF = int(1e9)

n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for i in range(n+1)]

# 자기에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 생각
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
#수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우, 무한이라고 출력
        if graph[a][b] == INF:
            print('INF')
        else:
            print(graph[a][b], end =' ')
    print()
# -


