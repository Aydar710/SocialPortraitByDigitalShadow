from abc import abstractmethod, ABC

import pandas


class PredictionStrategy(ABC):

    def __init__(self):
        answers_frame = pandas.read_csv('../answerprocessing/answers.csv', delimiter=',')
        dataset = answers_frame.values
        self.X = dataset[:, 8:].astype(float)
        self.y_o = dataset[:, 3].astype(float)
        self.y_c = dataset[:, 4].astype(float)
        self.y_e = dataset[:, 5].astype(float)
        self.y_a = dataset[:, 6].astype(float)
        self.y_n = dataset[:, 7].astype(float)

    @abstractmethod
    def predict_classes(self, x) -> map:
        pass
