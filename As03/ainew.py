# #SVM CLASSFICATION

# import numpy as np
# import pandas as pd
# import os
# from pandas import DataFrame,Series
# from sklearn import tree
# import matplotlib
# import matplotlib.pyplot as plt
# from sklearn import svm
# from sklearn.preprocessing import StandardScaler
# import statsmodels.formula.api as smf
# import statsmodels.api as sm
# from mpl_toolkits.mplot3d import Axes3D
# import seaborn as sns
# from sklearn import neighbors
# from sklearn import linear_model
# #Read CSV Files
# trainData = pd.read_csv('train.csv')
# testData = pd.read_csv('test.csv')
# testData2 = pd.read_csv('test.csv')
# trainData.fillna(value=0,inplace=True)
# testData.fillna(value=trainData['Age'].mean(),inplace=True)
# testData.fillna(value=trainData['Fare'].mean(),inplace=True)
# from sklearn.model_selection import cross_val_score, KFold
# train_y=trainData['Survived']
# train_ft=trainData.drop('Survived',axis=1)
# kf = KFold(n_splits=10)
# print(train_ft.head())
# print(train_y.head())
# from sklearn.svm import SVC, LinearSVC
# svc = SVC(C = 30, gamma = 0.01)
# svc.fit(train_ft, train_y) 
# acc_SVM = cross_val_score(svc,train_ft,train_y,cv=kf)
# print(acc_SVM.mean())
# from sklearn.neighbors import NearestCentroid
# NN = NearestCentroid()
# NN.fit(train_ft, train_y)
# acc_NN = cross_val_score(NN,train_ft,train_y,cv=kf)
# print(acc_NN.mean())
# predictions = svc.predict(testData)
# print(predictions)
# submission = pd.DataFrame({ 'PassengerId': testData2['PassengerId'],
#                             'Survived': predictions })
# submission.to_csv("subSVM.csv", index=False)

#KNN CLASSIFICATION
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import warnings
# import seaborn as sns
# import itertools
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import train_test_split
# from sklearn import preprocessing
# from sklearn import metrics
# trainData = pd.read_csv('train.csv')
# testData = pd.read_csv('test.csv')
# testData2 = pd.read_csv('test.csv')
# # trainData.fillna(value=0,inplace=True)
# # testData.fillna(value=trainData['Age'].mean(),inplace=True)
# # testData.fillna(value=trainData['Fare'].mean(),inplace=True)
# trainData['Age'].fillna(trainData['Age'].median(), inplace=True)
# testData['Age'].fillna(testData['Age'].median(), inplace=True)
# trainData['Embarked'].fillna(trainData['Embarked'].mode()[0], inplace=True)
# testData['Fare'].fillna(testData['Fare'].median(), inplace=True)
# drop_columns = ['Pclass', 'PassengerId', 'Parch', 'SibSp']
# trainData = trainData.drop(drop_columns, axis=1)
# testData = testData.drop(drop_columns, axis=1)
# features = ['Age', 'Fare', 'Sex', 'Embarked']
# X = trainData[features]
# X = preprocessing.StandardScaler().fit_transform(X)
# y = trainData['Survived']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
# neigh29 = KNeighborsClassifier(n_neighbors=29).fit(X_train, y_train)
# yhat29 = neigh29.predict(X_test)
# cm29 = metrics.confusion_matrix(y_test, yhat29)
# print('Test set Accuracy of K=29 : ', metrics.accuracy_score(y_test, yhat29))
# print(cm29)
# X_submit = np.array(testData[features])
# y_submit = neigh29.predict(X_submit)
# submit = testData2[['PassengerId']].copy()
# submit['Survived'] = y_submit
# print('Length of an survived value array: ', len(y_submit))
# print(submit.head())
# submit.to_csv('subKnn.csv', index=False)


#LINEAR REGRESSION
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
import itertools
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
trainData = pd.read_csv('train.csv')
testData = pd.read_csv('test.csv')
testData2 = pd.read_csv('test.csv')
trainData['Age'].fillna(trainData['Age'].median(), inplace=True)
testData['Age'].fillna(testData['Age'].median(), inplace=True)
trainData['Embarked'].fillna(trainData['Embarked'].mode()[0], inplace=True)
testData['Fare'].fillna(testData['Fare'].median(), inplace=True)
X=trainData.drop('Survived',axis=1)
y=trainData['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
res = LogisticRegression()
res.fit(X_train,y_train)
red=res.predict(X_test)
submission = pd.DataFrame({ 'PassengerId': testData2['PassengerId'],
                            'Survived': red })
submission.to_csv("subLin.csv", index=False)