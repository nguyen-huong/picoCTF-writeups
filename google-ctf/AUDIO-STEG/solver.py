import numpy as np
import wave

with wave.open('mk.wav', 'rb') as wav:
    frames = wav.readframes(wav.getnframes())

raw_bytes = np.frombuffer(frames, dtype=np.uint8)
byte_lsb=raw_bytes & 1
results = []
for i in range(0, len(byte_lsb)-7,8):
    byte = 0
    for j in range(8):
        byte = (byte << 1) | int(byte_lsb[i+j])
    results.append(byte)

data = bytes(results)
print(data[4:100])