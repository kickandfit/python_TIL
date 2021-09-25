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

# + [markdown] id="eLgYkX8h17eE"
# # 필요 라이브러리 설치

# + colab={"base_uri": "https://localhost:8080/"} id="oDU0P6mD1vu_" executionInfo={"status": "ok", "timestamp": 1631419993751, "user_tz": -540, "elapsed": 28344, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="8dd78830-ec59-4f45-f6fd-2368fdf066b7"
# !apt-get update
# !apt-get install g++ openjdk-8-jdk
# !pip3 install konlpy

# + [markdown] id="_rtFwQ522CDd"
# # 라이브러리 import, 데이터 셋 다운로드

# + id="f5lcD1rl1-SW"
import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
import re
from konlpy.tag import Okt
okt = Okt()
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np

okt = Okt()

# + colab={"base_uri": "https://localhost:8080/"} id="FOoxqCHj2PH3" executionInfo={"status": "ok", "timestamp": 1631419998465, "user_tz": -540, "elapsed": 1372, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="2a4e6a83-c859-48aa-8d23-6aca85827de7"
urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt", 
                           filename="ratings_train.txt")
urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt", 
                           filename="ratings_test.txt")

# + [markdown] id="WY66_myp2Ra6"
# # 데이터셋 살펴보기(EDA)

# + id="3kXYk5Jx2QJx"
train_data = pd.read_table('ratings_train.txt')
test_data = pd.read_table('ratings_test.txt')

# + colab={"base_uri": "https://localhost:8080/"} id="1eJNZaLq2Wem" executionInfo={"status": "ok", "timestamp": 1631419998859, "user_tz": -540, "elapsed": 18, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="c6e7f978-a177-4909-8590-1b2168255255"
train_data.info()

# + colab={"base_uri": "https://localhost:8080/"} id="Wtz5Xgs82YEX" executionInfo={"status": "ok", "timestamp": 1631419998860, "user_tz": -540, "elapsed": 16, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="5ffbabf4-c597-428d-ece2-531d00ea4c50"
test_data.info()

# + colab={"base_uri": "https://localhost:8080/", "height": 204} id="2bv3F9pn2ZKK" executionInfo={"status": "ok", "timestamp": 1631419998860, "user_tz": -540, "elapsed": 13, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="a3c355b8-efb0-4bf2-d40d-4374dfd14f3f"
train_data.head()

# + [markdown] id="m5Z5jLAU2de2"
# ## 텍스트 전처리

# + colab={"base_uri": "https://localhost:8080/"} id="xNj5-hin2aP2" executionInfo={"status": "ok", "timestamp": 1631419998860, "user_tz": -540, "elapsed": 11, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="e417f6cb-f113-4ffa-df44-bcae628dceec"
# 중복 제거를 위한 중복 체크
# 유니크한 value의 개수를 나타냄
train_data['document'].nunique(), train_data['label'].nunique()

# + colab={"base_uri": "https://localhost:8080/"} id="mnFy1oJE2fq1" executionInfo={"status": "ok", "timestamp": 1631419998861, "user_tz": -540, "elapsed": 9, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="ee735c02-d517-475e-abe9-24eb92f0389c"
test_data['document'].nunique(), test_data['label'].nunique() 

# + id="SGwrZ7Mf2iqS"
train_data.drop_duplicates(subset=['document'], 
                           inplace=True) # document 열에서 중복인 내용이 있다면 중복 제거

# + id="TCR0QoKn2lO_"
test_data.drop_duplicates(subset=['document'], 
                           inplace=True) # document 열에서 중복인 내용이 있다면 중복 제거

# + colab={"base_uri": "https://localhost:8080/", "height": 280} id="u1vbJYJX2nha" executionInfo={"status": "ok", "timestamp": 1631419999261, "user_tz": -540, "elapsed": 21, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="ee11a88c-dda4-4ad4-b0d5-60ef28c687a0"
train_data['label'].value_counts().plot(kind = 'bar')

