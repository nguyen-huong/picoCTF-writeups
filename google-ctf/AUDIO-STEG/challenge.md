# Check if it's actually an audio file (unsuccessful strings too)
```
file mk.wav
mk.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 48000 Hz
```
# Where to hide data
most of the times, hackers hide it using LSB (least significant bit), where each audio sample is stored as 2 bytes. Changing and manipulating audio sample using LSB produces no sound differences. Another method is hiding it thru the frequency domain of the audio. Graphing the spectrogram can help to visualize and see the text. 

# What worked
I Googled around for some help, and was able to find a script that does simple byte LSB encoding, and this helps me find the flag
```
b'CTF{THAT_WAS_EASY_AS_SUBZEROS_FATALITY}\n\xe2\xa9\x7f\x88\xf5\xa3\xf8=\x89\xda\x9c\xf4\x83\xddh\x80\xaa\x97V\t\xfa\x1d\xa9\xe8u\x89w\xe2\xaa\xa5v\x05\xc1A\x0f2\xc9\x84\xfb\xc5>\x94>\x07J\xa1\xd5\xf7h\x00_r\x00\xaa\x88\xa2'
```

