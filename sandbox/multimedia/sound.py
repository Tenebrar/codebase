import wave

# Source: http://www.kozco.com/tech/soundtests.html
# Piano Trill, 48k/16, Little Endian, Stereo WAV 1.2MB
# 6.3 seconds. Seven piano notes. That's it.
# It's stereo, so left and right don't exactly match.
filename = '/Users/peter/Downloads/piano2.wav'

# https://docs.python.org/3/library/wave.html
with wave.open(filename, 'rb') as w:
    print(w.getnchannels())
    print(w.getsampwidth())
    print(w.getframerate())
    print(w.getnframes())
    print(w.getcomptype())
    print(w.getcompname())
    print(w.getnframes())
