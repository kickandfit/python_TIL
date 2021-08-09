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

# # 파이썬 개발자라면
#
# - 데이터 구조를 알아야함
#     - 데이터 구조는 프로그램을 구축하는 근본적인 구조물
#     - 각각의 데이터 구조는 고유한 방식으로 구성
#     - 쓰임새에 따라 효율적인 데이터 구조가 다름
# - 데이터 구조와 알고리즘 지식을 쌓는 것은 필수
#

# # 딕셔너리, 맵, 해시테이블
#
# - 딕셔너리(dict)는 중심이 되는 데이터 구조
# - 딕셔너리는 임의의 수의 객체를 저장하고 각각은 고유의 키(key)로 식별
# - 딕셔너리는 'map, hashmap, lookup table, associative array'라고도 함
# - key와 연관련 모든 객체의 검색, 삽입, 삭제를 효율적으로 수행
# - 딕셔너리를 사용하면 주어진 키와 관련된 정보를 빠르게 찾을 수 있음
# - 딕셔너리는 컴퓨터 과학에서 자주 사용되는 데이터구조
#

# # dict : 믿음직한 딕셔너리
#
# - 딕셔너리를 활용할 수 있도록 '간편 문법'을 제공

# +
phonebook = { 'bob' : 7387, 'alice' : 3719, 'jack' : 7052}

# 재밌네 이거
squares = {x : x*x for x in range(6)}

# -

phonebook['alice']

squares

# #### 객체를 key로 사용하려면
#
# - 임의의 해시 가능 타입인 키를 사용해 색인
#
# ---------------------------------------------
# -내용 추가해야함
#

# #### collections.OrderedDict: 키 삽입 순서 기억
#
# - 키의 삽입 순서를 기억하는 특수한 dict 서브클래스인 collections.OrderedDict를 제공
# - 알고리즘이 작동하는 데 키 순서가 중요하면 OrderedDict 클래스 명시
# - OrderedDict는 핵심 언어에 내장된 것이 아니므로 collections 사용

# +
import collections

d = collections.OrderedDict(one=1, two=2, three=3)
d
# -

d['four'] = 4
d

d.keys()

# #### collections.defaultdict: 누락된 키의 기본값 반환
#
# - defaultdict 클래스는 또 다른 딕셔너리 서브클래스
# - 생성자에서 호출 가능한 함수를 입력받고, 용청된 키를 찾을 수 없는 경우 이 함수의 반환값을 반환함
#     - 이렇게 하면 get() 메서드를 사용하거나 일반 딕셔너리에서 KeyError 예외를 잡아내는 것과 비교하여 타이핑을 다소 줄이고 프로그래머의 의도를 좀 더 명확하게 만들 수 있음
#     

# +
from collections import defaultdict

dd= defaultdict(list)

# -

# 없는 키에 접근하려고 하면 기본 팩터리를
# 사용해 키를 마들고 초기화한다
# 예> 이 예에서 list():
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')
dd['dogs']

# #### collections.ChainMap: 여러 딕셔너리를 단일 매핑으로 검색
#
# - collections.ChainMap 데이터 구조는 여러 개의 딕셔너리를 하나의 매핑으로 그룹화
# - 조회할 때는 키가 발견될 때까지 내부의 딕셔너리들을 하나씩 검사
# - 삽입, 갱신, 삭제는 체인에 추가된 첫 번째 딕셔너리에만 영향

# +
from collections import ChainMap

dict1 = {'one' : 1, 'two' : 2}
dict2 = {'three' : 3, 'four' : 4}
chain = ChainMap(dict1, dict2)
chain

# +
# ChainMap은 키를 찾거나 못 찾을 때까지 왼쪽에서
# 오른쪽으로 체인에 있는 컬렉션을 검색

chain['three']
# -

chain['one']

chain['missing']

