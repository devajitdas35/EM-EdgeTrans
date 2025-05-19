import paho.mqtt.client as mqtt
import os
import datetime
import csv

# === CONFIG ===
BROKER_IP = "192.168.0.10"
TOPIC = "smart/vehicle/ultrasonic_data"
OUTPUT_DIR = "F:/EM-EdgeTrans/operational"
INDEX_FILE = "F:/EM-EdgeTrans/trace_index.csv"
DURATION = 1  # seconds per trace
ACTIVITY = "Operational"
LABEL = 1
MAX_TRACES = 100  # limit to 100 total captures

os.makedirs(OUTPUT_DIR, exist_ok=True)

# === Initialize trace index if not present ===
if not os.path.exists(INDEX_FILE):
    with open(INDEX_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["trace_id", "filename", "activity", "timestamp", "duration_sec", "label"])

# === Load existing trace IDs ===
def get_next_trace_id():
    if not os.path.exists(INDEX_FILE):
        return 1
    with open(INDEX_FILE, mode='r') as f:
        reader = csv.DictReader(f)
        ids = [int(row["trace_id"]) for row in reader]
        return max(ids, default=0) + 1

# === Capture Counter ===
capture_count = 0

# === MQTT Callback ===
def on_message(client, userdata, msg):
    global capture_count

    if capture_count >= MAX_TRACES:
        print(f"[✓] Reached {MAX_TRACES} traces. Stopping listener.")
        client.disconnect()
        return

    trace_id = get_next_trace_id()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"trace_operational_{timestamp}.cfile"
    filepath = os.path.join(OUTPUT_DIR, filename)

    print(f"[{trace_id:03d}/{MAX_TRACES}] Capturing: {filename}")
    os.system(f'python em_capture_script.py --output "{filepath}" --duration {DURATION}')

    with open(INDEX_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([trace_id, filename, ACTIVITY, timestamp, DURATION, LABEL])

    capture_count += 1

# === MQTT Setup ===
client = mqtt.Client()
client.connect(BROKER_IP)
client.subscribe(TOPIC)
client.on_message = on_message

print(f"[*] Listening for MQTT messages on topic '{TOPIC}'...")
client.loop_forever()
