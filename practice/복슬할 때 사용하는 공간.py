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


# +
# 8/31
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

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited) # 이 부분은 완전 탐색
            # 9/1 만약 return dfs(graph, i, visited) 로 하게 되면 첫 번째, 끝까지 가는 경로에 대한 내용
            
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

# +
# 8 /31
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
visited = [False]*9

def bfs(graph, start, visited):
    q = deque([start])
    
    while q:
        v = q.popleft()
        visited[v] = True # 9/1 이부분이 차이가 있는데
        # 결과는 차이가 없지만 , 이렇게 되면 for 문에서 visited[]를 처리후에
        # 한번더 처리함. 비효율 적이다 이거지
        # 이 부분의 목적은 start의 방문 처리를 위함이잖아?
        # 그니까 이 부분은 위에서 처리해 주는게 효과적이지
        
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
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

# +
# 8/31
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i # i번째 선택
    for j in range(i+1, len(array)): # 가장 작은 데이터 선택후 i로 이동
        if array[min_index] > array[j]:
            array[min_index] , array[j] = array[j] , array[min_index]
print(array)

#9/1 그니까 앞에서 부터 정렬할껀데, 앞에서 min 값을 넣을거지
# 그럼 앞 부분부터 인덱스 주고 다음 for문에서
# 최소값을 찾고 그 값을 앞부분으로 swap 해주면 된다는 게 핵심이 잖아
# -

# #### 정렬( 삽입 정렬과 버블정렬)

# +
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

# 선택 정렬과 완전 반대 로직 
def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
print(array)

# 9/1
# 삽입 정렬은 처음 값을 일단 나둬, 2번 쨰 부터 비교하는데
# 핵심은 for문을 거꾸로 뒤집고 값비교후에 작으면 앞으로 옮기고 앞 값이 크면
# 그 자리에 두고 포문을 나가는게 핵심 총 2번위 for문이 있음
# 버블 정렬은 값을 맨 뒤로 보내는 것임
# 선택 정렬과 차이를 보면 뒤로 보낼 때는 for 문을 뒤집으면 되기 때문에
# 앞에서 부터 하는 것이 아니기 때문에 max_index를 지정하지 않아도됨

# +
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]: # 작으면 왼쪽으로 이동하다가
            array[j], array[j-1] = array[j-1], array[j]
        else: # 크면 그대로 멈춰라
            break
array
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

# 9/1 퀵정렬의 핵심은 투 포인터를 사용한다는 점
# 피봇을 정하고 투 포인터로 이동하면서 left에서는 큰 값을 right에서는 작은 값을 찾음
# left와 right의 교차 여부에 따라 swap이 바뀜
# 교차하지 않는 다면 left와 right를 swap
# 교차한다면 pivot과 right를 swqp
# 이 과정을 통해 pivot을 기준으로 left에는 작은 값이 right에는 큰 값이 쌓임
# 재귀를 통해 left와 right 역시 정리해주면 정렬 완료


# +
# 8/31
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start +1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
        quick_sort(array, right+1, end)
        quick_sort(array, start, right -1 )

def quick_sort1(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort1(left_side) + [pivot] + quick_sort1(right_side)

quick_sort(array, 0, len(array) -1)
print(array)
print(quick_sort1(array))

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
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side) # 9/1 이부분이 재귀를 통해 left랑 right를 정렬하는 부분

print(quick_sort(array))


# -

# #### 병합정렬(추가)

# +
# 8/31
# 어렵넹 쉽지 않아
def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])
    merged_arr = []
    l, h = 0 , 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
            
        else:
            merged_arr.append(high_arr[h])
            h += 1
    
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    print(merged_arr, 'low : ',low_arr, 'high : ', high_arr)
    
    return merged_arr

array = [6,5,3,1,8,7,2,4]
merge_sort(array)

# 9/1 이 병합 정렬이 이론은 쉬운데 구현이 꽤나 까다로움
# 기본 아이디어는 배열을 나눠서 최소 단위로 나눈다음
# 합칠 때 정렬을 해주며 합치는 것이 포인트
# 우선 어려운 이유는 나눌 때 재귀적으로 나눠주기 때문에
# 재귀에 대한 이해가 부족하면 코드의 작동 방식이 이해가지 않음
# 처음 반으로 나누고 그다음 다시 반... 이런 식으로 최소 단위 까지 나눔
# 그러면 초기 설정 한 2개의 값에는 최소 단위 2개가 남음
# 이 두개를 합치는 데 이 때 변수 l,h를 설정 함 이유는 합쳐질 수록 포함되는 인자가 많아짐
# 주의 점은 합치는 merge_list는 재귀가 끝나는 부분에서 초기화 해줘야하고
# merge가 끝나는 부분에서 return을 merged_list로 해줘야함
# 그래야 최소 단위에서 합쳐진 후 다음 재귀 함수의 값이 합쳐지고 정렬된 값을 부여받음
# 또한 기억해야하는 것은 return 값이 merged_list임으로 실제 array는 영향을 받지 않음
# 마지막으로 합칠 때 정렬되는 방식은
# 두 개의 배열에서 각각 포인트가 이동하며, 비교된 값을 새로운 merged_list에 추가해주는 형태임
# 따라서 배열 이후 두개의 배열에서 더이상 비교할 수 없다면 남은 값을 추가해 줘야함
# 다만 기본 코드에서는 새로운 값을 나누고 추가할 때
# 값이 메모리에 할당 됨으로 개선의 여지가 있음
# -

# 8/31
# 최적화 코든데 이해가 안가네
# 이해가 안갈 수 밖에 시작이 마지막 return이니까
def merge_sort(arr):
    def sort(low, high): # 이건 sort라기 보다 나누는 거고
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high: # 이부분 부터가 temp에 정렬해서 넣는 코드고
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high): # 정렬된 값을 arr에 넣는 과정이네
            arr[i] = temp[i - low]

    return sort(0, len(arr))
array = [6,5,3,1,8,7,2,4]
merge_sort(array)
array

# #### 계수 정렬

# +
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * ( max(array) + 1 )

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print( i , end = ' ')

