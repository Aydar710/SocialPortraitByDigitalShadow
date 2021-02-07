import pandas
from sklearn.neural_network import MLPClassifier

# multi-layer perceptron classifier

# load dataset
answers_frame = pandas.read_csv('../answerprocessing/answers.csv', delimiter=',')

dataset = answers_frame.values
X = dataset[:, 8:].astype(float)
y_o = dataset[:, 3].astype(float)
y_c = dataset[:, 4].astype(float)
y_e = dataset[:, 5]
y_a = dataset[:, 6]
y_n = dataset[:, 7]

# X = [[0., 0.], [1., 1.]]
# y = [0, 1]

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15, 10), random_state=1, max_iter=100000)
clf.fit(X, y_c)
predictions = clf.predict(X)
print(predictions)
