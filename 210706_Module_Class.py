# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
## 실행 함수(메서드)만 가지고 있는 클래스

class Fun_cls: # 클래스 첫 글자는 대문자로 많이 적음
    
    # 클래스 기준 인스턴스 속성에 해당됨
    def usr_fun1(x, y, z = 10):

        tot = x + y + z
        print(f'x={x}, y={y}, z={z}, 합계={tot}')

    def usr_fun2(x, y, z):

        tot = x + y + z
        p_tot = tot *10
        return tot , p_tot

## 생성자를 가직 있는 클래스
## 사칙연산
class FourCal:
    
    # self는 자기자신을 의미함
    
    # 생성자 : 클래스 자체를 정의할 떄 사용함

    def __init__(self):
        self.result = 0 #FourCal 속성
        
    def add(self, num): # 함수/ 인스턴스(클래스 입장)/ 메서드
        self.result = self.result + num
        
        return self.result
    
    def sub(self, num):
        self.result= self.result - num
        return self.result
    
    def mul(self, num):
        self.result= self.result * num
        return self.result
    
    def Div(self, num) :
        self.result= self.result/num
        return self.result

        

# +
# 생성자가 있는 클래스의 경우

f_cal = FourCal()
tot = f_cal.add(10)
print(tot)

# +
#클래스 FourCal을 이용해서 객체 fcall을 생성해라
fcall = FourCal() #생성자가 있을때 생성자를 통해 초기화 해줘라

print('FourCal 클래스 result =', fcall.result) 
# -

if __name__ == "__main__": # 자기자신이 실행하면 실행하고 다른곳에서 호출하면 실행하지 말아라
    # __ 는 숨겨진 변수
    print('FourCal.sub 계산후 result =', fcall.result) 
    fcall.add(10)
    print('FourCal.add 계산후 result =', fcall.result) 
    fcall.sub(5)
    print('FourCal.sub 계산후 result =', fcall.result) 


    # 끝나고 재정의 하면 초기화된다
    fcall = FourCal() 
    fcal2 = FourCal()

    fcall.add(10)
    print('FourCal.add 계산후 result =', fcall.result) 
    print('FourCal.add 계산후 result =', fcal2.result) 










