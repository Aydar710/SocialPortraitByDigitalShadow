from abc import abstractmethod, ABC


class PredictionStrategy(ABC):

    @abstractmethod
    def predict_classes(self, X):
        pass