# 9/1 계수 정렬의 핵심은 테이블을 만들고 그 테이블에 해당 값의 개수를 카운드해서 넣어준다는 점
# 동작 원리를 보면 전체 data를 한번은 순차탐색해야함
# 해당 인덱스에 값을 넣기 위한 테이블을 max(array) + 1개 만큼 생성해 줌으로
# 경우에 따라 메모리에 심각한 비효율을 초래할 수 있음
# 정렬 후 보여주는 방식은 테이블 인덱스를 해당 테이블 값 만큼 출력해서 보여주는 것임
# 물론 새로운 list에 저장해서 그 리스트를 보여줄 수 있음
# 중요한 사실은 원래 array에는 영향을 끼치지 않는 다는 점임
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

# 순차 탐색의 장점은 정렬이 되어있든 되어있지 않든 값을 찾아낼 수 있다는 점임
# 다만 리스트를 모두 봐야할 수 있다는 점에서 시간이 오래 걸릴 수 있음
# 값의 존재 여부가 중요한 사항이라면 반드시 고려해야할 알고리즘임
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


# 9/1
# 이진 탐색의 핵심 아이디어는 투 포인터(?)라고 하기도 애매한데 음
# 반으로 나누고 그 반이 target과 일치하는지 확인하고
# 일치하지 않는다면, mid와 target의 위치에 따라 재귀 함수 인자를 구성
# target이 mid 보다 크다면 end 값을 mid -1 로 조정 (mid란 array[mid]의미)
# target이 mid 보다 작다면 start 값을 mid + 1로 조정
# 최소 단위 까지 탐색 최소 단위는 start>end 임

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
# #### 재귀를 사용하는 이유는 뭘까(9/1)
#
# - 장단점
#     - 재귀함수를 사용하게 되면 코드가 간결해짐
#     - 그러나 속도가 느림, 메모리가 많이 사용됨
#     - 반복문을 사용하게 되면 상대적으로 코드가 어려워짐
#     - 그러나 속도가 빠름
#
# - 단점을 해결하기 위한방법
#     - 꼬리 재귀 : 컴파일러가 꼬리 재귀 코드를 보고, 적절한 반복문을 컴파일 해주어야 작동
#     - return 연산이 없는 경우에만 적용, return 문에 함수만 작성되어 있으면 꼬리재귀, 함수만 있는 경우가 아니면 컴파일 할 수 없음

# +
#9/1
def yes_tail(n, ans):
  if n == 1:
    return 1
  return yes_tail(n-1, ans + n)

def no_tail(n):
  if n == 1:
    return 1
  return n + no_tail(n-1)
# -

# - 두 코드 모두 같은 역할을 하지만, yes_tail 함수처럼 return 에 함수 호출 이외에 다른 연산자가 붙지 않는 경우 꼬리 재귀로 컴파일 가능
#
#

# # 문자열 관련 알고리즘


# #### 유형 1. 회문(palindrome)