# #### types.MappingProxyType: 읽기 전용 딕셔너리를 만들기 위한 래퍼
#
# - MappingProxyType은 표준 딕셔너리르 감싼 래퍼
# - 감싸진 딕셔너리의 데이터에 대한 읽기 전용 인터페이스 제공
# - 변경 불가능한 프락시 버전의 딕셔너리를 만드는 데 사용
#     - 예> 클래스나 모듈의 내부 상태를 가져올 수 있으나 쓰기는 제한하고자 할 때 유용
#     - MappingProxyType을 사용하면 딕셔너리의 전체 사본을 만들 필요 없이 제약 적용 가능

# +
from types import MappingProxyType

writable = {'one' : 1, 'two' : 2}
read_only = MappingProxyType(writable)
read_only
# -

# 프락시는 읽기 전용
read_only['one']

# 에러 발생 : 읽기 전용이니까
read_only['one'] = 23

# 원본 업데이트가 프락시에 반영됨
writable['one'] = 42
read_only

# #### keypoint( 딕셔너리 )
#
# - 딕셔너리는 파이썬의 중심 데이터 구조
# - 내장된 dict 타입은 대부분의 상황에서 '충분이 좋음'
# - 읽기 전용이거나 정렬된 딕셔너리와 같은 특수한 구현도 파이썬 표준 라이브러리에서 이용 가능

# # 배열 데이터 구조
#
# - 배열은 대부분 프로그래밍 언어에서 사용할 수 있는 기본 구조
# - 배열은 어떻게 작동하며 용도는 무엇인가
#     - 인덱스를 기반으로 각 요소를 효율적으로 배치할 수 있는 고정 크기 데이터 레코드
#     - 인접한 메모리 블록에 정보를 저장하기 때문에 '연속적인' 데이터 구조로 간주
#     - 인덱스가 부여된 배열에서 요소를 찾기란 매우 빠름
#     - 접근 시간 O(1)을 보장

# #### list : 가변 동적 배열
#
# - 이름은 리스트지만 내부에서 '동적 배열'로 구현
# - 요소를 추가하거나 제거할 수 있음
# - 리시트는 메모리를 할당하거나 해제함으로써 요소를 담는 저장소 크기를 자동으로 조정
# - 리스트 역시 객체
# - 파이썬은 모든 것이 객체 임으로 서로 다른 종류의 데이터 타입을 뒤섞어서 단일 리스트에 저장가능
# - 그러나 전체 구조에 더 맣은 공간이 소비됨

arr = ['one' , 'two', 'three']
arr[0]

# 리스트에는 repr이 있음
arr

# 리스트는 변경할 수 있음
arr[1] = 'hello'
arr

del arr[1]
arr

# 리스트에는 임의의 데이터 타입을 담을 수 있음
arr.append(23)
arr

# #### tuple : 불변 컨테이너
#
# - tuple 객체는 변경 불가능
# - 요소를 동적으로 추가하거나 제거할 수 없음
# - 생성할 튜플의 모든 요소를 정의해야 함
# - 임의의 데이터 타입의 요소를 담을 수 있음
# - 데이터 타입 지정 배열보다 메모리 공간을 더 차지함

# +
# 소괄호로 묶지 않으면 tuple로 들어감
arr= 'one', 'two', 'three'

arr[0]
# -

arr

#튜프은 변경 불가
arr[1] = 23

del arr[1]

# +
# 튜플에는 임의의 데이터 타입을 담을 수 있음
# 요소를 추가하면 튜플의 복사본을 만듬

arr + (23, )

# -

# #### array.array: 기본적인 타입 지정 배열
#
# - 파이썬의 array 모듈은 바이트, 32비트 정수, 부동소수점 숫자 등과 같은 기본 C 스타일 데이터 타입을 담을 수 있는 메모리 효율적인 저장 공간을 제공
# - array.array 클래스로 작성된 배열은 리스트와 비슷하게 변경 가능
#     - 차이점은 단일 데ㅣ터 타입으로 제한된 '타입 지정 배열'
#     - 그러나 이런 제약 덕분에 공간 효율적
#     - 메모리에 빡빡하게 채워넣어져 같은 타입의 요소를 저장해야할 때
#     

