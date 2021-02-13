from collections import Counter

import pandas
from numpy import std, mean
from sklearn.datasets import make_classification
# define dataset
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score

# load dataset
answers_frame = pandas.read_csv('../answerprocessing/answers.csv', delimiter=',')

dataset = answers_frame.values
X = dataset[:, 8:].astype(float)
y_o = dataset[:, 3].astype(float)
y_c = dataset[:, 4].astype(float)
y_e = dataset[:, 5].astype(float)
y_a = dataset[:, 6]
y_n = dataset[:, 7]

# define the multinomial logistic regression model
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', penalty='l2', C=1.0, max_iter=100000)

# define the model evaluation procedure
#cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

# evaluate the model and collect the scores
#n_scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)

# report the model performance
#print('Mean Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))

# fit the model on the whole dataset
model.fit(X, y_o)

# define a single row of input data
row = [1,401,220,43,3]

# predict the class label
yhat = model.predict([row])

# summarize the predicted class
print('Predicted Class: %d' % yhat[0])

# predict a multinomial probability distribution
yhat = model.predict_proba([row])
# summarize the predicted probabilities
print('Predicted Probabilities: %s' % yhat[0])