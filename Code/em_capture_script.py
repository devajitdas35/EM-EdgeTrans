import argparse
import time
import numpy as np
from rtlsdr import RtlSdr

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=str, required=True)
    parser.add_argument('--duration', type=float, default=1.0)
    args = parser.parse_args()

    sdr = RtlSdr()
    sdr.sample_rate = 2.4e6
    sdr.center_freq = 150e6
    sdr.gain = 38.6

    num_samples = int(sdr.sample_rate * args.duration)
    print(f"[+] Capturing {args.duration}s of data to {args.output}...")
    samples = sdr.read_samples(num_samples)
    samples.astype('complex64').tofile(args.output)
    sdr.close()
    print("[+] Capture complete.")

if __name__ == "__main__":
    main()