# 단순한 회문
def isPalindrome(str):
    for i in range(len(str)//2):
        if str[i] == str[-i-1]: # -I-1 이부분이 재밌네
            continue
        else:
            print('회문이 아닙니다.')
    print('회문 입니다.')
data = 'abcba'
isPalindrome(data)
#9/1 조금만 깊게 생각해보면 재밌어
# 왜냐면 index는 0 부터 시작이고 마지막을 나타내는 값이 -1이니까
# 0 일때 -1 이어야하는거지 당연히 그럼 -i-1이어야하는 것이고

# +
# 전처리가 포함된 회문
from collections import deque
def isPalindrome(str):
    # 전처리
    list_str = deque()
    for char in str:
        if char.isalnum():
            list_str.append(char.lower())
    
# 회문 판별
    print(list_str)
    while len(list_str)>1:
        if list_str.popleft() != list_str.pop():
            print(list_str.popleft(), list_str.pop())
            print('회문이 아닙니다.')
            return
    print('회문 입니다.')
data1 = 'OMadam, I\'m AdamO'
isPalindrome(data1)

# 9/1 isalnum() : 문자열이 알파벳([a-zA-Z])과 숫자([0-9])로만 구성되었는지 확인하는 파이썬 문자열 메소드
# 하나하나 뜯어보면 str을 받아, str 자체가 interable하잖아?
# 그니까 하나씩 탐색해보는 거야, isalnum으로 그럼 한칸에 하나씩 append가 되겠지?
# 그다음 하는 방식은 왼쪽에서 꺼내고 오른쪽에서 꺼내서 비교하는 거야
# 문장 전체에서 회문을 찾는거지


# -

# - isalnum : 문자열이 알파벳([a-zA-Z])과 숫자([0-9])로만 구성되었는지 확인하는 파이썬 문자열 메소드

# +
# 슬라이싱을 이용한 회문판별
s= ['가나다다나가']
if s == s[::-1]:
    print('회문입니다')

# 9/1 :: 에 대해 정리가 한번 필요하겠네
# 그니까 슬라이싱의 기본은 a[start:end:step]
# 그럼 [::-1]은 처음부터 끝까지 -1 스텝으로 라는 의미겠지? 시작은 뒤에서 부터가 되는거고
# -

a = 'abcdefgh'
a[::0] # 이건 오류가 나겠지 왜? 0 라는 스텝이 없으니까

# 정규식을 이용한 전처리
import re
def inPalindrome(str):
    # 대문자 소문자로 변경
    str = str.lower()
    
    # 정규식 사용
    str = re.sub('[^a-z0-9]', '', str) # 9/1 정규식 간단하게 복습함하자
                                        # re.sub('패턴','바꿀문자열','적용할문자열')
    
    if str == str[::-1]:
        print('회문입니다')
    else:
        print('회문이 아닙니다')
data1 = 'OMadam, I\'m AdamO'
inPalindrome(data1) 

# #### re.sub('패턴', '바꿀문자열', '적용할문자열')

print( re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8') ) # 숫자만 찾아서 n으로 바꿈


# #### 회문정리
# - 슬라이싱을 활용하는 것이 시간이 제일 적게 걸림

# #### 유형 2. 문자열 뒤집기
#

# #### 1단계

# +
# 1단계 reverse() 사용하기

def reverseString(str):
    str.reverse()
    print(str)

a = ['a','b','c','d','e']
reverseString(a)

# 9/1 최근 현대 엔지비에서 나왔던 문제에서 쓴것 같아
# 문자열을 뒤집는 것은 아니었고 관측 대상이 오른쪽이라는 문제에서
# 배열을 뒤집는데 사용했던것으로 기억하네 ( reverse() )

# -

# #### 2단계

# +
# 2단계 슬라이싱 활용하기

a = 'abcde'
a = a[::-1]
print(a)

b = ['a','b','c','d','e']
b = b[::-1]
print(b)
# 오류가 발생한다면 할당에 제한이 걸린것이므로, b[:] = b[::-1] 을 사용하면 됨
# 9/1 이게 재밌는게 뭐냐면 거꾸로 뒤집는 건 슬라이싱을 활용할 수 있다는 것이고
# 더 다양한 케이스에 대해서 바꿀수 있다는 장점이 있지
# -

# #### 3단계

# +
# 3단계 투포인터
def reverseString(str):
    left_idx, right_idx = 0, len(str)-1
    while left_idx < right_idx:
        str[left_idx], str[right_idx] = str[right_idx], str[left_idx]
        left_idx += 1
        right_idx -= 1
    print(str)
b = ['a','b','c','d','e']
reverseString(b)

# 9/1 투포인터가 정말 많이 사용되는 구나
# 그럼 투포인터의 인덱싱을 lert는 시작 right는 마지막으로 주고
# 서로 바꿔가면 되겠지 같아도 상관 없어 교차만 안되면
# -

# #### 유형 3. 조건에 맞게 재정렬

data = ['1 A', '1 B', '6 A', '2 D', '4 B']
# 문제 리스트 안의 요소를 번호 순 정렬이 아닌 그 뒤의 문자 순으로 졍렬

# #### 1 단계 sort의 key

# +
# 오호 신박한데?

data = ['1 A', '1 B', '6 A', '2 D', '4 B']

def func(x):
    return x.split()[1], x.split()[0]
data.sort(key=func)
print(data)
print(func(data[0])) # 9/1 재밌는 것은 바로 적용은 못해 왜? data는 리스트거든
                     # 그말은 key를 위한 함수 값으로 쓰기 위해 func 을 만들었다는 의미거든
                     # 이 역할을 하는게 lambda 니까 다음 단계에서 lambda를 쓰겠지?

# 9/1 여기서 재밌는게 바로 key를 사용한다는 건데
# 데이터가 공백으로 나눠져 있잖아?
# 그니까 splict으로 다시 받는거지 그 뒤에 변환해서 받아주는 거고
# 그니까 key 값이라는 것은 데이터의 정렬을 할 때 기준 값으로 생각하면 편하겠지?
# -

# #### 2 단계 lambda 사용하기

# +
data = ['1 A', '1 B', '6 A', '2 D', '4 B']

data.sort(key = lambda x : (x.split()[1], x.split()[0]))
print(data)

# 9/1 단순 return을 받는 것이니까 lambda를 써도 되긴하는데
# 가독성이 좋지는 않다는 것
# 내가 코드를 개발시에 협업에 소통에 문제가 되긴하겠네
# -

# #### 3 단계

data = "hanpy 20101213 재미없다 235 재미있다"
# 회원의 아이디, 회원가입날짜, 사용자가 쓴 댓글들
# 문제는 이런식이다. 각각의 DB의 회원들을 댓글들 중에 숫자를 제거하고, 
# 댓글들을 정렬한 후에, 가입한 날짜 순으로 재정렬하라

# +
def divide_sentence(list_data):
    str_l, int_l = [], []
    list_datas = list_data.split()[2:]
    for data in list_datas:
        if data.isdigit():
            int_l.append(data)
        else:
            str_l.append(data)
    return str_l
# 9/1 어제는 메인 핵심 idea만 코딩 해봤으니까 문제 풀어 볼까?
# 메인 코드 복습먼저 해보면, 문자랑 숫자 리스트를 만들고
# 댓글이 문자랑 숫자로만 이루어졌다는 조건이 있으니까
# 문자인지만 확인하면 되겠지? isalnum은 문자, 숫자 다 판단이니까 기준을 잡고 넣어야겠네
# isdigit()은 숫자만 이니까 숫자에 추가하고
# 나머지는 문자에 추가하면 되겠네, isalpah() 문자인지를 판별하는 것있으니까 외워두고 문제 풀어볼까?

data = "hanpy 20101215 재미없다 235 재미있다"
data1 = "hanpya 20101214 재미없다 235 재미있다"

divide_sentence(data)

# 물론 이 부분 역시 커버 가능하긴 코드로 수정가능하지
# 그건 다음 복습때 할래
new_data = [data.split()[:2] + divide_sentence(data)] + [data1.split()[:2] + divide_sentence(data1)]


print(new_data) # 잘 들어갔는지 확인해보면서 하는 습관 가지자
# 그럼 정렬 하는 값을 만들어야 겠지?
new_data.sort(key = lambda x : int(x[1])) # 사실 int의 유무는 중요하지 않아
print(new_data)
# -

# - isalpha() 문자열이 문자인지를 판별하여 True,Fasle
# - isdigit() 문자열이 숫자인지를 판별하여 True,False

#9/1 확인해보고 싶었던 내용은 문자열로 숫자의 정렬이 될까였는데, 잘되네?
# 그다음 int로 바뀌주면 숫자 사용가능 하긴한데
# 바꿀 필요없다면 문자열에서 정렬을 비교하는 것도 나쁘진 않은 것 같어
a = ['3','1','4','52','3']
a.sort()
a

# #### 유형4. 특정 단어 추출

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"

# - 'hit'을 제외한 단어 중 가장 많이 등장하는 단어를 뽑는 코드

# #### 1단계 정규식을 사용한 구두점 제거

# +
import re
re.sub('[^\w]', ' ', paragraph)
#[^\w]은 모든 문자와 숫자를 제외하고 공백으로 바꿈

# 9/1 공백으로 바꾼이유가 어차피 split으로 아래서 지울거니까 그런건데
# 처음붜터 지워도 될것 같네
# -

# #### 2단계 정규식 추가 처리

# +
banned = 'hit'
word_list = re.sub('[^\w]', ' ' , paragraph).lower().split()
words = [word for word in word_list if word not in banned ]
print(words)

# 9/1 봐봐 결국에는 공백을 기준으로 지우잖어
# 위에서 지워도 상관없다 이거지
# 소문자로 바꿔준 것은 후에 판단때문이겠고
# -

# #### 3단계 counter()함수를 사용하여 빈도수 계산
#
# - counter 객체는 아이템에 대한 개수를 딕셔너리 형태로 리턴
# - 개수를 자동으로 계싼
# - most_common()을 사용하면 빈도수가 가장 높은 요소 추출 가능

# +
from collections import Counter

counts = Counter(words)
print(counts)

# +
#most_common 예시

data = [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 3]
dic_data = Counter(data)
print(dic_data)
print(dic_data.most_common()) # 빈도수가 높은 수로 정렬 후 보여줌
print(dic_data.most_common(2)) # ()의 int는 최빈수부터 몇개를 보여줄지
# -

# #### 자연어 처리의 또 다른 스킬

# +
from collections import Counter
sentences = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], ['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], 
             ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], 
             ['barber', 'went', 'huge', 'mountain']]

