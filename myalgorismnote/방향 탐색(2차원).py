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
# +
graph = [[0, 0, 1], [0, 1, 0], [1, 0, 1]]
n, m = 3,3

def dfs(x, y):
    
    if x<= -1 or x>=n or y<=-1 or y>=m:
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
