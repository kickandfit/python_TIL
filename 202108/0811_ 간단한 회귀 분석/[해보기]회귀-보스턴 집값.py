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

# + colab={"base_uri": "https://localhost:8080/"} id="sd8-_OcW3Amy" executionInfo={"status": "ok", "timestamp": 1628662797022, "user_tz": -540, "elapsed": 23629, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="5cdbfaaa-b1b1-42e4-fe71-3e2d7dd04149"
# 한글폰트 설치
# !apt-get update -qq
# !apt-get install fonts-nanum* -qq

# + colab={"base_uri": "https://localhost:8080/", "height": 241} id="90bHZB_f3bUV" executionInfo={"status": "ok", "timestamp": 1628663036891, "user_tz": -540, "elapsed": 651, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="f7f63d5a-daab-4e7e-ac93-7ad0eaf67497"
# 데이터 준비

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn.datasets import load_boston

boston = load_boston()

# boston 데이터셋 DataFrame 변환
bostonDF = pd.DataFrame(boston.data , columns = boston.feature_names)

# boston dataset의 target array는 주택 가격임. 이를 PRICE 컬럼으로 DataFrame에 추가
bostonDF['PRICE'] = boston.target
print('Bosteon 데이터셋 크기:', bostonDF.shape)
bostonDF.head()

# + colab={"base_uri": "https://localhost:8080/"} id="hb6iI56_4W84" executionInfo={"status": "ok", "timestamp": 1628663363266, "user_tz": -540, "elapsed": 271, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="d1700b71-61da-49fb-97b3-49aecb6d3927"
#데이터 탐색
bostonDF.info()

# + colab={"base_uri": "https://localhost:8080/", "height": 315} id="_5okNTN85rQy" executionInfo={"status": "ok", "timestamp": 1628663441580, "user_tz": -540, "elapsed": 284, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="140ecfd7-dfe0-45e3-8c79-4b5ec3492676"
# 데이터 통계 요약정보 확인
bostonDF.describe()

# + colab={"base_uri": "https://localhost:8080/", "height": 203} id="0Cc7Un0P5-Xv" executionInfo={"status": "ok", "timestamp": 1628663945707, "user_tz": -540, "elapsed": 282, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="5d4476a9-2dd5-49f2-84cb-0b029e6bf6ed"
# 속성(feature 또는 variable) 선택

bsotonDF = bostonDF[['RM', 'ZN','INDUS','NOX','AGE','PTRATIO','LSTAT','RAD','PRICE']]
bsotonDF.head()

# + colab={"base_uri": "https://localhost:8080/", "height": 334} id="99uFqcpg71Cj" executionInfo={"status": "ok", "timestamp": 1628664020978, "user_tz": -540, "elapsed": 309, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="9f44e7c3-6073-4b3b-b2ef-7e6d324e4521"
bostonDF.plot(kind = 'scatter', x='LSTAT', y= 'PRICE',
              c = 'coral', s=10, figsize=(10,5))
plt.show()


# + colab={"base_uri": "https://localhost:8080/", "height": 334} id="VSkwzQVp8I3g" executionInfo={"status": "ok", "timestamp": 1628664158104, "user_tz": -540, "elapsed": 974, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="686bc21e-050d-4d69-8b46-0ba9026d6584"
# seaborn으로 산점도 그리기
fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
sns.regplot(x = 'LSTAT', y='PRICE', data=bostonDF, ax=ax1) #회귀선 표시
sns.regplot(x = 'LSTAT', y='PRICE', data=bostonDF, ax=ax2,
            fit_reg=False) #회귀선 미표시
plt.show()

# + colab={"base_uri": "https://localhost:8080/", "height": 865} id="Qstzwhps8kGP" executionInfo={"status": "ok", "timestamp": 1628664363848, "user_tz": -540, "elapsed": 2395, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="b16dedde-dd30-4264-8783-4c9fa3d398f1"
# seaborn 조인트 그래프 - 산점도, 히스토그램
sns.jointplot(x = 'LSTAT', y='PRICE', data=bostonDF)
sns.jointplot(x = 'LSTAT', y='PRICE',  kind='reg', data=bostonDF)
plt.show()

