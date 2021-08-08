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

# # equal(동등한) 과 identical(동일한)
#
# - is 와 == 의 동작 차이 인지
# - == 동등 여부 확인, is 는 동일 여부 확인

# +
a = [1, 2, 3]
b = a
print(a)
print(b)
print()
print(a==b) # 동등한 지를 확인
print()
# 두 변수가 하나의 리스트 객체를 가리키고 있음을 확인

print(a is b) # 동일한 지를 확인


# +
# a 리스트 객체를 복사해 c에 넣음
# a와 c는 동등하지만 동일하지는 않다
# 서로 다른 객체를 가리키고 있음

c = list(a)
print(c)
print()
print(a==c)
print()
print(a is c)


# -

# #### keypoint( 동등 과 동일 )
#
# - 두 변수가 동일(identical)한 객체를 가리키는 경우 is 표현식은 True
# - == 표현식은 변수가 참조하는 객체가 동등한(equal: 내용이 같은) 경우 True로 평가
#

# # 문자열 변환 ( 모든 클래스는 __repr__이 필요하다 )
#
# - 파이썬에서 사용자 정의 클래스를 만들고 그 인스턴스를 콘솔에 출력해 보면 ( 인터프리터 세션에서 보면 ) 결과가 비교적 만족스럽지 않음
# - '문자열로' 전환하는 기본 동작이 기초적이고 세부 내용이 부족하기 떄문

# ## 클래스 사용 시
#
# - 기본적으로 얻을 수 있는 것은 클래스명과 객체 인스턴스의 id(Cpython에서는 객체의 메모리 주소)를 포함하는 문자열
# - 클래스의 속성을 직접 출력하거나 클래스에 사용자 정의 to_string() 메서드를 추가하여 문제 해결가능

# +
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

my_car = Car('red', 37281)
print(my_car)
# -

# 문제 해결 1
print( my_car.color, my_car.mileage)


# #### 이 방법의 문제점
# - 파이썬이 객체를 문자열로 표현하는 데 사용하는 규칙과 기본 제공 메커니즘을 무시함
# - 자신만의 문자열 변환 시스템을 만드는 대신 클래스에 __ str __ 과 __ repr __ (던더) 메서드를 추가하는 것이 좋음
# - 서로 다른 상황에서 객체가 문자열로 전환되는 방식은 제어하는 파이다운 방식
# - 아래 코드를 볼것

# #### 이 방식은 인스턴스 출력이나 검사시 개선된 결과를 얻을 수 있음

# +
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        
    def __str__(self):
        return f' a {self.color} car '
    
my_car = Car('red', 37281)
print(my_car)
my_car
# -

print(my_car)
print(type(my_car))
print(str(my_car))
print(type(str(my_car)))
print(f'{my_car}')
print(type(f'{my_car}'))


# ### 위의 예제가 던져주는 메세지
#     - __ str __ 구현을 사용하면 객체 속성을 직접 출력하거나, 별도의 to_string()함수를 작성할 필요 없음
#     - 문자열 전환을 제어하는 파이썬 다운 방식
#     - 사용자가 정의한 메서드나 속성과의 충돌을 피하는 데 도움이 됨
#     - 던더 메서드를 친숙히 할 것

# #  __ str __ vs __ repr __
#
# - 그러나 여전히 my_car 를 인터프리터 세션에서 검사하면 주소가 나옴
# - 이는 파이썬에서 객체가 문자열로 변환되는 방법을 제어아는 던더 메서드가 '2 가지' 이기 때문
# - 첫 번째는, __ str __ 이고, 두번 째는 __ repr __ 임
# - __ repr __ 의 동작 방식은 __ str __ 과 유사하지만 다른 상황에서 사용됨

# +
# 예시
# 차이 알아보기

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return ' __str__ for Car'
    
    def __repr__(self):
        return '__repr__ for Car'
    
my_car = Car('red', 37281)
print(my_car)
print()
print(f'{my_car}')
print()
my_car
# -

# 리스트나 딕셔너리는 __repr__을 사용함
str([my_car])

