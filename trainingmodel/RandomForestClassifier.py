import pandas
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

answers_frame = pandas.read_csv('../answerprocessing/answers.csv', delimiter=',')

dataset = answers_frame.values
X = dataset[:, 8:].astype(float)
y_o = dataset[:, 3].astype(float)
y_c = dataset[:, 4].astype(float)
y_e = dataset[:, 5]
y_a = dataset[:, 6]
y_n = dataset[:, 7]

clf = RandomForestClassifier()
clf.fit(X, y_o)

# feature importnace
print(clf.feature_importances_)

print(clf.predict([X[0]]))
print(clf.predict_proba([X[0]]))

# metrics
predictions = clf.predict(X)
accuracy = accuracy_score(y_o, predictions)
print('accuracy: ', accuracy)

classification_report = classification_report(y_o, predictions)
print(classification_report)