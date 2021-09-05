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

# ### 그리디

# +
#문제 1 큰수의 법칙 (my solution)

# N , M, K = map(int,input().split())
# data = list(map(int, input().split()))

N, M, K = 5, 8, 3
data = [2, 4, 5, 4, 6]
result = []
index = 0
data.sort(reverse = True)
while True:
    for _ in range(K):
        if len(result) <= M-1:
            result.append(data[index])
        else:
            break
    index += 1
    if len(result) >= M:
        break
print(result)      
sum = 0
for i in result:
    sum += i
print(sum)

# +
# 숫자 카드게임

n , m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
index = []
for i in range(n):
    index.append(min(data[i]))

print(max(index))


# +
# 1이 될때까지

n , k = map(int, input().split())
cnt = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n = int(n/k)
        cnt += 1
    else:
        n = n-1
        cnt += 1
print(cnt)
# -

# ### 구현

# +
# 문제 1 상하좌우
# I think it is really important code

n = int(input())
data = list(map(str, input().split()))

x, y = 1, 1
dx = [1,-1,0,0]
dy = [0,0,-1,1]
move = ['D','U','L','R']

for st in data:
    for i in range(4):
        if st == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny<1 or nx > n or ny > m:
        continue
    x, y = nx, ny
print(x, y)    
# -

# 문제 2 3이 포함된 시간 찾기 문제
h = 5
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print( count)

