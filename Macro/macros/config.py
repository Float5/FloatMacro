import pickle
import os

def run():
    while True:
        print("Enter the Config to Change")

        answer = input()

        if answer == "exit":
            break
        elif answer == "privateServerLink":
            privateServerLink()








def privateServerLink():
    print("Enter the Private Server Link")

    link = input()

    with open((os.path.abspath(__file__).replace("\\", "/")).replace("/config.py", "") + "/link.pickle", "wb") as data:
        pickle.dump(link, data)
