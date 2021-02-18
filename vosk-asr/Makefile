DOCKER ?= docker
TARGET ?= issabel/vosk-asr
VERSION ?= 0.3
LANGUAGE ?= es
TARGET_LATEST ?= latest

all:
	@echo "Building ${TARGET}"
	$(DOCKER) build -t $(TARGET)-$(LANGUAGE):$(VERSION) --build-arg VERSION=$(VERSION) --build-arg LANGUAGE=$(LANGUAGE) -f Dockerfile .

push:
	$(DOCKER) push $(TARGET)-$(LANGUAGE):$(VERSION)
	$(DOCKER) tag $(TARGET)-$(LANGUAGE):$(VERSION) $(TARGET)-$(LANGUAGE):$(TARGET_LATEST)
	$(DOCKER) push $(TARGET)-$(LANGUAGE):$(TARGET_LATEST)
