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

# #### DFS

# +
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

def dfs (graph, v, visited):
    visited[v] = True
    print(v , end = ' ')
    for now in graph[v]:
        if not visited[now]:
            dfs(graph, now, visited)
dfs(graph, 1, visited)

# -

# #### Bfs

# +
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
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        
    
visited = [False]*9
bfs(graph, 1, visited)
# -

# #### 정렬 ( 선택정렬 )

# +
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            array[min_index] , array[j] = array[j] , array[min_index]
print(array)
# -

# #### 정렬( 삽입 정렬)

# +
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)
# -

# #### 정렬( 퀵 정렬 )

# +
# 방법 1
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right: 
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        quick_sort(array, start, right-1)
        quick_sort(array, right+1 , end)
    
quick_sort(array, 0, len(array) -1)
print(array)
        

# +
# 방법 2 ( 그냥 감탄 밖에 안나오네 코드가 그냥 )
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
# -

# #### 계수 정렬

# +
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * ( max(array) + 1 )

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print( i , end = ' ')
# -

# #### 파이썬 내장 함수
#

# +
array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

array.sort()
print(array)


# -

# #### 순차탐색
# - 정렬되지 않은 리스트에서 무엇인가를 찾아야 할때

# +
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1
print('생성할 원소 갯수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요')        
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다')
array = input().split()
print(sequential_search(n, target, array))


# -

# #### 이진탐색
# - 데이터가 정렬되어 있어야만 사용할 수 있음
# - 데이터 양이 많고 정렬이 되어 있는 상태일 때면 고려

# +
# 재귀로 구현한 이진 탐색
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1, end)
    
n , target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n -1 )
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)


# +
# 반복문으로 구현한 이진 탐색

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid -1
            
        else:
            
            start = mid + 1
            
    return None
    
n , target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n -1 )
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)


# -


