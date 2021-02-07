from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense


class NeuralNetworkClassifier:

    # define baseline model
    def baseline_model(self):
        # create model
        model = Sequential()
        model.add(Dense(8, input_dim=5, activation='relu'))
        model.add(Dense(2, activation='softmax'))
        # Compile model
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model
