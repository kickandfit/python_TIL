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

# #### 임의의 객체 복사하기
#
#
# - copy.copy() : 얕은 복사
# - copy.deepcopy() : 깊은 복사
#

# # !r은 repr에 적용할때 사용함
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__ (self):
        return f'Point({self.x!r}, {self.y!r})'



# +
import copy

a = Point(23, 42)
b = copy.copy(a)

b
# -

a is b


# #### 이 부분에서의 핵심
# - 점(point) 객체는 좌표에 원시 타입(정수형)을 사용하기 때문에 이 경우 얕은 복사와 깊은 복사에는 차이가 없음

# +
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__ (self):
        return f'Point({self.x!r}, {self.y!r})'
    
class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright
        
    def __repr__(self):
        return (f'Rectangle({self.topleft!r},' f'{self.bottomright!r})')
    
rect = Rectangle(Point(0,1), Point(5,6))
srect = copy.copy(rect)

rect
# -

srect

rect is srect

rect.topleft.x = 999
srect

drect = copy.deepcopy(rect)
drect.topleft.x =222
drect

srect

rect


# #### keypoint ( 객체 복사하기 )
#
# - 객체의 얕은 복사본을 만들면 자식 객체가 복제되지 않는다. 따라서 사본은 원본과 완전히 독립적이지 않다
# - 깊은 복사는 객체의 자식 객체를 재귀적으로 복사한다. 복사본과 원본은 완전히 독립적이지만 시간이 더 걸린다
# - copy 모듈을 사용하여 임의의 객체를 복사할 수 있다

# # 추상화 클래스는 상속을 확인한다
#
# - 추상화 클래스는 파생 클래스가 기반 클래스의 특정 메서드를 구현함을 보장함
# - 추상화 클래스의 이점과 파이썬에 내장된 abc 모듈로 추상화 클래스를 정의하는 방법
#

# #### 유지 보수하기 좋도록 확인 사항
# - 기본 클래스를 인스턴스화하는 것은 불가능
# - 서브클래스에서 인터페이스 메서드를 구현하는 것을 잊어버리면 가능한 빨리 에러를 발생시킴

# +
class Base:
    def foo(self):
        raise NotImplementedError()
    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return 'foo() called'
    
    # 이런, bar()를 재정의하는 걸 잊어버렸네
    # def bar(self):
    #     return "bar() called"


# -

# #### 방금 코드가 던져주는 의미
#
# - Base의 인스턴스에서 메서드를 호출하면 NotImplementedError 가 올바르게 발생함

b = Base()
b.foo()

c = Concrete()
c.foo()

c.bar()

# #### 첫 번째 구현은 좋지만 완벽하지 않음
#
# - Base를 인스턴스화해도 에러가 나지 않는다.
# - 불완전한 서브클래스를 제공한다. Concrete를 인스턴스화해도 누락된 bar() 메서드를 호출하기 전에는 에러를 발생시키지 않음

# +
from abc import ABCMeta, abstractmethod

