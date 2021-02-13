from strategy.MLPStrategy import MLPStrategy
from strategy.MultinomialLogisticRegressionStrategy import MultinomialLogisticRegressionStrategy
from strategy.NeuralNetworkStrategy import NeuralNetworkStrategy
from strategy.RandomForestStrategy import RandomForestStrategy
from workexample.Predictor import Predictor

predictor = Predictor()
# print("random forest")
# predictor.set_strategy(RandomForestStrategy())
# predictor.predict_social_portrait("https://vk.com/id_sveta1999")
#
# print("MLP")
# predictor.set_strategy(MLPStrategy())
# predictor.predict_social_portrait("https://vk.com/id_sveta1999")

print("NeuralNetwork")
predictor.set_strategy(NeuralNetworkStrategy())
predictor.predict_social_portrait("https://vk.com/id_sveta1999")

# print("Multinomial logistic regresion")
# predictor.set_strategy(MultinomialLogisticRegressionStrategy())
# predictor.predict_social_portrait("https://vk.com/id_sveta1999")