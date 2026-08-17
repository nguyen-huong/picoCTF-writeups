import numpy as np
import wave
import matplotlib.pyplot as plt
from scipy import signal


with wave.open('mk.wav', 'rb') as wav:
    framerate = wav.getframerate()
    frames = wav.readframes(wav.getnframes())

samples = np.frombuffer(frames,dtype=np.int16).astype(float)
f,t,Sxx =signal.spectrogram(samples, fs=framerate,nperseg=2048,noverlap=1792)
Sxx_db =10*np.log10(Sxx + 1e-10)

plt.figure(figsize=(20,6))
plt.pcolormesh(t,f, Sxx_db, shading='gouraud', cmap='inferno')
plt.ylim(0,24000)
plt.title('mk.wav spectrogram')
plt.ylabel('frequency hz')
plt.xlabel('time in s')
plt.tight_layout()
plt.savefig('spectrogram.png', dpi=120)
