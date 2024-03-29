from strategy.PredictionStrategy import PredictionStrategy


class Oracle:

    def __init__(self, strategy: PredictionStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> PredictionStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: PredictionStrategy) -> None:
        self._strategy = strategy

    def predict_classes(self, X) -> map:
        return self._strategy.predict_classes(X)

    def get_strategy_name(self):
        return self._strategy.get_strategy_name()