# + colab={"base_uri": "https://localhost:8080/", "height": 280} id="ec19OGsc2o-u" executionInfo={"status": "ok", "timestamp": 1631419999261, "user_tz": -540, "elapsed": 19, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="cd60c639-ded9-4ecc-ad53-7e20c4dd6dcc"
test_data['label'].value_counts().plot(kind = 'bar')

# + colab={"base_uri": "https://localhost:8080/"} id="9shpLBUyEkcZ" executionInfo={"status": "ok", "timestamp": 1631419999261, "user_tz": -540, "elapsed": 16, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="c2078ccd-1b9b-41d9-d56f-b994f51f9622"
train_data.isnull().sum()

# + colab={"base_uri": "https://localhost:8080/"} id="uv5k7H-TE6Ci" executionInfo={"status": "ok", "timestamp": 1631419999262, "user_tz": -540, "elapsed": 15, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="aad4bb56-4564-44f6-99a3-bc31789ff9d7"
test_data.isnull().sum()

# + colab={"base_uri": "https://localhost:8080/"} id="YaugUKHw2qs8" executionInfo={"status": "ok", "timestamp": 1631419999262, "user_tz": -540, "elapsed": 11, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="b1f5fe63-c1b6-4256-83c7-8e35190c94f0"
train_data.document.isnull()

# + colab={"base_uri": "https://localhost:8080/"} id="W3yYNRUt2ugE" executionInfo={"status": "ok", "timestamp": 1631419999262, "user_tz": -540, "elapsed": 8, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="5bf2f412-7e12-4439-cded-4df292291902"
print(train_data.loc[train_data.document.isnull()])
print(test_data.loc[test_data.document.isnull()])

# + colab={"base_uri": "https://localhost:8080/"} id="UcJmVl5p2y_e" executionInfo={"status": "ok", "timestamp": 1631419999514, "user_tz": -540, "elapsed": 258, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="b969c89b-f7b8-4a24-81b7-f7b0968a20ef"
train_data = train_data.dropna(how = 'any') # Null 값이 존재하는 행 제거
print('학습용:', train_data.isnull().values.any()) # Null 값이 존재하는지 확인

# + colab={"base_uri": "https://localhost:8080/"} id="UtjVfH3621Gd" executionInfo={"status": "ok", "timestamp": 1631419999515, "user_tz": -540, "elapsed": 8, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="84032bbf-d9f4-45b7-e4bd-7aae62b0e0ce"
test_data = test_data.dropna(how = 'any') # Null 값이 존재하는 행 제거
print('테스트:', test_data.isnull().values.any()) # Null 값이 존재하는지 확인

# + colab={"base_uri": "https://localhost:8080/", "height": 204} id="mS7nQx5l21_8" executionInfo={"status": "ok", "timestamp": 1631419999515, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="114f9387-f4c9-46d1-db68-834cbe1d8bf4"
test_data.head()

# + colab={"base_uri": "https://localhost:8080/"} id="SYoQI0yB23c7" executionInfo={"status": "ok", "timestamp": 1631419999515, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="021d4792-d895-469a-e114-e1773671c13b"
train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
train_data['document']

# + colab={"base_uri": "https://localhost:8080/"} id="VM4eHVQw25lr" executionInfo={"status": "ok", "timestamp": 1631419999809, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="6076db4c-f686-4766-d920-aefadc0b7aaf"
test_data['document'] = test_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
test_data['document']

# + colab={"resources": {"http://localhost:8080/nbextensions/google.colab/files.js": {"data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK", "ok": true, "headers": [["content-type", "application/javascript"]], "status": 200, "status_text": ""}}, "base_uri": "https://localhost:8080/", "height": 76} id="FPNIXIuR26pM" executionInfo={"status": "ok", "timestamp": 1631420009464, "user_tz": -540, "elapsed": 9658, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="a0dd3404-8a11-4f45-a2a7-b7a0920598b2"
from google.colab import files
myfile = files.upload()

