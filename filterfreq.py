import numpy as np
import scipy.optimize as opt
import scipy.stats as st
import math
import matplotlib.pyplot as plt
from scipy import fftpack

#Curve fit representing 420, 640, 980Hz sine waves combined
#by reading and opening CSV file for data:
with open("combined_Output_mono.csv","r") as f: 
    print(f.readline())
    print(f.readline())
    f.close()
L=[] # time
R=[] # amplitude
with open("combined_Output_mono.csv","r") as f:
    f.readline()  #first line of CSV file does not contain needed data, so it is taken out
    for l in f:
        l.strip()
        things=l.split(",")
        L.append(float(things[0]))
        R.append(float(things[1]))
    f.close()
print(L[:5])
print(R[:5])
L = np.array(L)
R = np.array(R)
# Fig.1
# Plot combined signal in time domain
plt.plot(L,R)
plt.xlim([0,500]) #adjust x axis here for visibility
plt.ylim([-40000,40000]) #adjust y axis
plt.title('Combined frequencies')
plt.grid()
plt.show()

sig = R #amplitude
time_step = 1/44100 #1/sample rate
period = 5.
time_vec = L #time

# The FFT of the signal
sig_fft = fftpack.fft(sig)

# And the power (sig_fft is of complex dtype)
power = np.abs(sig_fft)**2

# The corresponding frequencies
sample_freq = fftpack.fftfreq(sig.size, d=time_step)

# Fig.2
# Plot the FFT power of combined signals
plt.figure(figsize=(6, 5))
plt.plot(sample_freq, power)
plt.xlabel('Frequency [Hz]')
plt.ylabel('power')
plt.xlim([-2000,5000])

# Find the peak frequency: we can focus on only the positive frequencies
pos_mask = np.where(sample_freq > 0)
freqs = sample_freq[pos_mask]
peak_freq = freqs[power[pos_mask].argmax()]

# Check that it does indeed correspond to the frequency that we generate
# the signal with
np.allclose(peak_freq, 1./period)

# Inside Fig.2
# An inner plot to show the peak frequency
axes = plt.axes([0.55, 0.3, 0.3, 0.5])
plt.title('Peak frequency')
plt.plot(freqs[:8], power[:8])
plt.setp(axes, yticks=[])

# scipy.signal.find_peaks_cwt can also be used for more advanced
# peak detection

# removing high freqs 980 Hz & 640Hz
high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
filtered_sig = fftpack.ifft(high_freq_fft)

# Fig.3
# Plot filtered signal with original signal back in time domain.
plt.figure(figsize=(6, 5))
plt.plot(time_vec, sig, label='Original signal')
plt.plot(time_vec, filtered_sig, linewidth=3, label='Filtered signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.xlim([0,500]) #adjust x axis here for visibility
plt.ylim([-40000,40000]) #adjust y axis

plt.legend(loc='best')

# Double check: re-compute and plot power
# the fft of signal
sig_fft1 = fftpack.fft(filtered_sig)

# power (sig_fft is of complex dtype)
power = np.abs(sig_fft1)**2

# corresponding frequencies
sample_freq = fftpack.fftfreq(filtered_sig.size, d=time_step)

# Fig.4
# Plot FFT power of filtered signal
plt.figure(figsize=(6, 5))
plt.plot(sample_freq, power)
plt.xlabel('Frequency [Hz]')
plt.ylabel('power')
plt.xlim([-1000,1000]) # x axis