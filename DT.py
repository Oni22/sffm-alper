import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn import tree

#Daten entnehmen
database = pd.read_csv('stoerungsauswertung.csv',delimiter=';')

#Daten zuweisen
features = ['Fehlergrund', 'Arbeitsgang','Produkt']
x = database[features]
y = database['Maßnahme']

#Trainingsdaten und Testdaten trennen
X_train, X_test, y_train, y_test = train_test_split (x,y, test_size=0.20 , random_state= 100)
classifier= DecisionTreeClassifier()
classifier.fit(X_train,y_train)
y_pred_en=classifier.predict(X_test)

#Modell aufstellen
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

#Testergebnisse predicten
pred = clf.predict([[33,210,3]])
print (pred)


print("Accuracy:", accuracy_score(y_test, y_pred_en))
print("CR:", classification_report(y_test,y_pred_en))
# SIEHE DT.PNG !!!
# import matplotlib.pyplot as plt
# fig = plt.figure(figsize=(7,4))
# _ = tree.plot_tree(clf, feature_names=features, filled=True)
# plt.show()
# fig.savefig("DT.png")
