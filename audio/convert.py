import os
from scipy.io.wavfile import read
import numpy as np

def convert_audio(name) -> list:
    audio_arrs = []

    # verify directory 
    if not os.path.isdir('data-' + name):
        print('User data directory does not exist.')
        return None
    else:
        files = [i for i in os.listdir('data-' + name) if i.endswith("wav")]
        for file in files:
            f = read('data-' + name + '/' + file)
            audio_arrs.append(f)

    # stack audio arrays
    return np.asarray(audio_arrs)
