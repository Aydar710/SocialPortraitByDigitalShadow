from abc import ABC

from strategy.PredictionStrategy import PredictionStrategy


class MLPStrategy(PredictionStrategy):

    def predict_classes(self, X):
        print("MLP strategy")