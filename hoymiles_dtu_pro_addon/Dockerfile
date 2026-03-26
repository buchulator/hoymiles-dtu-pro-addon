ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache python3 py3-pip

COPY run.sh /run.sh
COPY bridge.py /app/bridge.py

RUN chmod +x /run.sh

COPY rootfs/ /
