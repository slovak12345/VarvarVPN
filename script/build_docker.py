import os
import logging

try:
    os.mkdir("logs")
except:
    pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/build_docker.log"),
        logging.StreamHandler()
    ]
)

root_path=os.chdir("../")

logging.info(f"Root path of repository: {root_path}")