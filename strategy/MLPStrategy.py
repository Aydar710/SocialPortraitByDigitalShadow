import pandas
from sklearn.neural_network import MLPClassifier

from strategy.PredictionStrategy import PredictionStrategy


class MLPStrategy(PredictionStrategy):

    def predict_classes(self, x) -> map:
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15, 20, 10, 20), random_state=1, max_iter=100000)

        predictions = []
        for y in [self.y_o, self.y_c, self.y_e, self.y_a, self.y_n]:
            clf.fit(self.X, y)
            prediction = clf.predict([x])
            predictions.append(prediction)

        return {'O': predictions[0], 'C': predictions[1], 'E': predictions[2], 'A': predictions[3], 'N': predictions[4]}
