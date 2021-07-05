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

# ### [목표]
# - 년도별 서울시 인구 현황(내국인/외국인/고령자)
# - 년도별 외국인 남/여 비율

# +
# 구분자가 콤마(,)가 아닌 다른 구분자를 사용한 데이터 읽어오기
# 제목행 선택: header = 1(index 번호)
import pandas as pd

df1 = pd.read_csv('./Data/서울시 인구현황_구.txt', sep = '\t', header = 1)
df1.head(3)


# +
# 기간, 자치구, 전체인구/전체(남)/전체(여)/
# 내국인/내국인(남)/내국인(여)/외국인/외국인(남)/외국인(여)/65세이상

# df1['기간','자치구', '합계', '합계.1', '합계.2', '한국인', '한국인.1', '한국인.2','등록외국인', '등록외국인.1', '등록외국인.2','65세이상고령자']
# df1.loc[:, ['기간','자치구', '합계', '합계.1', '합계.2', '한국인', '한국인.1',
#            '한국인.2','등록외국인', '등록외국인.1', '등록외국인.2','65세이상고령자']]
df1 = df1.iloc[:, [0,1, 3, 4, 5, 6 ,7 ,8 ,9 ,10, 11, -1]]
df1
# -

df1.columns

# ### ※ 참고사항 : axis = 0 vs axis = 1
# - axis = 0은 DataFrame 에서 행 단위를 수정할 때 필요한 파라미터 값
# - axis = 1은 DataFrame 에서 열 단위를 수정할 때 필요한 파라미터 값

df1.drop(0, axis = 0, inplace = True) #DataFrame.drop(0) axis = 0 이 생략된 상태

df1.head()

# ### 열 이름 변경
# - DataFrame.rename(columns = {'합계' : '총인구'}, '합계.1':'총인구(남), ...'}) # 열이름 한두개 바꾸기
# - DataFrame.rename(columns = {DataFrame.columns(2) : '총인구', DataFrame.columns(3)':'총인구(남), ...'}) #열 이름 다수 변경
#

df1 = df1.rename(columns = {'합계' : '총인구', '한국인' : '내국인', '등록외국인' : '외국인'})
df1.head(3)

# +
ccol_name=['년도', '자치구', '총인구', '총인구(남)', '총인구(여)', '내국인', '내국인(남)', '내국인(여)',
          '외국인', '외국인(남)','외국인(여)', '65세이상']

for i in range(len(col_name)):
    df1.rename(columns={df1.columns[i]:col_name[i]}, inplace=True)

df1.head(3)

# -

# ### 년도별 총인구(남)/총인구(여) 값을 나타내는 그래프 작성

df1.info()

df2 = df1.iloc[:, 0:5]
df2.head()

# ### DataFrame 데이터 타입 변경하는 방법
# - pd.astype(dtype) # 모든 열의 데이터 타입 변경
# - pd.astype({'컬럼명' : dtype}) # 특정 열의 데이터 타입 변경

# pandas에서 데이터 타입 변경
df2['총인구'] = df2['총인구'].str.replace(',','')
df2['총인구(남)'] = df2['총인구(남)'].str.replace(',','')
df2['총인구(여)'] = df2['총인구(여)'].str.replace(',','')
df2.dtypes


df2 = df2.astype({'년도': int, '총인구' : int,'총인구(남)' : int,'총인구(여)' : int})
df2.dtypes

df2.head()

# +
# 그래프 한번에 보기
import matplotlib.pyplot as plt

gu = input('조회할 구 이름을 입력하세요')

df3 = df2[df2['자치구'] == gu]
plt.plot(df3['년도'],df3['총인구'])

plt.plot(df3['년도'],df3['총인구(남)'])
plt.plot(df3['년도'],df3['총인구(여)'])# plt.plot(x축, y축)
plt.show


# +
#그래프 따로보기
import matplotlib.pyplot as plt

gu = input('조회할 구 이름을 입력하세요')

df3 = df2[df2['자치구'] == gu]
plt.plot(df3['년도'],df3['총인구'])
plt.show()

plt.plot(df3['년도'],df3['총인구(남)'], label = 'man')
plt.plot(df3['년도'],df3['총인구(여)'], label ='woman')# plt.plot(x축, y축)
plt.legend()
plt.show

# +
#산점도 그래프 그리기
import matplotlib.font_manager as fm

font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)



df3.plot(kind ='hexbin', x = '총인구', y = '년도', label = 'total_population'
        , gridsize = 20)
plt.legend()
plt.show()
# hexbin 산점도 그래프
# -

#bar그래프 그리기
df3.plot(kind ='bar', x = '년도', y = ['총인구(남)','총인구(여)'])
plt.legend()
plt.show()