# 단어들을 하나의 리스트로 만들기
words = sum(sentences, []) # 넌 뭐냐 / sum( iterble, start)
print(words)
print()

#중복을 제거하고 빈도수를 기록하자.
vocab = Counter(words) # 파이썬의 Counter 모듈을 이용하면 단어의 모든 빈도를 쉽게 계산할 수 있다.
print(vocab)
print()

# most_common()는 상위 빈도수를 가진 주어진 수의 단어만을 리턴
vocab_size = 5
vocab = vocab.most_common(vocab_size) # 등장 빈도수가 높은 상위 5개의 단어
print(vocab)
print()

# 높은 빈도수 => 낮은 정수 인덱스
word_to_index = {}
i = 0
for (word, frequency) in vocab :
    i += 1
    word_to_index[word] = i
print(word_to_index)

# 9/1 sum으로 데이터 합치고
# counter로 중복 제거하면서 숫자 세고, 딕셔너리로 받고
# 딕셔너리 구조로 most_common 활용해서 정렬 한뒤에
# 인덱스를 새로 부여하는 거잖어?
# -

# #### 유형 5. 애너그램
#
# - 애너그램이란 문자를 재배열하여 다른뜻을 가진 단어로 바꾸는 것을 말함

# +
import collections
data = ["eat","tea","tan","ate","nat","bat"]
sort_data = collections.defaultdict(list)
for word in data:
    sort_data[''.join(sorted(word))].append(word)
print(sort_data.values())

# 9/1 어제 defaultdict를 처음 써봤잖어?
# 그니까 list로 받으면 없는 키가 들어오면 []를 넣어준다는거고
# 문자를 정렬하면 list로 받아들여 (확인함 해봐야겠고), 그니까 구분자를 ''로 없애고 join으로 합쳐
# 그 뒤에 생성된 key에 list로 들어오니까 append 해라 이거지

# +
# 9/1 확인하려고 해본건데 발견한 사실은
a ='adsfersdfe'
b = ''.join(sorted(a))
# print(a.sort) # 오류나는 부분
print(sorted(a))
print(b, type(b))

# sort는 str은 정렬해주지 못해
# 그렇지만 sorted는 리스트에 하나씩 추가하고 정렬해 줄 수 있네
# 그니까 작동 원리가 sort는 직접 바꾸고
# sorted는 리스트에 각각 담고 정렬해서 다시 되돌려준다고 볼수있겠네
# -

# - defaultdict
#     - 딕셔너리를 사용할 때, 지정되지 않는 키를 조회하면 에러메세지 출력
#     - 사용법 collections import 해야함
# - sort_data [''. join(sorted(word))]. append(word)
#     - word에 sorted하고 join을 해주는 이유 
#         - sorted()의 결과 값은 리스트가 됨
#         - ex) 'eat'가 sorted()를 만나면 ['a','e','t'] 가 출력됨
#         - 따라서 join을 활용하여 'aet'로 바꿔줌
#     - append를 한 이유
#         - sort_data[''.join(sorted(word))]의 결과 값이 리스트이기 때문
#         - 리스트에 넣어주기위해 append를 활용

# +
# 예시
a = {'a' : 1, 'b' : 2}
print(a['c'])

# 사용 방법
# 방법 1
import collections
a = collections.defaultdict(int)

# 방법 2
from collections import defaultdict
a = defaultdict(int)

# 9/1 defaultdict() 내부에 사용될 수 있는 형태가
# lst 되는건 아는데 str 도 되나?

# +
from collections import defaultdict


a = defaultdict(str)
a = {'a' : 1, 'b' : 2} # 이렇게 되면 재할당 되는 거라 오류나
                       # 키 값에 추가 할 때 사용해야되는 거네
print(a['c'])

# str 도 되네? 근데 기본으로 나오는 게 없네 ( 9/1 )
# -

# - defaultdict()의 인자로 위의 예시에는 int가 들어갔음
# - int 외에도 list, set이 들어갈 수 있음.
#     - int가 들어간 경우에는 없는 key값을 넣었을 때, 자동으로 value에 0이 들어감. int 대신 list를 넣으면 빈 리스트가 들어가게 됨

# +
# int를 인자로 넣은 경우
import collections
a = collections.defaultdict(int)
print(a['b'])    #   0
print(a)     #    defaultdict(<class 'int'>, {'b': 0})



# list를 인자로 넣은 경우
import collections
a = collections.defaultdict(list)
print(a['b'])     #    []
print(a)       # defaultdict(<class 'list'>, {'b': []})



# set을 인자로 넣은 경우
import collections
a = collections.defaultdict(set)
print(a['b'])     #     set()
print(a)        #  defaultdict(<class 'set'>, {'b': set()})

# 응용
import collections
a = collections.defaultdict(int)
a['H'] = 5
a['A'] = 3
a['N'] += 1
print(a)

