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

# ### CSV 형식의 파일 읽어오기
#
# - csv 모듈 이용
# - pandas 모듈 이용

# +
import pandas as pd
import csv

f=open('./Data/seoul.csv','r', encoding='cp949') 
# 엑셀을 열었는데 한글이 보이면 cp949
data = csv.reader(f, delimiter=",") # 안에 있는 데이터를 , 단위로 구분해서 가져와라

print(data)
f.close()
# -