# + colab={"base_uri": "https://localhost:8080/", "height": 1000} id="mvN1eqs09fBF" executionInfo={"status": "ok", "timestamp": 1628664567488, "user_tz": -540, "elapsed": 87922, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="ea46a96a-9445-46b9-a3cb-9d64b329ff24"
# seaborn pariplot으로 두 변수간 모든 경우의 수 그리기
sns.pairplot(bostonDF)
plt.show()

# + id="T-TQ-BGM97wV" executionInfo={"status": "ok", "timestamp": 1628665243842, "user_tz": -540, "elapsed": 301, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
x = bostonDF[['LSTAT']]
y = bostonDF['PRICE']

# + colab={"base_uri": "https://localhost:8080/"} id="r5kaMKwxA2UI" executionInfo={"status": "ok", "timestamp": 1628665393116, "user_tz": -540, "elapsed": 267, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="c5708b85-e356-4a03-ca7f-e000446f9cb6"
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size = 0.2,
                                                    random_state = 10)
print('train data개수: ', x_train.shape)
print('test data개수: ', x_test.shape)

# + colab={"base_uri": "https://localhost:8080/"} id="16PXdYCHBUUN" executionInfo={"status": "ok", "timestamp": 1628665452935, "user_tz": -540, "elapsed": 258, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="f356691a-1649-4043-e88e-90dea655c84b"
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train, y_train)

# + colab={"base_uri": "https://localhost:8080/"} id="qSVgacVtBpbJ" executionInfo={"status": "ok", "timestamp": 1628665493194, "user_tz": -540, "elapsed": 285, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="8baffc8f-b6a6-43a3-9355-3a745eef2c62"
r_square = lr.score(x_test,y_test)
r_square

# + colab={"base_uri": "https://localhost:8080/"} id="GAzOGKcEBzPb" executionInfo={"status": "ok", "timestamp": 1628665556000, "user_tz": -540, "elapsed": 487, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="171bee23-2114-437d-f47c-eaae1a568c77"
y_hat = lr.predict(x_test)
y_hat

# + colab={"base_uri": "https://localhost:8080/", "height": 334} id="j_93i-nACCTg" executionInfo={"status": "ok", "timestamp": 1628665620044, "user_tz": -540, "elapsed": 348, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="e7e0be93-549e-41d1-9242-18a113e9a976"
df_y = pd.DataFrame({'y_hat': y_hat, 'y':y_test})
plt.figure(figsize=(10,5))
ax1 = sns.kdeplot(y_test, label='y_test')
ax2 = sns.kdeplot(y_hat, label='y_hat', ax=ax1)
plt.legend()
plt.show()

# + colab={"base_uri": "https://localhost:8080/"} id="1RFLD4TFCSM5" executionInfo={"status": "ok", "timestamp": 1628665734187, "user_tz": -540, "elapsed": 276, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="bbb8a752-89a9-475e-9493-7f8fbc19ed65"
# 속성(변수) 선택
X = bostonDF[['LSTAT']] # 독립 변수 X
y = bostonDF['PRICE'] # 종속 변수 y
# train data와 test data로 구분( 7:3)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, #독립변수
                                                    y, # 종속변수
                                                    test_size=0.2, #검증 30%
                                                    random_state=10) #랜덤 추출 값
print('train data 개수:', X_train.shape)
print('test data 개수:', X_test.shape)

# + colab={"base_uri": "https://localhost:8080/"} id="fggdiq0bCuDi" executionInfo={"status": "ok", "timestamp": 1628665752350, "user_tz": -540, "elapsed": 363, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="adaaf8b8-00b6-439b-88c0-db36fe0b089e"
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 다항식 변환
poly = PolynomialFeatures(degree = 2)
X_train_poly = poly.fit_transform(X_train)
print('원 데이터:' , X_train.shape)
print('2차형 변환 데이터', X_train_poly.shape)

# + colab={"base_uri": "https://localhost:8080/"} id="bSYGbiagCyg8" executionInfo={"status": "ok", "timestamp": 1628665789916, "user_tz": -540, "elapsed": 287, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="ad6c1dbf-7602-4402-a59e-b91826e3caa6"
# train data를 가지고 모형 학습
pr = LinearRegression()
pr.fit(X_train_poly, y_train)

