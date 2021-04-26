from strategy.MLPStrategy import MLPStrategy
from strategy.MultinomialLogisticRegressionStrategy import MultinomialLogisticRegressionStrategy
from strategy.NeuralNetworkStrategy import NeuralNetworkStrategy
from strategy.RandomForestStrategy import RandomForestStrategy
from workexample.Predictor import Predictor

global predictor
predictor = Predictor()


def random_forest():
    print("random forest")
    predictor.set_strategy(RandomForestStrategy())
    predictor.predict_social_portrait("nursabir")


def mlp():
    print("MLP")
    predictor.set_strategy(MLPStrategy())
    predictor.predict_social_portrait("nursabir")


def neural_network():
    print("NeuralNetwork")
    predictor.set_strategy(NeuralNetworkStrategy())
    predictor.predict_social_portrait("nursabir")


def logistic_regression():
    print("Multinomial logistic regresion")
    predictor.set_strategy(MultinomialLogisticRegressionStrategy())
    predictor.predict_social_portrait("nursabir")


neural_network()
logistic_regression()
mlp()
random_forest()
