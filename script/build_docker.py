import os
import logging

try:
    os.mkdir("logs")
except:
    pass

l = logging.getLogger(__name__)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("logs/build_docker.log")

c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.INFO)

format_ = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

c_handler.setFormatter(format_)
f_handler.setFormatter(format_)

l.addHandler(c_handler)
l.addHandler(f_handler)

root_path=os.chdir("../")

l.info(f"Root path of repository: {root_path}")