import os
import logging as l

try:
    os.mkdir("logs")
except:
    pass


l.basicConfig(level=l.INFO, filename="logs/build_docker.log", filemode="w")

root_path=os.chdir("../")

l.info(root_path)