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

# # 파이썬 다운 반복문 작성하기

# #### 파이썬 답지 못한 반복문

# +
my_items = ['a','b','c']

i = 0

while i < len(my_items):
    print(my_items[i])
    i += 1
# -

# #### 파이썬 답지 않은 두 가지 이유
# - 수동으로 인덱스 i를 0으로 초기화하고 반복마다 인덱스를 신중하게 증가
# - 얼마나 반복할지 결정하기 위해 len() 사용

# #### 파이썬 다운 반복문 ( 개선 )
# - 그러나 아래코드 역시 자바스러운 반복 구조

for i in range(len(my_items)):
    print(my_items[i])

# - range 타입은 숫자의 불변적인 순서를 나타냄
# - range 객체는 실제로 숫자 순서를 나타내는 개별 값을 저장하지 않음
#     - 이터레이터로 동작하고 순서 값을 즉시 계산
#     

# #### 매우 파이썬적인 코드
# - for-each 반복문
# - 시퀀스의 항목을 인덱스로 검색하지 않고 직접 반복함
# - 매우 파이썬적인 반복문

for i in my_items:
    print(i)

# #### 인덱스가 필요한 경우
# - enumerate() 를 사용하라

for i, item in enumerate(my_items):
    print(f'{i} : {item}')

# #### 파이썬 이터레이터는..
# - 하나 이상의 값을 반환할 수 있음
# - 임의 개수의 숫자값을 담은 튜플을 반환 할 수 있고 for 문 안에서 열어 볼 수 있음

# +
emails = {'bob' : 'bob@example.com', 'Alice' : 'Alice@example.com'}

for name, email in emails.items():
    print(f'{name}->{email}')
# -

# #### 인덱스가 증가하는 크기를 제어해야 하는 경우
#
# - for i in range(a, n, s) : a에서 n-1까지 s만큼 증가시키며

# #### keypoint( 요점 정리 )
# - 파이썬에서 C 스타일 반복문을 작성하는 것은 파이썬 답지 않음
#     - 가능한 경우 반보고디는 인덱스와 정지 조건을 관리하지 마라
# - 파이썬의 for 반복문은 컨테이너나 시퀀스의 항목을 직접적으로 반복할 수 있는 'for-each' 반복문임

# # 내포식 이해하기
# - 내포식은 컬렉션에 대한 for 반복문이고 좀 더 간단하고 조밀한 구문으로 표현
# - 한줄 쓰기
# - 내포식은 너무 길지 않게 쓰자
#     - 한 단계 중첩까지만 쓰다 가독성이 나빠진다

squares = [x*x for x in range(10)]
squares

#세트에 활용하기
{x*x for x in range(-9, 10)}

#딕셔너리에 활용하기
{x : x*x for x in range(10)}

# #### keypoint ( 요점 정리 )
#
# - 내포식은 파이썬의 핵심 기능
# - 내포식은 for 반복문 패턴을 구현하기 위한 간편 문법
# - 리스트, 세트, 딕셔너리에 모두 적용가능

# #  리스트 분할 트릭과 스시 연산자
# - 슬라이싱 기능
# - 인덱스 구문의 확장 기능
# - 정렬된 컬렉션에서 특정 범위 항목에 접근하는데 사용
# -'[start : stop : step]'

# +
lst = [1, 2, 3, 4, 5]

lst[0:4:2]
# -

lst[0:2]

# #### 스트라이드
# - 스텝 매개 변수를 사용

lst[::2] # 전체를 가져오는데 한칸씩 건너 뛰어

lst[::-1]

lst[:]

lst[::]

# #### 짚고 넘어가야 할 포인트
# - [:] 즉 슬라이싱을 하면 얕은 복사가 진행된다

# #### 리스트 항목을 제거하지만, 리스트 객체 자체는 유지함

del lst[:]
lst

# #### 에러나는 이유
# - 2 번째 줄에서 리스트가 복사되어 a가 새로운 lst 객체를 가리킨다
# - del a 로 인해 lst[:]는 있지만 a가 지워졌다
# - 때문에 define 되지 않았다는 에러가 뜬다

lst = [1,2,3]
a=lst[:]
print( id (a))
print( id(lst))
del a
print( id(a))

lst = [1,2,3]
a=lst[:] # 슬라이싱이지만 슬라이싱한 부분을 재할당 함으로 복사된다
print( id (a))
print( id(lst))
del lst[:2] # lst 슬라이싱 개념으로 들어간다 ( list라는 객체에서 수행 된다 )
print( id(a))
print(lst)
print( a)

