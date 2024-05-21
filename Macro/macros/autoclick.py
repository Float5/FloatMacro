import sys
import os
sys.path.append((os.path.abspath(__file__).replace("\\", "/")).replace("/Macro/macros/autoclick.py", ""))
sys.path.append((os.path.abspath(__file__).replace("\\", "/")).replace("/Macro/macros/autoclick.py", "") + '/venv/Lib/site-packages')

from Macro.utils import macroFunctions
import threading
import keyboard
import time

working = False
second = 1
slots = [False, False, False, False, False, False, False, False, False, False]
slotNums = []

def run():
    cps = 0
    while True:
        print("How many clicks per second?")
        cps = input()

        try:
            cps = float(cps)
            break
        except ValueError:
            continue

    global slots
    slots = [False, False, False, False, False, False, False, False, False, False]
    while True:
        print("slots to use(1~10, slot0 = 10, done = 0)")
        slotNum = 0
        try:
            slotNum = int(input())
        except ValueError:
            continue

        if slotNum == 0:
            break

        slots[slotNum - 1] = True


    global slotNums
    slotNums = []
    for i in range(len(slots)):
        if slots[i]:
            slotNums.append(str(i + 1))

    print(slotNums)

    global second
    second = 1 / cps

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
    global second
    global slotNums

    if len(slotNums) == 0:
        while True:
            time.sleep(second)
            if working:
                macroFunctions.lClick()
            else:
                return
    elif len(slotNums) == 1:
        macroFunctions.press(slotNums[0])
        while True:
            time.sleep(second)
            if working:
                macroFunctions.lClick()
            else:
                return
    else:
        index = 0
        while True:
            time.sleep(second)
            if working:
                macroFunctions.press(slotNums[index])
                macroFunctions.lClick()
                index += 1
                if index >= len(slotNums):
                    index = 0
            else:
                return



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


