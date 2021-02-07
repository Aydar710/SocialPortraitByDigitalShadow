# load dataset
import pandas
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

answers_frame = pandas.read_csv('../answerprocessing/answers.csv', delimiter=',')

dataset = answers_frame.values
X = dataset[:, 8:].astype(float)
y_o = dataset[:, 3].astype(float)
y_c = dataset[:, 4].astype(float)
y_e = dataset[:, 5]
y_a = dataset[:, 6]
y_n = dataset[:, 7]

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(y_o)
encoded_yo = encoder.transform(y_o)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_yo)


def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(8, input_dim=len(X[0]), activation='relu'))
    model.add(Dense(2, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


estimator = KerasClassifier(build_fn=baseline_model, epochs=1, batch_size=5, verbose=0)

kfold = KFold(n_splits=10, shuffle=True)

results = cross_val_score(estimator, X, dummy_y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

estimator.fit(X, y_o)
estimator.predict_proba([X[0]])