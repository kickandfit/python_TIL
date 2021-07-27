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

#삽입 정렬 구현
data = [7, 2, 1 ,6 ,3, 5, 4, 9 ,8, 0]
for i in range(len(data)):
    min_index = i
    for j in range(i+1, len(data)):
        if data[min_index] > data[j]:
            min_index = j
    data[i], data[min_index] = data[min_index] , data[i]
print(data)


