from numpy import sin, linspace, pi, argmax, delete
from scipy import fft, arange
from scipy.io import wavfile

def findMaxFreqs(data, sampleRate, numFreqs=30):
	'''
	returns list of lists of index, frequency, and level for each of the most preset frequencies
	'''
	dataLength = len(data) # length of the signal
	dataTime = float(dataLength)/sampleRate
	k = arange(dataLength)
	freqArr = k/dataTime # two sides frequency range
	freqArr = freqArr[range(dataLength/2)] # one side frequency range
	spectrum = fft(data)/dataLength # fft computing and normalization
	spectrum =  spectrum[range(dataLength/2)]
	spectrum = abs(spectrum)
	spectrum[0] = 0

	topFreqs = []

	for i in range(numFreqs):
		topFreqs.append([argmax(spectrum), freqArr[argmax(spectrum)], spectrum[argmax(spectrum)]])
		spectrum[argmax(spectrum)] = 0
	return topFreqs

def condenseFreqs(data, percentDiff):
	'''
	takes the 2d list from findMaxFreqs, and condenses entries with similar frequencies into single
	entries. Returns the same format of 2d list, but shorter
	'''
	topFreqs = []
	topFreqs.append(data[0])

	for i in range(1,len(data)):
		for j in range(len(topFreqs)):
			if abs(topFreqs[j][1] - data[i][1]) < topFreqs[j][1] * percentDiff / 100:
				topFreqs[j][2] += data[i][2]
				break
		else:
			topFreqs.append(data[i])

	topFreqs.sort(key=lambda x: x[2], reverse=True)
	return topFreqs

y = wavfile.read("WAV-651/002.wav")
print condenseFreqs(findMaxFreqs(y[1], y[0], 100), 5)[:4]
