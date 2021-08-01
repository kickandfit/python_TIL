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

# #### itertools
#
# - permutations, combinations를 많이 사용함
# - permutations, combinations 등을 사용하게 되면, 그 내용이 그대로 저장은 되지만 특정 형식을 가지고 있지 않음
# - 즉 순열, 조합의 전체 내용이 하나의 메모리에 저장됨
# - list와 같은 새로운 데이터 구조를 활용해 각각의 요소에 인덱스를 부여해야만 하나하나 값을 활용할 수 있음
# - 그러나, 메모리 자체에 저장되어 있다고 하더라도, 그 데이터 자체는 iterable한 데이터임

# +
# permutations : iterable한 객체에서 r개의 데이터를 뽑아 순서를 고려하여 나열
from itertools import permutations

data = ['a', 'b', 'c']
result = list(permutations(data, 3))
print(result)
print(type(result[0]))

result = permutations(data, 3)
print(result)
for i in result:
    print (i)

# +
# combinations : iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 경우
from itertools import combinations

data = ['a', 'b', 'c']
result = list(combinations(data ,2))
print(result)

result = combinations(data, 2)
print(result)
# -

#product : iterable한 객체에서 r개의 데이터를 뽑아 일렬로 순서를 고려하여 나열하는 경우(중복을 포함)
from itertools import product
data = ['a', 'b', 'c']
result = list(product(data, repeat = 3)) # repaet = 3, 뽑고자하는 데이터수 3개
print(result)

#combinations_with_replacement : iterable한 객체에서 데이터를 뽑아 일렬로 순서를 고려하지 않고 나열하는 경우(중복포함)
from itertools import combinations_with_replacement
data = ['a', 'b', 'c']
result = list(combinations_with_replacement(data, 3))
print(result)

# ### heapq
# - 우선 순위큐를 구현하고자 할때 사용하는 라이브러리
# - 파이썬에서는 최소 힙으로 구성되어있음
# - 시간복잡도 O(NlogN)
# - 삽입 heaqp.heappush(), 추출 heapq.heappop()

# +
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))
        
    return result

result = heapsort([9,2,4,1,3,5,7,3,6,8,0])
print(result)


# +
# 최대 heapq 구현방법

def max_heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result = max_heapsort([9,2,4,1,3,5,7,3,6,8,0])
print(result)
# -

# ### bisect
#
# - 이진 탐색을 쉽게 구현할 수 있도록하는 라이브러리
# - 정렬된 배열 에서 특정한 원소를 찾아야하는 경우 매우 효과적
# - bisect_left()와 bisect_right() 함수가 가장 중요하게 사용됨
# - 시간 복잡도 O(logN)
#     - bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 매서드
#     - bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 매서드
# - bisect_left(), bisect_right() 함수는 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할때 효과적

# +
# bisect_left(), bisect_right() 활용
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]

x = 4

print(bisect_left(a, x)) # 2다음 위치에 4를 삽입 따라서 인덱스는 2
print(bisect_right(a, x)) # 오른쪽 4 다음 위치에 삽입 따라서 인덱스는 4


# +
# bisect_left(), bisect_right() 활용 특정 원소 개수찾기

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 8]

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))
# -

# ### collections
#
# ##### deque
#
# - 유용한 자료 구조를 제공하는 표준 라이브러리, 특히 deque 와 counter는 알고가야함
# - deque는 큐를 구현 할때 사용됨, deque 는 인덱싱을 사용 할 수 없음
# - 다만, 시작과 마지막에 데이터를 추가할 경우 매우 효과적으로 사용됨(시간복잡도 O(1))
# - 왼쪽에 추가 할때 appendleft(), 마지막에 추가할때 append(), 왼쪽(첫번째 원소제거) popleft(), 마지막 원소를 제거할 때 pop()

# +
from collections import deque

data = deque([1, 2, 3, 4])
print(data)
data.appendleft(0)
data.append(5)
print(data)
# -

# #### counter
#
# - 등장 횟수를 세는 기능을 제공
# - iterable한 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지 열려줌
# - dictionary 구조로 들어감

# +
# 원소별 등장 횟수 세기

from collections import Counter

counter = Counter(['red', 'blue', 'green','red', 'red', 'blue', 'blue'])

print(counter)
print(counter['red'])
print(counter['blue'])
print(counter['green'])
# -

# ###  math
#
# - 팩토리얼, 최대공약수, 최소공배수 등을 계산해주는 기능을 포함하고 있음

# +
import math
# math.lcm은 3.9 부터 사용가능

print(math.factorial(4))
print(math.sqrt(16))
print(math.gcd(21, 14))
print(math.pi)
print(math.e)
# -




