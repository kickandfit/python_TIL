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

# # 딕셔너리 트릭
#
# - 딕셔너리에는 대쳇값을 제공하면서 키를 찾는 get()메서드가 있음

# +
name_for_userid = {382 : "Alice", 
                  950 : "Bob",
                  590 : "Dilbert"}

def greeting(userid):
    return 'Hi %s !' %name_for_userid[userid]


# -

greeting(382)

greeting(33333)


# #### 하고 싶은 것
# - 사용자 아이디를 찾을 수 없는 경우 함수가 예외 대신 일반적인 인사말을 반환

def greeting(userid):
    if userid in name_for_userid:
        return 'Hi %s !' %name_for_userid[userid]
    else:
        return 'Hi there!'



greeting(33333)


# #### 문제점
# - 딕셔너리를 두 번 조회하기 때문에 비효율적
# - 인사말 문자열의 일부가 반복되기 때문에 장황
# - '파이썬답지' 않음
#     - 공식 문서에서는 허가보다 용서를 구하는게 쉽다( Easier to Ask for Forgiveness than Permission) 코딩 스타일 권장
#     - 파이썬 코딩 스타일은 유효한 키 혹은 속성이 존재한다고 가정, 가정이 틀렸다고 판명되면 예외를 처리하는 방식

# 파이썬 다운 코딩은
# # %s 는 문자열을 출력해라 ( %d 정수형, %f 실수형)
#예 1) %03d : 정수를 3칸에 맞추어 출력하는데 앞의 빈칸은 0으로 채워라
#예 2) %6.2f : 실수를 전체 6칸 소수이하 2칸에 맞추어 출력하라
def greeting(userid):
    try:
        return 'Hi %s'% name_for_userid[userid]
    except:
        return 'Hi there'


# #### 문제점
# - 두 번 조회하지 않으나 여전히 장황
#

# get() 메서드 활용 : get( 변수, 반환값) 변수가 키에 없다면, 반환값을 반환
def greeting(userid):
    return 'Hi %s!'% name_for_userid[userid].get(userid, 'there')


# #### keypoint( 딕셔너리 기본값 )
# - 멤버십을 테스트할 때 딕셔너리의 키를 명시적으로 확인하지 말것
# - EAEP 스타일의 예외 처리 또는 내장된 get() 메서드를 사용하는 편이 바람직함
# - 어떤 경우에는 표준 라이브러리의 collections.defaultdict 클래스가 도움이 됨

# # 재미있고 효과도 좋은 딕셔너리 정렬

xs = {'a':4, 'b':2 ,'c': 3, 'd': 1}

# #### 이를 정렬하기 위해서는 items()로 받아 정렬함
# - items()는 키-값 을 튜플로 묶어 반환
# - sorted를 통해 정렬

sorted(xs.items())

# #### 원리
# - 튜플들은 키 중복을 허용하지 않는 딕셔너리에서 가져온 것임으로, 첫 번째 인덱스 값은 고유함
# - 두 튜플을 비교할 때는 먼저 인덱스 0에 저장된 항목끼리 비교하고, 같다면 다음 인덱스 항목 비교
# - 따라서 딕셔너리에서 가져온 튜플은 첫번재 인덱스만을 가지고 비교함

# #### 키 함수
#
# - 키 함수는 단순히 비교하기 전에 각 요소에 대해 호출되는 일반적인 파이썬 함수
# - 키 함수는 딕셔너리 항목을 입력으로 받아 정렬 순서 비교를 위해 원하는 키를 반환
# - 문제는 '키'라는 단어가 두 가지 문맥에서 동시에 사용
#
# 키 함수는 딕셔너리 키를 다루지 않으며 그저 각 입력 항목을 임의의 비교 키로 연결하는 역할

sorted(xs.items(), key = lambda x:x[1])

# #### 키함수 개념 잡기
# - operator라는 모듈에 관련 기능을 구현
#     - 자주 쓰이는 키 함수들을 바로 쓸 수 있는 빌딩 블록 형태로 제공
#     - operator.itemgetter와 operator.attrgetter가 있음