# a['N'] += 1 부분을 보면, 우리는 a라는 딕셔너리에 'N' 값을 key로 지정하지 않음
# 에러가 뜨지 않고 0을 기준으로 더하기 1을 해준 것을 알 수 있다.

import collections
a = collections.defaultdict(list)
data = ['hanpy', 123, 'bbb', 81811]
for i in data:
    if type(i) == int:
        a['int_data'].append(i)
print(a)


# -

# #### 유형 6. 가장 긴 팰린드롬 찾기

# +
def palindrome(n, left, right):
    while right <= n and left >= 0 and data[left] == data[right-1]:
        right += 1
        left -= 1
        
    return data[left + 1: right -1]

data = 'ewqpbewqbfjabcdefedcbaienqnfkndkl'

res = ''
if data == data[::-1] or len(data) < 2:
    print(data)
else:
    for i in range(len(data)-1): # 9/1 근데 왜 반복문의 범위에 -1 을 하지?
                                  # 아 간단한 이유네, 회문의 최소 단위가 2니까 확인할 필요가 없는거네
                                  # 그래서 뺀거고
        
        # 이게 회문 판단이 2개 들어간 이유
        # 하나는 문자열의 개수가 짝수 중 회문
        # 다른 하나는 문자열 개수가 홀수 중 회문
        # res 는 계산 중 가장 긴 회문( 반복문에서 지속적인 업데이트 )
        res = max(res, palindrome(len(data), i, i+1), palindrome(len(data), i, i+2), key=len)
        
        # key 에 함수가 들어가 잖아? 근데 len 도 함수니까 들어 갈 수 있는 거지
        
    print(res)


# -

# #### if data == data [::-1] or len(data) < 2:
#
# - 위에서 작성한 코드는 순차적으로 인덱스 0부터 팰린드롬을 검사함 .data==data [::-1]인 경우 굳이 처음부터 검사를 할 필요가 없기 때문에 제거함. 이렇게 불필요한 계산을 하지 않게 하는 것을 가지치기라 함. 코드가 뻗어나가기 전에 가지를 쳐서 잘라낸다고 생각을 하자.
#       - 완전 탐색에 활용된 가지치기 스킬 찾아보고 이해 및 활용하기
#
#  
#
# #### res = max(res, palindrome(len(data), i, i+1), palindrome(len(data), i, i+2), key=len)
#
# - 이 부분을 보면, max안에 key인자가 들어있음. key=len의 의미는 내용 중에 길이가 가장 긴 값을 리턴한다는 의미.
#      - 즉, for문을 반복하면서, max를 활용하여 길이가 가장 긴 값을 res에 담은 후, 다시 res 변수를 max에 넣는 것을 반복하여 모든 팰린드롬의 경우 중에 가장 긴 팰린드롬을 찾는 것.
#
#  

# #### 백트래킹 ( 9/2 )
#
# - 재귀를 이용해 완전 탐색하고 가지치기를 추가하는 것
#     - 최적화문제와 결정문제를 해결 할 수 있음
#     - 결정 문제란 문제의 조건을 만족하는 해가 존재하는지에 따라 Yes/No 판별

# #### 백트래킹에서의 부분집합
# - 완전 탐색을 우선 코딩함

# +
def prinSet(n):
    for i in range(n):
        if A[i] == 1:
            print(data[i], end = ' ')
    print()
    
def powerset(k, n):            # k는 A배열의 k인덱스의 포함 유무를 판별한다.
    if n == k:
        printSet(k)
    else:
        A[k] = 1
        powerset(k+1, n)       # 배열 A에 체크하고 다음 인덱스로 넘어간다
        A[k] = 0               # 재귀로 되돌아와서 체크 했던걸 다시 원상복귀시킨다
        powerset(k+1, n)

data = 구하려는 리스트
n = len(data)                  # 부분집합을 구하는 리스트의 수
A = [0]* n                     # 포함 유무를 체크할 리스트 (0이 미포함, 1이 포함)
 
# -

# 부분집합의 합 ( 가지치기 추가 코드 )
def powerset(k, n, sum):
    if sum > 10:          # 부분집합의 합을 구하는 문제에서 구하고자하는 값인 10을 넘는다면 
                          # 더 이상 계산할 필요가 없으므로 return해버린다.(가지치기)
        return
    if n == k:
        printSet(k, sum)
    else:
        A[k] = 1
        powerset(k+1, n, sum+data[k])       
        A[k] = 0               
        powerset(k+1, n, sum)


# #### 최단 경로 ( 9/2 )
#
# - 다익스트라, 플로이드 워셜, 벨만 포드
# - 그리디 or 다이나믹이 그대로 적용됨

# +
#9/2 다익스트라
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input(),split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] *(n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
# 여기 까지는 input 값을 받는 과정
# 기본 적인 과정이니까 심심할 때 복습하면되
    
    
# 보면 참 신기하네, for 문을 n+1 즉 노드 개수 만큼 돌리는데
# 들어가는 건 distance란 말이지
# 근데 방문 하지 않은 노드를 방문하고, 가장 거리값이 짧은 노드의 인덱스 를 찾고
# 인덱스를 리턴받아 뭐할라는거지?
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] # 이건 start 에서 j[0]로 가는 비용이 j[1] 이니까 distance를 업데이트 해주는거고
    
    for i in range(n-1):
        
        now = get_smallest_node() # 여기서 쓰이는 구나
        # start 노드는 당연히 제외 되지 왜냐면, 방문 처리됐거든
        # 그럼 남은 노드가 n-1 개니까 for문도 n-1 만큼만 돌리면 되는 거거든
        
        visited[now] = True
        
        # 방문처리하고 난뒤에 하는 건
        # 그 그래프에 대해서 확인하는 거지
        # cost에 거리 값들을 더하고
        # 비교해서 작으면 업데이트 하는 거지
        for j in graph[now]:
            cost = distance[now] + j[1]:
            if cost < distance(j[0]):
                distance[j[0]] = cost



# +
# 개선된 dijkstra
import heapq