# + colab={"base_uri": "https://localhost:8080/", "height": 204} id="MCJheN0N29lR" executionInfo={"status": "ok", "timestamp": 1631420777866, "user_tz": -540, "elapsed": 386, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="2aafd0fa-0629-4851-b637-b02fd5a9864e"
k_stopword = pd.read_csv('/content/korean_stopword.csv')
k_stopword.head()

# + colab={"base_uri": "https://localhost:8080/"} id="IQPt_3133Flq" executionInfo={"status": "ok", "timestamp": 1631420778934, "user_tz": -540, "elapsed": 3, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="2291ec1b-51b3-40ea-ce53-d5c29b6e23ff"
stopword = list(k_stopword['불용어'])+['을','은','를','이가','과','의','는','에']
stopword[:10]

# + colab={"base_uri": "https://localhost:8080/"} id="wOQ5Ordx3f6J" executionInfo={"status": "ok", "timestamp": 1631421235124, "user_tz": -540, "elapsed": 455465, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="c2eeec04-e1fd-49d6-e350-da7af677ebbe"
X_train = []
for i in train_data.index:
    morph = okt.morphs(train_data.loc[i]['document'])
    temp_X = []
    for txt in morph:
      if txt not in stopword:
       temp_X.append(txt)
    X_train.append(temp_X)
X_train[:5]

# + colab={"base_uri": "https://localhost:8080/"} id="7HHwkelz63Tx" executionInfo={"status": "ok", "timestamp": 1631421235125, "user_tz": -540, "elapsed": 18, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="757e80d9-4d31-4933-da59-ba6549663693"
# 빈 샘플 제거
drop_train = []
for index, sentence in enumerate(X_train):
  if len(sentence) < 1:
    drop_train.append(index)
drop_train[:3]

# + colab={"base_uri": "https://localhost:8080/"} id="jPxqlMsl8Ot8" executionInfo={"status": "ok", "timestamp": 1631421235125, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="58820e4c-f44f-4e66-b1f5-2413e5cc088d"
y_train = np.array(train_data['label'])
y_train[:6]

# + colab={"base_uri": "https://localhost:8080/"} id="CAJWzqiP69uH" executionInfo={"status": "ok", "timestamp": 1631421235125, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="269de8ec-dbd1-41de-aad7-446d42dda522"
X_train = np.delete(X_train, drop_train, axis=0)
y_train = np.delete(y_train, drop_train, axis=0)
print(len(X_train))
print(len(y_train))

# + colab={"base_uri": "https://localhost:8080/"} id="PJJDlOO53jyk" executionInfo={"status": "ok", "timestamp": 1631421411873, "user_tz": -540, "elapsed": 176752, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="97468df9-85dc-48c2-a2bb-8b5c9a66f1ad"
X_test = []
for i in test_data.index:
    morph = okt.morphs(test_data.loc[i]['document'])
    temp_X = []
    for txt in morph:
      if txt not in stopword:
       temp_X.append(txt)
    X_test.append(temp_X)
X_test[:5]

# + colab={"base_uri": "https://localhost:8080/"} id="Zgp6XMRY7Cr6" executionInfo={"status": "ok", "timestamp": 1631421411873, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="4264c161-ff99-4c6e-de59-86c7bc9a6ed2"
# 빈 샘플 제거
drop_test = []
for index, sentence in enumerate(X_test):
  if len(sentence) < 1:
    drop_test.append(index)
drop_test[:3]

# + colab={"base_uri": "https://localhost:8080/"} id="VRj90KRk8YKR" executionInfo={"status": "ok", "timestamp": 1631421411874, "user_tz": -540, "elapsed": 8, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="3d12f3b2-0c5b-4600-c836-d6c909e0ddf9"
y_test = np.array(test_data['label'])
y_test[:6]

