import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names=['sepal-length','sepal-width','petal-length','petal-width','class']
dataset=pandas.read_csv(url,names=names)
print(dataset.shape)#150 rows and 5 columns
print(dataset.head(30))#first 30 rows
print(dataset.describe())#values lies between 0 to 8 cm
print(dataset.groupby('class').size())
dataset.plot(kind='box',subplots=True,layout=(2,2),sharex=False ,sharey=False)
plt.show()
print()
dataset.hist()
plt.show()
print()
scatter_matrix(dataset)
plt.show()
print()
#80% data for trained our model and 20% holding for validation dataset
array=dataset.values
X=array[:,0:4]
Y=array[:,4]
validation_size=0.20
seed=6
X_train,X_test,Y_train,Y_test=model_selection.train_test_split(X,Y,test_size=validation_size,random_state=seed)
seed=6
scoring='accuracy'