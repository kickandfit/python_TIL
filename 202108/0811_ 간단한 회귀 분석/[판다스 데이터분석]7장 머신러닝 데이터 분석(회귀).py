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

# + id="BEmNGmfZ3uom" executionInfo={"status": "ok", "timestamp": 1628646476745, "user_tz": -540, "elapsed": 6128, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
# 한글폰트 설치
# !apt-get update -qq
# !apt-get install fonts-nanum* -qq

# + id="LA91dXyG33-g" executionInfo={"status": "ok", "timestamp": 1628647270697, "user_tz": -540, "elapsed": 817, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats
import matplotlib.font_manager as fm

fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=9)
fm._rebuild()
# 그래프에 retina display 적용
# %config InlineBackend.figure_format = 'retina'
# Colab 의 한글 폰트 설정
plt.rc('font', family='NanumBarunGothic') 
mpl.rcParams['axes.unicode_minus'] = False


# + colab={"base_uri": "https://localhost:8080/", "height": 532} id="xw-9hvQR5P8-" executionInfo={"status": "ok", "timestamp": 1628647271530, "user_tz": -540, "elapsed": 576, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="b81e6772-668e-4e80-bbcf-3c71cb8d4500"
# [테스트]
# 데이터 준비

data = np.random.randint(-200, 100, 50).cumsum()
# 한글을 넣어놓고 그러보면 깨진다
plt.figure(figsize = (10, 8))
plt.plot(range(50), data, 'r')
plt.title('시간별 가격추이')
plt.ylabel('주식가격')
plt.xlabel('시간(분')

# + colab={"resources": {"http://localhost:8080/nbextensions/google.colab/files.js": {"data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK", "ok": true, "headers": [["content-type", "application/javascript"]], "status": 200, "status_text": ""}}, "base_uri": "https://localhost:8080/", "height": 76} id="m93a-erU6irK" executionInfo={"status": "ok", "timestamp": 1628647810757, "user_tz": -540, "elapsed": 76506, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="91803d2a-1e57-45a5-c1fc-bf6b6f2e3419"
from google.colab import files
uploaded = files.upload()

# + colab={"base_uri": "https://localhost:8080/", "height": 237} id="vw3PYsPc-BW9" executionInfo={"status": "ok", "timestamp": 1628648154834, "user_tz": -540, "elapsed": 233, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="a925fb26-fedd-46a7-80b2-1b1cccc98c8a"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df_auto = pd.read_csv('/content/auto-mpg.csv', header = None)

# 열 이름 지정

df_auto.columns = ['연비(mpg)', '실린더 수', '배기랑', '출력',
                   '차중','가속능력','출시년도','제조국','모델명']
df_auto.head()

# + colab={"base_uri": "https://localhost:8080/"} id="okyOo7HT_YmJ" executionInfo={"status": "ok", "timestamp": 1628648244924, "user_tz": -540, "elapsed": 244, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="5fa9614a-f4ac-40f5-fb70-b1fa2377f87b"
# 데이터 자료형 확인
df_auto.info()

# + colab={"base_uri": "https://localhost:8080/", "height": 315} id="XxmQzWiKAARY" executionInfo={"status": "ok", "timestamp": 1628648365666, "user_tz": -540, "elapsed": 243, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="303c69f3-a231-4b11-b332-7edc7d06b70f"
# 데이터 통계 요약정보 확인
df_auto.describe()

# + colab={"base_uri": "https://localhost:8080/"} id="HH1ufNU1AdwF" executionInfo={"status": "ok", "timestamp": 1628648595157, "user_tz": -540, "elapsed": 246, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="307042e2-cca3-4a66-a1a4-ab8091d0ba39"
# 출력 열의 자료형 변경 (문자열 -> 숫자)
df_auto['출력'].unique()

# + id="-pJ3hA46BVyD" executionInfo={"status": "ok", "timestamp": 1628649005877, "user_tz": -540, "elapsed": 249, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
df_auto['출력'].replace('?', np.nan, inplace=True)
df_auto.dropna(subset = ['출력'], axis = 0, inplace = True)
df_auto['출력'] = df_auto['출력'].astype('float')

# + colab={"base_uri": "https://localhost:8080/"} id="DnDWp1tCC6C8" executionInfo={"status": "ok", "timestamp": 1628649025126, "user_tz": -540, "elapsed": 245, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="b784e6a2-ec1f-4130-f1a8-3d40b0337081"
df_auto['출력'].isnull().sum()

# + colab={"base_uri": "https://localhost:8080/", "height": 203} id="bV99rtPYC-wF" executionInfo={"status": "ok", "timestamp": 1628649242266, "user_tz": -540, "elapsed": 272, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="f08144a3-a6bb-4c32-d887-bce57b295f9a"
#분석에 활용할 열(속성)을 선택
ndf = df_auto[['연비(mpg)', '실린더 수', '출력', '차중']]
ndf.head()