# + colab={"base_uri": "https://localhost:8080/"} id="4K4Jq6lD7Cr6" executionInfo={"status": "ok", "timestamp": 1631421411874, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="1ed27e50-c92a-43b8-d6da-716c6654639f"
X_test = np.delete(X_test, drop_test, axis=0)
y_test = np.delete(y_test, drop_test, axis=0)
print(len(X_test))
print(len(y_test))

# + [markdown] id="m_Dw0yh2-dAY"
# # 토큰화

# + colab={"base_uri": "https://localhost:8080/"} id="qOUhcUy_-NL8" executionInfo={"status": "ok", "timestamp": 1631421415660, "user_tz": -540, "elapsed": 3789, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="1924a8a6-a079-45a7-90d0-50cb82d6014d"
# 정수 인코딩
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
print(tokenizer.word_index)

# + colab={"base_uri": "https://localhost:8080/"} id="QHzgurNs-hTO" executionInfo={"status": "ok", "timestamp": 1631421415660, "user_tz": -540, "elapsed": 215, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="6034176b-8336-4cc8-ff37-1109212b46a3"
len(tokenizer.word_index)

# + colab={"base_uri": "https://localhost:8080/"} id="th6Vut0V-ip1" executionInfo={"status": "ok", "timestamp": 1631421420630, "user_tz": -540, "elapsed": 251, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="0423dbcc-75da-416e-8579-e81756f6924c"
threshold = 3
total_cnt = len(tokenizer.word_index) # 단어의 수
rare_cnt = 0 # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
total_freq = 0 # 훈련 데이터의 전체 단어 빈도수 총 합
rare_freq = 0 # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총 합

# 단어와 빈도수의 쌍(pair)을 key와 value로 받는다.
for key, value in tokenizer.word_counts.items():
    total_freq = total_freq + value

    # 단어의 등장 빈도수가 threshold보다 작으면
    if(value < threshold):
        rare_cnt = rare_cnt + 1
        rare_freq = rare_freq + value

print('단어 집합(vocabulary)의 크기 :',total_cnt)
print('등장 빈도가 %s번 이하인 희귀 단어의 수: %s'%(threshold - 1, rare_cnt))
print("단어 집합에서 희귀 단어의 비율:", (rare_cnt / total_cnt)*100)
print("전체 등장 빈도에서 희귀 단어 등장 빈도 비율:", (rare_freq / total_freq)*100)

# + colab={"base_uri": "https://localhost:8080/"} id="01i1PAlo-ktm" executionInfo={"status": "ok", "timestamp": 1631421422532, "user_tz": -540, "elapsed": 372, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="8215dea0-f040-42c0-b52d-1b724816e158"
# 전체 단어 개수 중 빈도수 2이하인 단어 개수는 제거.
# 0번 패딩 토큰과 1번 OOV 토큰을 고려하여 +2
vocab_size = total_cnt - rare_cnt + 2
print('단어 집합의 크기 :',vocab_size)

# + colab={"base_uri": "https://localhost:8080/"} id="w4T8-Qcw-luR" executionInfo={"status": "ok", "timestamp": 1631421427761, "user_tz": -540, "elapsed": 3091, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="86901582-1339-4165-d00a-21fc5e1af1e8"
tokenizer = Tokenizer(vocab_size, oov_token = 'OOV') 
tokenizer.fit_on_texts(X_train)
X_train = tokenizer.texts_to_sequences(X_train)
X_train[:3]

# + colab={"base_uri": "https://localhost:8080/"} id="ANPE3GfI-nmJ" executionInfo={"status": "ok", "timestamp": 1631420624066, "user_tz": -540, "elapsed": 20, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="6dbab71a-e2be-4fa5-f17f-f3d512b19304"
tokenizer.word_index

# + colab={"base_uri": "https://localhost:8080/"} id="-Q1atnXdBGZL" executionInfo={"status": "ok", "timestamp": 1631421434632, "user_tz": -540, "elapsed": 392, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="403acba4-d27e-4d82-e7cf-96f46df47c15"
print('리뷰의 평균 길이 :',sum(map(len, X_train))/len(X_train))

