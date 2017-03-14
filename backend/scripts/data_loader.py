import pandas as pd 
import numpy as np
import h5py
import math
import matplotlib.pyplot as plt
import scipy as sp
from scipy import io
import sys

def extents(f):     # rescale pixels, because they are not square on our plot
  delta = f[1] - f[0]
  return [f[0] - delta/2, f[-1] + delta/2]

if len(sys.argv) != 2:
	print ('Please specify one *.h5 file with data, for example d3data.h5')
	sys.exit(0)

fileName = sys.argv[1]
data_file = h5py.File(fileName, 'r')   # 'r' means that hdf5 file is open in read-only mode
dataStreams = data_file['DataStreams']

# Make it more general later
for stream in dataStreams:
	dataPath = 'DataStreams' + '/' + stream
	break

dataset = data_file[dataPath]

# If you wish to know about existing attributes
#for attr in dataset.attrs:
	#print attr

#scipy.io.savemat('d3.mat', dict(x=np.asarray(data_storage)))

# Reading metadata
nStart = float(dataset.attrs['RecordStartPoint'])
nEnd = float(dataset.attrs['RecordEndPoint'])
fp = float(dataset.attrs['Frequency'])
dl = float(dataset.attrs['MetersPerChannel'])

print('Record start point ' + str(nStart))
print('Record end point ' + str(nEnd))
print('Frequency ' + str(fp))
print('Meters per chanell ' + str(dl))

dataset = np.transpose(dataset)

print dataset.size
print dataset.shape
print dataset.dtype

NTmax = min(dataset.shape[0], 20000) # Split big files on 10-sec pieces
NLmax = dataset.shape[1]  			 # The length should remain the same

Nread = int(math.floor(dataset.shape[0]/NTmax))
NTleft = int(dataset.shape[0] - Nread*NTmax)

F = np.linspace(0, fp, num=NTmax)
L = np.linspace(nStart, nEnd, num=NLmax)


# Frequency borders for all filters
lowband = [2,  10] 
midband = [20, 40]
highband = [60, 100]

lowRange = np.round(np.interp(lowband, F, np.arange(NTmax)))
dNl = lowRange[1] - lowRange[0]
midRange = np.round(np.interp(midband, F, np.arange(NTmax)))
dNm = midRange[1] - midRange[0]
highRange = np.round(np.interp(highband, F, np.arange(NTmax)))
dNh = highRange[1] - highRange[0]
dN = max(dNl, dNm, dNh)
print 'NTmax', NTmax
print 'NLmax', NLmax
print 'NTleft', NTleft
print 'Nread', Nread

plt.hold(True)

lastImgLine = 0 # Remember last line, which was filled in Rrgb array.

for i in range(int(Nread)):
	if i == Nread - 1:
		R = np.double(dataset[(i) * NTmax:, 0:NLmax])
		T = np.arange((i) * NTmax, dataset.shape[0]) / fp
		F = np.linspace(0, fp, num=NTleft)
		lowRange = np.round(np.interp(lowband, F, np.arange(NTleft)))
		dNl = lowRange[1] - lowRange[0]
		midRange = np.round(np.interp(midband, F, np.arange(NTleft)))
		dNm = midRange[1] - midRange[0]
		highRange = np.round(np.interp(highband, F, np.arange(NTleft)))
		dNh = highRange[1] - highRange[0]
		dN = max(dNl, dNm, dNh)
	else:
		R = dataset[(i) * NTmax:(i + 1) * NTmax, 0:NLmax]
		T = np.arange((i) * NTmax, (i + 1) * NTmax) / fp

	S = sp.fft(R, axis=0)
	Rl = sp.ifft(S[int(lowRange[0]): int(lowRange[1]), :], n=int(dN), axis = 0)
	Rm = sp.ifft(S[int(midRange[0]): int(midRange[1]), :], n=int(dN), axis = 0)
	Rh = sp.ifft(S[int(highRange[0]): int(highRange[1]), :], n=int(dN), axis = 0)
	Tf = np.linspace(min(T), max(T), num=dN)  # Fix, now y axis is taken from the last cycle iteration.
	
	# RGB levels for filter visualization.
	# Numbers should be adjusted depending on the version of file: d3/d2.
	Red = 1 / 1e5
	Grn = 10 / 1e5
	Blu = 10 / 1e5
	if lastImgLine == 0:
		Rrgb = np.empty([Rh.shape[0], Rh.shape[1], 3])
	else:
		Rrgb = np.resize(Rrgb, (Rrgb.shape[0] + Rh.shape[0], Rh.shape[1], 3))

	print Rh.shape[0], Rh.shape[1]
	print Rrgb.shape
	Rrgb[lastImgLine:, :, 0] = np.absolute(Rl) * Red
	Rrgb[lastImgLine:, :, 1] = np.absolute(Rm) * Grn
	Rrgb[lastImgLine:, :, 2] = np.absolute(Rh) * Blu
	lastImgLine += Rh.shape[0]

plt.imshow(Rrgb, aspect='auto',  extent=extents(L / 1000) + extents(Tf), interpolation='none')#), origin='lower')
plt.savefig('waterfall.png')	
data_file.close()