import array
arr = array.array('f',[1.0, 1.5, 2.0, 2.5])
arr[1]

# repr 있음
arr

del arr[1]
arr

arr.append(42.0)

arr

# 배열은 '타입이 지정' 되어 있음
arr[1] = 'hello'

# #### str : 유니코드 문자의 불변 배열
#
# - str 객체를 사용하여 텍스트 데이터를 유니코드 문자의 불변이며 연속적 데이터로 저장
# - str은 불변의 문자 배열
# - str은 재귀적 데이터 구조
#     - 즉, str의 각 문자의 길이가 1인 str 객체
# - 문자열 객체는 단일 데이터 타입에 특화/ 밀집되어 있어 공간 효율적
# - 유니코드 텍스트를 저장하는 경우 사용해야함
#
# - 문자열은 파이썬에서 불변이므로 문자열을 수정하려고 하면 수정된 복사본이 만들어짐.
#     - 가변 문자열과 가장 비슷한 것은 개별 문자를 리스트에 저장하는 것
#    

arr = 'abcd'
arr[1]

arr

# +
# 문자열은 변경할 수 없음

arr[1] = 'e'
# -

del arr[1]

# +
# 문자열을 풀어서(unpack) 리스트로 만들어
# 변경 가능한 표현을 얻을 수 있음

list('abcd')
# -

''.join(list('abcd'))
# '구분자'.join(list) : 리스트 내의 문자열을
#  구분지로 구분하여 연결함

# 문자열은 재귀적 데이터 구조
# 재귀적 : 재귀란? 어떤 사건이 자기 자신을 포함하고 
# 다시 자기 자신을 사용하여 정의될 때 재귀적(recursive)라고 한다
type('abc'[0])

# #### bytes: 단일 바이트의 불변 배열
# - 바이트 객체는 (0<= x <=255 범위의 정수)의 불변이며 연속된 데이터
# - 개념적으로는 str 객체와 비슷하지만 불변의 바이트 배열로 생각
# - 문자열과 마찬가지로 bytes는 객체 생성을 위한 리터럴 문법을 제공
# - 바이트 객체는 불변 문자열과 달리 bytearray라는 전용 '가변 바이트 배열' 데이터 타입이 있음

arr = bytes((0,1,2,3))
arr[1]

#바이트 리터럴은 자체 문법이 있음
arr

arr = b'\x00\x01\x02\x03'
arr[2]

# 유효한 '바이트'만 허용됨
bytes((0, 300))

# 바이트는 변경 불가
arr[1] = 2

del arr[1]

# #### bytearray: 단일 바이트의 가변 배열
# - bytearray 타입은 (0<= x<= 255) 범위의 정수로 이뤄진 변경 가능한 연속 데이터
# - bytes 객체와 밀접한 연관이 있으며 주요한 차이점은 바이트 배열은 자유롭게 수정 가능
# - 요소를 덮어쓰거나 기존 요소를 제거하고 새로 추가 가능
# - bytearray 객체의 크기는 그에 따라 증가되거나 축소
# - bytearray는 불변의 byte로 변환 가능
#     - 그러나 시간 복잡도 O(N)

arr = bytearray((0, 1, 2, 3))
arr[1]

# 바이트 배열 repr:
arr

# 바이트 배열은 변경 가능
arr[1]= 23
arr[1]

arr

# 바이트 배열 크기는 늘어나거나 줄어들 수 있음
del arr[1]
arr

arr.append(42)
arr

# +
# 바이트 배열에는 '바이트만' 담을 수 있음
# 0<=x <= 255

arr[1] = 'hello'
# -

arr[1] = 300

# 바이트 배열은 바이트 객체로 다시 변환될 수 있음
# ( 이렇게 하면 데이터가 복사됨)
bytes(arr)

