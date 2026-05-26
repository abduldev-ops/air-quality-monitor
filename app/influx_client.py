from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from config import Config

client = InfluxDBClient(
                        url = Config.INFLUX_URL,
                        token = Config.INFLUX_TOKEN,
                        org = Config.INFLUX_ORG
                        )

write_api = client.write_api(write_options=SYNCHRONOUS)

def write_sensor_data(data:dict):
    point = (
        Point("air_quality_reading")
        .tag("node", "node1")
        .field("temperature", float(data["temperature"]))
        .field("pressure", float(data["pressure"]))
    )
    
    if "air_quality" in data:
        point = point.field("air_quality", float(data["air_quality"]))

    write_api.write(
    bucket = Config.INFLUX_BUCKET,
    org = Config.INFLUX_ORG,
    record = point)

    print(f"[InfluxDB] Written: {data}")
