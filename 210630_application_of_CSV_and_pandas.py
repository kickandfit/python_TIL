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
#plt 차트에서 한글 지원 방법 1
#전체에 대해서 폰트속성 변경
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
#from matplotlib import as fm과 같은 문법
#from matplotlib import rc 를 활용해도 됨 rc를 활용할거냐 아니면 fm을 활용하여 각각 관리할거냐

# 폰트의 위치, 한글 폰트만 활용가능
# 그중에서도 속성에서 truetype만 활용가능
font_path = "C:/Windows/Fonts/malgun.ttf" #한글 폰드 경로 및 이름 정의(window10 기반)
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name) # 차트 전체 폰트 속성 변경

plt.plot([33, 12, 22, 9, 45], label='abc', color='skyblue', 
         marker='o', linestyle = '--') #chart no.1 and option

# 순서랑 상관 없이 label = '', color= '', 이런식으로 옵션을 입력해라

plt.title('차트그리기 실습') # chart name
plt.xlabel('X-Label') #x axis namep
plt.ylabel('Y-Label') #y axis name
plt.legend() #print label
plt.show()

# +
#plt 차트에서 한글 지원 방법 2
#개별 폰트속성 변경
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name1 = fm.FontProperties(fname=font_path, size = 18) # 기본 폰트 및 사이즈 정의
font_name2 = fm.FontProperties(fname=font_path, size = 13)

plt.plot([33, 12, 22, 9, 45], label='abc', color='skyblue', 
         marker='o', linestyle = '--') 

plt.title('차트그리기 실습', fontproperties=font_name1) # 차트에 font_name 적용
plt.xlabel('X-Label', fontproperties=font_name2) #x axis namep
plt.ylabel('Y-Label', fontproperties=font_name2) #y axis name
plt.legend() #print label
plt.show()

# +
#['\t\t지점번호', '지점명', '일시', '평균기온(℃)', 
#'평균최고기온(℃)', '최고기온(℃)', '\t최고기온일자', 
#'평균최저기온(℃)', '최저기온(℃)', '최저기온일자']
# 날짜데이터(row[-1])를 가져와, "-"를 기준으로 글자 나누기
# 생일에 따른 년도별 최고기온/최저기온 차트 출력

import csv

f= open("./Data/seoul.csv")
data = csv.reader(f)  
header = next(data) 

max_temp = []
min_temp = []

for row in data:
    
    pre_max_temp=[]
    pre_min_temp=[]
    
    if row[-1] != "":
        if int(row[-1].split('-')[0]) >= 1985:
            if row[-1][-5:]=="05-01":
                
                pre_max_temp.append(float(row[4]))
                pre_min_temp.append(float(row[-2]))
                max_temp.append(pre_max_temp)
                min_temp.append(pre_min_temp)

                
plt.plot(max_temp)
plt.plot(min_temp)
plt.show()
# -


