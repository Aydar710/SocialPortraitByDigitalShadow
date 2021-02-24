from strategy.MLPStrategy import MLPStrategy
from strategy.MultinomialLogisticRegressionStrategy import MultinomialLogisticRegressionStrategy
from strategy.NeuralNetworkStrategy import NeuralNetworkStrategy
from strategy.Oracle import Oracle
from strategy.RandomForestStrategy import RandomForestStrategy

random_forest = RandomForestStrategy()
mlp_strategy = MLPStrategy()
nn_strategy = NeuralNetworkStrategy()
multinomial_logistic_regression_strategy = MultinomialLogisticRegressionStrategy()
oracle = Oracle(random_forest)

predictions = oracle.predict_classes([2, 0, 133, 1, 5, 4, 15])
print(predictions)