import operator
sorted(xs.items(), key = operator.itemgetter(1))

# #### operater 모듈 vs lambda 함수
# - operater 모듈을 사용하면 코드의 의도가 좀 더 명확해짐
# - 람다 표현식을 사용하면 읽기 쉽고 명료하게 표현
#     - 람다를 사용자 정의 키 함수로 사용하면 정렬 순서를 훨씬더 세밀하게 제어

# +
# 저장된 각 값의 절대 값을 기준으로 정렬

sorted(xs.items(), key = lambda x : abs(x[1]))

# -

# #### keypoint ( 재미있고 효과도 좋은 딕셔너리 정렬 )
#
# - 딕셔너리 및 기타 컬렉션의 정렬된 '뷰'를 만들 때 키 함수로 정렬 순서를 조정할 수 있음
# - 키 함수는 파이썬에서 중요한 개념
#     - 가장 많이 사용되는 키 함수들은 표준 라이브러리의 operator 모듈에 추가
# - 함수는 파이썬의 일급 시민으로, 파이썬 언어의 모든 곳에서 사용되는 강력한 기능

# # 딕셔너리로 switch/ case 문 모방하기
#
# - 파이썬에서는 switch/case 문이 없으므로 if.....elif.....else 체인을 쓰기도함
# - 딕셔너리를 활용하면 모방할 수 있음

def myfunc(a, b):
    return a + b


funcs = [myfunc]
funcs[0]

funcs[0](2,3)

# +
# 소름 돋는 아이디언데..?
# 이건 좀 소름이다
if cond == 'con_a':
    handle_a()
elif cond == 'con_b':
    handle_b()


func_dict = {
    'cond_a' : handle_a,
    'cond_b' : handle_b
}
func_dict.get(cond, handle_default)

cond = 'cond_a'
func_dict[cond]()


# -

# 활용
def dispatch_if(operator, x, y):
    if operator == 'add':
        return x+y
    elif operator == "sub":
        return x - y
    elif operator == 'mul':
        return x*y
    elif operator == 'div':
        return x/y


# #### 리뷰
# - dispatch_dict() 가 호출될 때마다 연산 코드 조회를 위한 임시 딕셔너리와 다수의 람다가 만들어짐
#     - 성능 측면에서 이상적이지 않음
#     - 빨리 처리해야 하는 코드의 경우 딕셔너리를 상수로 한 번만 만들어 놓고 함수가 호출될 떄 이를 참조하는 것이 적합
# - 간단한 산술연산을 원한다면, operator 모듈을 활용하라

# +
def dispatch_dict(operator, x, y): # operator 는 key 값을 호출하는 역할을 함
    return {
        'add' : lambda: x+y,
        'sub' : lambda: x-y,
        'mul' : lambda: x*y,
        'div' : lambda: x/y,
    }.get(operator, lambda: None)()# 이 뒤에 get 때문에 operator 가 key 탐색 역할을함/ 그리고 마지막()이 함수 인자전달 역할을함

#소름 돋는 코드다


# -

dispatch_dict('sub', 1, 2)

# #### keypoint ( 딕셔너리로 switch/case 구문 모방하기 )
#
# - 파이썬에는 switch/case 문이 없음
#     - 경우에 따라 딕셔너리 기반 처리 테이블을 사용하여 긴 if 체인을 피할 수 있음
# - 함수를 반환 받고 인자로 줄 수 있다는 것이 진짜 대단하구나...

# # 파이썬 딕셔너리 표현식의 특이점
#

# +
# 이건 뭐지?
{ True : 'yes' , 1 : 'no', 1.0 : 'maybe'}

# 결과가 뭘까 이게 도대체..
# -

xs = dict()
xs[True] = 'yes'
xs[1] = 'no'
xs[1.0] = 'maybe'
xs

