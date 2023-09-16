import os
import logging
import sys

docker_name="varvar_vpn"
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

exp_type=sys.argv[1]

logging.info(f"Selected type: {exp_type}")

root_path=os.path.abspath(".")

logging.info(f"Root path of repository: {root_path}")

docker_compose_path=root_path + "/Docker-compose.yml"

logging.info(f"Docker compose path of repository: {docker_compose_path}")

mount_path=root_path

container_path="/home/varvarvpn"

with open(root_path + "/VERSION") as f:
    VERSION = f.read()

logging.info(f"Start creating docker image of VarvarVPN with version {VERSION}...")

os.system(f"export CONTAINER_PATH=${container_path} && export MOUNT_PATH=${root_path} && docker-compose -f {docker_compose_path} run --rm --name {docker_name}_{exp_type} {docker_name}_{exp_type} bash")

logging.info(f"Finished build docker image {docker_name}:{VERSION}:")

os.system(f"docker image ls | grep {docker_name}")