import argparse
import tempfile
import queue
import sys

def record_audio(name, dir) -> str:
    try:
        import sounddevice as sd
        import soundfile as sf
        import numpy 
        assert numpy

        # grab system default device/sr
        device_info = sd.query_devices(None, 'input')
        samplerate = int(device_info['default_samplerate'])
        filename = tempfile.mktemp(prefix=name + '-', suffix='.wav', dir=dir)
        q = queue.Queue()

        def callback(indata, frames, time, status):
            """
            This is called (from a separate thread) for each audio block.
            """

            if status: print(status, file=sys.stderr)
            q.put(indata.copy())

        with sf.SoundFile(filename, mode='x', samplerate=samplerate, channels=1, subtype=None) as file:
            with sd.InputStream(samplerate=samplerate, device=None, channels=1, callback=callback):

                # write recording until exit
                while True: file.write(q.get())

    except KeyboardInterrupt: return filename
    except Exception as e: 
        print(type(e).__name__ + ': ' + str(e)) 
        return None