# #### keypoint ( 배열 데이터 구조 )
#
# - 내장 데이터 구조에 중점
# - Numpy와 같은 서드 파티 패키지가 빠른 배열 구현 제공
# - 질문 list
#     - 잠재적으로 여러 가지 데이터 타입의 임의 객체를 저장?
#         - 가변 : list, 불변 : tuple
#     - 숫자( 정수 또는 부동소수점 ) 데이터가 있고 메모리 효율과 성능이 중요한가?
#         - array.array 사용
#         - Numpy와 pandas를 사용해라
#         
#     - 유니코드 문자로 표시된 텍스트 데이터가 있나?
#         - 내장 str을 사용
#         - 가변 문자열이 필요하면 문자열로 구성된 list 사용
#     - 연속적인 바이트 블록을 저장하고 싶나?
#         - 변경 불가능한 bytes
#         - 변경 가능한 bytearray
#         
# - 우선은 list로 접근
#     - 성능이나 메모리 효율이 문제가 되는 경우, 교체

# ####  cf) 유니코드란 무엇인가?
#
# - 유니코드란, 숫자와 글자, 즉 키와 값이 1:1 매핑된 형태의 코드
#     - 아스키코드로 0x41 = A로 매핑된 것처럼, 아스키코드로 표현할 수 없는 문자들을 유니 코드라는 이름 아래 전 세계의 모든 문자를 특정 숫자(키)와 1:1 매핑한 것
#
#     - 유니코드는 블록으로만 나누어놓은 테이블도 많음
#     - 아스키코드표 처럼 한 눈에 들어오는 테이블로 표시 불가
#
# - U+ 라는 접두어가 붙어 있으면 유니코드  
#     - utf-8,utf-16같은 인코딩 방식은 이 유니코드표의 숫자 키들을 어떻게 표현하느냐에 따른 것
#     - utf-8은 가변바이트 사용, 1바이트로 표현이 충분한 경우 0x41=A로 표현
#     - utf-16은 16비트, 즉 2바이트로 표현하기 때문에 0x0041로 표현
#     - utf-8의 표현 방식이 대체로 효율적
#     - EUC-KR, CP949 2바이트로 한글을 표현할 수 있게 만든 방식
#     
#  

# # 레코드, 구조체, 데이터 전송 객체
# - 배열과 비교하여 레코드 데이터 구조는 고정된 수의 필드를 제공하며 각필드는 이름을 가질 수 있고 서로 다른 타입을 담을 수 있음
# - 레코드, 구조체 및 'POD(plain old data) 객체'를 구현하는 법을 공부
#

# #### dict: 간단한 데이터 객체
#
# - 레코드 데이터 타입 또는 데이터 객체로 사용하는 것이 가능
# - 딕셔너리를 사용한 데이터 객체는 변경 가능하며 필드는 언제든지 추가, 제거 할 수 있음

car1 = { 'color' : 'red', 'mileage' : 3812.4 , 'automatic' : True, }
car2 = { 'color' : 'blue', 'mileage' : 4023.1 , 'automatic' : False, }


# clear한 repr
car2

# 딕셔너리는 변경 가능
car2['mileage'] = 12
car2

car2['windshield'] = 'broken'
car2
# 잘못되거나 빠지거나 추가된 필드명은
# 보호되지 않음

# +
car3 = { 'color' : 'green',  'automatic' : True, 'windshield' : 'broken', }

car3
# -

# #### tuple: 불변 객체 그룹
#
# - 임의의 객체를 그룹화하는 간단한 데이터 구조
# - 변경 불가능, 생성후 수정 불가
# - 바이트고드 디스어셈블리에서 보면
#     - 튜플 상수를 생성하는 데는 하나의 LOAD_CONST 연산 코드
#     - 리스트 객체는 몇 가지 연산이 더 필요함

import dis
dis.dis(compile("(23, 'a', 'b','c')", '','eval'))

dis.dis(compile("[23, 'a', 'b','c']", '','eval'))

