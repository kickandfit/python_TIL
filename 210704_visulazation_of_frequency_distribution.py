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
import matplotlib.font_manager as fm

font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name) 
Rawdata = pd.read_csv('./Data/Data_for_study.csv')


Rawdata

# +
# 히스토그램 그리기
plt.hist(Rawdata.건강인지.to_numpy(), bins=9)
# x축 ticks 지정

plt.xticks(np.arange(1,6), labels=["매우 좋음", "좋음", "보통", "나쁨", "매우 나쁨"])
plt.tick_params(axis="x", direction="in", labelsize = 12, pad = 20)

# title, xlabel, ylabel 지정
plt.title("건강인지 히스토그램", fontsize = 30, pad = 30)
plt.xlabel('건강인지', fontsize = 20, loc = 'center', labelpad = 20)
plt.ylabel('도수', fontsize = 20, rotation = 0, loc = 'center', labelpad = 20)
plt.show()

# +
# 히스토그램 그리기, 비율로 그리기
plt.hist(Rawdata.건강인지.to_numpy(), bins=9, density = True)
# x축 ticks 지정

plt.xticks(np.arange(1,6), labels=["매우 좋음", "좋음", "보통", "나쁨", "매우 나쁨"])
plt.tick_params(axis="x", direction="in", labelsize = 12, pad = 20)

# title, xlabel, ylabel 지정
plt.title("건강인지 히스토그램", fontsize = 30, pad = 30)
plt.xlabel('건강인지', fontsize = 20, loc = 'center', labelpad = 20)
plt.ylabel('도수', fontsize = 20, rotation = 0, loc = 'center', labelpad = 20)
plt.show()
# -

Rawdata.건강인지.to_numpy()

#실제 정의에 맞게 그려보기
건강인지 = Rawdata.건강인지.to_numpy()
건강인지 = np.where(건강인지==1, "매우좋음",
               np.where(건강인지==2,"좋음",
               np.where(건강인지==3,"보통",
               np.where(건강인지==4,"나쁨","매우 나쁨"))))
plt.hist(Rawdata.건강인지, bins = 9 , density = True)
plt.show()


