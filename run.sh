#!/usr/bin/env bashio

DTU_HOST=$(bashio::config 'dtu_host')
DTU_PORT=$(bashio::config 'dtu_port')
MQTT_HOST=$(bashio::config 'mqtt_host')
MQTT_USER=$(bashio::config 'mqtt_user')
MQTT_PASSWORD=$(bashio::config 'mqtt_password')

echo "Starting Hoymiles DTU-Pro Modbus MQTT Bridge..."
echo "DTU: $DTU_HOST:$DTU_PORT"
echo "MQTT: $MQTT_HOST"

exec java -jar /app/app.jar \
  --dtu.host=$DTU_HOST \
  --dtu.port=$DTU_PORT \
  --mqtt.host=$MQTT_HOST \
  --mqtt.user=$MQTT_USER \
  --mqtt.password=$MQTT_PASSWORD
