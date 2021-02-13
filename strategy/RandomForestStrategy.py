import pandas
from sklearn.ensemble import RandomForestClassifier

from strategy.PredictionStrategy import PredictionStrategy


class RandomForestStrategy(PredictionStrategy):

    def make_classifier(self, X: list, y, should_print_feature_importance=False) -> RandomForestClassifier:
        classifier = RandomForestClassifier()
        classifier.fit(X, y)

        if should_print_feature_importance:
            # feature importance
            print(classifier.feature_importances_)

        return classifier

    def predict_classes(self, x) -> map:
        predictions = []
        for y in [self.y_o, self.y_c, self.y_e, self.y_a, self.y_n]:
            classifier = self.make_classifier(self.X, y)
            classifier.fit(self.X, y)
            prediction = classifier.predict([x])
            predictions.append(prediction)

        return {'O': predictions[0][0], 'C': predictions[1][0], 'E': predictions[2][0], 'A': predictions[3][0],
                'N': predictions[4][0]}

    # TODO: create method to get metrics
