import tflearn
import numpy as np

class HammeredModel:

    def __init__(self, trainX, trainY, testX, testY, learningRate, numIterations):
        self.trainX = trainX
        self.trainY = trainY
        self.testX = testX
        self.testY = testY
        self.learningRate = learningRate
        self.numIterations = numIterations

    def train(self):
        net = tflearn.input_data([None, 20, 80])
        net = tflearn.lstm(net, 128, dropout=0.8)
        net = tflearn.fully_connected(net, 10, activation='softmax')
        net = tflearn.regression(net, optimizer='adam', learning_rate = self.learningRate, loss='categorical_crossentropy')

        self.model = tflearn.DNN(net, tensorboard_verbose=0)
        while True:
            self.model.fit(self.trainX, self.trainY, n_epoch = 10, validation_set=(self.testX, self.testY), show_metric=True, batch_size=64)
            _y = self.model.predict(self.trainX)

        self.model.save('tflearn.lstm.model')

    # returns true if the audio sample (processed by AudioProcessor class) is drunk, returns false 
    # if the sample is sober
    def inference(self, processedAudioSample) -> bool:
        return self.model.predict(processedAudioSample)


# AudioProcessor class provides standarised functionality to perform conversions between .wav files 
# and interpretable tensors for use in the HammeredModel.  See method comments for guidance on how to use
class AudioProcessor:

    def __init__(self):
        print("Audio processor at your service.")

    # perform some processing to the audio sample, such that we can feed it to the model
    def processAudioSample(self, audioSample):
        
        return audioSample

    # takes a raw array of .wav file and boolean pairs, then breaks them down into tensors for training
    # and testing sets.  Returns them all for use in initialising the model
    def prepareData(self, rawData):
        trainX = "hello"
        trainY = "goodbye"
        testX = "yellow"
        testY = "mellow"
        return trainX, trainY, testX, testY
