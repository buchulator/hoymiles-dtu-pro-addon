FROM python:3.11-slim

WORKDIR /app

COPY bridge.py /app/bridge.py
COPY run.sh /run.sh

RUN chmod +x /run.sh
RUN pip install pymodbus paho-mqtt

CMD ["/run.sh"]
