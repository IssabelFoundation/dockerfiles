FROM alphacep/kaldi-vosk-server:latest

ARG URL
ENV URL=$URL

ARG LANGUAGE
ENV LANGUAGE=$LANGUAGE

ARG VERSION
ENV VERSION=$VERSION

RUN mkdir /opt/vosk-model-${LANGUAGE} \
   && cd /opt/vosk-model-${LANGUAGE} \
   && wget -q $(URL) -O vosk-model.zip \
   && unzip vosk-model.zip \
   && mv vosk-model-* model \
   && rm -rf vosk-model.zip

EXPOSE 2700
WORKDIR /opt/vosk-server/websocket
CMD python3 ./asr_server.py  /opt/vosk-model-${LANGUAGE}/model
