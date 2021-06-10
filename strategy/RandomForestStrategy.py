from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

from strategy.PredictionStrategy import PredictionStrategy


class RandomForestStrategy(PredictionStrategy):

    def make_classifier(self, X: list, y, should_print_feature_importance=False) -> RandomForestClassifier:
        classifier = RandomForestClassifier()
        classifier.fit(X, y)

        if should_print_feature_importance:
            # feature importance
            print("feature importance")
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

    def get_strategy_name(self):
        return "Random Forest"

    def print_metrics_for(self, y):
        classifier = self.make_classifier(self.X, y)
        predictions = classifier.predict(self.X)
        report = classification_report(y, predictions)
        print(report)

    def print_metrics(self):
        print("Metrics O")
        self.print_metrics_for(self.y_o)
        print("Metrics C")
        self.print_metrics_for(self.y_c)
        print("Metrics E")
        self.print_metrics_for(self.y_e)
        print("Metrics A")
        self.print_metrics_for(self.y_a)
        print("Metrics N")
        self.print_metrics_for(self.y_n)
