import sys
import os
sys.path.append((os.path.abspath(__file__).replace("\\", "/")).replace("/macroFunctions.py", ""))
sys.path.append((os.path.abspath(__file__).replace("\\", "/")).replace("/Macro/utils/macroFunctions.py", "") + '/venv/Lib/site-packages')

import pyautogui
import time
import webbrowser

from Macro.utils.positionClass import Position

import re
import subprocess

def is_running(name):
    for task in subprocess.check_output(['tasklist']).decode(
            'cp949', 'ignore').split("\r\n"):
        m = re.match("(.+?) +(\d+) (.+?) +(\d+) +(\d+.* K).*", task)
        if m is not None:
            if m.group(1) == name:
                return True
    return False







def getMousePosition():
    pos = Position(pyautogui.position().x, pyautogui.position().y)
    return pos

def moveTo(toX, toY):
    x = pyautogui.position().x
    y = pyautogui.position().y
    move(toX - x, toY - y)

def move(x, y):
    pyautogui.move(x, y)

def dragTo(x, y, duration):
    pyautogui.dragTo(x, y, duration)

def drag(x, y, toX, toY, duration):
    moveTo(x, y)
    dragTo(toX, toY, duration)

def lClick():
    pyautogui.click()

def rClick():
    pyautogui.click(button='right')


def press(key, duration=0):
    code = ScanCodes.get(key)
    PressKey(code)
    time.sleep(duration)
    ReleaseKey(code)

def hotkey(key1, key2):
    pyautogui.hotkey(key1, key2)


def altTab():
    hotkey("alt", "tab")


def rejoin():
    time.sleep(1)
    if is_running("RobloxPlayerBeta.exe"):
        hotkey("alt", "f4")
        time.sleep(1)

    press("f5")

def reset():
    press("esc")
    time.sleep(0.2)
    press("r")
    time.sleep(0.2)
    press("enter")
    time.sleep(0.2)

def closeRoblox():
    if is_running("RobloxPlayerBeta.exe"):
        hotkey("alt", "f4")



def slashConfirm():
    press("forwardSlash", 0.1)
    pyautogui.typewrite("Confirm")





































import ctypes

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))



ScanCodes = {
    "1" : 2,
    "2" : 3,
    "3" : 4,
    "4" : 5,
    "5" : 6,
    "6" : 7,
    "7" : 8,
    "8" : 9,
    "9" : 10,
    "0" : 11,
    "forwardSlash" : 53,
    "w" : 17,
    "enter" : 28,
    "esc" : 1,
    "r" : 19,
    "f5" : 63,

}