all: docker

install:
	echo "install"
build:
	echo "build"
docker:
	python3 script/build_docker.py
clean:
	git clean -f -x -d *