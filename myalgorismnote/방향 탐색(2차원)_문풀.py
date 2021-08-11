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

# #### 방향 탐색 설정시 중요한점
# - 여러방향 동시 탐색을 재귀로 하려고 한다면 추가 종료조건이 필요함
# - 그렇지 않으면 무한루프가됨
# - 종료 조건은 방문 처리를 해주면 됨
# - if move(x+1, y, 0), move(x-1,y,0)을 동시에 돌려주게되면 방문 처리해야함


# +
# 한 방향 탐색 알고리즘
def move(x,y, i):
    if x>10 or y>10 or x<=-1 or y<=-1:
        return
    print(x,y)
    # 아래로 탐색
    if i == 0:
        return move(x+1,y , 0)
    # 오른족 탐색
    elif i == 1:
        return move(x, y+1, 1)
    # 위로 탐색
    elif i == 2:
        return move(x-1, y, 2)
    # 왼쪽 탐색
    elif i == 3:
        return move(x, y-1, 3)
    # 대각선 탐색(우상)
    elif i == 4:
        return move(x+1, y+1, 4)
    # 대각선 탐색(좌하)
    else:
        return move(x-1, y-1, 5)

# for dir in range(5):
#     move(4,4,dir)
move(0,0, 1)
# +
graph = [[0, 0, 1], [0, 1, 0], [1, 0, 1]]
n, m = 3,3

def dfs(x, y):
    
    if x<= -1 or x>n or y<=-1 or y>m:
        return False
    
    # 이부분이 방문 여부 묻고 처리하는 부분
    if graph[x][y] ==0:
        
        #방문 처리 하고,
        graph[x][y] = 1
        
        # 탐색해라
        dfs(x-1, y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


# -

# for 문과 재귀를 이용한 dfs(삼성전자 바이러스 핵심코드)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n,m =7, 7
def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx<n and nx>=0 and ny < m and ny>=0:
            if board[nx][ny]==0:
                board[nx][ny] = 2
                dfs(nx,ny)


# +
# 한칸이 아니라 두칸으로 움직일 때, 회전이 포함될때

# keyidea1 
# set으로 관리하면 q에 집입할때 순열느낌으로 들어감
# 때문에 방문 처리시 중복을 거를 수 있음
# 위치 정보를 인덱싱 하기 위해
# pos1, pos2 로 관리하기 전 pos를 리스트화 해줘야함
pos = {(1,1),(1,2)} 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_next_pos(pos,board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x,pos2_y = pos[0][0],pos[0][1],pos[1][0],pos[1][1]
    for i in range(4):
        pos1_next_x,pos1_next_y,pos2_next_x,pos2_next_y = pos1_x+dx[i], pos1_y+dy[i],pos2_x+dx[i], pos2_y+dy[i]
        
        #이동가능 조건 파악
        if board[pos1_next_x][pos1_next_y]==0 and board[pos2_next_x][pos2_next_y]==0:
            next_pos.append({(pos1_next_x,pos1_next_y),(pos2_next_x,pos2_next_y)})
    
    #keyidea3: 회전처리
    # 가로로 놓여져 있다면 조건 만족시 회전
    if pos1_x==pos2_x:
        for i in [-1, 1]: # 이 -1, 1이 핵심이다
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})


# -

# #### 장애물이나 사물 배치시 고려해야할 사항
#
# - 완전 탐색을 진행할 것이라면, 10000이하의 수에 대해 진행해라
#   ( 대략 40이하의 수에 대해 진행할것 )

# +
# 1차원 회전 밑 방향전환 ( 2차원 맵에서)
# 이코드는 돌아가지 않음 핵심 부분만 정리하는 것

# 0, 1, 2, 3 / 북 , 동, 남 ,서 로 정의
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

dx = [-1,0,1,0]
dy = [0,1,0,-1] # 북, 동, 남, 서로 맞춰줌

turn_left()
nx = x + dx[direction]
ny = y + dy[direction] # 왼쪽으로 돌고 앞으로이동할 위치값 설정 / cf) 뒤로 이동은 ny = y - dy[direction]

# 조건 만족 시 이동
if d[nx][ny] ==0 and map[nx][ny] == 0:
    d[nx][ny] = 1 # 방문처리
    x = nx # x 이동
    y = ny # y 이동
    # 조건 탐색 후 이동 가능하면, 이동



