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

# ### 투포인터
# - 리스트에 순차적으로 접근해야할 때 2개의 점 위치를 기록하면서 처리
# - 특정한 합을 가지는 부분 연속 수열 찾기, 특정한 합을 가지는 부분 연속 수열 찾기 문제
# - 리스트 내에 음수가 있을경우 해결하기 어려움
#     - 이 밖에도 정렬되어 있는 두 리스트의 합집합 같은 문제에 효과적

# #### key idea (특정한 합을 가지는 부분 연속 수열 찾기)
#
#     1. 시작점과 끝점이 첫 번째 원소의 인덱스(0)을 가리키도록 한다
#     2. 현재 부분합이 M과 같다면 카운트
#     3. 현재 부분합이 M보다 작다면, end를 1 증가 시킴
#     4. 현재 부분합이 M보다 크거나 같으면 start를 1 증가시킴
#     5. 모든 경우를 확인할 때까지 2-4과정 반복

# +
# 부분합이 5인 경우 찾기(모든 리스트내 함수 양)

n, m = 5, 5 # m은 찾고자하는 부분합 데이터 개수 n
data=[1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    #end를 가능한 만큼 이동 시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum ==m :
        count += 1
    interval_sum -= data[start]
print(count)
# -

# #### keyidea(정렬되어 있는 두 리스트의 합집합)
#
#     1. 정렬된 리스트 a와 b 입력받기
#     2. 리스트 a 에서 처리되지 않은 원소 중 가장 작은 원소를 i를 가리키도록한다
#     3. 리스트 b 에서 처리되지 않은 원소 중 가장 작은 원소를 j를 가리키도록 한다
#     4. a[i]와 b[j] 중에서 더 작은 원소를 결과 리스트에 담는다
#     4. 리스트 a, b에서 더이상 처리할 원소가 없을 때 까지 2-4를 반복한다

# +
# 정렬되어 있는 두 리스트의 합집합

n, m = 3 , 4
a = [1, 3, 5]
b = [2, 4, 6, 8]
result = [0]*(n+m)
i, j , k = 0, 0, 0

while i < n or j < m :
    # 리스트 b의 모든 원소가 처리되었거나, 리스트 a의 원소가 더 작을 때
    
    if j >= m or (i<n and a[i] <= b[j]):
        
        #리스트 A의 원소를 결과 리스트로 옮기기
        result[k] = a[i]
        i += 1
    
    # 리스트 a의 모든 원소가 처리되었거나, 리스트 b의 원소가 더 작을 때
    else:
        
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end = ' ')
# -

# ### 구간 합 계산
#
# - 구간 합을 구해야하는 문제에서 사용된, 구간 합이란 연속적으로 나열된 N개의 수가 있을 때, 특정 구간의 모든 수를 합한 값을 말함
# - 이런 구간 합 계산 문제는 여러개의 쿼리(query)로 구성되는 문제 형태로 출제
# - ex) M 개의 쿼리가 존재한다면, 각쿼리는 left와 right로 구성되어 있으며 [left, right]는 구간을 의미함
# - 즉 모든 쿼리에 대하여 구간의 합을 출력하는 문제에서 사용됨 (시간 복잡도 O(NM))
# - 이 때 가장 많이 사용되는 기법이 접두사 합(prefix Sum) N개의 수의 위치에서 각각에 대하여 접두사 합을 미리 구해놓으면 됨
# - 접두사 합이란, 리스트의 맨 앞부터 특정 위치까지의 합을 구해놓을 것을 말함

# #### keyidea( 구간 합을 빠르게 계산하기 알고리즘)
#
#     1. N개의 수에 대하여 접두사 합(Prefix Sum)을 계산하여 배열 p에 저장한다.
#     2. 매 M개의 쿼리 정보 [l , r]을 확인할 때, 구간 합은 p[r] -p[l-1] 이다.

# +
# 접두사 합을 활용한 구간 합

n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합(prefix sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
# -






