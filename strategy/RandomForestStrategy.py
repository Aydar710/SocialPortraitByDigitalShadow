from abc import ABC

from strategy.PredictionStrategy import PredictionStrategy


class RandomForestStrategy(PredictionStrategy):

    def predict_classes(self, X):
        print("random forest strategy")