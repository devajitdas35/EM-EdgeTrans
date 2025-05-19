import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import json
from datetime import datetime

# MQTT Configuration
broker_ip = "192.168.0.10"
mqtt_topic = "smart/vehicle/ultrasonic_data"

# Setup GPIO pins
TRIG = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# MQTT Client Setup
client = mqtt.Client()
client.connect(broker_ip, 1883, 60)

def read_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    timeout = pulse_start + 0.04
    while GPIO.input(ECHO) == 0 and time.time() < timeout:
        pulse_start = time.time()

    pulse_end = time.time()
    timeout = pulse_end + 0.04
    while GPIO.input(ECHO) == 1 and time.time() < timeout:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    # Filter out invalid high distance readings
    if distance > 400 or distance <= 0:
        return None
    return distance

try:
    while True:
        distance_cm = read_distance()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if distance_cm is not None:
            payload = {
                "timestamp": timestamp,
                "distance_cm": distance_cm
            }
            client.publish(mqtt_topic, json.dumps(payload))
            print(f"[{timestamp}] Published Distance: {distance_cm} cm")
        else:
            print(f"[{timestamp}] Invalid distance reading skipped.")

        time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Stopped.")
