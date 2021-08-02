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
#우선 순위 큐를 활용한 다익스라 알고리즘 구현
# n개의 노드 , m 개의 간선
import heapq
n , m = 6, 11
# graph = [[] for _ in range(n+1)]
graph = [[],
 [(2, 2), (3, 5), (4, 1)],
 [(3, 3), (4, 2)],
 [(2, 3), (6, 5)],
 [(3, 3), (5, 1)],
 [(3, 1), (6, 2)],
 []]
# 스타트 노드 입력받기
start = 1
INF = int(1e9)
distance = [INF]*(n+1)
# for _ in range(m):
#     a , b, c = map(int, input().split())
#     graph[a].append((b,c))
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # 시작 노드를 넣는데 비용이 0이다
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        # 방문한적 있으면 무시
        if distance[now]< dist:
            continue
        for  i in graph[now]:
            cost = i[1]+ dist
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


# -

#one more
def dijkstra(start):
    q=[]
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist , now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))





