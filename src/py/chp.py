from asyncio import subprocess
import sys
from subprocess import Popen

profile = "chrome-default"

if len(sys.argv) > 1:
    try:
        pnum = int(sys.argv[1])
    except ValueError:
        print("Wrong execution. Usage: chp <PROFILE_NUMBER>")
        print("Profile numbers:")
        print("1 - Personal")
        print("2 - School")
        print("3 - Professional")
        print("4 - aiesec")
        print("0 - Default")
        exit(-1)

    if pnum == 1:
        profile = "chrome-personal"
    elif pnum == 2:
        profile = "chrome-escom"
    elif pnum == 3:
        profile = "chrome-professional"
    elif pnum == 4:
        profile = "chrome-aiesec"

filepath = "C:/prjs/pc-scripts/src/bat/" + profile + ".bat"
p = Popen(filepath, shell=False, stdout=subprocess.PIPE)
stdout, stderr = p.communicate()