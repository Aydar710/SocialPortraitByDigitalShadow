from strategy.MLPStrategy import MLPStrategy
from strategy.Oracle import Oracle
from strategy.RandomForestStrategy import RandomForestStrategy

random_forest = RandomForestStrategy()
mlp_strategy = MLPStrategy()
oracle = Oracle(mlp_strategy)

predictions = oracle.predict_classes([1, 401, 220, 43, 3])
print(predictions)
