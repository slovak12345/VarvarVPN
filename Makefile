CONTAINER_TYPE = release

.PHONY: all docker

all: docker

install:
	echo "install"
build:
	echo "build"
docker: 
	python3 script/build_docker.py $(CONTAINER_TYPE)
clean:
	git clean -f -x -d *