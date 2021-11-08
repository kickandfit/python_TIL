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
n,m,k = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

smell = [[[0,0]] * n for _ in range(n)]

priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

# +
dx, dy = [-1,1, 0 ,0], [0, 0, -1, 1]

def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]
                
def move():
    new_array = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if array[x][y] != 0:
                direction = directions[array[x][y]-1]
                found = False
                
                for index in range(4):
                    nx = x + dx[priorities[array[x][y]-1][direction - 1][index]-1]
                    ny = y + dy[priorities[array[x][y]-1][direction - 1][index]-1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0:
                            directions[array[x][y]-1] = priorities[array[x][y]-1][direction-1][index]
                        
                        if new_array[nx][ny] == 0:
                            new_array[nx][ny] = array[x][y]
                        else:
                            new_array[nx][ny] = min(new_array[nx][ny],array[x][y])
                        found = True
                        break
                    if found:
                        continue
                    for index in range(4):
                        nx = x + dx[priorities[array[x][y]-1][direction - 1][index]-1]
                        ny = y + dy[priorities[array[x][y]-1][direction - 1][index]-1]
                        if 0 <= nx and nx < n and 0 <= ny and ny < n:
                            if smell[nx][ny][0] == array[x][y]:
                                directions[array[x][y]-1] = priorities[array[x][y]-1][direction-1][index]
                            new_array[nx][ny] = array[x][y]
                            break
    return new_array
time = 0
while True:
    update_smell()
    new_array = move()
    array = new_array
    time += 1
    
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check:
        print(time)
        break
    
    if time >= 1000:
        print(-1)
        break
# 어디가 틀린지 모르겠다 ㅎㅎ


# +
# 모험가 길드 - my sol
from collections import deque

people = [4, 5, 3, 2 ,3, 2, 1, 1, 1]
lst = deque()
temp = sorted(people)
temp.reverse()
cnt = 0
lst = deque(temp)
print(lst)
while lst:
    for _ in range(lst[0]):
        lst.popleft()
    cnt += 1
print(cnt)

# example
people.sort()
result = 0
count = 0
for i in people:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)

# +
# 뱀

n = int(input())
k = int(input())
data = [[0]* (n+1) for _ in range(n+1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1
    
l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x), c))
    
dx = [0, 1, 0 , -1] # 동 남 서 북
dy = [1, 0, -1, 0]

# 이 아이디어 재밌네 ( dx, dy를 방향을 주고 나머지를 돌린다라..)
def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else :
        direction = (direction + 1) % 4
    
    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보 ( 꼬리가 앞쪽 )
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if 1<= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny]!=2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx,ny))
                px,py = q.pop(0)
                data[px][py] = 0
            
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time
print(simulate())

# +
# 특정 거리의 도시 찾기
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range((n+1))]
visited = [False]*(n+1)
distance = [-1] * (n+1)
distance[x] = 0
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
check = False
for i in range(n+1) :
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)

print(distance)
# -


