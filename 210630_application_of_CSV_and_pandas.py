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
import csv
f= open("./Data/seoul.csv") # seoul.csv 파일 읽기 모드로 불러옴
data = csv.reader(f) # csv 파일 자체가 ,로 나눠져 있어서 생략하면 
                      #기본으로 가져오기때문에 문제 없음
header = next(data) # 첫번째 행(제목행) header 변수 저장
print(header)
print()

max_tem = 0
max_dat = ""

for row in data:
    if row[-5] !="":
        if float(row[4])>max_tem:
            max_tem = float(row[-5])
            max_day = row[-1]
    
print(f'최고기온 : {max_tem}, 날씨: {max_day}')
f.close()
# -
# ### matplotlib 라이브러리를 이용한 시각화
#
# - 파이썬 시각화 모듈
# - 2D 형테의 그래프, 이미지 등을 사용할 때 적용
# - 실제 과학 컴퓨팅 연구 분야나 인공지능 연구 분야에서도 많이 활용
# - https://matplotlib.org/


# +
import matplotlib.pyplot as plt
# from matplot import pyplot as plt 와 같은의미

# plt.plot(x axiss, y axis)
# 교재 4장 참조

plt.plot([10, 20, 30, 40]) #메모리에 차트(꺽은선 graph) 생성
plt.show() #메모리에 생선된 차트를 화면에 나타나게 해줌

# +
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [22, 13, 15, 48, 16]

plt.plot(x, y) # creat value of x axis and y axis
plt.show()

# +
#plt 영역에여러 개의 차트 및 내용 표시
import matplotlib.pyplot as plt

plt.plot([33, 12, 22, 9, 45], label='abc', color='skyblue', marker='o') #chart no.1 and option
plt.plot([50, 40, 30, 20, 10], 'pink', label="cba", marker='^', linestyle = '--')#chart no.2 and option
# 순서랑 상관 없이 label = '', color= '', 이런식으로 옵션을 입력해라

plt.title('plotting whatever i want') # chart name
plt.xlabel('X-Label') #x axis namep
plt.ylabel('Y-Label') #y axis name
plt.legend() #print label
plt.show()

# +
#plt 차트에서 한글 지원 방법

import matplotlib.pyplot as plt

plt.plot([33, 12, 22, 9, 45], label='abc', color='skyblue', 
         marker='o', linestyle = '--') #chart no.1 and option

# 순서랑 상관 없이 label = '', color= '', 이런식으로 옵션을 입력해라

plt.title('plotting whatever i want') # chart name
plt.xlabel('X-Label') #x axis namep
plt.ylabel('Y-Label') #y axis name
plt.legend() #print label
plt.show()
# -


