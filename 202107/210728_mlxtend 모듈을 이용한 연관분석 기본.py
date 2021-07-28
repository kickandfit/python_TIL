# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ### 연관분석
# - mlxtend : http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/association_rules/
#

# +
# # !pip install mlxtend
# -

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

dataset=[['사과','치즈','생수'],
        ['생수','호두','치즈','고등어'],
        ['수박','사과','생수'],
        ['생수','호두','치즈','옥수수']]


tren = TransactionEncoder()
tren_ary = tren.fit(dataset).transform(dataset)
print(tren.columns_)
print(tren_ary)

df1 = pd.DataFrame(tren_ary, columns = tren.columns_)
df1

# ###  apriori
# - 지지도를 계산해 주는 모듈
# - tren.columns_ : ['고등어', '사과', '생수', '수박', '옥수수', '치즈', '호두']
# - min_support : 최소 지지도(전체의 입력 값)
# - itemsets 토픽 표현 : use_colnames = True

# ### apply() 참조
# -lambda x : len(x)
# - def aa(x):
#     - return len(x)
# - pandas에서 DataFrame 구조에서 map과 같은 역할을 함

fre_items = apriori(df1, min_support = 0.3, use_colnames = True)
fre_items['length'] = fre_items['itemsets'].apply(lambda x:len(x))
# fre_items

fre_items1 = fre_items[(fre_items['length']>=2)
                      &(fre_items['support']>=0.3)
                     ].sort_values(by='support', ascending=False)
# fre_items1

fre_items = apriori(df1, min_support = 0.3, use_colnames = True)
from mlxtend.frequent_patterns import association_rules
association_rules(fre_items, metric="confidence", min_threshold=0.3)


association_rules(fre_items, metric="lift", min_threshold=1.3)







