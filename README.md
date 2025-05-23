# 📶 Cellular Modem – 5G Communication System Simulator

This repository presents a comprehensive simulation framework for a **5G cellular modem**, built in Python. It includes modular implementations of key physical and network layer functionalities to **simulate, analyze, and evaluate** various aspects of 5G wireless communication.

## 📁 Folder Structure 

- main.py                           # Entry point for the simulation

- config.py                         # Configuration of parameters (modulation, SNR, etc.)

- transmitter/
  - source_encoder.py             # Converts input text/bits into bitstream
  - channel_encoder.py            # Adds redundancy (e.g., LDPC, Polar codes)
  - modulator.py                  # BPSK/QPSK/16-QAM/64-QAM/256-QAM modulation
  - pulse_shaping.py              # (Optional) RRC filtering for pulse shaping

- channel/
  - awgn.py                       # Adds AWGN noise to the signal
  - fading.py                     # Simulates Rayleigh/Rician fading
  - synchronization.py           # Models timing and frequency synchronization

- receiver/
  - demodulator.py                # Demaps received symbols to bits
  - channel_decoder.py            # FEC decoding (LDPC/Polar)
  - source_decoder.py             # Reconstructs original input from bitstream

- utils/
  - bit_operations.py             # Bit-level conversions and SNR utilities
  - plotting.py                   # Eye diagrams, BER curves, constellations
  - metrics.py                    # BER, SER, PSNR computation tools

- test/
  - test_chain.py                 # Unit tests or demo simulations for each module
