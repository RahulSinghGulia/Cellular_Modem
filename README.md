# 📶 Cellular Modem – 5G Communication System Simulator

This repository presents a comprehensive simulation framework for a **5G cellular modem**, built in Python. It includes modular implementations of key physical and network layer functionalities to **simulate, analyze, and evaluate** various aspects of 5G wireless communication.

---

## 🚀 Core Functionalities

### 🌀 Modulation & Demodulation
- Supports key 5G modulation schemes: **QPSK**, **16-QAM**, **64-QAM**, and **256-QAM**
- Simulates digital signal transmission and reception processes

### 📡 OFDM System Design
- Implements **Orthogonal Frequency Division Multiplexing (OFDM)**
- Includes IFFT/FFT operations, cyclic prefix addition/removal, and time-domain signal generation

### 🌐 Channel Modeling
- Simulates common wireless channels: **AWGN**, **Rayleigh**, and **Rician** fading
- Models **MIMO** channels for advanced antenna systems

### 🛡️ Channel Coding & Error Correction
- Implements modern error correction techniques such as **LDPC** and **Polar Codes**
- Includes noisy decoding simulation for performance evaluation

### ⚙️ Physical Layer Simulation
- Integrates modulation, OFDM, and channel modeling into a full PHY pipeline
- Simulates **Bit Error Rate (BER)** performance across varying **SNR** levels

### 📶 Beamforming & MIMO
- Supports **Massive MIMO** beamforming techniques
- Utilizes **Singular Value Decomposition (SVD)** for MIMO precoding and spatial multiplexing

### 📊 Resource Allocation & Scheduling
- Implements **dynamic scheduling** strategies for subcarriers and time slots
- Optimizes resource usage for multiple users under varying conditions

### 🛰️ Network Layer Functionality
- Models the **5G NR frame structure** and time-frequency resource grid
- Simulates **handover scenarios** between base stations for mobility testing

---

## 📁 Folder Structure (Coming Soon)
<pre><code>```plaintext modem_sim/ │ ├── main.py # Entry point for the simulation ├── config.py # Configuration of parameters (modulation, SNR, etc.) │ ├── transmitter/ │ ├── source_encoder.py # Converts input text/bits into bitstream │ ├── channel_encoder.py # Adds redundancy (e.g., convolutional, LDPC) │ ├── modulator.py # BPSK/QPSK/16-QAM/64-QAM/256-QAM modulation │ ├── pulse_shaping.py # (Optional) RRC filtering │ ├── channel/ │ ├── awgn.py # Adds AWGN noise │ ├── fading.py # Multipath Rayleigh or Rician fading │ ├── synchronization.py # Timing/frequency synchronization models │ ├── receiver/ │ ├── demodulator.py # Symbol demapping │ ├── channel_decoder.py # FEC decoding │ ├── source_decoder.py # Reconstructs original bitstream/text │ ├── utils/ │ ├── bit_operations.py # Bit-to-symbol conversions, SNR calculations │ ├── plotting.py # Eye diagrams, BER curves, constellations │ ├── metrics.py # BER, SER, PSNR computation │ └── test/ ├── test_chain.py # Unit tests or demo runs for each module ``` </code></pre>


