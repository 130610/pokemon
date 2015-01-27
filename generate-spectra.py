from numpy import sin, linspace, pi
from scipy import fft, arange
from scipy.io import wavfile

y = wavfile.read("WAV-651/143.wav")
sr = y[0]
y = y[1]
ts = 1.0/sr
l = ts*len(y)

t = arange(0, l, ts)

n = len(y) # length of the signal
spectrum = fft(y)/n # fft computing and normalization
spectrum =  spectrum[range(n/2)]
