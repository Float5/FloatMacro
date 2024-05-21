import pickle
import sys
import os
sys.path.append((os.path.abspath(__file__).replace("\\", "/")).replace("/Macro/macros/biomefinder.py", ""))
sys.path.append((os.path.abspath(__file__).replace("\\", "/")).replace("/Macro/macros/biomefinder.py", "") + '/venv/Lib/site-packages')

import pyautogui
from Macro.utils import macroFunctions
import threading
import keyboard
import time
import webbrowser


working = False
biomeCodes = {
    "1" : "Grasslands",
    "2" : "Night",
    "3" : "Blizzard",
    "4" : "Nature",
    "5" : "StormSurge",
    "6" : "Flare",
    "7" : "StarryNight",
    "8" : "Radiation",
    "9" : "PureVSCorruptWar",
    "10" : "HolyVSUnholyWar",
    "11" : "TheHeavens",
    "12" : "TheVoid",
    "13" : "CultistArmy",
    "14" : "TheBlindingLight",
    "15" : "TheShroudingDarkness",
}

wannaBiomes = []
slotNums = []

image_path = ""

def run():
    global image_path
    global working
    global wannaBiomes
    global slotNums

    wannaBiomes = []

    while True:
        print("Enter the Biome Code(exit, help)")
        answer = input()

        if answer == "exit":
            break
        elif answer == "help":
            for i in range(len(biomeCodes)):
                print(f"{i + 1} : {biomeCodes.get(str(i + 1))}")
        elif answer == "all":
            wannaBiomes = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
        else:
            if answer in biomeCodes:
                wannaBiomes.append(answer)

    wannaBiomes = list(set(wannaBiomes))

    while True:
        print("Enter the Slots to Use(exit, 1~9,0)")
        answer = input()
        try:
            num = int(answer)
            if num >= 0 and num < 10:
                slotNums.append(answer)
        except:
            if answer == "exit":
                break
            else:
                continue

    slotNums = list(set(slotNums))

    image_path = (os.path.abspath(__file__).replace("\\", "/")).replace("/macros/biomefinder.py", "") + '/images/image/biomefinder/'

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
    global biomeCodes
    global image_path

    link = ""

    with open((os.path.abspath(__file__).replace("\\", "/")).replace("/biomefinder.py", "") + "/link.pickle", "rb") as data:
        link = pickle.load(data)


    macroFunctions.closeRoblox()
    webbrowser.open(link)
    first = True

    while working:
        while working:
            if first:
                first = False
            else:
                macroFunctions.rejoin()

            time.sleep(1)
            robloxExecuted = False
            while working:
                if macroFunctions.is_running("RobloxPlayerBeta.exe"):
                    print("로블록스 실행 감지됨")
                    robloxExecuted = True
                    break
            if robloxExecuted:
                break

        while working:
            try:
                image_location = pyautogui.locateOnScreen(image_path + "BCWO_Loaded.png", confidence=0.6)
                print("BCWO 로딩 완료 감지됨")
                break
            except Exception:
                continue

        time.sleep(1)
        macroFunctions.lClick()
        time.sleep(0.5)
        macroFunctions.altTab()
        time.sleep(0.5)
        macroFunctions.altTab()
        time.sleep(0.5)

        macroFunctions.press("forwardSlash")
        time.sleep(0.2)
        macroFunctions.press("enter")
        time.sleep(0.2)

        for i in range(len(slotNums)):
            time.sleep(0.1)
            macroFunctions.press(slotNums[i])
            time.sleep(0.1)
            macroFunctions.lClick()

        time.sleep(0.5)

        macroFunctions.press("w", duration=3)

        chatToggle = False

        while working:
            isEnd = False
            if chatToggle == False:
                macroFunctions.press("forwardSlash")
            else:
                macroFunctions.press("enter")
            chatToggle = not chatToggle
            time.sleep(1)
            flag = False
            foundBiome = "Grasslands"
            for i in range(1, len(biomeCodes)):
                try:
                    image_location = pyautogui.locateOnScreen(image_path + biomeCodes.get(str(i + 1)) + ".png", confidence=0.8)
                    print(f"바이옴을 찾았습니다! ({biomeCodes.get(str(i + 1))})")
                    flag = True
                    foundBiome = str(i + 1)
                except Exception:
                    continue
            if flag:
                if foundBiome not in wannaBiomes:
                    break
                else:
                    #winsound.Beep(200, 2000)
                    macroFunctions.press("enter")
                    time.sleep(0.1)
                    macroFunctions.reset()
                    time.sleep(0.5)
                    for i in range(10):
                        macroFunctions.press("forwardSlash")
                        time.sleep(0.1)
                        macroFunctions.press("1")
                        time.sleep(0.1)
                        macroFunctions.press("enter")
                        time.sleep(0.1)
                    while True and working:
                        try:
                            image_location = pyautogui.locateOnScreen(
                                image_path + "Grasslands.png",
                                confidence=0.7)
                            isEnd = True
                            break
                        except:
                            try:
                                image_location = pyautogui.locateOnScreen(
                                    image_path + "Grasslands.png",
                                    confidence=0.7)
                                isEnd = True
                                break
                            except:
                                for i in range(len(slotNums)):
                                    time.sleep(0.1)
                                    macroFunctions.press(slotNums[i])
                                    time.sleep(0.1)
                                    macroFunctions.lClick()
                    if isEnd:
                        break









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
