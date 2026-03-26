import time
import json
from pymodbus.client import ModbusTcpClient
import paho.mqtt.client as mqtt

DTU_IP = "192.168.178.98"
MQTT_HOST = "core-mosquitto"
MQTT_PORT = 1883

MQTT_TOPIC_STATE = "hoymiles/dtu/state"
MQTT_TOPIC_LIMIT_STATE = "hoymiles/dtu/state/power_limit"
MQTT_TOPIC_CMD = "hoymiles/dtu/cmd/power_limit"

client_modbus = ModbusTcpClient(DTU_IP)
client_mqtt = mqtt.Client()

def read_all_registers():
    rr = client_modbus.read_input_registers(30000, 100, unit=1)
    if rr.isError():
        return None
    return rr.registers

def read_power_limit():
    rr = client_modbus.read_holding_registers(40000, 1, unit=1)
    if rr.isError():
        return None
    return rr.registers[0] / 100.0  # zurück in Prozent

def set_power_limit(percent):
    value = int(percent * 100)
    rq = client_modbus.write_register(40000, value, unit=1)
    return not rq.isError()

def on_mqtt_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        if "limit" in payload:
            percent = payload["limit"]
            if 0 <= percent <= 100:
                ok = set_power_limit(percent)
                print("Set power limit:", percent, "% →", ok)
    except Exception as e:
        print("MQTT command error:", e)

def main():
    client_mqtt.on_message = on_mqtt_message
    client_mqtt.connect(MQTT_HOST, MQTT_PORT, 60)
    client_mqtt.subscribe(MQTT_TOPIC_CMD)
    client_mqtt.loop_start()

    while True:
        if not client_modbus.connect():
            print("Modbus connection failed")
            time.sleep(5)
            continue

        # Register lesen
        data = read_all_registers()
        if data:
            payload = json.dumps({"registers": data})
            client_mqtt.publish(MQTT_TOPIC_STATE, payload)

        # Leistungsbegrenzung lesen
        limit = read_power_limit()
        if limit is not None:
            client_mqtt.publish(MQTT_TOPIC_LIMIT_STATE, json.dumps({"limit": limit}))
            print("Current limit:", limit)

        time.sleep(5)

if __name__ == "__main__":
    main()
