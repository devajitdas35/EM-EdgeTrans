import time
import os
import csv
from datetime import datetime

OUTPUT_DIR = "F:/EM-EdgeTrans/malicious_cpu"
INDEX_FILE = "F:/EM-EdgeTrans/trace_index.csv"
NUM_TRACES = 100  # Changed from 200 to 100
WAIT_TIME = 10
DURATION = 1
ACTIVITY = "Malicious CPU Stress State"
LABEL = 3

os.makedirs(OUTPUT_DIR, exist_ok=True)

if not os.path.exists(INDEX_FILE):
    with open(INDEX_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["trace_id", "filename", "activity", "timestamp", "duration_sec", "label", "path"])

existing_ids = []
if os.path.exists(INDEX_FILE):
    with open(INDEX_FILE, mode='r') as f:
        reader = csv.DictReader(f)
        existing_ids = [int(row["trace_id"]) for row in reader]
start_id = max(existing_ids, default=0) + 1

for i in range(start_id, start_id + NUM_TRACES):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"trace_malicious_cpu_{timestamp}.cfile"
    filepath = os.path.join(OUTPUT_DIR, filename)

    print(f"[{i:03d}/100] Capturing malicious CPU trace: {filename}")
    os.system(f'python em_capture_script.py --output "{filepath}" --duration {DURATION}')

    with open(INDEX_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([i, filename, ACTIVITY, timestamp, DURATION, LABEL, filepath])

    time.sleep(WAIT_TIME)
