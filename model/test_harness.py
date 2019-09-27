from GitHammeredModels import AudioProcessor
from GitHammeredModels import HammeredModel
import numpy as np

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=FutureWarning)

processor = AudioProcessor()

rawData = np.random.randn(2, 10)
print(rawData)

trainX, trainY, testX, testY = processor.prepareData(rawData)