# #### 중요한 것은 차이가 아니다
# - tuple의 잠재적인 단점은 저장된 데이터를 가져오는 방법이 정수 인덱스라는 것
# - 튜플에 저장된 개별 속성에는 이름을 지정할 수 없음
# - 코드 가독성에 영향을 미침
# - 튜플은 ad-hoc 구조
#     - 두 개의 튜플에 같은 수의 필드와 동일한 속성이 저장되어 있는지 확인하기가 어려움
#     - 필드 순서를 뒤섞는 것과 같은 실수를 발생 시킬 수 있음
#     - 튜플에 저장된 필드 수를 가능한 적게 유지하는 것이 좋음
#     

# +
# 필드 : 색상, 주행거리, 자동 여부

car1 = ('red', 3812.4, True)
car2 = ('blue', 40231.0, False)

# -

# 튜플 인스턴스에는 clear한 repr
car1, car2

# 주행거리
car1[1]

# 변경 불가
car1[2] = False

# +
# 잘못되거나 빠지거나 추가된 필드명은
# 보호되지 않음

car3 = (3431.5, 'green', True, 'silver')
car3


# -

# #### 사용자 정의 클래스 작성: 코드가 늘어날 수록 제어할 것도 는다
#
# - 클래스를 사용하면 데이터 객체에 대한 재사용 가능한 '청사진'을 정의하여 모든 객체가 동일한 필드 집합을 제공하도록 할 수 있음
# - 일반적인 파이썬 클래스를 레코드 데이터 타입으로 사용할 수도 있음, 다른 내장 타입들이 제공하는 편의 기능들을 사용하고 싶다면 추가 작업이 필요
#     - __ init __ 생성자에 새로운 필드를 추가하려면 장황해지고 시간이 오래걸림
# - 또한 객체의 기본 문자열 표현은 사용자 정의 클래스에는 별로 도움이 되지 않음
#     - 자신만의 __ repr __ 메서드를 추가해야 함
# - 메서드는 매우 장황하며 새로운 필드를 추가할 때 마다 갱신해야 함
# - 클래스에 저장된 필드는 변경 가능하며 새로운 필드를 자유롭게 추가가능
# - 접근 제어를 세밀하게 할 수 있고 @property 데코레이터를 사용하여 읽기 전용 필드를 만들수 있지만 접착 코드를 만들어야함
#

class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic
        
    def __repr__(self):
        return f'{__class__.__name__}({self.color}, ' f'{self.mileage}, {self.automatic})'
car1 = Car('red', 3812.4, True)
car2 = Car('blue', 40231.0, False)

car2.mileage

# +
# 클래스는 변경가능
car2.mileage = 12
car2.windshield = 'broken'
car2.windshield

# 문자열 표현은 그다지 유용하지 않음
# ( 손수 작성한 __repr __ 메서드를 추가해야함 )
# -

# #### typing.NamedTuple: 개선된 네임트 튜플
#
# - collections.namedtuple 클래스와 비슷함
# - 주요한 차이점은 레코드 타입을 정의하고 타입 힌트를 지원함
# - 타입 주석은 mypy와 같은 별도의 타입 확이도구 없이 적용되지 않음
#

# +
from typing import NamedTuple

class Car(NamedTuple):
    color : str
    mileage : float
    automatic : bool

car1 = Car('red', 3812.4, True)

# -

# clear한 rper
car1
# 필드에 접근함

car1.mileage

#필드는 변경할 수 없음
car1.mileage = 12

#mypy 같은 별도 타입 확인 도구 없이는
# 타입 주석은 적용되지 않음
Car('red', 'Not_A_FLOAT', 99)

