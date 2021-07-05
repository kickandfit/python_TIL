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
import pandas as pd
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
df1 = pd.read_csv('./Data/서울시 인구현황_구.txt', sep = '\t', header = 1)
df1.head(3)

# +
df1 = df1.iloc[:, [0,1, 9 ,10, 11]]
df1.drop(0, axis = 0, inplace = True)
col_name=['년도', '자치구', '외국인', '외국인(남)','외국인(여)']
for i in range(len(col_name)):
    df1.rename(columns={df1.columns[i]:col_name[i]}, inplace=True)

df1.head(3)
# -

df2 = df1.iloc[:, 0:5]
df2

df2['외국인'] = df2['외국인'].str.replace(',','').replace("…","0")
df2['외국인(남)'] = df2['외국인(남)'].str.replace(',','').replace("…","0")
df2['외국인(여)'] = df2['외국인(여)'].str.replace(',','').replace("…","0")
df2

df2 = df2.astype({ '외국인' : int,'외국인(남)' : int,'외국인(여)' : int})
df2.dtypes

# +
year = input('조회할  년도을 입력하세요')

df3 = df2[df2['년도'] == year]
df3.plot(kind ='bar', x = '자치구', y = '외국인')
plt.title('외국인 해당 년도 현황')
plt.xlabel('자치구', size=15)
plt.ylabel('인구수', size=15)
plt.show()


# -

df2['합계'] = df2['외국인(남)'] + df2['외국인(여)']
df3['비율(남)'] = df2['외국인(남)'] / df2['합계']
df3['비율(여)'] = df2['외국인(여)'] / df2['합계']
df3.plot(kind ='bar', x = '자치구', y = ['비율(남)','비율(여)'])
plt.title('외국인 해당 년도 현황')
plt.xlabel('자치구', size=15)
plt.ylabel('인구수', size=15)
plt.show()


