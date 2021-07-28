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

#선택 정렬 구현
data = [7, 2, 1 ,6 ,3, 5, 4, 9 ,8, 0]
for i in range(len(data)):
    min_index = i
    for j in range(i+1, len(data)):
        if data[min_index] > data[j]:
            min_index = j
    data[i], data[min_index] = data[min_index] , data[i]
print(data)

# 삽입 정렬 / 7.28
data = [7, 2, 1 ,6 ,3, 5, 4, 9 ,8, 0]
for i in range(1,len(data)):
    for j in range(i, 0 , -1):
        
        if data[j] < data [j-1]:
            data[j], data[j-1] = data[j-1], data[j]
        else:
            break

# +
#퀵정렬 구형/ 7.28
array = [7, 2, 1 ,6 ,3, 5, 4, 9 ,8, 0]
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start +1
    right = end
    
    while left <= right:
        
        while array[left]<= array[pivot] and left<=end :
            left += 1
            
        while right > start and array[right] >= array[pivot]:
            
            right -= 1
        if left <= right:
            array[left], array[right] = array[right],array[left]
        else:
            array[pivot], array[right] = array[right], array[pivot]
        quick_sort(array, start, right -1 )
        quick_sort(array, right+1 , end)
    
quick_sort(array, 0, len(array)-1)
print(array)


# +
# 파이썬을 활용한 퀵정렬 using 재귀함수
array = [7, 2, 1 ,6 ,3, 5, 4, 9 ,8, 0]
def quick_sort(array):
    if len(array) <=1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x >=pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

quick_sort(array)

# +
# reveiw quick_sort()
array = [7, 2, 1 ,6 ,3, 5, 4, 9 ,8, 0]
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    
    while left<=end and array[pivot]>= array[left]:
        left += 1
    while right> start and array[pivot] <= array[right]:
        right -= 1
        
    if left >= right :
        array[pivot], array[right] = array[right], array[pivot]
        
    else:
        array[left], array[right] = array[right], array[left]
    
    
    quick_sort(array, start, right -1 )
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
# +
#계수정렬
array = [7, 5, 9 , 0 ,3 ,1, 6, 2, 9, 1, 4, 8 ,0, 5, 2]

count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end= " ")
    
# -