# + colab={"base_uri": "https://localhost:8080/", "height": 336} id="Q3hhAxkWDzwR" executionInfo={"status": "ok", "timestamp": 1628649409864, "user_tz": -540, "elapsed": 792, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="6d240971-7088-4fc7-b426-7d01a4b8af17"
## 종속 변수 Y인 "연비(mpg)"와 다른 변수 간의 선형관계를 산점도로 확인
# Matplotlib으로 산점도 그리기
ndf.plot(kind = 'scatter', x= '차중', y= '연비(mpg)',
         c='coral', s=10, figsize=(10,5))
plt.show()

# + colab={"base_uri": "https://localhost:8080/", "height": 336} id="LyuxM6CvEUqk" executionInfo={"status": "ok", "timestamp": 1628649649118, "user_tz": -540, "elapsed": 1158, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="fcc7f0a3-96ea-4d62-a9c6-aa16b28a73f9"
# seaborn으로 산점도 그리기
fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
sns.regplot(x = '차중', y='연비(mpg)', data=ndf, ax=ax1) #회귀선 표시
sns.regplot(x = '차중', y='연비(mpg)', data=ndf, ax=ax2,
            fit_reg=False) #회귀선 미표시
plt.show()

# + colab={"base_uri": "https://localhost:8080/", "height": 869} id="tQKa2zRuFNHg" executionInfo={"status": "ok", "timestamp": 1628649942875, "user_tz": -540, "elapsed": 2624, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="7656f157-91de-4abd-b8f5-d72408be5926"
# seaborn 조인트 그래프 - 산점도, 히스토그램
sns.jointplot(x ='차중', y ='연비(mpg)', data=ndf)
sns.jointplot(x='차중', y='연비(mpg)', kind='reg', data=ndf)
plt.show()

# + colab={"base_uri": "https://localhost:8080/", "height": 748} id="FXr0eYBDGY-d" executionInfo={"status": "ok", "timestamp": 1628654846173, "user_tz": -540, "elapsed": 7537, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="56c0fc55-098a-47b7-b457-2237b41f5e7c"
# seaborn pairplot으로 두 변수 간의 모든 경우의 수 그리기
sns.pairplot(ndf)
plt.show()


# + id="7rgfETlqZKAZ" executionInfo={"status": "ok", "timestamp": 1628657132808, "user_tz": -540, "elapsed": 292, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
# 속성(변수) 선택
X = ndf[['차중']] # 독립 변수 X
y = ndf['연비(mpg)'] # 종속 변수 y

# + colab={"base_uri": "https://localhost:8080/"} id="48JE6ecHZ3dB" executionInfo={"status": "ok", "timestamp": 1628657135989, "user_tz": -540, "elapsed": 276, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="235a70cd-1ac6-44d5-c35d-63e8c7305dea"
# train data와 test data로 구분( 7:3)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, #독립변수
                                                    y, # 종속변수
                                                    test_size=0.3, #검증 30%
                                                    random_state=10) #랜덤 추출 값
print('train data 개수:', len(X_train))
print('test data 개수:', len(X_test))

# + colab={"base_uri": "https://localhost:8080/"} id="r3h4mR7SbUyt" executionInfo={"status": "ok", "timestamp": 1628657136373, "user_tz": -540, "elapsed": 13, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="1d4a8299-48b4-43d1-f00e-1e7fcd7796af"
# sklearn 라이브러리에서 선형회귀분석 모듈 가져오기

from sklearn.linear_model import LinearRegression

# 단순회귀 분석 모형 객체 생성

lr = LinearRegression()

# train data 를 가지고 모형 학습

lr.fit(X_train, y_train)

# + colab={"base_uri": "https://localhost:8080/"} id="-NgbOeO_eIf-" executionInfo={"status": "ok", "timestamp": 1628657136374, "user_tz": -540, "elapsed": 9, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="72babc84-52ff-4136-d780-8e788c30289a"
# 학습을 마친 모형에 test data를 적용하여 결정계수( R-제곱 ) 계산
# R제곱은 바로 다른 말로 설명력 혹은 결정계수 라함
# 독립변수가 종속변수에 대해 얼만큼만의 설명력을 가지게 디는지 나타내는 수지
# 결정 계수 = 1: 히귀직선 y를 완전히 설명가능, 회귀식 정확도 매우높음
# 결정 계수 = 0 : 추정된 회귀직선은 x와 y의 관계 설명 불가

r_square = lr.score(X_test, y_test)
r_square

