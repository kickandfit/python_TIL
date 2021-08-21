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

# ### 함수

# #### 함수는 객체다
#
# - 함수는 객체이기 때문에, 다른 변수에 호출이 아닌 할당할 수 있다

# #### 함수 이름과 함수는 별개다
#
# - 즉, 함수 내용 자체를 메모리에 저장시키고, yell이라는 것으로 참조한다고 볼 수 있다.
# - 그리고 bark = yell 을 통해, bark 역시 함수를 가리키도록한다.
# - 이후, yell라는 변수를 메모리에서 지우더라도, bark가 함수를 참조하고 있기 때문에 함수는 살아있다.
# - 그리고 그 함수의 이름은 yell이다

# +
# 메모리를 할당해 bark가 yell을 가리키도록 함
#string.upper() : 모든 string을 대문자로 변환
def yell(text):
    return text.upper()+'!'
yell('hello')
bark = yell

print(bark('wolf'))
print(id(bark))
print(id(yell))
del yell
bark('what')

# 함수를 가르키는 변수와 함수 자체는 실제 별개의 대상이다

# 즉 함수를 생성하면 yell이라는 함수가 생성되 그 함수를 가리키는 변수 역시 yell 이라 한 것
print(bark.__name__)
# -

# ####  함수는 데이터 구조에 저장할 수 있다.

funcs = [bark, str.lower, str.capitalize]
funcs

for f in funcs:
    print(f, f('hey there'))

# 그러니까 이름을 불러오고, 그에 맞는 텍스트를 넣어주는 것.
# 호출하는 방식이 함수 이름을 불러오고 그다음 함수 그 자체를 불러오는 방식
funcs[0]('heyho')


# #### 함수는 다른 함수로 전달할 수 있다
#
# - 이거 매우 중요한 것 같은데..
# - 함수를 다른 함수의 인자로 줄 수 있다는 건 진짜 재미있네
# - 함수를 인자로 받을 수 있는 함수를 고차 함수라고 하며 함수형 프로그래밍 스타일에서 필요
#

# +
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

for i in funcs:
    print(i, end = ' ')
    greet(i)


# +
def whisper(text):
    return text.lower() + '...'

greet(whisper)
# -

list(map(funcs[0], ['hello', 'hi', 'hey']))


# #### 함수는 중첩될 수 있다
# - 중첩함수 내부함수 라고도 함
# - 함수 밖( 즉, speak 함수 밖) 에서 whisper() 은 존재하지 않음

def speak(text):
    def whisper(t):
        return t.lower() + "....."
    return whisper(text)
speak('Hello, World')

# 함수가 내부에서만 존재함을 보여주는 예시1
print(whisper(yo))

# 함수가 내부에서만 존재함을 보여주는 예시1
speak.whisper


# ##### 함수 내부에 함수를 사용하고 호출 받는 방법
#
# - 함수 내부에 함수를 짬
# - return 받을 때 함수 name을 받고 yell()의 yell( return yell )
# - 외부에서 변수에 함수 이름을 통해 같은 메모리를 가르치게 만든 후
# - 참조하여 사용한다

# +
def get_speak_fuc(volume):
    def whisper(text):
        return text.lower()+'......'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else : 
        return whisper
print(get_speak_fuc(0.3))    
print()
print(get_speak_fuc(0.7))
print()

speak_fuc = get_speak_fuc(0.7)
print(speak_fuc('hello'))

# -

# ##### lexical closure ( 렉시컬 클로저 혹은 클로저 )
#
# - text 라는 매가 변수가 없어졌음.
# - 그러나 부모 함수에서 정의된 text 매개 변수에 접근 할 수 있음
# - 클로저는 프로그램 흐름이 더 이상 해당 범위에 있지 않은 경우에도 둘러짠 어휘 범위 안의 값들을 기억함

# +
# 예시 1
def get_speak_fuc1(text, volume):
    def whisper():
        return text.lower() + '.......'
    def yell ():
        return text.upper() + '!!'
    
    if volume >0.5:
        return yell
    else:
        return whisper
    
get_speak_fuc1('hello, world', 0.7)()


# +
# 예시 2
def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))


# -

# ####  객체는 함수처럼 동작할 수 있다
#
# - 모든 함수는 파이썬에서 객체이다 그러나 모든 객체는 함수는 아니다
# - 그러나 모든 객체를 호출 가능하게 만들 수 있다
# - 따라서 객체를 '함수처럼 취급'할 수 있다
#
# ==============================================
#
# - 객체가 호출 가능하다는 것의 의미
#     - 소 괄호 형식의 함수 호출 문법을 사용하고 인자를 전달할 수 있음을 의미
#     - 이 기능은 모두 __call__ 던더 메서드로 구동

# +
# 호출 가능한 객체를 정의하는 클래스

