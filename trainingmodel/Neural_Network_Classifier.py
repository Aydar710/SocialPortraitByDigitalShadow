import numpy
import pandas
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import classification_report, accuracy_score
import pickle
# define baseline model

from tensorflow.python.keras.wrappers.scikit_learn import KerasClassifier

# load dataset
answers_frame = pandas.read_csv('../answerprocessing/answers.csv', delimiter=',')

dataset = answers_frame.values
X = dataset[:, 8:]
y_o = dataset[:, 3]
y_c = dataset[:, 4]
y_e = dataset[:, 5]
y_a = dataset[:, 6]
y_n = dataset[:, 7]

X = numpy.asarray(X).astype(numpy.float32)
y_o = numpy.asarray(y_o).astype(numpy.float32)


# load dataset
# dataframe = pandas.read_csv("iris.csv", header=None)
# dataset = dataframe.values
# X = dataset[:, 0:4].astype(float)
# Y = dataset[:, 4]


# define baseline model
def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(8, input_dim=5, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# encode class values as integers
encoder = LabelEncoder()
encoder.fit(y_o)
encoded_Y = encoder.transform(y_o)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

model = baseline_model()
estimator = KerasClassifier(build_fn=model, epochs=5, batch_size=5, verbose=0)

kfold = KFold(n_splits=10, shuffle=True)

results = cross_val_score(estimator, X, dummy_y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean() * 100, results.std() * 100))

# fit the keras model on the dataset
model.fit(X, dummy_y, epochs=100, batch_size=4)

_, accuracy = model.evaluate(X, dummy_y)
print('Accuracy: %.2f' % (accuracy * 100))

predictions = model.predict_classes(X)
print(predictions)
classification_report = classification_report(y_o, predictions)
print(classification_report)