# + colab={"base_uri": "https://localhost:8080/"} id="EhHfjIfrC7sv" executionInfo={"status": "ok", "timestamp": 1628665816024, "user_tz": -540, "elapsed": 280, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="a1c5174a-32c2-4d3b-89e3-6fff6044a080"
X_test_poly = poly.fit_transform(X_test)

# 학습을 마친 모형에 test data를 적용하여 결정계수 계산
r_square = pr.score(X_test_poly, y_test)
r_square

# + colab={"base_uri": "https://localhost:8080/", "height": 334} id="KwF_fHAnDCDq" executionInfo={"status": "ok", "timestamp": 1628665890210, "user_tz": -540, "elapsed": 368, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="438ddfa7-7849-43ce-a8e0-9dc7d8a7ea0e"
# train data의 산점도와 test data로 예측한 회귀선 그래프 출력
x_hat = pr.predict(X_test_poly)
df_y_test = pd.DataFrame({'y_hat': y_hat, 'y': y_test})
df_y_test['차이'] = df_y_test['y_hat']-df_y['y']
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
ax.plot(X_train, y_train, 'o', label = 'Train Data')
ax.plot(X_test, y_hat, 'r+', label ='Predicted Value')
ax.legend(loc = 'best')
plt.xlabel('LSTAT')
plt.ylabel('PRICE')
plt.show()
plt.close()

# + colab={"base_uri": "https://localhost:8080/", "height": 336} id="JtqqWZQbDGiX" executionInfo={"status": "ok", "timestamp": 1628665941974, "user_tz": -540, "elapsed": 335, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="e98590ea-d409-41c8-ff0d-57f40308bdc7"
# 모형에 전체 X 데이터를 입력하여 예측한 값 y_hat과 실제 값 y와 비교
X_ploy = poly.fit_transform(X)
y_hat = pr.predict(X_ploy)

plt.figure(figsize=(10,5))
ax1 = sns.kdeplot(y_test, label='y')
ax2 = sns.kdeplot(y_hat, label='y_hat', ax=ax1)
plt.legend()
plt.show()

# + colab={"base_uri": "https://localhost:8080/"} id="q6ySQ7U9Dgzo" executionInfo={"status": "ok", "timestamp": 1628666078071, "user_tz": -540, "elapsed": 269, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="724d6585-961e-4d1c-e146-dbea1b07e3ca"
# 다중회귀분석

# 속성(변수) 선택
X = bostonDF[['RM','ZN','INDUS','NOX','AGE','PTRATIO','LSTAT','RAD']
] # 독립 변수 X
y = bostonDF['PRICE'] # 종속 변수 y
# train data와 test data로 구분( 7:3)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, #독립변수
                                                    y, # 종속변수
                                                    test_size=0.3, #검증 30%
                                                    random_state=10) #랜덤 추출 값
print('train data 개수:', X_train.shape)
print('test data 개수:', X_test.shape)

# + colab={"base_uri": "https://localhost:8080/"} id="LerEL2WoD-Eg" executionInfo={"status": "ok", "timestamp": 1628666109786, "user_tz": -540, "elapsed": 262, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="70bf52da-764b-417d-8bff-3a4cac907b05"
# sklearn 라이브러리
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 단순회귀분석 모형 객체 생성
lr = LinearRegression()

lr.fit(X_train, y_train)

# 학습을 마친 모형에 test data를 적용하여 결정
r_square = lr.score(X_test, y_test)
r_square

# + colab={"base_uri": "https://localhost:8080/", "height": 334} id="O-4SXb-REJzY" executionInfo={"status": "ok", "timestamp": 1628666155127, "user_tz": -540, "elapsed": 336, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="2eea432a-adc1-49bd-b152-e14bd633ce8a"
y_hat = lr.predict(X_test)
df_y = pd.DataFrame({'y_hat':y_hat, 'y':y_test})
y_hat = lr.predict(X_test)

plt.figure(figsize=(10,5))
ax1 = sns.kdeplot(y_test, label='y_test')
ax2 = sns.kdeplot(y_hat, label='y_hat', ax=ax1)
plt.legend()
plt.show()

# + id="SqAkeCuSEUyD"

