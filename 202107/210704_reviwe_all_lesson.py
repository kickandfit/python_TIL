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
# 고유값찾기 : 로또 번호 생성기
import numpy as np

num_lst = []

while len(num_lst) <= 6:
    num = np.random.randint( 1, 46 )
    
    if num not in num_lst:
        num_lst.append(num)

print(f'로또 번호 : {num_lst[:-1]} 보너스 번호 : {num_lst[-1]}')

# +
# 문법 in에 대한 고찰( for과 if만을 활용하기 )

import numpy as np

num_lst = []
eval_num = []

while len(num_lst) <= 10:
    num_lst.append( np.random.randint(1,11))

print(num_lst)
for i in num_lst:
                
    if len(eval_num) == 0:
        eval_num.append(i)
        continue
    cnt = 0
    for j in eval_num:

        if i == j:
            cnt +=1
            break
        
 
    if cnt == 0:
        eval_num.append(i)
            
            
print(eval_num)

# +
# cnt 쓰지 않고 해보기
import numpy as np

num_lst = []
eval_num = []

while len(num_lst) <= 100:
    num_lst.append( np.random.randint(1,11))

for i in num_lst:
    if len(eval_num) == 0:
        eval_num.append(i)
        continue
    
    for j in range(len(eval_num)):
        if i == eval_num[j]:
            break
        
        if j == len(eval_num) - 1:
            eval_num.append(i)

print(eval_num)


# +
#split 함수 짜보기

txt_lst = '''동준이는 원래 스터디 카페에 같이 등록하기로 했다.
그런데 관장님의 갑작스러운 부탁으로 동준이는 내일 단기 알바를 하러 가기로 했다.'''
txt = txt_lst.replace('\n',' ')
        
나누는단어=" "
리스트형_변수=[]
단어_변수=""
글자수=len(나누는단어)

txt=txt.replace('\n', ',')

for 순번 in range(len(txt)-(글자수-1)):
    if txt[순번:순번+글자수] != 나누는단어:
        단어_변수 = 단어_변수 + txt[순번]
    else:
        리스트형_변수.append(단어_변수)
        단어_변수=""

if 단어_변수!="":
    리스트형_변수.append(단어_변수)

print(리스트형_변수)

# +
txt_lst = '''동준이는 원래 스터디 카페에 같이 등록하기로 했다.
그런데 관장님의 갑작스러운 부탁으로 동준이는 내일 단기 알바를 하러 가기로 했다.'''
txt = txt_lst.replace('\n',' ')

spl = input("나눌 단어를 입력하세요")
word_lst = ""
result = []
len_word = len(spl)
a= 0 

for i in range(len(txt)):

    
    if txt[i:i+len_word] != spl:
        if i >= a :
            word_lst += txt[i]
    else:
        result.append(word_lst)
        word_lst = ""
        a = i+len_word
    
    if i == len(txt) -1:
        result.append(word_lst)
        
print(result)

# +
# CSV 파일 읽기 , max/ min 값 찾기
import csv

f = open('./Data/seoul.csv', encoding = 'cp949')
data = csv.reader(f)
header = next(data)
print(header)
print()

max_tem = ["",0.0]
min_tem = ["",100.0]


for row in data:
    if row[4] != "":
        
        if float(row[4]) > max_tem[1]:
            max_tem[1] = float(row[4])
            max_tem[0] = row[2]
        
        if float(row[-2]) < min_tem[1]:
            min_tem[1] = float(row[-2])
            min_tem[0] = row[2]

print(f'최고기온 : {max_tem[1]}, 최고기온 날짜 : {max_tem[0]}, 최저기온 : {min_tem[1]}, 최저기온 날짜 : {min_tem[0]}')

# +
# pandas로 읽어오기
import pandas as pd

df = pd.read_csv('./Data/seoul.csv', encoding = 'cp949')

print(df['최고기온(℃)'].max())
print(df['최저기온(℃)'].min())

# -

df[df['최저기온(℃)'] == df['최저기온(℃)'].min()]["일시"]

# ### 미션 : 연간_인구현황.csv 파일에서 2018~2020년 데이터 추출하기
#
# - 추출 데이터:0~9세 데이터(전체/남/여)
# - 차트 : 전체/남/여/지역별 그리기
#

# +
import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name) 
f = open('./Data/연간_인구현황.csv', encoding = 'cp949')
data = csv.reader(f)

header=next(data)
print(header)
print()

age_0_to_9_national = []
age_0_to_9_man = []
age_0_to_9_wom = []
rigeonal_name = []
for row in data:
    age_0_to_9_national.append( int(row[3].replace(",","")) )
    rigeonal_name.append(row[0][:-13])
    age_0_to_9_man.append( int(row[6].replace(",","")) )
    age_0_to_9_wom.append( int(row[9].replace(",","")) )
index = np.arange(len(age_0_to_9))

plt.bar(index, age_0_to_9_national, label = "0 to 9 population")
plt.bar(index, age_0_to_9_man, label = "0 to 9 man_population")
plt.bar(index, age_0_to_9_wom, label = "0 to 9 woman_population")
plt.xticks(index, rigeonal_name, rotation = 90)
plt.legend(loc = 'best')
plt.show

# -

#