# + colab={"base_uri": "https://localhost:8080/"} id="HwCSDutvgoYq" executionInfo={"status": "ok", "timestamp": 1628657136947, "user_tz": -540, "elapsed": 11, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="3ee681e8-163b-4819-c28b-86d1449645e6"
# 회귀식의 기울기( w )
print('기울기 a:' , lr.coef_) # 기울기를 불러주는 함수


# + colab={"base_uri": "https://localhost:8080/"} id="4_hBLNZigzO9" executionInfo={"status": "ok", "timestamp": 1628657136949, "user_tz": -540, "elapsed": 9, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="11c9f29a-5f10-4496-c5a4-c99f3c77135f"
# 회귀식의 y 절편
print('y절편 b:', lr.intercept_)

# + colab={"base_uri": "https://localhost:8080/"} id="yY8xbwdXg7En" executionInfo={"status": "ok", "timestamp": 1628657137195, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="27076f9a-d7c2-4ce9-e92b-41b604c45809"
# 모형에 전체 X 데이터를 입력하여 예측한 값 y_hat을 실제 y값과 비교
y_hat = lr.predict(X_test)
y_hat

# + colab={"base_uri": "https://localhost:8080/", "height": 417} id="3MjrYs5NhLIR" executionInfo={"status": "ok", "timestamp": 1628658561112, "user_tz": -540, "elapsed": 243, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="e592ad08-3ac4-48f7-a99e-26a1d4fdbbaf"
df_y = pd.DataFrame({'y_hat': y_hat, 'y':y_test})
df_y

# + colab={"base_uri": "https://localhost:8080/", "height": 336} id="4pgbOQPziWkx" executionInfo={"status": "ok", "timestamp": 1628658563038, "user_tz": -540, "elapsed": 908, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="3f3774d2-ff6c-4838-ff4e-cd474817ad58"
# 오차를 구하고 제곱을 해서 평균을 낼 것
# 평균제곱 오차
plt.figure(figsize=(10,5))
ax1 = sns.kdeplot(y_test, label='y_test')
ax2 = sns.kdeplot(y_hat, label='y_hat', ax=ax1)
plt.legend()
plt.show()

# + colab={"base_uri": "https://localhost:8080/"} id="D4uVlpctmIyK" executionInfo={"status": "ok", "timestamp": 1628658563040, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="cc21d729-f69b-4fd2-ea47-2ed64d00055d"
((df_y['y_hat']-df_y['y'])**2).mean()

# + colab={"base_uri": "https://localhost:8080/"} id="QPw1ynhqnO3Y" executionInfo={"status": "ok", "timestamp": 1628658912807, "user_tz": -540, "elapsed": 299, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="f4b3d437-3ea2-44ac-f8ea-0d9f10a5fb80"
# 속성(변수) 선택
X = ndf[['차중']] # 독립 변수 X
y = ndf['연비(mpg)'] # 종속 변수 y
# train data와 test data로 구분( 7:3)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, #독립변수
                                                    y, # 종속변수
                                                    test_size=0.3, #검증 30%
                                                    random_state=10) #랜덤 추출 값
print('train data 개수:', X_train.shape)
print('test data 개수:', X_test.shape)

# + colab={"base_uri": "https://localhost:8080/"} id="Jigd4Tr5osuB" executionInfo={"status": "ok", "timestamp": 1628659166144, "user_tz": -540, "elapsed": 248, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="0c3af0da-2ce0-491c-8a31-5f6731a5b4ab"
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 다항식 변환
poly = PolynomialFeatures(degree = 2)
X_train_poly = poly.fit_transform(X_train)
print('원 데이터:' , X_train.shape)
print('2차형 변환 데이터', X_train_poly.shape)

# + colab={"base_uri": "https://localhost:8080/"} id="z5D5X1W5pnaP" executionInfo={"status": "ok", "timestamp": 1628659456638, "user_tz": -540, "elapsed": 249, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="d663d1b0-05bb-43be-8e65-516c53614fc7"
# train data를 가지고 모형 학습
pr = LinearRegression()
pr.fit(X_train_poly, y_train)

# + colab={"base_uri": "https://localhost:8080/"} id="TIIVREntqxfu" executionInfo={"status": "ok", "timestamp": 1628659534772, "user_tz": -540, "elapsed": 322, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="aba2a4a9-fa08-4d3b-f584-c3cbd6e2b035"
X_test_poly = poly.fit_transform(X_test)

# 학습을 마친 모형에 test data를 적용하여 결정계수 계산
r_square = pr.score(X_test_poly, y_test)
r_square

# + id="QounTlBirEjo" executionInfo={"status": "ok", "timestamp": 1628659571497, "user_tz": -540, "elapsed": 334, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
# train data의 산점도와 test data로 예측한 회귀선 그래프 출력
x_hat = pr.predict(X_test_poly)

