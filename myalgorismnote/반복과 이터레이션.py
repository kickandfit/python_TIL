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

# #### BoundedRepeater를 활용한 정의된 반복 횟수 후 중지 기능

# #### 기본 idea
# - 컨테이너에서 컬렉션으로 모두 사용하면 StopIteration 예외를 발생시키자

class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value
    


# #### 파이썬 다운 코드

repeater = BoundedRepeater('Hello' , 3)
for item in repeater:
    print(item)

# #### 코드 간편 문법 제거하기

repeater = BoundedRepeater('Hello',3)
iterator = iter(repeater)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print(item)


# #### keypoint( 아름다운 이터레이터 )
# - 이터레이터는 파이선 객체에 대한 시퀀스 인터페이스르 제공한다
#     - 메모리 효율적이며 파이썬 답다
# - 반복을 지원하려는 객체는 __ iter __ 및 __ next __ 던더 메서드를 제공하여 이터레이터 프로토콜을 구현해야함
# - 클래스 기반 이터레이터는 파이썬에서 반복 가능한 객체를 만드는 방법 중 하나일 뿐

# # 제너레이터는 단순화된 이터레이터다
#
# - 클래스 기반 이터레이터는 상용구(boilerplate) 코드가 많이 필요함
# - '제너레이터'와 yield 키워드롤 사용하여 적은 코드로 이터레이터를 만들 수 있음

# ## 무한 제너레이터

# #### 제너레이터
#
# - 일반 함수와 달리 yield를 사용하여 데이터를 호출자에게 전달

def repeater(value):
    while True:
        yield value


for x in repeater('Hi'):
    print(x)

# #### 제너레이터는 어떻게 작동할까?
# - 우선 제너레이터 함수를 호출해도 함수가 실행되지 않음
# - '제너레이터 객체'를 만들고 반환할 뿐
# - 제너레이터 함수의 코드는 제너레이터 객체에서 next()가 호출될 때만 실행됨

repeater('Hey')

# next 호출시에만 실행
generator_obj = repeater('Hey')
next(generator_obj)


# ####  제너레이터 동작원리
# - 함수 안에서 return문이 실행되면 호출자에게 제어권을 영구적으로 넘김
# - 반면 yield가 호출되면 함수의 호출자에게 제어권을 전달하지만 '일시적'임
# - return 문이 함수의 로컬 상태를 삭제하는 반면, yield 문은 함수를 일시적으로 중단하고 로컬 상태를 유지
# - 실질적으로 이것은 지역 변수와 제너레이터 함수 실행 상태가 잠시 숨겨질 뿐 완전히 사라지지 않음을 의미
# - next()를 호출하여 언제든 다시 시작할 수 있음

# ## 생성을 멈추는 제너레이터

# #### 제너레이터 함수가 yield 이외의 방식으로 반환되면 그 순간 값 생성을 중단함
#

def repeat_three_times(value):
    yield value
    yield value
    yield value



for x in repeat_three_times('Hey'):
    print(x)


# #### 지정횟수 만큼 생성하는 제너레이터

def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value


for x in bounded_repeater('Hi', 4):
    print(x)


# #### 최종구현

def bounded_repeater(value, max_repeats):
    for x in range(max_repeats):
        yield value


# #### keypoint( 제너레이터는 단순한 이터레이터다 )
# - 제너레이터 함수는 이터레이터 프로토콜을 지원하는 객체를 작성하기 위한 간편문법
#     - 제너레이터는 클래스 기반 이터레이터를 작성할 때 필요한 상용구 코드를 대부분 추상화한다
# - yield 문을 사용하면 제너레이터 함수 실행을 일시적으로 중단하고 값을 되돌려 줄 수 있다
# - 제어 흐림이 yield문 이외의 방법으로 제너레이터 함수를 떠나면 제너레이터는 StopIteration 예외를 발생시킨다

# ## 제너레이터 표현식

iterator = ('Hello' for i in range(3))
iterator


# #### 위코드는 bounded_repeater 제너레이터 함수와 동일한 값 시퀀스를 생성

# +
#두 코드는 같은 코드
def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value

iterator = bounded_repeater('Hello', 3)
# 한줄 쓰기

iterator = ('Hello' for i in range(3)) # 다만 일회용
# -

# #### 주의 사항
# - 제너레이터 표현식은 한 번 사용되면 다시 시작하거나 사용할 수 없음
# - 어떤 경우에는 제너레이터 함수나 클래스 기반 이터레이터를 사용하는 것이 좋음

