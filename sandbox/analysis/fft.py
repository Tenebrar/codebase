import numpy as np
import matplotlib.pyplot as plt

t = np.arange(256)  # [0..255]
sp = np.fft.fft(np.sin(t))

print(sp.real)

freq = np.fft.fftfreq(t.shape[-1])

print(freq)

plt.plot(freq, sp.real, freq, sp.imag)
# plt.show()

# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html#Three-dimensional-Contour-Plots
