import time
import os
import csv
from datetime import datetime

OUTPUT_DIR = "F:/EM-EdgeTrans/idle"
INDEX_FILE = "F:/EM-EdgeTrans/trace_index.csv"
NUM_TRACES = 100
WAIT_TIME = 10  # seconds between captures
DURATION = 1  # capture duration in seconds
ACTIVITY = "Idle"
LABEL = 0

# Ensure output and index directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize trace index if not present
if not os.path.exists(INDEX_FILE):
    with open(INDEX_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["trace_id", "filename", "activity", "timestamp", "duration_sec", "label"])

# Load last trace_id if index exists
existing_ids = []
if os.path.exists(INDEX_FILE):
    with open(INDEX_FILE, mode='r') as f:
        reader = csv.DictReader(f)
        existing_ids = [int(row["trace_id"]) for row in reader]
start_id = max(existing_ids, default=0) + 1

# Start capturing
for i in range(start_id, start_id + NUM_TRACES):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"trace_idle_{timestamp}.cfile"
    filepath = os.path.join(OUTPUT_DIR, filename)

    print(f"[{i:03d}/100] Capturing idle trace: {filename}")
    os.system(f'python em_capture_script.py --output "{filepath}" --duration {DURATION}')

    # Append entry to trace_index.csv
    with open(INDEX_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([i, filename, ACTIVITY, timestamp, DURATION, LABEL])

    time.sleep(WAIT_TIME)