class Base(metaclass = ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    
    @abstractmethod
    def bar(self):
        pass
    
class Concrete(Base):
    def foo(self):
        pass
    
    # bar()를 선언하는 걸 또 잊어버렸다.
    
assert issubclass(Concrete, Base)

c = Concrete()
# -

# ####  이렇게 작성하면 유용한 점 ( 위의 코드 )
# - Base의 서브클래스에서 추상 메서드 구현을 깜박했다면
# - '인스턴스화할 때' TypeError를 발생시김
# - 또한 발생한 예외는 누락된 메서드가 무엇인지 알려줌
# - abc 없이는 누락된 메서드가 실제로 호출된 경우에만 NotImplementedError를 발생

# #### keypoint( 추상화 클래스 ABC ( Abstract Base Class))
#
# - 추상화 클래스는 파생 클래스가 인스턴스화될 때 기반 클래스의 추상 메서드를 모두 구현하였는지 확인한다.
# - 추상화 클래스를 사용하면 버그를 방지하고 클래스 계층을 쉽게 유지 관리 할 수 있다.

# # 네임드튜플은 어디에 적합한가
# - 네임드튜플 컨테이너 타입이 있음
# - 네임드튜플은 클래스를 수동으로 정의하는 데 대한 훌륭한 대안
# - 기본 tuple 데이터 타입의 확장
#     - tuple 은 임의의 객체를 그룹화하기 위한 간단한 데이터 구조
#     - 불변이기에 생성되면 수정할 수 없음
#     - 튜플에 저장된 개별 속성에는 이름을 지정할 수 없음
#     - 튜플에는 같은 수의 필드와 같은 속성이 담겨 있다고 보장하지 못함
#     - 필드 순서를 혼동해서 '실수로 인한 버그'가 자주 발생

tup = ('hello', object(), 42)
tup

tup[2] = 23

# #### 해결사 네임트 튜플
# - 변경 불가능한 컨테이너
# - 최상위 속성에 데이터를 저장한 후 속성을 업데이트하여 데이터를 수정할 수 없음
# - 한 번만 쓰고 여러번 읽음의 원칙을 따름
# - 말 그대로 이름 지어진 튜플

# - 첫 번째 인자 매개 변수는 타입명이라고 하며 namedtuple 함수를 호출하여 생성되는 새 클래스의 이름
# - namedtuple은 우리가 결과 클래스를 할당할 변수명을 알 수 없기 때문에 사용할 클래스 이름을 명시적으로 알려 줘야함
# - 이 클래스명은 namedtuple이 개발자를 위해 자동으로 생성하는 독스트링과 __ repr __ 구현에 사용됨
#

# +
from collections import namedtuple

Car1 = namedtuple('Car', 'color mileage')

# -

'color mileage'.split()
Car2 = namedtuple('Car1323', ['color', 'mileage'])
my_car = Car2('red', 3812.4)
my_car.mileage

my_car[0]

tuple(my_car)

# +
color, mileage = my_car
print( color, mileage)

print(*my_car)
print(str(my_car))
# -

my_car

my_car.color = 'blue'

# #### 네임드튜플 정리
# - 내부적으로 일반 파이썬 클래스로 구현
# - 메모리 사용량도 일반 클래스보다 '좋음'
# - "네임드튜플은 파이썬에서 불변 클래스를 수동으로 정의할 때 사용할 수 있는 메모리 활용의 효율적인 지름길"

# ### 네임드튜플 상속하기
#
# - 네임드튜플은 일반 파이썬 클래스 위에서 만들어지기 때문에 네임드튜플 객체에 메서드 추가 가능

# +
from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color =='red':
            return '#ff0000'
        else:
            return '#000000'
        
c = MyCarWithMethods('red', 1234)
c.hexcolor()
# -

# #### 위 코드의 문제점
# - 다소 거추장 스러움
# - 불변 속성들로 구성된 클래스를 원한다면 할 만한 가치가 있을지도 모름
# - 새로운 '불변' 필드를 추가하기가 까다로움
# - 네임드튜플 계층을 만드는 가장 쉬운 방법은 기본 튜플의_fields 속성을 사용하는 것

Car = namedtuple('Car', 'color mileage')
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge', ))

ElectricCar('red', 1234, 45.0)

# #### 내장 도우미 메서드
#
# - _ fields 속성 외에도 각 네임드튜플 인스턴스는 유용한 몇 가지 도우미 메서드를 제공함
# - _ 로 시작함
# - 이 문자는 보통 해당 메서드나 속성이 클래스 또는 모듈의 안정된 공개 인터페이스의 일부가 아니라 '프라이빗'임을 뜻함
# - 네임드튜플의 경우 밑줄 명명 규칙은 다른 의미를 가짐
# - 네임드튜플에서는 밑줄로 시작하는 도우미 메서드 및 속성은 네임드튜플의 공개 인터페이스에 포함됨
# - 사용자 정의 튜플 필드와의 충돌을 피하기 위해 밑줄을 사용했을 뿐
#

# ####  네임드 튜플 딕셔너리로 변경하기

my_car._asdict()

import json
json.dumps(my_car._asdict())

# #### 네임드 튜플 (얕은) 복사본을 생성하고 필드의 일부 선택적 대체

my_car._replace(color='blue')

# #### 네임드 튜플 객체 시퀀스나 반복 가능 객체로부터 새로운 네임드튜플 인스턴스 생성

Car._make(['red',999])


# #### 네임드튜플을 사용하면 좋은 경우
#
# - 데이터를 잘 구조화하여 코드를 정돈하고 가독성이 더 좋게함
# - 딕셔너리처럼 형식이 고정된 임시 데이터 타입에서 네임드튜프로 바꾸면 개발자의 의도를 좀더 명확하게 표현 가능
# - 리팩터링을 시도하다 보면 자신이 직면한 문제에 대해 고민해볼 수있음
# - 구조화되지 않은 튜플과 딕셔너리 대신 네임드튜플을 사용하면 동료가 작업을 더 쉽게 수행할 수 있게 함
# - '더 깔끔하고' 유지 보수가 쉬운 코드를 작성하는 데 도움이 되지 않는 경우에는 네임드튜플 사용을 자제

# #### keypoint( 네임드튜플 )
#
# - collections.namedtuple은 불변 클래스를 수동으로 정의하는 메모리 효율적 지름길
# - 네임드 튜플은 데이터를 이해하기 쉬운 구조로 만들어 코드를 정리하는 데 도움을 줌
# - 네임트튜플은 유용한 도우미 메서드를 제공
#     - _ make, _ replace, _ asdict()

# # 클래스 변수 대 인스턴스 변수의 함정
#
# - 클래스 메서드와 인스턴스 메서드를 구별하는 것 외에도 파이썬의 객체 모델은 클래스아 인스턴스의 '변수'를 구별함
# - 파이썬 객체, '클래스 변수'와 '인스턴스 변수'라는 두가지 데이터 속성이 존재
# - 클래스 변수
#     - 클래스 정의 안에(그러나 인스턴스 메스드 밖에) 선언
#     - 특정 클래스 인스턴스에 묶여 있지 않음
#     - 클래스 자체에 내용을 저장, 같은 클래스에서 생성된 모든 객체는 동일한 클래스 변수 집합을 공유함
#     - 클래스변수를 수정하면 동시에 모든 객체 인스턴스에 영향을 미침
#
# - 인스턴스 변수
#     - 항상 특정 객체 인스턴스에 묶여 있음
#     - 그 내용은 클래스에 저장되지 않음 클래스에서 생성된 개별 객체에 저장됨
#     - 인스턴스 변수의 내용은 객체 인스턴스마다 완전히 독립적
#     - 해당 객체에만 영향을 미침

class Dog:
    num_legs = 4 # <-클래스 변수
    
    def __init__(self, name):
        self.name = name # <- 인스턴스 변수
        


# #### 새 Dog 인스턴스를 만들면 각 인스턴스는 name이라는 인스턴스 변수를 얻음

jack = Dog('jack')
jill = Dog('jill')
print( jack.name, jill.name)

print(jack.num_legs, jill.num_legs)

# #### 각 Dog 인스턴스 또는 '클래스 자체에서' num_legs에 접근 가능

jack.num_legs, jill.num_legs

Dog.num_legs

# #### 클래스르 통해 인스턴스 변수에 접근하려고 하면 에러 (Attribute Error)
#
# - 인스턴스 변수는 각 객체에 특정되고 __ init __ 생성자가 실행될 때 마다 생성
# - 클래스 자체에는 존재하지 않음
#
#     - 이것이 클래스 변수와 인스턴스 변수의 주요 차이점

Dog.name

# #### 클래스 변수를 바꾸면 모든 인스터스에 영향을 미침

# +
# 클래스 변수 바꾸기

Dog.num_legs = 6
# -

jack.num_legs, jill.num_legs

# +
# 인스턴스에서 클래스 변수에 해당하는 값 바꿔보기
Dog.num_legs=4
jack.num_legs= 6

jack.num_legs, jill.num_legs, Dog.num_legs
# -

# #### 위의 코드
#
# - 원하는 결과를 얻은 것 같이 보임
# - 문제는 잭 인스턴스에 num_legs 인스턴스 변수를 도입했다는 점
# - 새로운 num_legs 인스턴스 변수는 동일한 이름의 클래스 변수를 '가려' 객체 인스턴스 범위에 접글할 때 이를 무시하고 숨김

# 마지막 말 설명 예제 코드
jack.num_legs, jack.__class__.num_legs


# - 즉 이 클래스 변수는 '동기화 되지 않는' 것처럼 보임
# - 그 이유는 jack.num_legs에 값을 써서 클래스 변수와 똑같은 이름의 인스턴스 변수가 만들어졌기 때문
# - 나쁜 것은 아니지만 이 뒤에서 무슨 일이 일어나는 것인지는 인지해야함
#     - 사실은, 객체 인스턴스를 통해 클래스 변수를 수정하려고 시도하는 것, 즉 실수로 이름이 같은 인스턴스 변수를 만들어 원래 클래스 변수를 가리는 것은 객체 지향프로그래밍의 함정

# #### 개가 없는 예제
#

# - CountedObject는 공유 카운터 역할을 하는 num_instances 를 클래스 변수를 갖고, 클래스가 선언되면 카운터가 0으로 초기화된 채로 있음

class CountedObject:
    num_instances = 0
    
    def __init__(self):
        self.__class__.num_instances += 1




