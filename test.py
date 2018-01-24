import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold

from sklearn.svm import LinearSVC
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_validate
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.model_selection import cross_val_predict

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


X, y = loadfile()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.1, random_state=0)
y_test = list(map(int, y_test))



clf1 = LinearSVC(random_state=0, loss='squared_hinge', C=1)  # C=1 since it is the optimum value for LinearSVC
clf1.fit(X_train, y_train)
y_pred = clf1.predict(X_test)
y_pred = list(map(int, y_pred))
rec_linear = recall_score(y_test, y_pred, average='weighted')
f1_linear = f1_score(y_test, y_pred, average='weighted')
accuracy=accuracy_score(y_test,y_pred)

print(rec_linear,f1_linear,accuracy)