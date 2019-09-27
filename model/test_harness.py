from GitHammeredModels import AudioProcessor
from GitHammeredModels import HammeredModel
import numpy as np

processor = AudioProcessor()

rawData = np.zeros((2, 10))
print(rawData)

trainX, trainY, testX, testY = processor.prepareData(rawData)
