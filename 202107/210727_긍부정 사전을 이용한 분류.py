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

# ### KNU 한국어 감성사전 -DI LAB
# - SentiWord info.json 한국어 감성사전 제공

import json
import pandas as pd
from tqdm import tqdm


SentiWord = pd.read_json('c:/pydata/sw/SentiWord_info.json')
SentiWord.to_csv('c:/pydata/sw/SentiWord_info.csv', index=False)

SentiWord = pd.read_csv('c:/pydata/sw/SentiWord_info.csv')
word = '알쏭'
SentiWord.loc[len(SentiWord)] = ['징용','징용',-2]
SentiWord.loc[len(SentiWord)] = ['합의','합의',1]
SentiWord.tail()
def pos_neg(word):
    tmp =SentiWord[(SentiWord['word']==word) | (SentiWord['word_root']==word)]
    try:
        word_res = (word,tmp['polarity'][tmp.index[0]])
    except:
        word_res = (word, 0)
    return word_res


pos_neg('알쏭')

# +
df = pd.read_csv('c:/pydata/중앙일보_일본 올림픽.csv', encoding = 'cp949')
txt = ''
for i in df.index:
    txt = txt +' ' +str(df['상세내용'].loc[i])
    
# print(txt)
    
# -



# +
from konlpy.tag import Okt
okt = Okt()
morp = okt.morphs(txt)

# morp

# +
from tqdm import tqdm
pos_list = []
neg_list = []
unkown_list = []

for noun in tqdm(morp, '긍/부정 나누기'):
    word_res = pos_neg(noun)
    if word_res[1] > 0:
        pos_list.append(word_res[0])
    elif word_res[1] < 0 :
        neg_list.append(word_res[0])
    else:
        unkown_list.append(word_res)

# -

print('긍정키워드 수:', len(pos_list),'개')
print('부정키워드 수:', len(neg_list),'개')
print('중립 또는 모름 키워드 수:', len(unkown_list),'개')

# +
from collections import Counter #jdk 제공 모듈

pos_count = dict(Counter(pos_list).most_common()) # 단어별 갯수 계산 및 내림차순 정렬, 딕셔너리 구조
neg_count = dict(Counter(neg_list).most_common())
unkown_count = dict(Counter(unkown_list).most_common())
print(pos_count)
print('========================================')
# print(neg_count)
# print('========================================')
# print(unkown_count)
# print('========================================')
# -

#데이터 추가하기!
SentiWord.loc[len(SentiWord)] = ['징용','징용',-2]
SentiWord.loc[len(SentiWord)] = ['합의','합의',1]
SentiWord.tail()


stop_words = '로 것 와 당 명 위 신 사람 하기 뜻 점 순 타 보'
stop_words = stop_words.split(" ")
stop_words

tmp_dic={}
for key, values in pos_count.items():#items()는 딕셔너리 구조를 튜플구조로
    if key not in stop_words:
        tmp_dic[key]=values
pos_count = tmp_dic


from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


### https://www.w3schools.com/colors/colors_hexadecimal.asp
def color_func(**kawargs):
    color="#0b1177"
    return color



img_path = 'c:/pydata/sw/good.jpg'
cloud_mask = np.array(Image.open(img_path))
cloud_mask.shape

img = Image.open(img_path)
img.size

wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf",
                      background_color="white", mask=cloud_mask)
wc = wordcloud.generate_from_frequencies(pos_count)
plt.figure(figsize=(10,15))
plt.imshow(wc.recolor(color_func=color_func), interpolation='bilinear')
plt.axis("off")
plt.show()


### https://www.w3schools.com/colors/colors_hexadecimal.asp
def color_func2(**kawargs):
    color="#f20101"
    return color


tmp_dic={}
for key, values in neg_count.items():#items()는 딕셔너리 구조를 튜플구조로
    if key not in stop_words:
        tmp_dic[key]=values
neg_count = tmp_dic
img_path = 'c:/pydata/sw/bad.jpg'
cloud_mask = np.array(Image.open(img_path))
cloud_mask.shape
img = Image.open(img_path)
wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf",
                      background_color="white", mask=cloud_mask)
wc = wordcloud.generate_from_frequencies(neg_count)
plt.figure(figsize=(10,15))
plt.imshow(wc.recolor(color_func=color_func2), interpolation='bilinear')
plt.axis("off")
plt.show()





