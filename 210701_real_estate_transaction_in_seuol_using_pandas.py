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

df1=pd.read_csv("./Data/서울특별시_부동산_실거래가_정보_2020년.csv", encoding='cp949')

df1[df1['자치구명']=='성북구']
# -