def dijkstra(start):
    q = []
    # 주목 할 부분은 dist랑 위치가 바뀌어서 들어가
    # 이 부분은 즉 우선순위를 dist에 주겠다는 의미잖아?
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heap.heappop(q)
        
        # 이 부분이 참 볼 때 마다 이해가 잘안가
        # 그니까 distance[now] 는 아래서 업데이트가 될거란 말야
        # dist가 크다는게 왜 방문 했던 적이 있는게 되는 거지?
        # 아래 코드 보고 다시 돌아와보자
        # 그럼 당연히 두번째 나오는 dist는 distance[now] 보다 클 수 밖에 없어
        # 왜냐고? heap 들어갈 때 append 조건이
        # cost = dist + i[1] 로 업데이트 된다음 들어간다는 거고
        # 같은 i[0] 가 들어가도, 작은 값이 앞에나오니까
        # 참 머리로 돌리기 쉽지가 않네
        if distance[now] < dist:
            continue
        
        # cost를 기준으로 distance 테이블에서 확인하는 것은 같은데
        # heap에다가 우선순위를 줘서 cost 를 기준으로 넣었단 말이지?
        # minheap 이니까 cost는 언제 들어가든 처음 나오는 게 제일 작을 거란거야
        # 안에서 그렇게 돌아가니까
        for i in graph[now]:
            cost = dist + j[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))


# -

# #### 다익스트라 사용 경우 정리
# - 다익스트라 알고리즘은 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것
# - 다익스트라는 ' 한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우' : 그러니까 start 노드를 설정하는 거잖아
# - 목적을 아니까 당연한 거지만 일차원 테이블로 최단 경로를 구할 수 있네 당연히 start는 정해지고 end만 정하면 되는 거니까

# #### 플로이드 워셜 알고리즘
# - '모든 지점에서 다른 지점 모든 지점까지의 최단 경로를 구해야하는 경우' 에 사용
# - 그러니까 start에서 end가 모두 다르니까 이차원 테이블을 활용해야하는 거네 당연히

# +
# 구현

INF = int(1e9)

n,m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)] # 여기서 부터 차이가 나는거야
                                           # 모든 경로에 대해 찾아야 하니까 2차원 테이블로 구성할 필요가 있는거지
                                           # 다익스트라는 2차원이 필요하지 않아 그렇지만, 그래프에 해당하는 정보를 담기 위해서
                                           # list로 2차원 처럼 받은 거고
                                           # 여기서는 거리 테이블 대신 이 테이블을 쓰겠지
