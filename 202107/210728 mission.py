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

# ### mission
# - 쿠팡 리뷰 데이터를 이용해 연관분석, 토픽 관계성 분석

from selenium import webdriver
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import time

url = 'https://play.google.com/store/apps/details?id=com.coupang.mobile&hl=ko&gl=US&showAllReviews=true'
driver = webdriver.Chrome('c:/pydata/chromedriver.exe')
driver.get(url)
n = 20
for i in range(n):
    try:
        driver.find_element_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz:nth-child(4) > div > div.ZfcPIb > div > div > main > div > div.W4P4ne > div:nth-child(2) > div.PFAhAf > div > span > span').click()
        time.sleep(2)
    except:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)
html = driver.page_source
soup = bs(html , 'html.parser')
soup

body_soup = soup.find_all('div', class_="UD7Dzf")
new_list = []
for i in body_soup:
    body = i.find('span', jsname="bN97Pc").text
    new_list.append(body)

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import re
from konlpy.tag import Okt


# +
dataset = []
df = pd.DataFrame(new_list, columns=['댓글'])
okt= Okt()
for txt in tqdm(df['댓글']):
    dataset.append(okt.nouns(re.sub('[^가-힣a-zA-Z ]', "", txt)))
tren = TransactionEncoder()
tren_ary = tren.fit(dataset).transform(dataset)

tren_df = pd.DataFrame(tren_ary, columns=tren.columns_)
# -

from mlxtend.frequent_patterns import association_rules
apr_item = apriori(tren_df, min_support = 0.1, use_colnames = True)
association_rules(apr_item, metric = 'lift', min_threshold = 1.0)

import networkx as nx
import matplotlib.pyplot as plt
from apyori import apriori

support_res = (list(apriori(dataset, min_support = 0.05)))
df1 = pd.DataFrame()
df1 = pd.DataFrame(support_res)
df1['length'] = df1['items'].apply(lambda x: len(x))

df1

    df = df1[(df1['length']==2)&(df1['support']>=0.05)].sort_values(by = 'support', ascending = False)
    gra = nx.Graph()
    arp = (df['items'])
    gra.add_edges_from(arp)


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

plt.figure(figsize=(10, 8))
nx.draw_networkx(gra, node_color=list(prk.values()), node_size=nsize,
                 alpha=0.5, edge_color='0.1', #cmap=plt.cm.YlGn,
                 font_family=font_family,font_size=15)
plt.draw()
# -


