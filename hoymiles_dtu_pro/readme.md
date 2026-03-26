# Hoymiles DTU-Pro Modbus MQTT Bridge (Home Assistant Add-on)

Dieses Add-on liest eine Hoymiles DTU-Pro (ohne S!) per Modbus TCP aus
und veröffentlicht die Daten über MQTT.

## Konfiguration

- dtu_host: IP der DTU-Pro
- dtu_port: 502
- mqtt_host: core-mosquitto
- mqtt_user: MQTT Benutzer
- mqtt_password: MQTT Passwort

## Voraussetzungen

- MQTT Broker (z.B. Mosquitto)
- DTU-Pro im lokalen Netzwerk erreichbar
