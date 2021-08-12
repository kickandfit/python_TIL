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

# + colab={"base_uri": "https://localhost:8080/"} id="01PbXrDU_M_2" executionInfo={"status": "ok", "timestamp": 1628749225219, "user_tz": -540, "elapsed": 609, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="42b4b304-c81b-42cb-8ea4-baebfeccd907"
from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import svm


uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'

df = pd.read_csv(uci_path, header = None)

# 열 이름 지정

df.columns = ['id','clump', 'cell_size',
              'cell_shape', 'adhesion', 'epithlial',
              'bare_nuclei', 'chromatin',
              'normal_nucleoli', 'mitoses', 'class']
df['bare_nuclei'].replace('?', np.nan, inplace = True) # ? 를 nan 으로 변경
df.dropna(subset = ['bare_nuclei'], axis = 0, inplace = True) # 누락데이터 행 삭제
df['bare_nuclei'] = df['bare_nuclei'].astype('int') # 문자열을 상수열로 변경

# 속성(변수) 선택
X = df[['clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
        'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses']]
y = df['class']

X = preprocessing.StandardScaler().fit(X).transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 10)

from sklearn.neighbors import KNeighborsClassifier

# 모형 객체 생성 ( k = 5 설정 )
knn = KNeighborsClassifier(n_neighbors = 5)

# train data를 가지고 모형 학습

knn.fit(X_train, y_train)
y_hat = knn.predict(X_test)
df = pd.DataFrame({'y_hat' : y_hat , 'y' : y_test})
df['차이'] = df['y_hat'] == df['y']
print('오답 수: ', len(df)- sum(df['차이'])) # True 는 1 이니까
knn_matrix = metrics.confusion_matrix(y_test, y_hat)
print(knn_matrix)

knn_report = metrics.classification_report(y_test, y_hat)
print(knn_report)


# + colab={"base_uri": "https://localhost:8080/"} id="t0HTfMz8AK0v" executionInfo={"status": "ok", "timestamp": 1628749235016, "user_tz": -540, "elapsed": 571, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="103d42a0-10e4-430b-b429-3c7a2df12f39"


uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'

df = pd.read_csv(uci_path, header = None)

# 열 이름 지정

df.columns = ['id','clump', 'cell_size',
              'cell_shape', 'adhesion', 'epithlial',
              'bare_nuclei', 'chromatin',
              'normal_nucleoli', 'mitoses', 'class']
df['bare_nuclei'].replace('?', np.nan, inplace = True) # ? 를 nan 으로 변경
df.dropna(subset = ['bare_nuclei'], axis = 0, inplace = True) # 누락데이터 행 삭제
df['bare_nuclei'] = df['bare_nuclei'].astype('int') # 문자열을 상수열로 변경

# 속성(변수) 선택
X = df[['clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
        'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses']]
y = df['class']

X = preprocessing.StandardScaler().fit(X).transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 10)
svm_model = svm.SVC()

svm_model.fit(X_train, y_train)

y_hat = svm_model.predict(X_test)
df = pd.DataFrame({'y_hat' : y_hat , 'y' : y_test})
df['차이'] = df['y_hat'] == df['y']
print('오답 수: ', len(df)- sum(df['차이'])) # True 는 1 이니까
from sklearn import metrics
svm_matrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_matrix)
svm_report = metrics.classification_report(y_test, y_hat)
print(svm_report)

# + colab={"base_uri": "https://localhost:8080/"} id="hlzVMJ7bBChT" executionInfo={"status": "ok", "timestamp": 1628749393149, "user_tz": -540, "elapsed": 536, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="c575d6ab-fcc1-4725-bb4d-bf7f874a3619"
df = sns.load_dataset('titanic')
rdf = df.drop(['deck', 'embark_town'], axis = 1)

rdf = rdf.dropna(subset = ['age'], how = 'any' , axis = 0)

most_freq = rdf['embarked'].value_counts(dropna = True).idxmax ()
rdf['embarked'].fillna(most_freq, inplace = True)
ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis = 1)
onehot_embarked = pd.get_dummies(ndf['embarked'], prefix = 'town')
ndf = pd.concat([ndf, onehot_embarked], axis = 1)
ndf.drop(['sex','embarked'], axis = 1, inplace = True)
X=ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male',
       'town_C','town_Q','town_S']]
y = ndf['survived']
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = 0.3, random_state = 10)
print('train data 개수: ', X_train.shape)
print('test data 개수: ', X_test.shape)
tree_model = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth = 5)
tree_model.fit(X_train, y_train)
y_hat = tree_model.predict(X_test)
df = pd.DataFrame({'y_hat':y_hat, 'y':y_test})
df['차이'] = df['y_hat'] == df['y']
print('오답 수: ', len(df) - sum(df['차이']))
tree_matrix = metrics.confusion_matrix(y_test, y_hat)
print(tree_matrix)
tree_report = metrics.classification_report(y_test, y_hat)
print(tree_report)

# + id="-7rOZGhfB2mQ"

