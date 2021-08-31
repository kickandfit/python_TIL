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
            dfs(graph, i, visited)
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
        visited[v] = True
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
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

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
# # 문자열 관련 알고리즘


# #### 유형 1. 회문(palindrome)

# 단순한 회문
def isPalindrome(str):
    for i in range(len(str)//2):
        if str[i] == str[-i-1]:
            continue
        else:
            print('회문이 아닙니다.')
    print('회문 입니다.')
data = 'abcba'
isPalindrome(data)

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
        
            
# -

# 슬라이싱을 이용한 회문판별
s= ['가나다다나가']
if s == s[::-1]:
    print('회문입니다')

# +
# 정규식을 이용한 전처리
import re
def inPalindrome(str):
    # 대문자 소문자로 변경
    str = str.lower()
    
    # 정규식 사용
    str = re.sub('[^a-z0-9]', '', str)
    
    if str == str[::-1]:
        print('회문입니다')
    else:
        print('회문이 아닙니다')
data1 = 'OMadam, I\'m AdamO'
inPalindrome(data1) 


# -

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
# -

# #### 3단계

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
# -

# #### 2 단계 lambda 사용하기

# +
data = ['1 A', '1 B', '6 A', '2 D', '4 B']

data.sort(key = lambda x : (x.split()[1], x.split()[0]))
print(data)
# -

# #### 3 단계

data = ["hanpy 20101213 재미없다 235 재미있다", ...]
# 회원의 아이디, 회원가입날짜, 사용자가 쓴 댓글들
# 문제는 이런식이다. 각각의 DB의 회원들을 댓글들 중에 숫자를 제거하고, 
# 댓글들을 정렬한 후에, 가입한 날짜 순으로 재정렬하라

def divide_sentence(list_data):
    str_l, int_l = [], []
    list_datas = list_data.split()[2:]
    for data in list_datas:
        if data.isdigit():
            str_l.append(data)
        else:
            int_l.append(data)


# - isalpha() 문자열이 문자인지를 판별하여 True,Fasle
# - isdigit() 문자열이 숫자인지를 판별하여 True,False

# #### 유형4. 특정 단어 추출

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"

# - 'hit'을 제외한 단어 중 가장 많이 등장하는 단어를 뽑는 코드

# #### 1단계 정규식을 사용한 구두점 제거

import re
re.sub('[^\w]', ' ', paragraph)
#[^\w]은 모든 문자와 숫자를 제외하고 공백으로 바꿈

# #### 2단계 정규식 추가 처리

banned = 'hit'
word_list = re.sub('[^\w]', ' ' , paragraph).lower().split()
words = [word for word in word_list if word not in banned ]
print(words)

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
# -

# #### 유형 5. 애너그램
#
# - 애너그램이란 문자를 재배열하여 다른뜻을 가진 단어로 바꾸는 것을 말함

import collections
data = ["eat","tea","tan","ate","nat","bat"]
sort_data = collections.defaultdict(list)
for word in data:
    sort_data[''.join(sorted(word))].append(word)
print(sort_data.values())

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
    for i in range(len(data)-1):
        
        # 이게 회문 판단이 2개 들어간 이유
        # 하나는 문자열의 개수가 짝수 중 회문
        # 다른 하나는 문자열 개수가 홀수 중 회문
        # res 는 계산 중 가장 긴 회문( 반복문에서 지속적인 업데이트 )
        res = max(res, palindrome(len(data), i, i+1), palindrome(len(data), i, i+2), key=len)
        
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


