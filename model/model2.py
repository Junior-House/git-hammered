import tensorflow as tf
import numpy as np

class HammeredModel:

    def __init__(self, trainingDataset, testingDataset, learningRate, numIterations):
        self.trainingDataset = trainingDataset
        self.testingDataset = testingDataset
        self.learningRate = learningRate
        self.numIterations = numIterations

    def train():
        print("Gooday mate")
        return

    # returns true if the audio sample is drunk, returns false if the sample is sober
    def inference(audioSample) -> bool:
        print("He's drunk as a skunk mate")
        return True


fred = HammeredModel([1, 2], [3, 4], 0.01, 1000)
print(fred.trainingDataset)
print(fred.testingDataset)
print(fred.learningRate)
print(fred.numIterations)