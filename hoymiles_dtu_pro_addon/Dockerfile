ARG BUILD_FROM
FROM $BUILD_FROM

# Python installieren (falls nicht im Base-Image)
RUN apk add --no-cache python3 py3-pip

# Skripte kopieren
COPY run.sh /run.sh
COPY bridge.py /app/bridge.py

RUN chmod +x /run.sh

# rootfs kopieren (für s6-overlay)
COPY rootfs/ /