# ### 제너레이터 표현식 대 리스트 내포식

listcomp = ['Hello' for _ in range(3)]
genexpr = ('Hello' for _ in range(3))

# #### 차이점
# - 리스트 내포식은 리스트 객체 생성
# - 제너레이터 표현식은 리스트를 생성하지 않음
#     - 클래스 기반 이터레이터 또는 제너레이터 함수처럼 '필요할 때' 값을 생성함
# - 제너레이터 표현식을 변수에 할당하면 얻을 수 있는 것은 반복 가능한 '제너레이터' 객체
# - 제너레이터 표현식이 생성하는 값에 접근하려면 next()를 호출해야함
#     - 생성된 모든 값을 담을 리스트 객체를 만들기 위해서는 제너레이터 표현식을 리스트로 호출

list(genexpr)

# ### 값 걸러 내기

even_squares = (x*x for x in range(10) if x%2 ==0)
for x in even_squares:
    print(x)


# +
#코드 구조화

def generator():
    for item in collection:
        if condition:
            yield expression


# -

# ### 인라인 제너레이터 표현식

# #### 인라인 제너레이터 표현식
# - '필요할 때' 생성하기 때문에 매우 메모리 효율적

for x in ('Bob dia' for i in range(3)):
    print(x)

sum((x*2 for x in range(10)))

# sum() 의 소괄호 생략가능
sum(x*2 for x in range(10))


# ### 너무 좋더라도
#
# - 중첩된 제너레이터 표현식은 쓰지 말것. 유지보수가 힘들어짐

# #### keypoint ( 제너레이터 표현식 )
#
# - 제너레이터 표현식은 리스트 내포식과 비슷
#     - 리스트 객체는 생성하지 않음
#     - '필요할 때'만 값을 생성함
# - 제너레이터 표현식은 한 번 사용되면 다시 생성하거나 재사용할 수 없음
# - 제너레이터 표현식은 간단한 '임시' 이터레이터를 구현하는 데 가장 적합함
#     - 복잡한 이터레이터의 경우 제너레이터 함수 또는 클래스 기반 이터레이터를 작성하는 것이 좋음

# ## 이터레이터 체인
# - 여러 개의 이터레이터를 연결함으로써 매우 효율적인 데이터 처리 '파이프 라인'을 작성할 수 있음

# 1에서 8가지 일련의 정수값 생성 제너레이터
def integers():
    for i in range(1,9):
        yield i
chain = integers()
list(chain)


# +
# 다른 이터레이터와 연결 하기

def squared(seq):
    for i in seq:
        yield i*i
chain = squared(integers())
list(chain)


# -

# - '데이터 파이프라인' 또는 '제너레이터 체인'이 동작하는 모습
#     - 파이프라인에 새로운 블링 블록을 추가할 수 있음
#     - 데이터는 한 방향으로만 흐르고 각 처리 단계는 잘 정의된 인터페이스를 통해 다른 처리 단계와 격리

# +
def negated(seq):
    for i in seq:
        yield -i

chain = negated(squared(integers()))
list(chain)
# -

# #### 중요한 점
# - '한 번에 한 항목씩' 이뤄짐
# - 체인 처리 단계 사이에 버퍼링이 없음
#     - 다음의 처리 단계들이 한번에 수행
#     1. integers 제너레이터는 단일 값을 산출함. 3이라고 가정
#     2. 이는 squared 제너레이터를 '활성화'하여 3X3을 처리하여 그 결과인 9를 다음 단계로 전달
#     3. squared 제너레이터에 의해 생성된 제곱수는 즉시 negated 제너레이터로 공급되고 -9로 수정하여 값을 내보냄
#     

# +
# 가독성 높이기

integers = range(8)
squared = (i*i for i in integers)
negated = (-i for i in squared)

list(negated)
# -

# #### 단점
#
# - 제너레이터 표현식은 함수 인자로 구성활 수 없음
# - 하나의 처리 파이프라인에서 동일한 제너레이터 표현식을 여러번 재사용할 수 없음
#

# #### keypoint( 이터레이터 체인 )
#
# - 제너레이터는 효율적이고 유지 보수가 쉬운 데이터 처리 파이프라인을 형성하기 위해 연결될 수 있음
# - 체인으로 연결된 제너레이터들은 체인을 통과하는 각 항목을 개별적으로 처리
# - 제너레이터 표현식을 사용하여 파이프라인 정의를 간결하게 작성할 수 있지만 가독성에 영향을 줄 수 있음