# + colab={"base_uri": "https://localhost:8080/", "height": 279} id="YL98mEq0BMfx" executionInfo={"status": "ok", "timestamp": 1631421437854, "user_tz": -540, "elapsed": 372, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="568e93f9-ca19-48f6-bcef-3e615ee05ad3"
plt.hist([len(s) for s in X_train], bins=50)
plt.xlabel('length of samples')
plt.ylabel('number of samples')
plt.show()


# + id="EcrV3SH9BOC5"
def below_threshold_len(max_len, nested_list):
  cnt = 0
  for s in nested_list:
    if(len(s) <= max_len):
        cnt = cnt + 1
  print('전체 샘플 중 길이가 %s 이하인 샘플의 비율: %s'%(max_len, (cnt / len(nested_list))*100))


# + colab={"base_uri": "https://localhost:8080/"} id="9oENWb9UBSKZ" executionInfo={"status": "ok", "timestamp": 1631421442526, "user_tz": -540, "elapsed": 388, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="0fc17e59-a845-472b-cb66-7c40e95648a6"
max_len = 30
below_threshold_len(max_len, X_train)

# + [markdown] id="JzxC5nDTBZzZ"
# ## 데이터 길이 맞추기

# + colab={"base_uri": "https://localhost:8080/"} id="YjnNUKSfBTDi" executionInfo={"status": "ok", "timestamp": 1631421446819, "user_tz": -540, "elapsed": 958, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="ffec97eb-bced-442e-f880-8c82ac70d0c4"
from tensorflow.keras.preprocessing.sequence import pad_sequences
X_train = pad_sequences(X_train, maxlen = max_len)
X_train[:3]

# + colab={"base_uri": "https://localhost:8080/"} id="t3V0pcevBekP" executionInfo={"status": "ok", "timestamp": 1631421450221, "user_tz": -540, "elapsed": 668, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="23a9612b-b14d-45dc-af4f-be039d6953dd"
X_test = tokenizer.texts_to_sequences(X_test)
X_test = pad_sequences(X_test, maxlen = max_len)
X_test.shape

# + colab={"base_uri": "https://localhost:8080/"} id="NgWLZZbNCC96" executionInfo={"status": "ok", "timestamp": 1631421451690, "user_tz": -540, "elapsed": 262, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="29f9a690-ed70-4229-ba73-ce6a358ae429"
vocab_size

# + [markdown] id="EkrOrcgFYj6j"
# # RNN을 이용한 학습

# + id="hQu5_8p8BhIm"
# RNN 
from tensorflow.keras.layers import Embedding, Dense, SimpleRNN
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# + id="gpA7W185BmiL"
model_RNN = Sequential()
model_RNN.add(Embedding(input_dim = vocab_size, output_dim = 128))
model_RNN.add(SimpleRNN(128, return_sequences = True))
model_RNN.add(SimpleRNN(64, return_sequences = False))
model_RNN.add(Dense(32, activation='relu'))
model_RNN.add(Dense(1, activation='sigmoid'))

# + colab={"base_uri": "https://localhost:8080/"} id="uISrtf8bBqLR" executionInfo={"status": "ok", "timestamp": 1631421910817, "user_tz": -540, "elapsed": 391, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="20005df6-991f-4c1e-c3f2-72517d565e62"
model_RNN.compile(optimizer='adam',
             loss = 'binary_crossentropy',
             metrics = ['acc'])
model_RNN.summary()

# + id="2vHQHYsxCp9I"
# 검증 데이터 손실(val_loss)이 증가하면, 
# 과적합 징후므로 검증 데이터 손실이 4회 증가하면 
# 학습을 조기 종료(Early Stopping)합니다. 
es = EarlyStopping(monitor='val_loss', 
                   mode='min', verbose=1, patience=4)
