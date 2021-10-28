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
# 전화번호 목록 : 효용성 테스트 실패
def solution(phone_book):
    n_phone_book = sorted(phone_book)
    num_list = defaultdict(str)
    for i,k in enumerate(n_phone_book):
        num_list[i] = k
    for i in num_list:
        if i < len(num_list):
            for j in range(i+1,len(num_list)):
                if num_list[i] == num_list[j][:len(num_list[i])]:
                    answer = False
                    break
                else:
                    answer = True
                    continue
        if answer == False:
            break      
        else:
            continue
    return answer

# 문자열을 정렬하면 앞의 숫자 순서대로 나온다, 즉 숫자 크기가 아니라 맞춰서 정렬되기 때문에 뒤에 부분 생각할 필요가 없다


# -

# 전화번호 목로 : 통과
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer


# +
# zip 과 , startswich를 활용한 풀이
a = [1,2,3]
b = (4,5,6)
c = 'abce'
print(list(zip(a,a[1:])))

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


# -

# 파이썬 정렬 알고리즘 h-index
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


# N으로 표현하기
def solution(N, number):
    possible_set = [0,[N]] # 조합으로 나올수 있는 가능한 숫자들, 여기에 계속 append하며 이후에 사용함
    if N == number: #주어진 숫자와 사용해야 하는 숫자가 같은 경우는 1개면 족하므로 1으로 놓는다. 
        return 1
    for i in range(2, 9): # 2부터 8까지로 횟수를 늘려 간다. 
        case_set = [] # 임시로 사용할 케이스 셋, 각 I 별로 셋을 만들어 possible set에 붙인다.
        basic_num = int(str(N)*i) # 같은 숫자 반복되는 거 하나를 추가한다.
        case_set.append(basic_num)
        for i_half in range(1, i//2+1): # 사용되는 숫자의 횟수를 구해야 하는데, 
                                         #절반 이상으로 넘어가면 같은 결과만 나올 뿐이므로 절반까지만을 사용한다. 
            for x in possible_set[i_half]:
                for y in possible_set[i-i_half]: # x와 y를 더하면 i 가 되도록 만든 수다. 
                    print(possible_set)
                    case_set.append(x+y)# 각 사칙연산 결과를 더한다.
                    case_set.append(x-y)
                    case_set.append(y-x)
                    case_set.append(x*y)
                    if y !=0:
                        case_set.append(x/y)
                    if x !=0:
                        case_set.append(y/x)
            if number in case_set:
                return i
            possible_set.append(case_set) # 최종 결과물 set에 사칙 연산 결과를 더한다.
    return -1 #N 이 8까지 답이 없으면 -1을 출력한다.


# +
# 타켓넘버 - bfs 풀이

from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


# +
# 타켓넘버 - dfs 풀이

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer


# +
# 더 맵게 - heapq 사용

import heapq
def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    cnt = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except:
            return -1
        cnt += 1
        
    return cnt


# +
# 구명 보트 - 그리디

def solution(people, limit):
    answer = 0
    p_list = sorted(people)
    start , end = 0, len(people)-1
    cnt = 0
    while start <= end:
        cnt += 1
        if p_list[start] + p_list[end] <= limit:
            start += 1
        end -= 1
    return cnt


# +
# 단속카메라 - 그리디

def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[0], reverse=True)
    
    now = routes[0][0]
    for i in routes[1:]:
        if i[1] >= now:
            continue
        else:
            now = i[0]
            answer += 1
    
    return answer

# 아이디어가 중요하다


# -

# 섬연결하기 - 크루스칼
def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합
    
    while len(routes)!=n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1] # visited 와 비슷한 개념이라고 봐도 무방
                break
    return ans


# +
# 섬연결하기 - 다른 사람 풀이
def ancestor(node, parents):
    if parents[node] == node:
        return node
    else:
        return ancestor(parents[node], parents)

def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents = [i for i in range(n)]
    bridges = 0
    for w, f, t in edges:
        if ancestor(f, parents) != ancestor(t, parents):
            answer += w
            parents[ancestor(f, parents)] = t
            bridges += 1
        if bridges == n - 1:
            break
    return answer


# -

# 징검다리 - 이분탐색
def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()  # 징검다리 정렬
    rocks.append(distance)  # 마지막 도착지와의 거리까지 계산하기 위해
    
    left, right = 0, distance  # 이분 탐색 스타트!
    while left <= right:
        # 나는 거리의 최솟값을 mid로 잡겠다!(거리가 mid 이하이면 다 없앤다!)
        mid = (left + right) // 2  
        min_distance = float('inf')  # 각 mid 에서 최솟값을 저장할 녀석
        current = 0  # 현재 위치
        remove_cnt = 0  # 바위를 제거한 개수
        
        # 거리 재기 스타트
        for rock in rocks:
            diff = rock - current  # 바위와 현재 위치 사이의 거리
            if diff < mid:  # mid 보다 거리가 짧으면 바위 제거
                remove_cnt += 1
            else:  # mid 보다 거리가 길거나 같으면 바위 그대로 두고
                current = rock  # 현재 위치를 그 바위로 옮기고
                min_distance = min(min_distance, diff)  # 해당 mid 단계에서의 최소거리인지 체크
        
        # mid를 설정하는 단계
        if remove_cnt > n:  # 바위를 너무 많이 제거 했다. mid를 줄여서 바위를 조금만 제거하자
            right = mid - 1
        else:  # 바위를 너무 적게 제거했다 and 딱 맞다. mid를 늘려서 바위를 더 제거하거나 mid의 최댓값을 올려보자
            answer = min_distance
            left = mid + 1

    return answer


# +
from collections import deque
def bfs(begin, target, words, visited):
    count = 0
    stack = deque([[begin, 0]])
    while stack:
        cur, depth = stack.popleft()
        if cur == target:
            return depth
        
        for i in range(len(words)):
            if visited[i] == True:
                continue
            cnt = 0
            for a,b in zip(cur, words[i]):
                if a!=b:
                    cnt += 1
            if cnt == 1:
                visited[i] = True
                stack.append([words[i], depth+1])
                
            

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    visited = [False]*(len(words))

    answer = bfs(begin, target, words, visited)

    return answer
