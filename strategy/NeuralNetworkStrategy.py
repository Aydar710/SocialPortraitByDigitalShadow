from keras.utils import np_utils
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense

from strategy.PredictionStrategy import PredictionStrategy


class NeuralNetworkStrategy(PredictionStrategy):

    # define baseline model
    def baseline_model(self, output_neurons: int):
        # create model
        model = Sequential()
        model.add(Dense(8, input_dim=len(self.X[0]), activation='relu'))
        model.add(Dense(output_neurons, activation='softmax'))
        # Compile model
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def predict_classes(self, x) -> map:
        predictions = []
        for y in [self.y_o, self.y_c, self.y_e, self.y_a, self.y_n]:
            # encode class values as integers
            encoder = LabelEncoder()
            encoder.fit(y)
            encoded_Y = encoder.transform(y)
            # convert integers to dummy variables (i.e. one hot encoded)
            dummy_y = np_utils.to_categorical(encoded_Y)

            model = self.baseline_model(output_neurons=len(dummy_y[0]))

            # fit the keras model on the dataset
            model.fit(self.X, dummy_y, epochs=100, batch_size=4)
            prediction = model.predict_classes([x])
            predictions.append(prediction)

        return {'O': predictions[0][0], 'C': predictions[1][0], 'E': predictions[2][0], 'A': predictions[3][0],
                'N': predictions[4][0]}

    def get_strategy_name(self):
        return "Neural Network"

    def print_metrics_for(self, y):
        encoder = LabelEncoder()
        encoder.fit(y)
        encoded_Y = encoder.transform(y)
        dummy_y = np_utils.to_categorical(encoded_Y)
        model = self.baseline_model(output_neurons=len(dummy_y[0]))

        model.fit(self.X, dummy_y, epochs=100, batch_size=4)
        predictions = model.predict_classes(self.X)
        report = classification_report(y, predictions)
        print(report)

    def print_metrics(self):
        print("Metrics O")
        self.print_metrics_for(self.y_o)
        print("Metrics C")
        self.print_metrics_for(self.y_c)
        print("Metrics E")
        self.print_metrics_for(self.y_e)
        print("Metrics A")
        self.print_metrics_for(self.y_a)
        print("Metrics N")
        self.print_metrics_for(self.y_n)