#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
# === CONFIG ===
idle_dir = r"F:\EM-EdgeTrans\idle"
op_dir   = r"F:\EM-EdgeTrans\operational"
sample_type = np.complex64
fs = 2_400_000
trace_total_length = 2_400_000
trim_start = 200_000
middle_length = 2_000_000
num_traces_to_plot = 3  # Number of sample traces to visualize

# === LOAD FILES ===
def load_trimmed_psd(folder):
    filenames = sorted([f for f in os.listdir(folder) if f.endswith(".cfile")])
    psds = []
    for fname in filenames[:num_traces_to_plot]:
        full_path = os.path.join(folder, fname)
        trace = np.fromfile(full_path, dtype=sample_type)
        if len(trace) >= trace_total_length:
            trimmed = np.abs(trace[trim_start:trim_start + middle_length])
            f, Pxx = welch(trimmed, fs=fs, nperseg=1024)
            psd = 10 * np.log10(Pxx + 1e-12)
            psds.append((f, psd, fname))
    return psds, len(filenames)

# Load and count
idle_psds, idle_count = load_trimmed_psd(idle_dir)
op_psds, op_count = load_trimmed_psd(op_dir)

# === PLOT ===
plt.figure(figsize=(14, 6))

for i, (f, psd, fname) in enumerate(idle_psds):
    plt.subplot(2, num_traces_to_plot, i + 1)
    plt.plot(f / 1e6, psd, color='blue')
    plt.title(f"Idle: {fname}", fontsize=8)
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("PSD (dB/Hz)")
    plt.grid(True)

for i, (f, psd, fname) in enumerate(op_psds):
    plt.subplot(2, num_traces_to_plot, num_traces_to_plot + i + 1)
    plt.plot(f / 1e6, psd, color='green')
    plt.title(f"Operational: {fname}", fontsize=8)
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("PSD (dB/Hz)")
    plt.grid(True)

plt.tight_layout()
plt.savefig("idle_operational.png", dpi=300, bbox_inches="tight")
plt.show()


# In[3]:


import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# === CONFIG ===
dirs = {
    "Malicious": "F:/EM-EdgeTrans/malicious",
    "Malicious_CPU": "F:/EM-EdgeTrans/malicious_cpu"
}
colors = {
    "Malicious": "orange",
    "Malicious_CPU": "red"
}
sample_type = np.complex64
fs = 2_400_000
trace_total_length = 2_400_000
trim_start = 200_000
middle_length = 2_000_000
num_traces_to_plot = 3  # Number of traces per class

# === LOAD FILES ===
def load_trimmed_psd(folder):
    filenames = sorted([f for f in os.listdir(folder) if f.endswith(".cfile")])
    psds = []
    for fname in filenames[:num_traces_to_plot]:
        full_path = os.path.join(folder, fname)
        trace = np.fromfile(full_path, dtype=sample_type)
        if len(trace) >= trace_total_length:
            trimmed = np.abs(trace[trim_start:trim_start + middle_length])
            f, Pxx = welch(trimmed, fs=fs, nperseg=1024)
            psd = 10 * np.log10(Pxx + 1e-12)
            psds.append((f, psd, fname))
    return psds, len(filenames)

# === PLOT SETUP ===
plt.figure(figsize=(14, 6))
row_idx = 0

for label, folder in dirs.items():
    psds, count = load_trimmed_psd(folder)
    print(f"Total {label} traces: {count}")
    for i, (f, psd, fname) in enumerate(psds):
        plot_idx = row_idx * num_traces_to_plot + i + 1
        plt.subplot(len(dirs), num_traces_to_plot, plot_idx)
        plt.plot(f / 1e6, psd, color=colors[label])
        plt.title(f"{label}: {fname}", fontsize=8)
        plt.xlabel("Frequency (MHz)")
        plt.ylabel("PSD (dB/Hz)")
        plt.grid(True)
    row_idx += 1

plt.tight_layout()
plt.savefig("malicious_malicious_cpu.png", dpi=300, bbox_inches="tight")
plt.show()


# In[5]:


import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.ndimage import gaussian_filter1d

# === CONFIG ===
base_dirs = {
    "Idle": r"F:\EM-EdgeTrans\idle",
    "Operational": r"F:\EM-EdgeTrans\operational",
    "Malicious": r"F:\EM-EdgeTrans\malicious",
    "Malicious_cpu": r"F:\EM-EdgeTrans\malicious_cpu"
}
sample_type = np.complex64
trace_length = 2_400_000         
num_traces_to_average = 100      
fs = 2_400_000                   

colors = {
    "Idle": "blue",
    "Operational": "green",
    "Malicious": "red",
    "Malicious_cpu": "orange"
}

# === Function to compute PSD
def compute_psd(trace):
    f, Pxx = welch(trace, fs=fs, nperseg=1024)
    return f, 10 * np.log10(Pxx + 1e-12)

# === Combined PSD Plot
plt.figure(figsize=(7, 3))  

for label, folder in base_dirs.items():
    files = sorted([f for f in os.listdir(folder) if f.endswith(".cfile")])[:num_traces_to_average]
    psds = []

    for fname in files:
        full_path = os.path.join(folder, fname)
        trace = np.fromfile(full_path, dtype=sample_type)
        amplitude = np.abs(trace[:trace_length])
        f, psd = compute_psd(amplitude)
        psds.append(psd)

    psd_mean = np.mean(psds, axis=0)
    psd_smooth = gaussian_filter1d(psd_mean, sigma=2)

    plt.plot(f / 1e6, psd_smooth, label=f"{label}", color=colors[label])

plt.xlabel("Frequency (MHz)", fontsize=9)
plt.ylabel("PSD (dB/Hz)", fontsize=9)
plt.title("Average PSD Across 100 Traces per Activity", fontsize=10)
plt.grid(True, linewidth=0.3)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig("combined_psd_average_100.pdf", bbox_inches="tight")
plt.show()


# In[ ]:




