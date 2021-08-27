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

# 뭐가 틀린건데 도대체 뭐가 문제인줄 모르겠다 우선은
K, P , N = map(int, input().split()) 
product = 1
for i in range(N):
    product *= P
result = (K*product)%1000000007
print(result)




