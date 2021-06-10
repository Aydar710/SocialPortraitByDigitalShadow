import pandas
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier

from strategy.PredictionStrategy import PredictionStrategy


class MLPStrategy(PredictionStrategy):

    def predict_classes(self, x) -> map:
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15, 20, 10, 20), random_state=1,
                            max_iter=100000)

        predictions = []
        for y in [self.y_o, self.y_c, self.y_e, self.y_a, self.y_n]:
            clf.fit(self.X, y)
            prediction = clf.predict([x])
            predictions.append(prediction)

        return {'O': predictions[0][0], 'C': predictions[1][0], 'E': predictions[2][0], 'A': predictions[3][0],
                'N': predictions[4][0]}

    def get_strategy_name(self):
        return 'MLP'

    def print_metrics_for(self, y):
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15, 20, 10, 20), random_state=1,
                            max_iter=100000)
        clf.fit(self.X, y)
        predictions = clf.predict(self.X)
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
