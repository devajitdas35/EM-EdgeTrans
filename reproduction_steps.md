# Reproduction Steps for EM-EdgeTrans Dataset

## Hardware Setup
1. Place a near-field H-probe near the Raspberry Pi 4B's CPU.
2. Connect the H-probe to an RTL-SDR v3 USB receiver.
3. Connect the RTL-SDR to a host PC running GNU Radio.

## Software Setup
1. Install Python 3.8+ and pip
2. Install dependencies:
   pip install -r requirements.txt

## Data Collection
1. Run `idle_capture_loop.py` to collect idle traces.
2. Run `em_capture_trigger.py` to capture traces during MQTT-based sensor transmission.
3. Run `malicious_capture_loop.py` while executing MQTT flooding on the Pi to capture malicious traces.
4. Each trace will be stored in `.cfile` format under its respective class folder (idle, operational, malicious).
5. Traces are automatically indexed in `trace_index.csv`.

## Data Analysis
1. Run `preprocess_em_traces.py` to convert raw `.cfile` to numpy arrays (`X.npy`, `y.npy`).
2. Run `plot_psd_combined.py` or `enhanced_psd_analysis.py` to generate Power Spectral Density plots.
3. Use baseline ML models in `models/` to evaluate classification performance (optional).

## Output
- All results and figures will be saved as `.pdf` or `.npy` in the respective folders.
- Each `.cfile` is approximately 16 MB (1 sec, 2.048 MSPS, complex64).
