from asyncio import subprocess
from subprocess import Popen

filepath = "C:/prjs/pc-scripts/src/bat/" + "pcinit" + ".bat"
p = Popen(filepath, shell=False, stdout=subprocess.PIPE)
stdout, stderr = p.communicate()