# + colab={"base_uri": "https://localhost:8080/", "height": 417} id="HZsKAnoqrNhZ" executionInfo={"status": "ok", "timestamp": 1628659709118, "user_tz": -540, "elapsed": 259, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="85c1faa4-c381-41fe-f373-65fbc563f0bf"
df_y_test = pd.DataFrame({'y_hat': y_hat, 'y': y_test})
df_y_test['차이'] = df_y_test['y_hat']-df_y['y']
df_y_test

# + colab={"base_uri": "https://localhost:8080/", "height": 336} id="lI6Z8svRrdAD" executionInfo={"status": "ok", "timestamp": 1628659892339, "user_tz": -540, "elapsed": 673, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="9642e8ce-3d24-444f-fb07-a11de5681f28"
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
ax.plot(X_train, y_train, 'o', label = 'Train Data')
ax.plot(X_test, y_hat, 'r+', label ='Predicted Value')
ax.legend(loc = 'best')
plt.xlabel('차중')
plt.ylabel('연비(mpg)')
plt.show()
plt.close()

# + colab={"base_uri": "https://localhost:8080/", "height": 336} id="GQ-20sexsbu5" executionInfo={"status": "ok", "timestamp": 1628660285340, "user_tz": -540, "elapsed": 1158, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="13877c03-1c49-4d38-8c14-0fb2088fc403"
# 모형에 전체 X 데이터를 입력하여 예측한 값 y_hat과 실제 값 y와 비교
X_ploy = poly.fit_transform(X)
y_hat = pr.predict(X_ploy)

plt.figure(figsize=(10,5))
ax1 = sns.kdeplot(y_test, label='y')
ax2 = sns.kdeplot(y_hat, label='y_hat', ax=ax1)
plt.legend()
plt.show()

# + colab={"base_uri": "https://localhost:8080/"} id="KZ4Xjr3OtPGK" executionInfo={"status": "ok", "timestamp": 1628660721904, "user_tz": -540, "elapsed": 259, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="9882eb80-db7a-42c9-efe2-c13ebb1d0e88"
# 다중회귀분석

# 속성(변수) 선택
X = ndf[['실린더 수','출력','차중']] # 독립 변수 X
y = ndf['연비(mpg)'] # 종속 변수 y
# train data와 test data로 구분( 7:3)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, #독립변수
                                                    y, # 종속변수
                                                    test_size=0.3, #검증 30%
                                                    random_state=10) #랜덤 추출 값
print('train data 개수:', X_train.shape)
print('test data 개수:', X_test.shape)

# + colab={"base_uri": "https://localhost:8080/"} id="MHzijg5HvmR1" executionInfo={"status": "ok", "timestamp": 1628661865039, "user_tz": -540, "elapsed": 268, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="ee7e1d17-85d8-486d-94f3-3364b6a19970"
# sklearn 라이브러리
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 단순회귀분석 모형 객체 생성
lr = LinearRegression()

lr.fit(X_train, y_train)

# 학습을 마친 모형에 test data를 적용하여 결정
r_square = lr.score(X_test, y_test)
r_square

# + colab={"base_uri": "https://localhost:8080/"} id="9RevOm5mz6XJ" executionInfo={"status": "ok", "timestamp": 1628661914173, "user_tz": -540, "elapsed": 240, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="cc70a81e-e638-4a42-d66d-c5748aca3533"
# 회귀식 기울기
print('X 변수의 계수 a:', lr.coef_)

# + colab={"base_uri": "https://localhost:8080/"} id="-pUjOO0X0JfG" executionInfo={"status": "ok", "timestamp": 1628662211696, "user_tz": -540, "elapsed": 273, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="e3adee3c-885b-4f28-9724-b1de798f6ad7"
y_hat = lr.predict(X_test)
y_hat

# + colab={"base_uri": "https://localhost:8080/", "height": 417} id="WYrzGxwb1SHc" executionInfo={"status": "ok", "timestamp": 1628662256002, "user_tz": -540, "elapsed": 251, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="4d999b0e-4c06-43bb-8958-0a5373622b19"
df_y = pd.DataFrame({'y_hat':y_hat, 'y':y_test})
df_y

# + colab={"base_uri": "https://localhost:8080/", "height": 337} id="58aBsZmc1c75" executionInfo={"status": "ok", "timestamp": 1628662405480, "user_tz": -540, "elapsed": 967, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="7f2bc2c4-6ee7-43c9-e362-dd9c022c37f7"
y_hat = lr.predict(X_test)

plt.figure(figsize=(10,5))
ax1 = sns.kdeplot(y_test, label='y_test')
ax2 = sns.kdeplot(y_hat, label='y_hat', ax=ax1)
plt.legend()
plt.show()

# + id="HDvjO8MV2BP3"

