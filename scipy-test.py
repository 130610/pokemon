from numpy import sin, linspace, pi
from pylab import plot, show, title, xlabel, ylabel, subplot
from scipy import fft, arange
from scipy.io import wavfile

def plotSpectrum(y,Fs):
 """
 Plots a Single-Sided Amplitude Spectrum of y(t)
 """
 n = len(y) # length of the signal
 k = arange(n)
 T = n/Fs
 frq = k/T # two sides frequency range
 frq = frq[range(n/2)] # one side frequency range

 Y = fft(y)/n # fft computing and normalization
 Y = Y[range(n/2)]
 
 plot(frq,abs(Y),'r') # plotting the spectrum
 xlabel('Freq (Hz)')
 ylabel('|Y(freq)|')

y = wavfile.read("test.wav")
sr = y[0]
ts = 1.0/sr
l = ts*len(y[1])
print sr
print ts
print l

t = arange(0, l, ts)

subplot(2,1,1)
plot(t,y[1])
xlabel('Time')
ylabel('Amplitude')
subplot(2,1,2)
plotSpectrum(y[1],sr)
show()
