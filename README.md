# EM-EdgeTrans: Electromagnetic Side-Channel Dataset for Smart Transportation

EM-EdgeTrans is a labeled EM side-channel dataset captured from a Raspberry Pi 4B executing typical edge computing tasks in smart transportation settings. This dataset supports research in side-channel analysis, behavioral profiling, and lightweight intrusion detection.

## 📁 Dataset Structure

```plaintext
EM-EdgeTrans/
├── Code/                              # Scripts for EM trace capture and analysis
│   ├── cpu_stress.py                  # Script to stress CPU for DoS simulation
│   ├── data_analysis.py               # PSD computation, visualization
│   ├── em_capture_script.py           # General capture handler
│   ├── idle_capture_loop.py           # Capture idle state traces
│   ├── operational_capture_loop.py    # Capture operational state (sensor + MQTT)
│   ├── malicious_capture_loop.py      # Capture MQTT flood attack traces
│   ├── malicious_cpu_capture_loop.py  # Capture CPU stress attack traces
│   ├── mqtt_flood.py                  # MQTT flooding tool
│   └── ultrasonic_sensor.py           # Sensor trigger script
│
├── Data/                              # Raw trace data and metadata
│   ├── idle/                          # 100 EM traces (idle state)
│   ├── operational/                   # 100 EM traces (sensor + MQTT)
│   ├── malicious/                     # 100 EM traces (MQTT flood)
│   ├── malicious_cpu/                 # 100 EM traces (CPU stress)
│   ├── trace_index.csv                # Metadata for all traces
│   └── 
│
├── README.md                          # Project overview and usage
└── capture_config.yaml            # SDR and capture configuration
```

---

## ⚙️ Data Collection Setup

- **Device**: Raspberry Pi 4B (Broadcom BCM2711 Cortex-A72)
- **Sensor**: HC-SR04 Ultrasonic Sensor
- **EM Probe**: Near-field magnetic probe (9 kHz – 9 GHz)
- **Receiver**: RTL-SDR v3 with GNU Radio
- **Sampling Rate**: 2.4 MSPS
- **Center Frequency**: 200 MHz
- **Trace Format**: `.cfile` with `complex64` IQ samples
- **Trace Length**: 2,400,000 samples (~1 second)

---

## 📈 Analysis & Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/devajitdas35/EM-EdgeTrans.git
   cd EM-EdgeTrans
   ```

2. Install dependencies:
   ```bash
   pip install -r Code/requirements.txt
   ```

3. Run analysis scripts:
   ```bash
   python Code/data_analysis.py
   ```

Each `.cfile` trace can be processed using Welch’s method for PSD, amplitude stats, or machine learning-based classification tasks. Example Jupyter notebooks are included for visual inspection and experiments.

---

## 🔬 Applications

- Side-channel leakage characterization
- Device behavior classification
- Lightweight intrusion detection
- Edge-based security monitoring

---
## 🔗 Citation
To cite this dataset, please refer to the related journal paper (link coming soon).
