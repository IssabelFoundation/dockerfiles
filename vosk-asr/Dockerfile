FROM alphacep/kaldi-vosk-server:latest

ARG LANGUAGE
ENV LANGUAGE=$LANGUAGE

ARG VERSION
ENV VERSION=$VERSION

RUN mkdir /opt/vosk-model-${LANGUAGE} \
   && cd /opt/vosk-model-${LANGUAGE} \
   && wget -q https://alphacephei.com/vosk/models/vosk-model-small-${LANGUAGE}-${VERSION}.zip \
   && unzip vosk-model-small-${LANGUAGE}-${VERSION}.zip \
   && mv vosk-model-small-${LANGUAGE}-${VERSION} model \
   && rm -rf vosk-model-small-${LANGUAGE}-${VERSION}.zip

EXPOSE 2700
WORKDIR /opt/vosk-server/websocket
CMD python3 ./asr_server.py  /opt/vosk-model-${LANGUAGE}/model
