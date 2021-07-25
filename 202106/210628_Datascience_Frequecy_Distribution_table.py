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
import numpy as np
import matplotlib.pyplot as plt

# pandas는 DataFram을 이용해, 데이터를 관리하는 모든 과정을 편리하게 해줌
# numpy는 빠른 수학 연산에 필수인 라이브러리
# matplotlib.pyplot은 시각화에 필수인 라이브러리
# -

Rawdata = pd.read_csv("./Data/Data_for_study.csv")
Rawdata

# +
# 질적 변수 도수분포표 만들기

Rawdata.성별.value_counts()
#valeue_counts() 시리즈로 빈도표를 출력
#1은 남자, 2는 여자, 총 55748명 중 남자가 29,059명, 여자가 26,689명

# +
성별_빈도표 = pd.DataFrame(Rawdata.성별.value_counts())
성별_빈도표.columns = ["freq"]
성별_빈도표["ratio"] = np.round(성별_빈도표.freq/sum(성별_빈도표.freq),2)
성별_빈도표

#pd.DataFrame.columns : DataFrame의 컬럼명(열)을 조작한다
#np.round(array,n) : array의 값들을 n의 자리에서 반올림한다.

# +
# 양적 도수 분포표 만들기

키_빈도표 = pd.DataFrame(Rawdata.키.value_counts())
키_빈도표.columns = ["freq"]
키_빈도표["ratio"] = np.round(키_빈도표.freq/sum(키_빈도표.freq),2)
키_빈도표

#데이터를 쉽게 보려고 만들었는데 여전히 가독성 저하
#키와 같은 양적 변수는 들어갈 수 있는 값이 매우 다양하여 등급(class)이 많음
#도수분포표로 만들면 보기 힘들기 때문에, 범주화(Categonization)시켜 단순화
# -

키_array = Rawdata.키.to_numpy()
print("min",키_array.min())
print("max",키_array.max())
#DataFrame.column.to_numpy() : DataFrame의 특정열 column을 numpy의 array로 변환
#array.min() : 배열의 최솟값
#array.max() : 배열의 최댓값


#최솟값, 최댓값을 기준으로 범주화하기
키_범주 = np.where(키_array <= 140, "140 이하",
               np.where((키_array>140)&(키_array<=150),"140~150",
                np.where((키_array>150)&(키_array<=160),"150~160",
                np.where((키_array>160)&(키_array<=170),"160~170",
                np.where((키_array>170)&(키_array<=180),"170~180",
                np.where((키_array>180)&(키_array<=190),"180~190","190 이상"))))))
키_도수분포표 = pd.DataFrame(pd.Series(키_범주).value_counts(),columns=["freq"])
키_도수분포표.sort_index(inplace=True)
키_도수분포표
#np.where(조건, ,a,b): 조건에 해당하는 경우 a로 해당하지 않는 경우 b를 반환
#DataFrame.sort_index():index로 정렬함

#비율 추가
키_도수분포표["ratio"] = np.round(키_도수분포표.freq/sum(키_도수분포표.freq),2)
키_도수분포표

# +
#누적 빈도, 누적 비율추가(cumulative frequency, cumulative ratio)
키_도수분포표["cum_freq"] = np.cumsum(키_도수분포표.freq)
키_도수분포표["cum_ratio"]= np.cumsum(키_도수분포표.ratio)
키_도수분포표

# np.cumsum(array):array 주어진 순서대로 누적함

# +
# 상대 빈도(Relative frequency = ratio)
print("만연령 min:",Rawdata.연령.min())
print("만연령 max:",Rawdata.연령.max())

# 대상 집단의 연령범위는 만 12~18세이며, 성별이 남,녀 두가지가 들어 있음
# 단순하게 도수분포료를 보고, 해당 집단의 특성을 파악하면 정보 전달의 오류가 발생함
# 키 170cm는 12세 여성이라는 집단에서는 굉장히 큰 키이지만, 18세 남성 집단에서는 큰 키가 아님
# 위 도수분포표는 만 12~18세 중 고등학생 표본집단을 대상으로 하였기에 위 도수분포표만으로는 둘은 같게 볼 수 있음
# 보다 정밀한 데이터 파악을 위해선, 연구자의 의도를 가장 잘 보여줄 수 있는 도수분포표 생성이 필요함
# 따라서 다음 단계에서는 만 16세인 사람으로 한정하여, 남성과 여성의 키를 알아보도록 하겠음

# +
def cat_height(array):
    cat_array = np.where(키_array <= 140, "140 이하",
               np.where((키_array>140)&(키_array<=150),"140~150",
                np.where((키_array>150)&(키_array<=160),"150~160",
                np.where((키_array>160)&(키_array<=170),"160~170",
                np.where((키_array>170)&(키_array<=180),"170~180",
                np.where((키_array>180)&(키_array<=190),"180~190","190 이상"))))))
    return cat_array

def Freq_table(array):
    
    freq_table = pd.DataFrame(pd.Series(array).value_counts(), columns=["freq"])
    freq_table.sort_index(inplace = True)
    freq_table["ratio"] = freq_table.freq/sum(freq_table.freq)
    freq_table["cum_freq"] = np.cumsum(freq_table.freq)
    freq_table["cum_ratio"] = np.round(np.cumsum(freq_table.ratio),2)
    
    #반올림 및 총합 생성
    freq_table.loc["총합"] = [sum(freq_table.freq), sum(freq_table.ratio),"",""]
    freq_table["ratio"] = np.round(freq_table["ratio"], 2)
    
    return freq_table
    
# 위에서 만들었던, 양적 변수의 범주화(키)와 도수분포표를 출력하는 코드들을 정리
# 별개의 함로 만들어 추가로 총합이 계산되도록 추가
# 코드 함수화를 통해, 코드의 재활용성, 가시성, 유지보수의 용이함 등의 이점


# -

남자_16세_키 =Rawdata[(Rawdata["연령"]==16)&(Rawdata["성별"]==1.0)]["키"].to_numpy()
여자_16세_키 =Rawdata[(Rawdata["연령"]==16)&(Rawdata["성별"]==2.0)]["키"].to_numpy()

Freq_table(cat_height(남자_16세_키))

Freq_table(cat_height(여자_16세_키))

# +
# 위의 표를 하나로 합쳐보기

# 성별에 따른 변수명 구분을 위해 column 앞에 특정 문자를 붙여줌
M_DF = Freq_table(cat_height(남자_16세_키))
M_DF = M_DF.add_prefix("M")
F_DF = Freq_table(cat_height(여자_16세_키))
F_DF = F_DF.add_prefix("F")

# 병합 및, 결측값은 0으로 채움
T_DF = pd.concat([M_DF,F_DF], axis = 1).sort_index()
T_DF.fillna(0, inplace=True)

T_DF

# 아래 표를 보면, 남성(M)과 여성(F)의 도수분포표를 비율(ratio)을 이용하여, 두집단의 규모 차이를 무시하고 비교 가능
# 만 16세 남성의 59%는 170~180cm에 존재하며, 만 16세 여성의 50%sms 160~170cm에 존재함을 알 수 있음
# -