str({my_car})

# #### 위의 예제가 던져주는 메세지
# - 코드의 의도를 좀 더 명확하게 표현하기 우해 문자열 전환 메서드를 직접 선택하고자 한다면 str(),rper() 함수를 사용하는 것이 좋음
# - 이 함수들이 사용하는 편이 보기 좋으면서 결과가 똑같기에 __ str __ 또는 __ rper __ 을 직접 호출하는 것보다 바람직

# 즉 아래처럼 호출하라는 의미
print(str(my_car))
print(repr(my_car))

# ### __ repr __ 과 __ str __ 차이점 알아보기
# - datetime.date 객체를 만들고 문자열 변환을 제어하는 방법을 알아봄

# +
import datetime

today = datetime.datetime.today()

str(today)
# -

# #### 위 코드의 의미
# - 날짜 객체의 __ str __ 함수 결과는 원래 '읽을 수' 있어야 함
# - 이 함수의 목적은 애플리케이션 사용자에게 보여 줘도 괜찮을 정도로 사람이 읽을 수 있는 간결한 텍스트 표현을 반환하는 것
# - 즉 str(today) 는 ISO 날짜 형식과 비슷한 것을 얻게 되는 것

repr(today)


# #### 위 코드의 의미
#
# - __ reper __ 을 사용하면 그 결과는 무엇보다 명확해야함
# - 이 메서드의 결과 문자열은 개발자의 디버깅을 도와주려는 의도를 강하게 반영
# - 그 대상이 무엇인지 가능한 명시적으로 밝혀야 함
# - repr()을 호출하면 더 정교한 결과를 얻게 됨
# - 즉 전체 모듈과 클래스 이름까지 포함됨

# #### 모든 클래스에 __ repr __ 이 필요한 이유
#
# - __ str __ 메서드를 추가하지 않으면 파이썬을 __ str __ 을 사용해야 할 때도 __ repr __ 을 사용한다. 따라서 클래스에 적어도 __ repr __ 메서드는 항상 추가하는 것이 좋음
# - 최소한의 구현으로 거의 모든 경우에 유용한 문자열 변환 결과가 보장됨
# - 기본 문자열 변환 지원을 빠르고 효율적으로 클래스에 추가하는 방법은 다음과 같음
#     - def __ repr __ (self): return f'Car({self.color!r}, {self.mileage!r})'
#     - !r 변환 플래그를 사용하며 출력 문자열이 str(self.color)와 str(self.mileage) 대신 repr(self.color)와 repr(self.mileage)
#         - 다만, 형식 문자열 내에서 클래스명을 반복 사용한다는 것이 아쉬움
#         - 이 반복을 피하기 위해 __ class __ . __ namge __ 속성을 사용함
#             - 이 방식은 클래스 이름이 변경 될때, __ repr __ 구현을 수정하지 않아도 됨
#             - 중복 배체 원칙을 따르게 됨

# +
# 최종 __repr__ 사용

def __repr__(self):
    return ( f'{self.__class__.__name__}(' f'{self.color}, {self.mileage})')

# 이 구현의 단점
# 형식 문자열이 상당히 길어서 다루기 힘들다는 것
# 그러나 신중하게 형식화하면 코드를 못지게 유지하고 PEP8을 준수 할 수 있음



# +
# 최종코드
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return f'a {self.color} Car'
    
    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color}, {self.mileage})')
  
my_car = Car('red', 37281)
print(repr(my_car))
print()
print(str(my_car))
print()
print(my_car)
print()


# -

# #### keypoint ( __ repr __ vs __ str __ )
#
# - str 및 repr 던더 메서드를 사용하여 자신의 클래스에서 문자열 변환을 제어 가능
# - __ str __ 의 결과는 읽을 수 있어야 함 . __ repr __ 의 결과는 모호하지 않아야 함
# - 항상 __ repr __ 을 추가하라. __ str __ 의 기본 구현은 __ repr __ 을 호출하기만 함
#

