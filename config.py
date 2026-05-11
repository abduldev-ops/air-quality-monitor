import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MQTT_BROKER = os.getenv("MQTT_BROKER")
    MQTT_PORT = int(os.getenv("MQTT_PORT, 8883"))
    MQTT_USERNAME = os.getenv("MQTT_USERNAME")
    MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")
    MQTT_TOPIC = os.getenv("MQTT_TOPIC", "airquality/node1")

    INFLUX_URL = os.getenv("INFLUX_URL")
    INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")
    INFLUX_ORG = os.getenv("INFLUX_ORG")
    INFLUX_BUCKET = os.get_env("INFLUX_BUCKET", "air_quality")
