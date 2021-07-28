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
#순차탐색

def sequential_search(n, target, array):
    for i in range(n):
        
        if array[i]==target:
            return i + 1# 인덱스가 0부터 시작함으로 +1
print('생성할 원소 개수를 입력한 뒤 한칸 띄고 찾을 문자 입력')
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('생성할 개수만큼 문자열 입력. 구분은 띄어쓰기')
array = input().split()

print(sequential_search(n, target, array))


# +
# 재귀함수로 구현한 이진탐색

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n -1 )
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)


# +
# 반복문을 이용한 이진탐색 구현
def binary_search(array, target, start, end):
    while start <= end:
    
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        
        elif array[mid]> target:
            end = mid -1
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n -1 )
print(result)
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)
# -


