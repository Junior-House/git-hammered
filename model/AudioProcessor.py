import numpy as np

# AudioProcessor class provides standarised functionality to perform conversions between .wav files 
# and interpretable tensors for use in the HammeredModel.  See method comments for guidance on use
class AudioProcessor:

    def __init__(self):
        print("Audio processor at your service.")

    # process a given single, unlabeled, audio sample, into a given tensor for model interpretability
    def processAudioSample(self, audioSample):
        # perform the processing here
        return audioSample

    # takes a raw array of .wav file and boolean pairs, then breaks them down into tensors for training
    # and testing sets.  Returns them all for use in initialising the model
    def prepareData(self, rawData):
        trainX = "hello"
        trainY = "goodbye"
        testX = "yellow"
        testY = "mellow"
        return trainX, trainY, testX, testY