# 대각 성분은 거리가 0으로 업데이트하고
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 나머지 간선 정보를 입력받아 테이블에 채워야지
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
# 자이제 거처갈때 어떻게 되는지에 대한 내용 나와야지
# 그럼 생각해봐 a에서 b로 가는 것과 a에서 k를 거쳐 b로 갈때를 비교하잖아?
# 그럼 최종 적으로 바뀌어야 되는 것은 k 가 되겠지 근데 사실 상관 없을 것 같긴해
# 그치 상관이 없이 k의 위치는
# 왜? 어차피 거처가는 거고 일일히 다 확인해야되는건 마찬가지거든
for a in range(1, n+1):
    for k in range(1, n+1):
        for b in range( 1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for a in range( 1, n + 1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INF', end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()
# -

# - 플로이드 워셜은 N^3 이잖아?
#     - 엄청나게 느릴 수 밖에 없어 2초 제한이면 계산 횟수가 5000만 건인데
#     - N 이 100 정도 까지 안에서만 계산할 수 있다는 거네

# #### 벨만 포드
#
# - 처음 다루는 것이니까 잘해보자
#     - ' 한 지점에서 다른 지점까지 최단 경로를 구하기 위함 '
#     - 단, 음의 가중치가 있어도 구할 수 있음
#     - 음수 사이클 여부를 알 수 있음
#         - 정점의 개수가 N 이라면 인접 간선을 검사하고 거리 값 갱신 과정을 N-1 로 제한하면 알 수 있음
#         - 시작 정점에서 도달 정점까지의 최대 간선의 개수는 N-1 개이기 때문

# #### 알고리즘 프로세스
# - 다익스트라와 비슷한데
# - 계산 과정이 N-1 번으로 제한되네 근데 다익스트라도 n-1 인데 차이가 뭘까 도대체
# - 모든 계산 과정 후에 갱신되는 경우가 생기면 사이클이 생긴것으로 판단
# - 크게 다른게 없네?

# +
# 구현
graph = {
    'A' : {'B' :-1, 'C':4},
    'B' : {'C' :3, 'D':2, 'E':2},
    'C' : {},
    'D' : {'B' :1, 'C':5},
    'E' : {'D' :-3},
}

def bellman_ford(graph, start):
    distance, predecessor = dict(), dict() # 거리 값, 각 정점의 이전 정점을 저장할 딕셔너리
    
    # 거리 값을 모두 무한대로 초기화 / 이전 정점은 None으로 초기화
    for node in graph:
        distance[node] = float('inf')
        predecessor[node] = None
    distance[start] = 0
    
    for i in range(len(graph) -1):
        
        for node in graph:
            
            
            # 각 정점마다 모든 인접 정점들을 탐색
            # (기존 인접 정점까지의 거리 > 기존 현재 정점까지 거리 + 현재 정점부터 인접 정점까지 거리)
            # 인 경우 갱신
            
            for neighbor in graph[node]:
                
                if distance[neighbor] > distance[node] + graph[node][neighbor]:
                    distance[neighbor] = distance[node] + graph[node][neighbor]
                    predecessor[neighbor] = node
     
    # 음수 사이클 존재 여부 검사 
    # V-1번 반복 이후에도 갱신할 거리 값이 존재한다면 음수 사이클 존재
    for node in graph:
        for neighbor in graph[node]:
            if distance[neighbor] > distance[node] + graph[node][neighbor]:
                return -1,' 그래프에 음수 사이클이 존재합니다.'
    return distance, predecessor

print(bellman_ford(graph, "A"))


# -

# #### 9/2 그래프 이론( 여기를 제일 안해가지고 제일 못하니까 해보자 )
#
# - 현대에서 이게 나와가지고 이번에
# - 다음번에는 잘준비해보자

# #### 그래프 이론을 떠올려야 하는 힌트와 Tip
# - 다른 개체와 연결되어 있다 라는 문구
#     - EX) 여러 도시가 연결되어 있다
# - 트리 자료 구조가 가장 많이 사용됨
# - 최소 힙의 경우 항상 부모 노드가 자식 노드보다 크기가 작은 자료구조로 트리 자료 구조
# - 트리는 (전통적으로는 무방향 그래프로 간주) 컴퓨터 공학에서는 방향 그래프로 간주
#     - 트리는 비순환, 루트 노드 존재, 부모와 자식관계, 계층 모델

# #### 서로소 집합
#
# - 서로소 부분 집합들로 나누어진 원소들의 데이터 처리를 하기 위한 자료구조
# - 서로소 집합 자료구조는 union과 find 연산

# +
# 특정 원소가 속한 집합을 찾기
def find_parend(parent, x):
    
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a,b):
    
    # 두 집합을 가져와서 parent를 찾어
    a = find_parent(parent, a)
    b = find_parend(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
# 이게 핵심이네
# 그니까 정보를 입력 받으면서 union 연산을 진행하는거지?
# find 는 말그대로 그 집합이 속한 집합을 찾는거고
# 부모 테이블이랑은 조금 다른 이야기네, 결국에 이코드는 타고타고 가는 구조고


# -

# 개선된 서로서 집합
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
# 즉 이건 경로 압축, 그 원소가 속한 집합에 대해 모두 부모를 가르키게함
# 이걸 쓰면 타고타고 가는게 아니라 부모 테이블 역시 다 다 루트 노드를 가르키게 되겠네


# #### 서로소 집합을 활용한 사이클 판별
# - 방향있는 그래프에서는 사이클 여부는 DFS를 이용하여 판별가능

# +
#싸이클 판별여부
cycle = False

for i in range(e): # e 는 간선의 개수
    a,b = map(int, input().split())
    
    if find_parent(parent, a) == find_parent(parent, b):
        clcle = True
        break
        
    else:
        union_parent(parent, a, b)
# 이게 전체 코드인데 어떤 내용이냐면
# 사이클이 루트 노드가 다르잖아? 그럼 합쳐
# 근데 루트 노드가 같잖아? 그럼 사이클이 발생한거야
# 예를 들어서 1 2 3 노드가 서로 연결되어 있다고 하면
# 2 ->1 , 3->1 로 유니온 연산이 진행된다음 2 와 3을 비교 하는데 2,3의 루트 노드는 1로 같음으로 사이클이 발생했다고 보는 것
# -
# #### 9/3 신장 트리 / 크루스칼
# - 기본 알고리즘 하고 오늘 이부분 문제 풀자잉


# +
import sys

# input = sys.stdin.readline
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a> b:
        parent[a] = b
    else:
        parent[b] = a

# 노드의 개수와 간선의 개수 받기        
v, e = map(int, input().split())
parent = [0] * (v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 함수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i
    
# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))

# 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

# 뭐야 크루스칼은 거의 그냥 find, union, 사이클 판별이네
# 거기에 cost 추가 해놓구
# cost별로 정렬 해놓고
# 비용 큰 애부터 꺼내서 합치고 cost만 더해주는 건데?
# -

# #### 위상정렬
# - 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열'

# +
from collections import deque

# 노드의 개수와 간선의 개수 받기        
v, e = map(int, input().split())
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프에 대한 모든 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입차수 증가
    indegree[b] += 1
    
# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()
    
    # 처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    # q가 빌 때까지 반복
    while q:
        
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
                
        # 위상 정렬을 수행한 결과 출력
        for i in result:
            print(i, end = ' ')
        print('다음')
            
topology_sort()

# 그니까 처음 입력할때
# 차수 입력해주고 늘려준다음에
# 차수가 0 인 애부터 큐에 넣고 다음으로 넘어가면서
# 진입 차수 줄여가면서 0 되면 다시 큐에 넣고 빼
# 큐에서 뺀 값은 결과 리스트에 넣어주고 그 값을 활용해서
# 현재 그래프의 정보에 대해 판단하는 알고리즘 이네
# -

# #### 9/3 더 알아두면 좋은 알고리즘( 이 부분이 책의 마지막 부분이긴해 )
# - 소수판별
# - 에스토스테네스의 체
# - 투 포인터

# #### 소수 판별
#
# - 2 보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지않는 자연수

# 기본 아이디어
def is_prime_number(x):
    
    for i in range(2, x):
        
        if x % i == 0:
            return False
    return True


# +
# 개선된 소수 판별 알고리즘
# 그니까 어쩐 수는 약수가 있다면 대칭을 이룸
# 그럼 재미있는 것은 제곱근 까지만 확인하면 뒤에는 확인할 필요가 없다는거지

import math

def is_prime_number(x):
    
    for i in range(2, int(math.sqrt(x)+ 1)):
        
        if x % i == 0:
            return False
    return True



# -

# #### 에스토스테네스의 체

# +
import math

n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)+1)):
    if array[i]:
        j = 2 # 이게 배수를 건들기 위한 것
        
        while i*j <= n:
            array[i*j] = False
            j += 1
                   
# for i in range( 2, n+1):
#     if array[i]:
#         print(i, end = ' ')

# 재밌네 이거
# 그니까 True False Table을 만들고
# 배수 지워가면서 True 인 애들에 대해서만 계속해라 이거잖아
# 재밌네
# -

# #### 투포인터
# - 순차적으로 접근해야할 때 2개의 점의 위치를 기록하면서 처리 하는 알고리즘

# +
n = 5
m = 5 # 찾고자 하는 부분합
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키면서 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n :
        interval_sum += data[end]
        end += 1
    
    # 부분합이 m일 때, 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
print(count)
# -

# #### 정렬되어 있는 두 리스트의 합집합

# +
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [0] *(n+m)
i = 0
j = 0
k = 0

while i < n or j < m :
    if j >= m or ( i < n and a[i] <= b[j] ):
        
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end = ' ')
    
