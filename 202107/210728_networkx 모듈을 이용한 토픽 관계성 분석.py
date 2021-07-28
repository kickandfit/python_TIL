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

# ### networkx 기본

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import re

graph = nx.Graph()
df=pd.DataFrame({'from' : ['a', 'b', 'c', 'a', 'd', 'e'], 
                 'to' : ['d', 'a', 'e', 'c', 'a', 'e'],
                'weight' : [1, 2, 3, 4, 5, 6]})
print(df)
gra = nx.from_pandas_edgelist(df, 'from', 'to', create_using = nx.DiGraph)
nx.draw(gra, with_labels = True)
plt.show()

# +
# 연습
#graph.add_nodes_from((1,2,3,4,5))
# graph.add_edges_from([(1,2),(1,3),(1,4),(3,5)])
# nx.draw(graph, with_labels=True)
# plt.show()
# -

# ### 전국 공원리뷰를 이용한 네트워크 분석

f = open('c:/pydata/korpark10.txt', 'r', encoding = 'utf-8')
txt_data = f.readlines() # read 는 전체 파일을 메모리 하나의 공간에 넣는것
# readlines는 전체 파일을 메모리에 줄단위로 공간에 넣는다
# readline은 한줄만 가져온다
f.close()
txt_data[:5]

# ### 정규식 표현

# +
from konlpy.tag import Okt
from tqdm import tqdm
okt = Okt()

dataset = []
for txt in tqdm(txt_data):
    nons =okt.nouns(re.sub('[^ㄱ-ㅣ가-힣a-zA-Z]\s',"",txt))
    if len(nons) >= 1:
        dataset.append(nons)
print(dataset[:5])
# -

from apyori import apriori

support_res = (list(apriori(dataset, min_support = 0.05)))

df1 = pd.DataFrame(support_res)
df1

df1['length'] = df1['items'].apply(lambda x: len(x))
df1

df = df1[(df1['length']==2)&(df1['support']>=0.05)].sort_values(by = 'support', ascending = False)

gra = nx.Graph()
arp = (df['items'])
gra.add_edges_from(arp)
arp

import numpy as np
prk = nx.pagerank(gra)
nsize = np.array([val for val in prk.values()])
nsize = 2000*(nsize-min(nsize))/(max(nsize)-min(nsize))

pos = nx.planar_layout(gra)
pos

# +
# 한글폰트 설정
from matplotlib import font_manager
font_family = font_manager.FontProperties(fname='C:/Windows/Fonts/malgunsl.ttf').get_name()

plt.figure(figsize=(7,7))
nx.draw_networkx(gra, node_color=list(prk.values()), node_size=nsize,
                 alpha=0.5, edge_color='0.3', #cmap=plt.cm.YlGn,
                 font_family=font_family,font_size=15)
plt.draw()

# -

#













