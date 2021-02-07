from strategy.MLPStrategy import MLPStrategy
from strategy.Oracle import Oracle
from strategy.RandomForestStrategy import RandomForestStrategy

random_forest = RandomForestStrategy()
MLP_strategy = MLPStrategy()
oracle = Oracle(random_forest)
oracle.predict_classes("")
oracle.strategy = MLP_strategy
oracle.predict_classes("")