# #### struct.Struct: 직렬화된 C구조체
#
# - struct.Struct 클래스는 파이썬 bytes 객체로 직렬화된 C 구조체와 파이썬 값 사이의 변환을 수행
#     - 파일에 저장되거나 네트워크로부터 들어오는 이진 데이터처리에 사용
#     
# - 구조체는 char, int, long, unsigned 등 다양한 C 데이터 타입의 배열을 정의 할 수 있는 형식 문자열 같은 미니 언어를 사용해 정의
# - 직렬화된 구조체는 순수하게 파이썬 코드 내에서 처리되는 데이터 객체를 나타내는 데 사용되지 않음
#     - 파이썬 코드에서만 사용되는 데이터를 메모리에 저장하는 방법이라기보다 주로 데이터 교환형식으로 사용됨
#     - 경우에 따라 기본 데이터를 구조체에 담으려면 다른 데이터 타입으로 유지하는 것보다 메모리를 적게 사용할 수 있음
#     - 그러나 고급( 아마도 불필요한 ) 최적화

# +
from struct import Struct

MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)
# -

# 데이터 블롭(blob)만 얻음
data

# 데이터 블롭은 다시 풀(unpack) 수 있음
MyStruct.unpack(data)

# #### types.SimpleNamespace: 세련된 속성 접근
#
# - 파이썬에는 데이터 객체를 구현하기 위한 또하나의 '난해한' 방법인 types.SimpleNamespace 가 있음
# - 네임스페이스의 속성에 접근할 수 있도록 해줌
# - SImpleNamespace 인스턴스는 모든 키를 클래스 속성으로 노출
#     - 즉, obj['key'] 대괄호 인덱스 문법 대신 obj.key '점' 속성 접근 사용 가능
#     - 모든 인스턴스는 기본적으로 유효한 __ repr __ 도 포함
# - SimpleNamesapce는 기본적으로 속성을 가져올 수 있고 출력 해줌
# - 속성은 자유롭게 추가, 수정, 삭제 가능

from types import SimpleNamespace
car1 = SimpleNamespace( color = 'red',
                      mileage = 3812.4,
                      automatic = True)

# 기본 repr
car1

# 인스턴스 속성 접근을 지원하고 변경할 수 있음
car1.mileage = 12
car1.windshield = 'broken'
del car1.automatic
car1

# #### keypoint ( 레코드, 구조체, 데이터 전송 객체 )
#
# - 레코드 또는 데이터 객체를 구현하는 데는 다양한 옵션이 존재
#
#     - 몇(2~3)개의 필드만 가지고 있다
#         - 필드 순서를기억하기 쉽거나 필드명이 불필요할 경우 튜플
#     - 불변 필드가 필요
#         - 일반 튜플, collections.namedtuple, typing.NamedTuple
#     - 오타가 발생하지 않도록 필드 이름을 고정할 필요가 있다
#         - collections.namedtuple, typing.NamedTuple
#     - 간단하게 유지하기를 원한다
#         - 딕셔너리
#     - 데이터 구조를 완전히 제어할 필요가 있다
#         - @property의 세터(setter)와 게터(getter)를 사용하여 사용자 정의 클래스
#     - 객체에 동작(메서드)를 추가해야 한다
#         - 사용자 정의 클래스를 처음부터 작성
#         - collections.namedtuple, typing.NameTuple
#     - 데이터 디스크에 저장하거나 네트워크로 전송해야 해서 데이터를 일렬로 빽빽하게 담아야 한다
#         - struct.Struct
#         
#     - 안전하고 기본적인 선택?
#         - typing.NamedTuple

# # 세트와 멀티세트
#
# - 표준 라이브러리의 내장 데이터 타입과 클래스를 사용하여 변경 가능하거나 변경 불가능한 세트와 멀티세트 데이터 구조를 구현
# - '세트'는 중복 요소를 허용하지 않는 정렬되지 않은 컬렉션
#     - 일반적으로 세트는 특정 값이 세트에 포함되는지를 빠르게 테스트하고 새값을 삽입하거나 삭제하며 두 세트의 합집합 또는 교집합을 계산하는 데 사용
# - '제대로' 구현된 세트라면 구성둰 테스트가 O(1)이라는 시간 복잡도
# - 합집합, 교집합,차집합, 부분집합 작업은 평균 O(N) 시간 소요

