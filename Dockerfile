FROM eclipse-temurin:17-jre

WORKDIR /app

# Modbus → MQTT Bridge (funktioniert mit DTU-Pro)
ADD https://github.com/wasilkum/hoymiles-mqtt-integration/releases/latest/download/app.jar /app/app.jar

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
