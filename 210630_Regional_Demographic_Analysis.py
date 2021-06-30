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
# csv 파일을 받아올때, 숫자가 '문자'로 받아졌는지 파일 타입 체크할 것
# 파일 타입을 숫자로 받기 위해, 숫자 사이에 ','와 같은 문자가 있는지 체크할 것

import csv
import matplotlib.pyplot as plt

f = open('./Data/202105_인구현황.csv')
data = csv.reader(f)
header = next(data)

for row in data:
    if '서울' in row[0]:
        
        tot_pop = [int(i.replace(",","")) for i in row[3:104]]
        man_pop = [int(i.replace(",","")) for i in row[106:207]]
        wom_pop = [int(i.replace(",","")) for i in row[209:310]]
        
plt.style.use('ggplot') # style을 사용하면 이쁘게 보여줌

plt.plot(tot_pop, label='tot')
plt.plot(man_pop, label='man')
plt.plot(wom_pop, label='wom')

plt.legend()
plt.show()

f.close()

# +
# csv 파일을 받아올때, 숫자가 '문자'로 받아졌는지 파일 타입 체크할 것
# 파일 타입을 숫자로 받기 위해, 숫자 사이에 ','와 같은 문자가 있는지 체크할 것
# open 이라는 것은 한번 쓰면 파일을 못쓰게 그 줄을 날려버림

import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name) 
f = open('./Data/202105_인구현황.csv', encoding = "cp949")
data = csv.reader(f)
header = next(data)

loc_lst=['서울', '경기', '부산', '인천', '울산', '광주', '대전', '대구']



    
for loc_n in loc_lst:
    
    f = open('./Data/202105_인구현황.csv', encoding = "cp949")
    data = csv.reader(f)
    
    for row in data:
        
        if loc_n in row[0]:

            tot_pop = [int(i.replace(",","")) for i in row[3:104]]
    
            plt.style.use('ggplot') # style을 사용하면 이쁘게 보여줌
            plt.figure(figsize=(10,5))

            plt.plot(tot_pop, label= loc_n)

            plt.legend()
            plt.show() 
    

    f.close()

# +

# open 이라는 것은 한번 쓰면 파일을 못쓰게 그 줄을 날려버림
# open, close는 일회성이다

import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name) 
f = open('./Data/202105_인구현황.csv', encoding = "cp949")
data = csv.reader(f)
header = next(data)

loc_lst=['서울', '경기', '부산', '인천', '울산', '광주', '대전', '대구']



plt.style.use('ggplot') # style을 사용하면 이쁘게 보여줌
plt.figure(figsize=(10,5))

for loc_n in loc_lst:
    
    f = open('./Data/202105_인구현황.csv', encoding = "cp949")
    data = csv.reader(f)
    
    for row in data:
        
        if loc_n in row[0]:

            tot_pop = [int(i.replace(",","")) for i in row[3:104]]
    
    
    plt.plot(tot_pop, label= loc_n)
    
    f.close()
    
plt.legend()
plt.show()
