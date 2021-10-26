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
