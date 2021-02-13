from collections import Counter

import pandas
from numpy import std, mean
from sklearn.datasets import make_classification
# define dataset
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score

from strategy.PredictionStrategy import PredictionStrategy


class MultinomialLogisticRegressionStrategy(PredictionStrategy):

    def predict_classes(self, x) -> map:
        # define the multinomial logistic regression model
        model = LogisticRegression(multi_class='multinomial', solver='lbfgs', penalty='l2', C=1.0, max_iter=100000)

        # define the model evaluation procedure
        # cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

        # evaluate the model and collect the scores
        # n_scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)

        # report the model performance
        # print('Mean Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))

        predictions = []
        for y in [self.y_o, self.y_c, self.y_e, self.y_a, self.y_n]:
            # fit the model on the whole dataset
            model.fit(self.X, y)

            # predict the class label
            predicted_class = model.predict([x])
            predictions.append(predicted_class)

        return {'O': predictions[0][0], 'C': predictions[1][0], 'E': predictions[2][0], 'A': predictions[3][0],
                'N': predictions[4][0]}
