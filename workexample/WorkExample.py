from strategy.MLPStrategy import MLPStrategy
from strategy.MultinomialLogisticRegressionStrategy import MultinomialLogisticRegressionStrategy
from strategy.NeuralNetworkStrategy import NeuralNetworkStrategy
from strategy.RandomForestStrategy import RandomForestStrategy
from workexample.Predictor import Predictor

global predictor
predictor = Predictor()


def random_forest(id):
    print("random forest")
    predictor.set_strategy(RandomForestStrategy())
    predictor.predict_social_portrait(id)


def mlp(id):
    print("MLP")
    predictor.set_strategy(MLPStrategy())
    predictor.predict_social_portrait(id)


def neural_network(id):
    print("NeuralNetwork")
    predictor.set_strategy(NeuralNetworkStrategy())
    predictor.predict_social_portrait(id)


def logistic_regression(id):
    print("Multinomial logistic regresion")
    predictor.set_strategy(MultinomialLogisticRegressionStrategy())
    predictor.predict_social_portrait(id)


def predict(id):
    random_forest(id)
    mlp(id)
    neural_network(id)
    logistic_regression(id)



