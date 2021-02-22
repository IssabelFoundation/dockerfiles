DOCKER ?= docker
TARGET ?= issabel/number-parser

all:
	@echo "Building ${TARGET}"
	$(DOCKER) build -t $(TARGET) -f Dockerfile .

push:
	$(DOCKER) push $(TARGET)
