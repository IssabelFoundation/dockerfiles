#https://alphacephei.com/vosk/models

DOCKER ?= docker
TARGET ?= issabel/vosk-asr
VERSION ?= 0.2
LANGUAGE ?= en
URL ?= https://alphacephei.com/vosk/models/vosk-model-en-us-aspire-0.2.zip
TARGET_LATEST ?= latest

all:
	@echo "Building ${TARGET}"
	$(DOCKER) build -t $(TARGET)-$(LANGUAGE):$(VERSION) --build-arg URL=$(URL) --build-arg VERSION=$(VERSION) --build-arg LANGUAGE=$(LANGUAGE)  --build-arg KALDI_MKL=0  -f Dockerfile .

push:
	$(DOCKER) push $(TARGET)-$(LANGUAGE):$(VERSION)
	$(DOCKER) tag $(TARGET)-$(LANGUAGE):$(VERSION) $(TARGET)-$(LANGUAGE):$(TARGET_LATEST)
	$(DOCKER) push $(TARGET)-$(LANGUAGE):$(TARGET_LATEST)
