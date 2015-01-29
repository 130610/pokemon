from numpy import sin, linspace, pi, argmax, delete
from scipy import fft, arange
from scipy.io import wavfile

y = wavfile.read("test.wav")
sr = y[0]
y = y[1]
n = len(y) # length of the signal
T = float(n)/sr
k = arange(n)

#t = arange(0, l, ts)

freq = k/T # two sides frequency range
freq = freq[range(n/2)] # one side frequency range

spectrum = fft(y)/n # fft computing and normalization
spectrum =  spectrum[range(n/2)]
spectrum = abs(spectrum)

print freq[argmax(spectrum)]

#topvals = [] 
#
#for i in range(0,20):
#	topvals.append(argmax(spectrum) + i)
#	spectrum = delete(spectrum, argmax(spectrum))
#
#print topvals
