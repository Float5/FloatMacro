import os
import sys


from Macro.utils import macroFunctions

from Macro.macros import autoclick
from Macro.macros import gilgamash
from Macro.macros import biomefinder
from Macro.macros import config

def clear():
    print("\n"*10)


def main():
    print("Welcome to BCWO Float Macro")
    print("Input any letter to Start")
    input()
    clear()


    while True:
        print("Enter the macro name")
        macroName = input()

        if macroName == "autoclick":
            autoclick.run()
        elif macroName == "gilgamash":
            gilgamash.run()
        elif macroName == "biomefinder":
            biomefinder.run()
        elif macroName == "config":
            config.run()
        elif macroName == "exit":
            exit()
        else:
            print(f"{macroName} is not founded")

        clear()