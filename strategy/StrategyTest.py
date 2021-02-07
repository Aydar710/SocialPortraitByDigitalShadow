from strategy.MLPStrategy import MLPStrategy
from strategy.NeuralNetworkStrategy import NeuralNetworkStrategy
from strategy.Oracle import Oracle
from strategy.RandomForestStrategy import RandomForestStrategy

random_forest = RandomForestStrategy()
mlp_strategy = MLPStrategy()
nn_strategy = NeuralNetworkStrategy()
oracle = Oracle(random_forest)

predictions = oracle.predict_classes([2, 0, 133, 1, 5])
print(predictions)