original_lst = lst
lst[:] = [7,8,9] # 이 부분에서 [:]를 하지 않는다면 lst에 재할당 되므로 연결이 끊어진다
# 그러나 [:]를 붙이면 lst 객체 자체를 가리키고, 그 부분은 [7,8,9] 이므로
# original_lst도 변하게 된다
print(original_lst)
print( id(original_lst))
print( id (lst))

# lst가 재할당 됨으로 연결이 끊어짐
original_lst = lst
lst = [1, 2, 3]
print(lst)
print(original_lst)
print(id(original_lst))
print(id(lst))

# #### keypoint
# - '스시연산자'는 리스트의 하위 리스트를 선택하는 데 유용할 뿐 아니라, 리스트를 비우거나 거꾸로 뒤집거나 복사하는 데 사용
# - 하지만 이 기능을 모르는 팀원들은 혼란스러움

# # 아름다운 이터레이터
# - 파이썬의 '이터레이터 프로토콜'을 보면 파이썬 객체에서도 동일한 프로그래밍 스타일을 지원할 수 있음
# - __ iter __ , __ next __ 를 지원하는 객체는 for-in 반복문에서 자동으로 작동
# - 이터레이터 프로토콜을 지원하는 클래스 작성하기

# #### 무한 반복

repeater = Repeater('Hello')
for item in repeater:
    print(item)


# #### 짚고 넘어가야할 부분
# - iter 던더 메서드 작성
# - 이 던더 메서드에서는 RepeatoerIterator 객체를 생성하고 반환함
#     - 이 RepeatoerIterator는 for-in 반복문 예제가 작동하도록 하기 위한 도우미 클래스

class Repeater:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return RepeaterIterator(self)


# #### 짚고 넘어가야 할 부분
#
#     1. __ init __ 메서드에서 Repeater 객체에 각 RepeaterIterator 인스턴스를 연결
#         - 반복될 '소스' 객체를 유지
#     2. RepeaterIterator. __ next __ 에서 '소스' Repeater 인스턴스로 돌아가 연결된 소스 값 반환

class RepeaterIterator:
    def __init__(self, source):
        self.source = source
    def __next__(self):
        return self.source.value


# #### 두 클래스의 의미
#
# - Repeator 클래스와 RepeaterIterator는 함께 작동하여 파이썬의 이터레이터 프로토콜을 지원
#     - __ iter __ , __ next __ 가 파이썬 객체를 반복 가능하게 만드는 keypoint
# - for - in 반복과 호환되는 Repeater 객체를 만들었음
# - 아래 코드를 보면 무한 반복

# +
repeater = Repeater('Hello')

for item in repeater:
    print(item)
# -

# # 파이썬에서 for-in 반복문은 어떻게  동작할까?

# - 먼저 __ iter __ 메서드를 호출하여 반복을 위한 repeater 객체를 준비했음
#      - 이 메서드는 실제 '이터레이터 객체'를 반환
# - 그 후 값들을 검색하기 위해 이터레이터 객체의 __ next __ 메서드를 반복적으로 호출

repeater = Repeater('Hello')
iterator = repeater.__iter__()
while True:
    item = iterator.__next__()
    print(item)

# #### 설명
# - 이터레이터는 컨테이너의 내부 구조와 완전히 분리된 상태에서 컨테이너의 모든 항목을 처리할 수 있는 인터페이스 제공

# - 이 반복문은 이터레이터 프로토콜을 사용하는 방법을 파이썬 인터프리터 세션에서 수동으로 '에뮬레이트' 할 수 있음
# - emulate : 기능을 다른 소프트웨서 구현하여 똑같은 기능을 하도록 하는 것

repeater = Repeater('Hello')
iterator = repeater.__iter__()
next(iterator)


# #### 던더 메소드의 의미 ( facade( 퍼사드 ) 함수와 같음 )
#
# - 변수.__ iter __ () ,변수. __ next __ ()는 iter(변수), next(변수)와 같음
# - x.__ len __ () ----> len(x) 와 같음

# # 더 단순한 이터레이터 클래스

# #### 앞의 예제
# - Repeator 와 RepeatorIterator 두개의 분리된 클래스 사용
# - Repeator에서 __ iter __ 를 호출한 다음, RepeatorIterator 에서 __ next __ 를 통해 다음 값을 가져왔음
#

# #### 하나의 클래스 만들기

# - iter 는 인스턴스 객체를 받아오고 ( 반복 해야할 객체 )
# - next는 다음 값을 받아옴

class Repeater:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.value

# # 누가 무한 반복을 원하겠는가








