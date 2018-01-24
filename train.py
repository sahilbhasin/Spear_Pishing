#import DataProcessing
from sklearn.datasets import load_iris
import numpy as np
import nltk
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score

def loadfile():

    i_data = []
    i_target = []
    dataset = open("output_Table")

    for records in dataset:
        rc = records.split(',')
        i_data.append(rc[:-1])
        i_target.append(rc[11].strip('\n'))


    X=np.array(i_data)
    y=np.array(i_target)

    X = StandardScaler().fit_transform(X)


    return(X,y)

def linearsvc():
    #c=0.01
    #x_axis=[]
    #y_axis=[]
    X,y=loadfile()
    #for j in range(5):
    clf = LinearSVC(random_state=0, loss='squared_hinge', C=1)  # CLASSIFIER as LinearSVC and diff values of C
    clf.fit(X, y)
    scoring = ['f1_macro', 'precision_macro', 'recall_macro']
    scores = cross_validate(clf, X, y, cv=10, scoring=scoring, return_train_score=False)
    f_measure = 0
    i = 0
    #for i in range(10):
        #f_measure = f_measure + scores['test_f1_macro'][i]
    f_measure = f_measure / 10
    # print(c,f_measure)
    print(scores['test_f1_macro'],scores['test_precision_macro'],scores['test_recall_macro'])
    #x_axis.append(c)
    #y_axis.append(f_measure)



    #c=c*10
        #print(f_measure)

    #   PLOT THE GRAPH
    #plt.plot(x_axis, y_axis, color='red', label="LinearSVC",linewidth = 3,marker='o', markerfacecolor='yellow')
    #plt.show()

linearsvc()