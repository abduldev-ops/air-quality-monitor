import json
import ssl
import paho.mqtt.client as mqtt
from config import Config
from app.influx_client import write_sensor_data

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[MQTT] Connected. Subscribing to {Config.MQTT_TOPIC}")
        client.subscribe(Config.MQTT_TOPIC)
    else:
        print(f"[MQTT] Connection failed with code {rc}")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode("utf-8"))
        print(f"[MQTT] Received: {payload}")
        write_sensor_data(payload)
    except json.JSONDecodeError as e:
        print(f"[MQTT] Could not parse JSON: {e}")
    except Exception as e:
        print(f"[MQTT] Error processing message: {e}")

def start_mqtt():
    client  =mqtt.Client()
    client.username_pw_set(Config.MQTT_USERNAME, Config.MQTT_PASSWORD)
    client.tls_set(tls_version=ssl.PROTOCOL_TLS)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(Config.MQTT_BROKER, Config.MQTT_PORT, keepalive=60)
    client.loop_start()
    return client