import pandas
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

answers_frame = pandas.read_csv('../answerprocessing/answers.csv', delimiter=',')


def make_classifier(X, y, should_print_feature_importance=False) -> RandomForestClassifier:
    classifier = RandomForestClassifier()
    classifier.fit(X, y)

    if should_print_feature_importance:
        # feature importance
        print(classifier_o.feature_importances_)

    return classifier


dataset = answers_frame.values
X = dataset[:, 8:].astype(float)
y_o = dataset[:, 3].astype(float)
y_c = dataset[:, 4].astype(float)
y_e = dataset[:, 5].astype(float)
y_a = dataset[:, 6].astype(float)
y_n = dataset[:, 7].astype(float)

classifier_o = make_classifier(X, y_o)
classifier_c = make_classifier(X, y_c)
classifier_e = make_classifier(X, y_e)
classifier_a = make_classifier(X, y_a)
classifier_n = make_classifier(X, y_n)

classifier_o.fit(X, y_o)
classifier_c.fit(X, y_o)
classifier_e.fit(X, y_o)
classifier_a.fit(X, y_o)
classifier_n.fit(X, y_o)

prediction_o = classifier_o.predict([X[0]])
print(prediction_o)
# print(classifier_o.predict_proba([X[0]]))

# metrics
predictions = classifier_o.predict(X)
accuracy = accuracy_score(y_o, predictions)
print('accuracy: ', accuracy)

classification_rep = classification_report(y_o, predictions)
print(classification_rep)