# 반복문을 돌리는 데, 두 집합의 원소 개수보다 작을 때 계속돌려
# 그리고 b 리스다가 다 처리됐거나, a[i]<=b[j] 일때 추가하고 i+=1
# 아닐 때 b[j]를 추가하고 마지막에 k 를 늘려주라는 거네
# -

# #### 구간합 계산

# +
n = 5
data = [10, 20, 30, 40,50]

sum_value = 0
prefix_sum = [0] # 리스트에 넣네? # 그렇지 보면 1번째 부터 인덱스 쓸거니까
                 # 리스트처음에 0을 넣을 필요 없다 이거지

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left -1]) # 3번째 - 4번째면 
                                               # 구간합 기준 2번째까지 에서 4번째 값이니까 left -1
prefix_sum
# +
# 백준 4673 번 셀프넘버
# 그니까 set으로 하는데
# generated_num을 10001에 대해 순차 탐색하면서 set에 넣어
# 그럼 중복은 제외 되니까
# 차집합으로 푼다라.. 괜찮네

natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i, end = ' ')

# +
# 4673 다른 풀이
array = [True for _ in range(10001)]
array[0] = False

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    if i < 10001:
        array[i] = False

for i in range(1,10001):
    if array[i]:
        print(i, end = ' ')


# +
# 한수 1065 번
N = int(input())
result = 0

for i in range(1,N+1):
    if i <= 99 :
        result += 1
    else:
        N = str(i)
        if int(N[0])-int(N[1]) == int(N[1])-int(N[2]):
            result += 1
print(result)

# -

from itertools import permutations
import math
a = '110'
c = list()
for i in range(1, len(a)+1):
    b = set(permutations(a, i))
    for k in b:
       c.append(k)
print(c)

# +
# 프로그래머스 소수 찾기
# my solution
# solution 에 다 풀었는데 다른 좋은 풀이는 복습하면서
# 구성해보자
import sys
import math
from itertools import permutations
cnt = 0
def solution(numbers):
    global cnt
    n = 10000000
    array = [True for i in range(n+1)]
    array[1], array[0] = False, False
    for i in range(2, int(math.sqrt(n))+1):
        if array[i]:
            j = 2
            while i*j <= n :
                array[i*j] = False
                j += 1
    # 모든 숫자 소수 판별 끝났고 이제 문자열 조합해서
    # array[i] = True 인 지만 생각하면 되네
    

    result = []
    for i in range(1,len(numbers)+1):
        pre = set(permutations(numbers, i))
        for j in pre:
            if int(''.join(j)) not in result:
                result.append(int(''.join(j)))
    for num in result:
        if array[num]:
            cnt += 1
          
    return cnt

# |= 이거 뭐야 | union 연산자네 그니까 내가 생각했던 add 가아닌
# 병합 연산자 할당자를 써버리네
# 내가 한 방법은 set을 쓰고 unique 한 연산자에 대해
# reslut에 추가 했다면
# 여기서는 a 에다가 set을 map으로 한번에 집어 넣네

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

# -



# +
def is_prime_number(yellow):
    prime_list = []
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            a = int(yellow //i)
            prime_list.append((a, i))
    prime_list.sort()
    return prime_list

test = is_prime_number(2)
bt_num = []
for i in test:
    bt_num.append([int((i[1]+2)*2 +(i[0])*2), i])
print(bt_num)
brown = 10
result = []
for j in bt_num:
    if brown == j[0]:
        result=([j[1][0]+2,j[1][1]+2])
result

# +
# 프로그래머스 카펫 풀이
# 2단계가 뭐 이리 어렵냐 ㅋㅋ
import math

# yellow 약수의 조합을 묶고, 
# return 받아 그 list
def is_prime_number(yellow):
    prime_list = []
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            a = int(yellow //i)
            prime_list.append((a, i))
    prime_list.sort()
    return prime_list

def solution(brown, yellow):
    test = is_prime_number(yellow)
    bt_num = []
    
    for i in test:
        bt_num.append([int((i[1]+2)*2 +(i[0])*2), i])
    
    result = list()
    for j in bt_num:
        if brown == j[0]:
            result=([j[1][0]+2,j[1][1]+2])
    # 노랑을 배치하고
    # 갈색을 주위에 배치했을 때
    # 그 갈색의 수가 주어진 brown 가 갔냐
    # 총 메트릭스의 n,m을 출력해 주면 되겠네
    
    # 갈색을 모든 경우에 대해 체크하면 되겠네
    
    return result

# 모범답안
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0: # 나눠 떨어져야 배열을 만들 수 있으니까
            if 2*(i + red//i) == brown-4: # 내가 생각했던 그 리스트에 넣고 판별을 이렇게 하네
                return [red//i+2, i+2] #배열을 나타내려면 이렇게 하긴 해야지
            
# 코드가 너무 짧아지니까 열받네



# +
# 완주하지 못한 선수 처음 풀이
# 시간 초과
# 테스트 케이스 모두 통과

from collections import Counter
def solution(participant, completion):
    participant_dict = Counter(participant)
    
    answer = ""
    
    for complete in completion:
        if complete in participant:
            participant_dict[complete] -= 1
            
    # print(participant_dict)
    
    for fail in participant_dict:
        if participant_dict[fail] != 0:
            answer = fail
    return answer


# 두번째 풀이
# 이건 통과 했네
from collections import deque
def solution(participant, completion):
    answer = ""
    a = sorted(participant)
    q_participant = deque(sorted(participant))
    q_completion = deque(sorted(completion))
   
    for i in range(len(q_participant)):
        if len(q_completion) != 0 and len(q_participant) != 0:
            a = q_participant.popleft()
            b = q_completion.popleft()
            
            if a != b:
                answer = a
               
                break
        else:
            answer = q_participant.popleft()
        
    return answer


# 이 미친 풀이는 뭐야...
# 그니까 Counter에서 빼서 한번에 넣을 수 있네
# 키를 넣고 첫번째 것만 꺼내라는 거잖아
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# +
import collections

participant = ['ㅁ', 'ㄴ', 'ㅇ','ㄹ','ㄹ']
completion =  ['ㅁ', 'ㄴ', 'ㅇ','ㄹ']
answer = collections.Counter(participant) - collections.Counter(completion)
answer
# -


