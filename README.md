# EM-EdgeTrans: Electromagnetic Side-Channel Dataset for Smart Transportation

EM-EdgeTrans is a labeled EM side-channel dataset captured from a Raspberry Pi 4B executing typical edge computing tasks in smart transportation settings. This dataset supports research in side-channel analysis, behavioral profiling, and lightweight intrusion detection.

## 📁 Dataset Structure
```
data/
├── idle/              # Idle EM traces
├── operational/       # Sensor + MQTT publish traces
├── malicious/         # MQTT flood attack traces
├── trace_index.csv    # Metadata for all traces
```

## ⚙️ Data Collection Setup
- **Device:** Raspberry Pi 4B (Broadcom BCM2711 Cortex-A72)
- **Sensor:** HC-SR04 (Ultrasonic)
- **EM Capture:** Near-field H-probe (9 kHz – 9 GHz)
- **Receiver:** RTL-SDR v3 + GNU Radio
- **Sampling Rate:** 2.048 MSPS, Center Freq: 100 MHz

## 📈 Included Scripts
- `scripts/`: For synchronized data capture and MQTT control
- `analysis/`: PSD visualization and preprocessing tools
- `meta_data.txt`: Class definitions and activity mapping

## 📄 Usage
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run analysis or training scripts as needed


## 🔗 Citation
To cite this dataset, please refer to the related journal paper (link coming soon).
