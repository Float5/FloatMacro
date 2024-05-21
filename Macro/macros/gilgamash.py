import sys
import os
sys.path.append((os.path.abspath(__file__).replace("\\", "/")).replace("/Macro/macros/gilgamash.py", ""))
sys.path.append((os.path.abspath(__file__).replace("\\", "/")).replace("/Macro/macros/gilgamash.py", "") + '/venv/Lib/site-packages')

from Macro.utils import macroFunctions
import threading
import keyboard
import time


working = False

def run():
    global working
    working = False
    t_start = threading.Thread(target=start)
    t_start.start()

    while not working:
        time.sleep(0.1)
        continue

    t_start.join()

    t_on = threading.Thread(target=on)
    t_on.start()

    t_stop = threading.Thread(target=stop)
    t_stop.start()

    while working:
        time.sleep(0.1)
        continue

    t_on.join()
    t_stop.join()


def on():
    global working

    if working:
        macroFunctions.slashConfirm()



def start():
    global working
    while not working:
        if keyboard.read_key() == "f1":
            working = True
            print("start")
            continue

def stop():
    global working
    while working:
        if keyboard.read_key() == "f3":
            working = False
            print("stopped")
            continue


