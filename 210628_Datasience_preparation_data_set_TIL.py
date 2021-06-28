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

print("HI, git and py")

3+4

# 210628 | Learn datasience as example
import pandas as pd

Rawdata = pd.read_spss("./Data/kyrbs2019.sav") 
# 파일 경로 위치가 계속해서 에러났음.
# 파일 위치는 현재 작업하고 있는 쥬피터 노트북의 폴더가 기준
# ./ 는 현재 쥬피터 노트북의 위치를 나타냄 거기서 시작하여, 경로를 설정해줘야함
# 원시자료를 다루고자 할 때, 변수들이 정리되어 있는 지침서나 코딩북을 참조할 것.

Target_DF = Rawdata[["SEX","AGE","HT","WT",
                     "E_S_RCRD","E_SES","PR_HT","PA_TOT",
                     "M_SLP_EN","AC_LT","TC_LT","INT_WD_MM","INT_WK_MM"]]
# 타겟 변수 추출(필요 변수 추출)

# 타켓 변수 한글이름 변환
Target_DF.columns=["성별","연령","키","몸무게"
                  "학업성적","경제상태","건강인지","운동일수","스트레스인지",
                  "피로회복정도","음주경험","흡연경험","주중_인터넷이용시간","주말_인터넷이용시간"]
#파이썬에는 한글 변수 사용이 가능하나 타 언어에서는 불가능함으로 사용 지양
#한글 변수보다는 영어 변수에 익숙해질 것

Target_DF

# +
#NaN(Missing value, 결측값) 어떠한 연유로 값이 누락되었음
#결측값을 해결하는 문제는 데이터 분석에서 매우 민감하고 중요한 부분, 그러나 현재는 통계가 목적이 아니므로 간단히 해결하고감
Target_DF.isna().sum()

#결측값이 발생한 이유에 대한 분석은 보고서를 읽는 것이 가장 정확함
# -

Target_DF["주중_인터넷이용시간"] = Target_DF.주중_인터넷이용시간.fillna(0)
Target_DF["주말_인터넷이용시간"] = Target_DF.주말_인터넷이용시간.fillna(0)
Target_DF.dropna(inplace = True)
Target_DF.reset_index(drop = True, inplace = True)
Target_DF
#settingWithCopyWarning
#Pandas의 메모리 절약하기 위한 방법인 데이터 종속성으로 인해 발생하는 문제
#기존의 RawData와 Target_DF가 별개로 존재하게 되므로 발생하는 문제
#이를 해결하기 위해 copy함수를 이용해서 Target_DF를 생성할 때, Rawdata와 별개로 흐르게 만들면 됨

#추출된 데이터 set을 저장해 놓기
Target_DF.to_csv("Data_for_study.csv", index = False)


