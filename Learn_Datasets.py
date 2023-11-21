import sklearn
from sklearn import datasets
#from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.model_selection import cross_val_score

#load iris dataset
iris = datasets.load_iris()
#pisahkan atribut dan label pada iris dataset
x = iris.data
y = iris.target

#membuat model dengan decision tree classifier
clf = tree.DecisionTreeClassifier()

#mengevaluasi performa model dengan cross_val_score
scores = cross_val_score(clf, x, y, cv=5)

#membagi dataset menjadi training dan dataset
#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
#menghitung panjang/jumlah data pada x_test
#len(x_test)