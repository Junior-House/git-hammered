import argparse

def play_audio(filename):

    try:
        import sounddevice as sd
        import soundfile as sf

        # read file and playback
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs)
        status = sd.wait()
        if status: print('Error during playback: ' + str(status))

    except KeyboardInterrupt: print('\nInterrupted by user')
    except Exception as e: print(type(e).__name__ + ': ' + str(e))