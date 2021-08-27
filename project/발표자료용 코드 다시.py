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

# +
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import Binarizer
from sklearn.metrics import accuracy_score, precision_score,classification_report, recall_score, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from imblearn.ensemble import BalancedBaggingClassifier
from sklearn.model_selection import train_test_split, cross_val_score

df = pd.read_csv('./TravelInsurancePrediction.csv')
df['FrequentFlyer'] = df['FrequentFlyer'].map({'Yes': 1, 'No': 0})
df['EverTravelledAbroad'] = df['EverTravelledAbroad'].map({'Yes': 1, 'No': 0})
df["Employment Type"] = df["Employment Type"].map({"Government Sector" : 1, "Private Sector/Self Employed" : 0})
df['GraduateOrNot'] = df['GraduateOrNot'].map({'Yes': 1, 'No': 0})

# df = df.drop(["GraduateOrNot"] , axis=1)
df_index = ['Age', 'AnnualIncome', 'ChronicDiseases',"GraduateOrNot", 
          'FrequentFlyer', 'FamilyMembers', 'Employment Type',
          'EverTravelledAbroad']
df_label_index = ['TravelInsurance']
ndf = df[['Age', 'AnnualIncome', 'ChronicDiseases', 'GraduateOrNot',
          'FrequentFlyer', 'FamilyMembers', 'Employment Type',
          'EverTravelledAbroad', 'TravelInsurance']]
X = ndf[list(ndf.columns)[:-1]]
y = ndf[list(ndf.columns)[-1]]
# y = y.astype({'TravelInsurance': int})
# X = preprocessing.StandardScaler().fit(X).transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                    random_state=10)

# +
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from imblearn.over_sampling import SMOTENC ,SMOTEN
from imblearn.combine import *
from imblearn.under_sampling import *
from imblearn.over_sampling import *
from sklearn.tree import DecisionTreeClassifier
from imblearn.ensemble import *
from sklearn.ensemble import RandomForestClassifier

                #언더샘플링
sample_list = {'enn' : EditedNearestNeighbours(), 
               'rus' : RandomUnderSampler(random_state=0),
              'nm1' : NearMiss(version=1),
               'renn' : RepeatedEditedNearestNeighbours(),
              'allknn' : AllKNN(), 
               'cnn' : CondensedNearestNeighbour(random_state=0),
              'oss' : OneSidedSelection(random_state=0),
               'ncr' : NeighbourhoodCleaningRule(),
              'iht' : InstanceHardnessThreshold(random_state=0,estimator=LogisticRegression(solver='lbfgs', multi_class='auto')),
                #오버샘플링
               'smote_nc' :  SMOTENC(categorical_features=[0, 2], random_state=0),
               'smote' : SMOTEN(random_state=0),
                #언더 오버 조합
               'smote_enn' : SMOTEENN(random_state=0),
               'smote_tomek' : SMOTETomek(random_state=0)
              }

model_list = {'Decisiontree' : tree.DecisionTreeClassifier(criterion='entropy', max_depth=5),
             'BalancedBagging' : BalancedBaggingClassifier(base_estimator=DecisionTreeClassifier(),
                                sampling_strategy='auto',
                                replacement=False,
                                random_state=0),
             'BalancedRandomForest': BalancedRandomForestClassifier(n_estimators=100, random_state=0),
             'EasyEnsemble' : EasyEnsembleClassifier(random_state=0),
             'RandomForest': RandomForestClassifier(random_state=0),
             }

def get_clf_eval(y_test, pred):
    confusion = confusion_matrix(y_test, pred)
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    report = classification_report(y_test, pred)
    print('오차행렬')
    print()
    print(confusion)
    print()
    print('report')
    print()
    print(report)
    print()
    print('정리')
    print()
    print('정확도 : {:.4f}\n정밀도 : {:.4f}\n재현율 : {:.4f}'.format(accuracy, precision, recall))

for under in sample_list:
    X_resampled, y_resampled  = sample_list[under].fit_resample(X_train, y_train)
    for model in model_list:
        model_ = model_list[model]
        model_.fit(X_resampled, y_resampled)
        y_hat = model_.predict(X_test)
        
        print('샘플링 방법 : ',under)
        print()
        print(model,'모델')
        get_clf_eval(y_test, y_hat)

# -