# # 자신만의 예외 클래스 정의하기
#
# - 사용자 정의 예외 처리 클래스를 작성하는 것은 큰 가치가 있음
# - 잠재적인 에러 사례가 분명하게 드러나게 되므로 결과적으로 함수와 모듈을 유지 보수하기 더 쉬워짐
# - 사용자 정의 에러 타입을 사용하여 디버깅 정보를 추가 제공 가능
#

# #### 아래 코드 설명
# - ValeError와 같은 '상위 수준' 일반 예외 클래스를 사용하는 데는 단점이 존재
# - 함수를 라이브러리로 제공했고 내부를 잘 알지 못하는 팀원이 호출한다면, 이 검사를 실패하면 디버그 스택 추적에서 도움이 되지 않음

def validatae(name):
    if len(name)<10:
        raise ValueError


# #### 보완코드

# +
class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name)<10:
        raise NameTooShortError(name)


# -

validate('jane')


class BaseValidationError(ValueError):
    pass
class NameTooShortError(BaseValidationError):
    pass
class NameTooLongError(BaseValidationError):
    pass
class NameTooCuteError(BaseValidationError):
    pass


try:
    validate(name)
except BaseValidationError as err :
    handle_validation_error(err)

# #### keypoint ( 자신 만의 예외 클래스 정의하기 )
#
# - 고유한 예외 타입을 정의하면 코드의 의도가 좀 더 명확하게 표시되고 디버그하기 쉬워짐
# - 파이썬 내장 Exeption 클래스 또는 ValueError나 KeyError 와 같은 구체적인 예외 클래스에서 사용자 정의 예외를 파생
# - 상송을 사용하여 논리적으로 그룹화된 예외 계층을 정의

# # 객체 복제하기
#
# - 파이썬의 할당문(assignment statement)은 객체의 사본을 만들지 않으며 이름만 연결
# - 변경할 수 없는 객체의 경우에는 일반적으로 차이가 없음
# - 변경 가능한 객체 또는 변경 가능한 객체의 컬렉션(collection)을 다룰 때면 이러한 객체의 '실체 사본' 또는 '복제본'을 만드는 방법이 필요

# 컬렉션 복사하는 방법
#
# - 리스트, 딕셔너리, 세트 같은 변경 가능한 내장 컬렉션은 기존 컬렉션을 팩터리 함수에 건에 복사함

new_list = list(original_list)
new_dict = dict(original_dict)
new_set = set(original_set)

# #### 이 메서드의 문제
#
# - 사용자 정의 객체는 처리하지 못하며, 그보다 더 근본적으로 '얉은 복사본'을 만듬
# - '얕은 복사'와 '깊은 복사'의 차이
#     - '얕은 복사'
#         - 새 컬렉션 객체를 생성한 다음 원래 객체에서 찾은 자식 객체에 대한 참조로 채우는 것
#         - '얕은 복사'는 '한 단계 깊이'까지만 복사함
#         - 복사 프로세스가 재귀적으로 진행되지 않음으로 자식 객체 자체의 복사본을 만들지 않음
#         
#     - '깊은 복사'
#         - 복사 프로세스를 재귀적으로 처리
#         - 새 컬렉션 객체를 생성한 다음 원래 객체에서 찾은 자식 객체의 복사본을 재귀적으로 채우는 것을 의미함
#         - 객체의 전체 객체 트리를 따라 그 자식들까지 완전히 독립적으로 복사된 복제본을 만들 수 있음

# 얕은 복사 만들기
xs = [[1,2,3],[4,5,6],[7,8,9]]
ys = list(xs) # 얕은 복사 만들기


xs

ys

xs.append(['new student'])
xs

xs[1][0] = 'X'
ys

# 깊은 복사본 만들기
# copy.copy() 얇은 복사본 만들기
import copy
xs = [[1,2,3],[4,5,6],[7,8,9]]
zs = copy.deepcopy(xs)

# #### 의미
# - 내장 컬렉션의 경우 간단히 리스트, 딕셔너리, 세트의 팩터리 함수를 이용하여 얕은 복사본을 사용하는 것이 더 파이썬다운것


