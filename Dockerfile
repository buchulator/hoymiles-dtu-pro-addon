FROM eclipse-temurin:17-jre

WORKDIR /app

# wget installieren und JAR herunterladen
RUN apt-get update && apt-get install -y wget && \
    wget -O app.jar https://github.com/wasilkum/hoymiles-mqtt-integration/releases/latest/download/app.jar

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