# +
# 문제 3 왕실나이트
axis = [ 'a', 'b','c','d','e','f','g','h']
columns = [1, 2, 3, 4, 5, 6, 7, 8]
txt = input()
board = [['']*8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        board[i][j]= axis[j]+str(columns[i])
dx = [2, 2, -2, -2,-1, -1, 1,1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

x, y = 0, 0

for i in range(8):
    for j in range(8):
        if txt == board[i][j]:
            x, y = i, j
cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if nx<8 and ny<8 and nx>0 and ny>0:
        cnt += 1
print(cnt)
            
# -

board[0][0][0]

# +
# 게임 개발 / 문제가 이해하기 어렵네
N, M = 4, 4
direction = [0, 3, 2, 1] #위(북) ,왼(서) , 아래(남) , 오른(동) // 반시계방향
x,y,direction = 1, 1, 0
map = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
d = [[0]*M for _ in range(N)]
d[x][y]=1

dx = [-1,0,1,0]
dy = [0,1,0,-1] #아래 , 위 , 오른쪽, 남쪽

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
count = 1
turn_time = 0
while True:
    
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    
    if d[nx][ny] ==0 and map[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    else : 
        turn_time += 1
        
    if turn_time == 4:
        nx = x -dx[direction]
        ny = x -dy[direction]
        
        if map[nx][ny] ==0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)


# -

# ### BFS/ DFS 구현 문풀

# +
# DFS

def dfs(graph, v, visited):
    if visited[v]:
        return
    visited[v] = True
    print(v , end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)
    
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

#bfs
from collections import deque
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
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

# +
#음료수 얼려먹기
n,m =4, 5
box = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    if x>=n or y>=m or x<=-1 or y <=-1:
        return False

    if box[x][y] == 0:
            
        box[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        
        return True
    return False
result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result += 1

print( result )


# +
# 부분 완전탐색 bsf 구현
#음료수 얼려먹기

from collections import deque

n,m =4, 5
box = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bsf(x,y):
    if box[x][y] == 1:
        return False
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and ny >=0 and nx<n and ny<m:
                if box[nx][ny] ==0:
                    box[nx][ny] = 1
                    q.append((nx,ny))
    return True
result = 0
for i in range(n):
    for j in range(m):
        if bsf(i,j)==True:
            result += 1

print( result )


# -

# 미로 탈출 (사실 완전 탐색이라는 부분에서 둘다 풀이가능)
from collections import deque
n,m = 5,6
board = [[1,0,1,0,1,0,],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs ( x, y ):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or ny< 0 or nx>=n or ny >=m:
                continue

            if board[nx][ny] == 0:
                continue

            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx,ny))
                
    return board[n-1][m-1]
print(bfs(0,0))

from collections import deque
# dfs에서 최단 경로이기 때문에 오른쪽과 아래쪽으로만
# 내려가도록 만든다
# 즉, ㅇ른쪽과 아래로만 해서 밑으로 가라는 의미
# 다만 첫번째 칸에서 중복으로 세기때문에 마지막에 -1 해줘야한다.
n,m = 5,6
board = [[1,0,1,0,1,0,],[1,1,1,1,1,1],[0,0,0,0,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
dx = [1,0]
dy = [0,1]
cnt = 0
def dsf(x,y):
    global cnt
    if x>=n or y>=m or x<=-1 or y<=-1:
        return
    if board[x][y] == 0:
        return
    
    if board[x][y] == 1:
        cnt+=1
        board[x][y] += cnt
        
        for i in range(2):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            dsf(nx,ny)
    return board[n-1][m-1] -1
print(dsf(0,0))
print(board)

[[1,0,1,0,1,0,],
 [1,1,1,1,1,1],
 [0,0,0,0,0,1],
 [1,1,1,1,1,1],
 [1,1,1,1,1,1]]


# ### 이진탐색
#
# - 핵심 아이디어
# - mid = (start + end)//2
# - target과 비교, mid가 크면 end = mid - 1 mid가 작으면 start = mid + 1
# - 종료 조건 : start > end (재귀) start <= end (반복문)

# +
#코드 구현
# 재귀로 구현하는 이진 탐색 코드
def binary_search(array, targe, start, end):
    if start > end:
        return
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    elif array[mid] >target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_serach(array, target, mid +1, end)
    
n, target = list(map(int, input().split()))
array = list(map(int, input().split))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)


# +
# 반복문으로 구현한 이진탐색

def binary_search(array, targe, start, end):
    while start <=end:
        mid = (start + end)//2
        
        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None


# +
# 부품찾기 binary_search 활용

# import sys

# input_data = sys.stdin.readline().rstrip()
def binary_search(array, target, start, end):
    if start > end:
        return
    mid = (start + end)//2
    
    if mid == target:
        return mid
    
    elif mid < target:
        return binary_search(array, target, mid + 1, end)
    
    else:
        return binary_search(array, target, start, mid -1)
    
# def binary_search(array, target, start, end):
#     while start<=end:
        
#         mid = (start + end)//2
        
#         if target == mid:
#             return mid
        
#         elif target< mid :
#             end = mid -1
#         else:
#             start = mid + 1
    
#     return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    
    result = binary_search(array, i, 0, n-1)
    
    if result != None:
        print('yes', end = ' ')
    else:
        print('No', end = ' ')

# +
# 계수정렬을 이용한 문제 풀이
n = int(input())
array = [0] * 10001

for i in input.split():
    array[i] = 1
m = int(input())

x = list(map(int, int(input().split())))

for i in x:
    if array[i] == 1:
        print('Yes', end = ' ')
    else:
        print('No', end = ' ')

# +
# 떡볶이 떡 만들기( 이진 탐색)
N = [19, 14, 10, 17]
M = 6

N.sort()
start = 0
end = N[-1]
result = 0
while (start <= end):
    total = 0
    mid = (start+end)//2
    for x in N:
        if x>mid:
            total += x -mid
    if total <M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
    
# -
#binary_search 구현
def binary_search(array, start, end, target):
    if start > end:
        return
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    if array[mid] < target:
        return binary_search(array, mid+1, end, target):
    if array[mid] > target:
        return binary_search(array, start, mid-1, target)
# 반복문 구현
def binary_search1(array, start, end, target):
    while start<=end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1


# # 다이나믹 프로그래밍

# 1로 만들기
n =int(input())
dp = [0]*(n+1)
div_lst = [2, 3, 5]
for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    for num in div_lst:
        if i % num == 0:
            dp[i] = min(dp[i],dp[i//num]+1)
print(dp)

# # 다익스트라

# +
import heapq
INF = int(1e9)
n,m = map(int, input().split())
start = int(input())
graph = [[]*m for _ in (n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    
distance = [INF] * (n+1)
def dijstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop()
        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[0]=cost
                heapq.heappush(q, (cost, i[0]))


# -
# # 그래프 이론

# #### 여행계획
# - 문제는 위상 정렬이 keypoint인데
# - 가능하냐를 묻는 거니까 조금 추가적으로 들어가네
# - 이거 엔지비 문제랑 비슷하네

# +
# n, m = map(int, input().split())
n , m = 5, 4
Sch = [[0, 1, 0, 1, 1], [1, 0, 1, 1, 0], 
       [0, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]]
parent = [0] * (n + 1)
# for _ in range(n):
#     Sch.append(list(map(int, input().split())))
# print(Sch)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

    

for i in range(n):
    for j in range(n):
        if Sch[i][j] == 1:
            union_parent(parent, i+1, j+1)
    
# print(graph)
# 계획을 세워 보면 여행지 리스트를 받고
# Sch 에서 1인지 확인 후 끝까지 가면 Yes 아니면 No
des = [2, 3, 4, 3]
det = True
for i in range(1, len(des)):
    if parent[des[i]] == parent[des[i-1]]:
        continue
    else:
        det = False
if det:
    print('Yes')
else:
    print("No")

print(parent)
# 그니까 이 문제를 어떻게 풀었냐면
# 핵심 아이디어는 같은 집합에 속해 있으면 어디든 갈수 있다는 거야
# 주어진 정보에 따라서 union을 진행하고
# 마지막에 체크해준거지 같은 집합에 속해 있는지를

# +
# 여행 계획 모법 답안
# 핵심 키 아이디어는 맞췄네
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n , m = 5, 4
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            graph[i+1].append(j+1)
            union_parent(parent, i+1, j+1)
            
plan = list(map(int, input().split()))

result = True

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if result:
    print('Yes')
else:
    print('No')
    
# 핵심 아이디어, 핵심 코드 정확히 일치하네

# +
# 탑승구
# 이렇게 풀어볼까
# 탑승구를 각각의 개체로 생각한다음에
# 도킹 가능한 애들끼리 하나의 집합을 형성하고
# 그 집합 개수와 비행기의 개수를 비교해서 출력 개수를 잡아보면 되겠네

g = int(input())
p = int(input())

parent = [0]*(g+1)

for i in range(1,g+1):
    parent[i] = i
    
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0        

# 이 아이디어 재밌네
# 근데 이거 틀렸어 왜냐면 4 가 들어가면 처음 데이터면 4 랑 3 이 유니온되는데
# 3은 서로소 집합에 들어가면 안되
# 3은 도킹 가능한지 모르거든
# 웃긴 건 뭐냐면
# 1 1 4 로 들어 갈 수 있는데
# 그렇게 들어가면 바로 나와서 답이 틀리거든
# 책이 틀리기도 하네 ㅋㅋ

# 모법 답안 이러고 제시된건데, 틀렸어..
# for _ in range(p):
#     data = find_parent(parent, int(input()))
#     if data == 0:
#         break
#     union_parent(parent, data, data-1)
#     result += 1

print(result)
#이것도 될것 같은데....
#오히려 이게 더 맞는거 같아
pd = list()     
for a in range(p):
    i = int(input()) 
    if i not in pd:
        pd.append(i)

if p <= len(pd):
    print(p)
else:
    print(len(pd))
# -