# ####  위와 같은 결과가 나온 이유는, key가 모두 같다고 인지했기 때문
#
# - 파이썬은 bool을 int의 서브클래스로 취급
#     - 불타입은 정수형의 하위 타입이며 불값은 거의 모든 문맥에서 각각 0과 1처럼 동작하지만 문자열로 변환될때는 예외적으로 각각 'False' 또는 'True'다

True == 1 == 1.0

# True는 1과 같이 사용됨으로 인덱스로 사용될 수 있다
['no', 'yes'][True]


# #### {True: 'maybe'} 에서 key는 왜 여전히 True 인가
#
# - 키는 왜 여전히 True인가
#     - 반복된 할당으로 1.0으로 바뀌어야 정상아닌가?
#     - CPython 인터프리터 소스 코드에 의하면 딕셔너리는 새로운 값이 연결될 때, 키 객체 자체를 업데이트 하지는 않음
#     - value 값은 업데이트됨

# #### 딕셔너리 값이 덮어써진 이유는 단순히 키가 같아서 인 것처럼 보임
# - 사실 이 효과는 __ eq __ 동등성 검사만으로 인한 것이 아님
# - 파이썬 딕셔너리는 해시 테이블 데이터 구조로 뒷받침됨
# - 해시 테이블은 각 키의 해시값에 따라 키를 서로 다른 '메모리 영역'에 저장함
#     - 해시값은 키로부터 나오며 키를 고유하기 식별하는 고정 길이의 숫자값
#     - 키 객체 전체를 다른 키들과 동등성 검사를 수행하는 것 보다 조회 테이블에서 숫자인 해시 값을 찾는게 빠름
#     - 문제는 해시값 계싼법이 완벽하지 않다는점
#     - 실제로, 다른 둘 이상의 키가 같은 해시값을 가지게 되고, 결국 같은 조회 테이블 메모리에 저장됨
#     - 키 두 개가 같은 해시값을 갖고 있다면 이를 '해시 충돌'이라고 하며, 항목을 삽입하고 찾아내는 데 필요한 해시 테이블 알고리즘이 처리해야하는 특수한 경우임
#  

# #### 해시 충돌 문제인지를 알아보기 위한 검사

# #### 이 클래스의 특징
# - 첫째, __ eq __ 던더 메서드가 항상 True를 반환
#     - 때문에 이 클래스의 모든 인스턴스는 '어떠한' 다른 객체와도 동일한 것처럼 가장
# - 둘째, 각 AlwaysEquals 인스턴스 내장된 id() 함수에 의해 생성된 고유한 해시값을 반환

class AlwaysEquals:
    def __eq__(self, other):
        return True
    
    def __hash__(self):
        return id(self)


objects = [AlwaysEquals(),
          AlwaysEquals(),
          AlwaysEquals(),
          ]
[hash(obj) for obj in objects]

# #### 위 클래스는 True ,1 , 1.0 의 문제의 핵심을 정확하게 반영함
# - 다른 객체와 동일하다고 가장하지만
#     - 고유한 해시값을 갖는 객체를 만들 수 있음
#     - 이것은 동등성 비교 결과만으로 딕셔너리 키를 덮어쓰는지 시험해 볼 수 있음

# 동등한 키를 사용하더라도 더 이상 값이 덮어쓰이지 않음
{AlwaysEquals() : 'Yes' , AlwaysEquals(): 'no'}


# #### 아이디어를 뒤집어 동일한 해시값을 반환해도 키를 덮어 쓸수 있는지 확인

class SameHash:
    def __hash__(self):
        return 1


a = SameHash()
b = SameHash()

a ==b

hash(a), hash(b)

id(a), id(b)

{a: 'a', b: 'b'}

# #### 위 예제가 주는 의미
# - 해시 충돌만으로는 '키를 덮어쓰는' 효과는 발생하지 않음
#

# #### 결국
# - 딕셔너리는 동등성을 검사하고 해시값을 비교하여 두 개의 키가 같은지 여부를 결정
# - 즉 True, 1, 1.0 은 동등하고 해시값도 같기 때문에 '키를 덮어쓰는 효과'가 발생됨

True == 1 == 1.0

hash(1), hash(1.0), hash(True)

