import audio.record as record
import argparse
import os
import shutil
import time
import inflect
import threading
import string
import signal
p = inflect.engine()
sem = threading.Semaphore(0)

TRAIN_USER_COUNT = 10
USER_COUNTDOWN_START = 5

def str2bool(v):
    if isinstance(v, bool): return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'): return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'): return False
    else: raise argparse.ArgumentTypeError('Boolean value expected.')

def countdown(start_num):
    while (start_num >= 0):
        print(start_num)
        start_num -= 1

def run_alpha():

    # countdown start
    start_num = USER_COUNTDOWN_START
    while start_num >= 0:
        print('\rStarting in ' + str(start_num), end='')
        start_num -= 1
        if start_num == -1: sem.release()
        time.sleep(1)
    print('')

    # print letters
    for letter in string.ascii_lowercase:
        print(letter)
        time.sleep(0.65)
    time.sleep(1)
    os.kill(os.getpid(), signal.SIGINT)

def prompt_user(name, dir) -> str:

    # display starting message
    print('\nWelcome to Git Hammered.')
    time.sleep(2)
    print('Please recite the letters as they appear on the screen.')
    time.sleep(2)

    # start counting thread
    thread = threading.Thread(target=run_alpha)
    thread.start()

    # start audio capture
    sem.acquire()
    filename = record.record_audio(name, dir)
    thread.join()
    print('\nRecording finished: ' + repr(filename))
    print('Thank you! But remember — it is scientifically impossible to ' 
        + 'be too plastered. Do yourself a solid and go crack a cold one.')
    return filename

if __name__ == "__main__":

    # parse user arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-n', '--name', required='true', 
        help='specify the user\'s name for training')
    args = parser.parse_args()

    # build directory
    dir_name = 'prompt-' + args.name
    if not os.path.isdir(dir_name): os.mkdir(dir_name)

    try: prompt_user(args.name, dir_name)
    except Exception as e:
        print("Error collecting training data: " + e)