# +
vowels = {'a', 'e', 'i', 'o', 'u'}
squares = {x*x for x in range(10)}
non_set = set()

# 빈 세트를 주려면 set()를 호출해야함
vowels, squares, non_set
# -

# #### set: 나만의 믿음직한 세트
#
# - set은 파이썬의 내장 세트 구현
# - 변경 가능하며 요소를 동적으로 삽입하고 삭제할 수 있음
# - 파이썬의 세트는 dict 데이터 타입에 의해 뒷받침되며 동일한 성능 특성을 공유함
# - 해시 가능한 객체라면 모두 세트에 저장할 수 있음

vowels = {'a', 'e', 'i', 'o', 'u'}
'e' in vowels

# intersection 교집합
letters = set('alice')
letters.intersection(vowels)


# 추가하기
vowels.add('x')
vowels

len(vowels)

# #### frozenset : 불변 세트
#
# - frozenset 클래스는 set의 '불변' 버전으로 생성된 후에는 변경 불가
# - 프로즌세트는 정적이며 요소에 대한 쿼리 작업만 허용
#     - 삽입이나, 삭제는 허용되지 않음
#     - cf> 쿼리란 : 데이터베이스에게 특정 데이터를 보여달라는 클라이언트의 요청
# - 프로즌세트는 정적이며 해시 가능하기 때문에 딕셔너리 키 또는 다른 세트의 요소로 사용할 수 있음

vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
vowels.add('p')

# #### collections.Counter: 멀티세트
#
# - collections.Counter 클래스는 요소가 두 번 이상 나타날 수 있는 멀티 세트 타입을 구현함
# - 요소가 세트의 일부인지 아닌지 뿐만 아니라 세트에 포함된 '횟수'를 추적할 때 유용

# +
from collections import Counter

inventory = Counter()

loot = {'sword' : 1, 'bread' : 3}
inventory.update(loot)
inventory
# -

more_loot = {'bread' :1, 'apple' : 1}
inventory.update(more_loot)
inventory

# - Counter 객체의 요소 수를 셀 때는 주의
#     - len()을 호출하면 멀티세트의 고유 요소 수를 반환하는 반면, sum() 함수를 사용하면 총 요소수가 반환
#     

len(inventory) # 고유 요소

sum(inventory.values()) # 총 요소

inventory.values()

inventory.keys()

# #### keypoint( 세트와 멀티세트 )
#
# - 세트는 파이썬과 파이썬 표준 라이브러리에 포함된 또 다른 유용하고 범용적으로 사양되는 데이터 구조
# - 변경 가능한 세트가 필요하면 내장 set 타입을 사용
# - frozenset 객체는 해시 가능하며 딕셔너리 또는 세트의 키로 사용할 수 있음
# - collections.Counter는 멀티세트 또는 '가방(bag)' 데이터 구조를 구현함

# # 스택( LIFO )
#
# - 스택은 삽입과 삭제를 '후입선출(last-in, first-out)' 방식으로 빠르게 처리해 주는 객체 컬렉션
# - 리스트나 배열과 달리 스택은 일반적으로 요소 객체로의 임의 접근을 허용하지 않음
# - 삽입 및 삭제 작업은 '푸시'와 '팝'이라고 함
# - 스택과 큐는 비슷함
#     - 둘 다 순차적인 컬렉션이며, 원소에 접근하는 순서만 다름
#     - 큐에서는 가장 오래전에 추가된 요소를 제거(first-in, first-out), 스택을 사용하면 가장 최근 추가 항목 제거
# - 제대로 구현한 스택은 삽입 및 삭제 작업에 O(1) 시간이 걸림
#     - 알고리즘에서 광범위한 용도로 쓰임
#     - 언어 구문 분석 및 런타임 메모리 관리('호출 스택') 에 쓰임
#     - 트리 또는 그래프 데이터 구조에서 깊이 우선 탐색은 스택을 활용한 짧고 아름다운 알고리즘

