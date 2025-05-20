# EM-EdgeTrans: Electromagnetic Side-Channel Dataset for Smart Transportation

**EM-EdgeTrans** is a labeled electromagnetic (EM) side-channel dataset captured from a Raspberry Pi 4B simulating real-world edge computing tasks in the context of smart transportation systems. This dataset supports research in side-channel analysis, behavioral profiling, and lightweight intrusion detection at the edge.

---

## 📁 Dataset Structure

```plaintext
EM-EdgeTrans/
├── Code/                              # Scripts for EM trace capture and analysis
│   ├── cpu_stress.py                  # Script to stress CPU for DoS simulation
│   ├── data_analysis.py               # PSD computation, visualization, ML
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
│   └── capture_config.yaml            # SDR and capture configuration
│
├── README.md                          # Project overview and usage
└── LICENSE                            # Dataset or code license
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

> Devajit Das, *EM-EdgeTrans: A Dataset for Electromagnetic Side-Channel Analysis on Edge Devices*, Frontiers of Computer Science, 2025 (Under Review).

---

## 📜 License

- **Code**: MIT License
- **Dataset**: CC BY 4.0 International

Please attribute the dataset if used in research or derivative work.