class Adder:
    def __init__ (self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x

plus_3 = Adder(3) # n에 3을 주고 인스턴스 생성
plus_3(5) # 객체를 함수처럼 호출하면 __call__메서드가 실행되고 ( 5 )를 x에 전달하게됨
# -

# #### keypoint( 함수는 객체 )
#
#     1. 파이썬에는 모든 게 객체이며 함수 역시 객체이다.
#         
#         일급 함수
#         
#         - 함수를 변수에 할당 가능
#         - 데이터 구조에 저장 가능 ( 리스트와 같은 구조 )
#         - 다른 함수로 전달 가능 ( 즉 함수를 인자로 받을 수 있음)
#         - 다른 함수로부터 반환 받는 것 가능
#         
#     2. 일급 함수를 사용하면 프로그램의 동작을 추상화해 전달 가능
#     
#     3. 함수는 중첩될 수 있으며, 부모 함수의 일부 상태를 포착하여 전달할 수 있음. 이를 클로저라함
#     
#     4. 객체를 호출 가능하게 만들 수 있음. 이 경우 객체를 함수처럼 취급할 수 있음
#  
#

# #### 람다는 단일 표현식 함수다
#
# - lambda 키워드는 작은 익명의 함수를 선언하기 위한 손쉬운 방법
# - 람다 함수는 def 키워드로 선언된 일반 함수처럼 작동하며 함수 객체가 필요할 때마다 사용 가능
# - 람다 함수는 명령문 이나 주석을 사용할 수 없으며 return 문도 사용할 수 없다

# +
#lambda 함수 활용 사례
# 앞 인자 두개 받아서 x+y를 return 받아라
add = lambda x,y : x+y
add (5,3)

# def add (x,y):
#     return x+y # 위의 식과 같은 내용

# +
# 함수 이름을 바인딩할 필요가 없음
# 람다의 일부로 계산하고자 하는 표현을 말한 다음, 람다 표현식을 일반 함수처럼 호출하여 즉시 평가

(lambda x,y:x+y)(3,5)
# -

# #### 람다를 사용할 수 있는 경우
#
#
# - 기술적으로 함수 객체를 제공해야 할 때마다 람다 표현식을 사용할 수 있음.
# - 람다는 익명이기 때문에 제일 먼저 이름을 부여할 필요가 없음
# - 람다는 함수를 정의하는데 편리하고 '비격식적인' 지름길을 제공
#
#     - 대표적 사례로 대체 키로 리스트를 정렬하기 위한 짧고 간결한 key 함수를 작성하는 것
#     

# key 함수 작성
tuples = [(1, 'd'), (2, 'b'), (4, 'a'),(3,'c')]
sorted(tuples, key = lambda x : x[1])

# +
# 너는 뭐냐 도대체
# key 함수는 정렬의 기준을 제시해주는 함수구나!!

sorted(range(-5,6), key= lambda x : x*x)


# +
# 렉시컬 클로저 로써의 람다 함수 사용
# 프로그램 흐름이 해당 범위를 벗어났을 때도 해당 어휘 범위의 값을 기억하는 함수를 칭함

def make_adder(n):
    return lambda x : x+n

# 위를 풀어 쓰면 아래와 같음
# 즉 람다 x에 인자를 주기 위해서는 ()에 값을 넣어줘야함
def m(n):
    def a(x):
        return x+n
    return a


plus_3 = make_adder(3)
plus_4 = make_adder(4)

plus_2 = m(2)
plus_1 = m(1)
print(plus_3(10), plus_4(20), plus_2(10), plus_1(1))


# -

# #### 람다 함수를 자제해야 하는 경우
#
# - 람다 함수는 자주 사용하지 말아야하고 사용할 때 특별한 주의가 필요함
# - 람다를 사용한 복잡한 map() 이나 filter() 는 혼란 스러움을 가중시킬 수 있음
# - 리스트 컴프리핸션이나 제너레이터 표현식을 사용하는 것이 깔끔함

# +
# 나쁜 코드
class Car:
    rev = lambda self : print('Wroom!')
    crash = lambda self : print('Boom!')
    
my_car = Car()
print(my_car.crash(), my_car.rev())



# +
# 아직 클래스를 잘 모르겠당

# +
# 나쁜 코드

list(filter(lambda x:x%2 == 0, range(16)))
# -

# 좋은 코드
[x for x in range(16) if x % 2 == 0]

# #### keypoint( 람다 함수 )
#
#     1. 람다 함수는 이름에 묶이지 않는(익명) 단일 표현식 함수
#     
#     2. 람다 함수는 일반적인 파이썬 문을 사용할 수 없고, 항상 암시적 return 문을 포함함
#     
#     3. 일반( 이름 지어진 ) 함수 또는 리스트 내포식을 사용하면 더 명확하게 되는가? 명확하게 표현 할 수 있다면,
#     람다 사용을 자제해라