# #### keypoint ( 딕셔너리 표현식의 특이점 )
# - 딕셔너리는 __ eq __ 의 비교 결과가 동등하고 해시값이 같다면 키를 동일하게 취급
# - 예기치 않은 키 충돌로 인해 신기한 결과가 발생하기도 함

# ## 딕셔너리를 병합하는 많은 방법
#

# 방법 1
xs = {'a':1, 'b':2}
ys = {'b':3, 'c':4}
zs = {}
zs.update(xs)
zs.update(ys)
zs


# #### 고려해야할 문제
# - 키 충돌 문제, 다중 딕셔너리 병합에 대한 문제 고려

# update의 간단한 구현
def update(dict1, dict2):
    for key, value in dict2.items():
        dict[key] = value


# #### update()를 호출하는 순서가 충돌 해결 방식에 영향을 줌
# - 마지막 업데이트가 받아들여져 중복 키 'b'는 두 번째 소스 딕셔너리인 ys에서 나온 값 3과 연결됨
#     - 물론 딕셔너리 여러 개를 하나로 병합하기 위해 원하는 만큼 update()를 반복 호출 할 수 있음
#

# 방법이 인자 풀기( 두개의 딕셔너리 병합 )
zs = dict(xs, **ys) # xs에 ys를 병합해라
zs

# +
# 임의의 수의 딕셔너리를 병합하는 간단한 방법

zs = dict(**xs, **ys)
# 음 안되는데? 중복 키값을 처리를 못하는데
# 이론적으로는 오른쪽이 우선순위를 갖는다고 하는데 글쎄..
# -

# #### keypoint( 딕셔너리를 병합하는 여러 방법 )
#
# - 파이썬 3.5 dltkddptjsms ** 연산자를 사용한 표현식 하나로 딕셔너리 객체 여러개를 병합할 수 있음
#     - 적용은 왼쪽 부터임으로, 오른쪽 값이 덮어씀
# - update() 메서드를 대신 사용할 수 있음

# # 보기 좋은 딕셔너리 출력

mapping = {'a' : 23, 'b' : 42, 'c': 0Xc0ffee }
mapping

# #### json 모듈 사용하기

# +
import json

print(json.dumps(mapping, indent = 4, sort_keys = True))
# -

# #### 그러나 json 모듈로 딕셔너리로 출력하면
# - 기본 타입만을 담은 딕셔너리에서만 작동
# - 함수와 같이 기본이 아닌 데이터 타입을 포함하는 딕셔너리를 출력할 수 없음
# - json.dump() 에는 집합과 같은 복잡한 데이터 타입을 문자열화 할수 없다는 단점도 있음

# #### pprint 활용하기

# +
import pprint

mapping['d']= {1, 2, 3, 4}
pprint.pprint(mapping)
# -

mapping # 현재는 딕셔너리가 pprint와 같이 볼수 있어서 딱히..?

# #### keypoint ( 좋은 딕셔너리 출력 )
#
# - 딕셔너리 객체의 기본 문자열 변환은 읽기 어려울 수 있음
# - pprint 및 json 모듈은 파이썬 표준 라이브러리에 내장된 '고급' 옵션
# - json.dump()를 기본 데이터 타입이 아닌 키나 값과 함께 사용할 때는 Type Error 가 발생하므로 주의

# #### 해쉬란
#
# 용어
# - 해쉬(Hash): 임의 값을 고정 길이로 변환하는 것을 의미.
# - 해쉬 함수(Hash Function): 특정 연산을 이용하여 키 값을 받아서 value를 가진 공간의 주소로 바꾸어주는 함수를 의미.
# - 해쉬 테이블(Hash Table): 해쉬 구조를 사용하는 데이터 구조.
# - 해쉬 값(해쉬 주소, Hash Value or Address): Key값을 해쉬 함수에 넣어서 얻은 주소값을 의미. 이 값을 통해 슬롯을 찾아감.
# - 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간을 의미. (아래 그림에서는 bucket)
#
#
# ![image.png](attachment:image.png)
#
#


