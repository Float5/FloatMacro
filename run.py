from Macro import main
import os


path = (os.path.abspath(__file__).replace("\\", "/")).replace("/run.py", "")
main.main()
