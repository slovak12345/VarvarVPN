import os
import logging

docker_name="VarvarVPN"
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

root_path=os.path.abspath(".")

logging.info(f"Root path of repository: {root_path}")

with open(root_path + "/VERSION") as f:
    VERSION = f.read()

logging.info(f"Start creating docker image of VarvarVPN with version {VERSION}...")

os.system(f"docker build -f {root_path + "/Dockerfile"} -t {docker_name}:{VERSION} .")

logging.info(f"Finished build docker image {docker_name}:{VERSION}:")

os.system(f"docker image ls | grep {docker_name}")