# ModelCheckpoint를 사용하여 검증 데이터의 
# 정확도(val_acc)가 이전보다 좋아질 경우에만 모델을 저장합니다.
mc = ModelCheckpoint('best_model_RNN.h5', 
                     monitor='val_acc', mode='max', 
                     verbose=2, save_best_only=True)

# + colab={"base_uri": "https://localhost:8080/"} id="4G_CirZUCuAO" executionInfo={"status": "ok", "timestamp": 1631422528771, "user_tz": -540, "elapsed": 610925, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="1038c613-e867-4565-d036-78c69ef2125a"
history = model_RNN.fit(X_train, y_train, 
                    epochs=10, 
                    callbacks=[es, mc], 
                    batch_size=60, 
                    validation_split=0.2)

# + id="hVxOu6juCxOE"
from tensorflow.keras.models import load_model
loaded_model_RNN = load_model('best_model_RNN.h5')
def sentiment_predict_RNN(new_sentence):
  new_sentence = okt.morphs(new_sentence) # 토큰화
  new_sentence = [word for word in new_sentence if not word in stopword] # 불용어 제거
  encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
  pad_new = sequence.pad_sequences(encoded, maxlen = max_len) # 패딩
  score = float(loaded_model_RNN.predict(pad_new)) # 예측
  if(score > 0.5):
    print("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(score * 100))
  else:
    print("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 - score) * 100))


# + colab={"base_uri": "https://localhost:8080/"} id="bWfjDjhOC1p7" executionInfo={"status": "ok", "timestamp": 1631422573360, "user_tz": -540, "elapsed": 265, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="d098a541-69c3-482e-adfe-850bbc2259ac"
sentiment_predict_RNN('이게 영화냐 발로 만들어도 더 재미있겠다')

# + colab={"base_uri": "https://localhost:8080/"} id="-CJPnGfVC2qJ" executionInfo={"status": "ok", "timestamp": 1631422575560, "user_tz": -540, "elapsed": 374, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="0d379d21-3b1f-4f2b-9bfc-19ed1f3cf31b"
sentiment_predict_RNN('보다가 집에 가고 싶었다')

# + colab={"base_uri": "https://localhost:8080/"} id="6C4f6HH1C4Fl" executionInfo={"status": "ok", "timestamp": 1631422576760, "user_tz": -540, "elapsed": 253, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="813f04b9-98d2-4ec1-c0e9-596c9e8face9"
sentiment_predict_RNN('진짜로 보고 싶냐')

# + colab={"base_uri": "https://localhost:8080/"} id="a3W5-8D9C5Hv" executionInfo={"status": "ok", "timestamp": 1631422578182, "user_tz": -540, "elapsed": 389, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="111219d0-6dce-4343-a973-c09bd6a6f3ed"
sentiment_predict_RNN('헐... 진짜 보고싶냐?')

# + colab={"base_uri": "https://localhost:8080/"} id="Jmc1_KnTC6Z6" executionInfo={"status": "ok", "timestamp": 1631422579546, "user_tz": -540, "elapsed": 366, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="f622743c-8da0-46d5-cd5a-07dc796a9031"
sentiment_predict_RNN('끝까지 본 나를 칭찬한다')

# + colab={"base_uri": "https://localhost:8080/"} id="ozdmzuCzG46k" executionInfo={"status": "ok", "timestamp": 1631422610917, "user_tz": -540, "elapsed": 237, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="4f935905-6786-4c3b-8db8-a0fc97238f0b"
sentiment_predict_RNN('보다 꿈을 꿨어요')

# + colab={"base_uri": "https://localhost:8080/"} id="iTNH4j8oXWFR" executionInfo={"status": "ok", "timestamp": 1631422621880, "user_tz": -540, "elapsed": 370, "user": {"displayName": "\uc591\ub355\ud45c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "16565402416710841856"}} outputId="35309317-b82b-4707-eb9f-c4394208d722"
sentiment_predict_RNN('나만 볼 수 없다')

# + id="TbM-NQriXaXU"

