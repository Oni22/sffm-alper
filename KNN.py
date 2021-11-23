from os import error
from matplotlib import colors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from matplotlib import colors

#Daten entnehmen
dataset = pd.read_csv('stoerungsauswertung.csv',delimiter=";")   
#Daten trennen
X = dataset.iloc[:, [0,1]].values  
y = dataset.iloc[:, 3].values

# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)
# #Daten skalieren (alle Daten zw. -1 und 1)
# sc_X = StandardScaler() 
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)
# #Model aufstellen
# classifier = KNeighborsClassifier(n_neighbors=6, metric="euclidean") 
# classifier.fit(X_train,y_train)
# #testergebnisse predicten
# y_pred = classifier.predict(X_test) 

#neu Daten predicten
classifier2 = KNeighborsClassifier(n_neighbors=6) 
classifier2.fit(X,y)
prediction = classifier2.predict([[33,208]])
print(prediction)

# ##MODELL BEWERTEN
# cm = confusion_matrix(y_test, y_pred)
# print("Confusion Matrix:")
# print(cm)
# print("f1-score:", f1_score(y_test, y_pred, average='weighted') )
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print(classification_report(y_test,y_pred))
# #OPTIMALES K DURCH MEAN ERROR BESTIMMEN
# error = []
# for i in range(1, 20):
#     knn = KNeighborsClassifier(n_neighbors=i)
#     knn.fit(X_train, y_train)
#     pred_i = knn.predict(X_test)
#     error.append(np.mean(pred_i != y_test))
# plt.figure(figsize=(12, 6))
# plt.plot(range(1, 20), error, color='red', linestyle='dashed', marker='o',
#          markerfacecolor='blue', markersize=10)
# plt.title('Fehlerrate für n-Wert')
# plt.xlabel('n')
# plt.ylabel('Fehlerrate')
# plt.show()

# #TESTERGEBNISSE AUSGEBEN
# from matplotlib.colors import ListedColormap  
# x_set, y_set = X_test, y_test 
# x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step  =0.01),  
# np.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))  
# plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),  
# alpha = 0.75, cmap = ListedColormap(('red', 'pink','blue','yellow','grey','green','black','orange')))  
# plt.xlim(x1.min(), x1.max())  
# plt.ylim(x2.min(), x2.max())  
# for i, j in enumerate(np.unique(y_set)):  
#     plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],  
#         color = ListedColormap(('red', 'pink', 'blue','yellow','grey','green','black','orange'))(i), label = j)  
# plt.title('KNN mit Testsatz')  
# plt.xlabel('Fehlergrund')  
# plt.ylabel('Arbeitsgang')  
# plt.legend()  
# plt.show()  