# #### list : 간단한 내장 스택
# - list 타입은 O(1) 시간에 푸쉬 및 팝 작업을 수행함으로 괜찮은 데이터 구조
# - 파이썬 내부적으로 동적 배열로 구현
#     - 항목이 추가되거나 제거될 때, 저장된 항목의 저장 공간 크기를 가끔식 조정해야 하는 경우가 있음
#     - 리스트는 저장소를 필요보다 많이 할당해 두므로 푸시 또는 팝을 수행할 때마다 크기를 조정해야 하는 건 아님
# - 단점은 연결 리스트 기반 구현(collections.deque)에서 제공하는 안정적인 삽입과 삭제보다 성능에서 일관성이 떨어짐
# - 반면, 리스트는 요소로의 무작의 접근을 빠른 시간에 수행할 수 있다는 이점을 추가로 제공
#     - 리스트를 스택으로 사용할 때 인지해야할 중요한 성능상의 주의점
#         - 삽입, 삭제 시 O(1) 성능을 얻으려면 새항목은 append()를 사용하여 추가
#         - 제거할 때는 pop() 메서드를 사용하여 끝에 있는 항목부터 제거
#             - 최적의 성능을 위해 리스트 기반 스택은 더 높은 인덱스 쪽으로 커지고 더 낮은 인덱스 쪽으로 줄어들어야 함
#             

s = []
s.append('eat')
s.append('sleep')
s.append('code')
s

s.pop()

# #### collections.deque: 빠르고 강력한 스택
#
# - deque 클래스는 O(1) 시간에 어느 쪽에서든 요소를 추가, 삭제할 수 있는 양단 큐
# - deque는 양쪽 끝에서 요소를 동일하게 추가, 제거해도 되기 때문에 큐와 스택으로 모두 사용가능
# - deque 객체는 이중 연결 리스트로 구현되어 요소를 삽입하고 삭제하는데 탁월하고 일관된 성능 제공
#     - 스택 중간의 임의 원소에 접근하려 할때 O(N) 성능을 갖음
#

# +
from collections import deque

s = deque()
s.append('eat')
s.append('sleep')
s.append('code')
s
# -

s.pop()

# #### queue.LifeQueue: 병렬 컴퓨팅을 위한 잠금 체계
# - LifeQueue 스택 구현은 동기 방식이며 동시에 여러 생산자와 소비자를 지원하는 잠금 체계를 제공
# - LifeQueue 외에도 queue 모듈에는 병렬 컴퓨팅에 유용한 다중 생산자/다중 소비자 큐를 구현하는 클래스 포함
# - 잠금 체계가 필요없다면 list나 deque를 사용하는 것이 좋음

from queue import LifoQueue
s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('code')
s

s.get()

s.get_nowait()
# 큐가 비어있다면 get()은 영원히 기다림

# #### 파이썬의 스택 구현 비교
# - 병렬 처리 지원하지 않아도 된다면, list or collections.deque 선택
#     - list는 동적 배열로 구성
#         - 동적 배열은 빠른 임의 접근 가능
#         - 항목이 추가되거나 삭제될 때 가끔 크기를 조정해야함
#         - 리스트는 저장 공간을 여유 있게 할당하므로 시간 복잡도 O(1)
#         - append(), pop()을 사용하여, '오른쪽'부터 제거하지 않으면 O(N)
#     - collections.deque
#         - 양쪽 끝에서 추가 및 삭제를 최적화하는 이중 연결 리스트
#         - 성능이 안정적이고 '잘못된 끝'에서 항목을 추가하거나 제거하는 것을 고려하지 않아도됨
#         
#     - collections.deque는 파이썬에서 스택을 구현할 때 탁월한 선택

# #### keypoint( 스택 )
# - 여러가지 스택 구현을 제공함
# - collections.deque는 안전하고 빠른 범용 스택 구현을 제공함
# - 내장된 list 타입은 스택으로 사용할 수 있지만, append(), pop()을 사용 권장( 삽입, 제거 )


