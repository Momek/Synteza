import PtBase
import PtAudio
import matplotlib.pyplot as plt
import numpy as np


lista = ['_+t', 't+e','e+m', 'm+_', '_+p', 'p+e','e+r', 'r+a','a+_','_+t','t+u','u+r','r+a','_+w','w+y','y+_','_+s',
's+_','_+t','t+o','o+_','_+p','p+n','n+i','i+a','a+h','h+_','_+c','c+e','e+l','l+s','s+j','j+u','u+_','_+sz','sz+a','a+_',
'_+w','w+y','y+n','n+o','o+si','si+i','i+_']

wave = 0
for l in lista:
    wave = np.append(wave, PtBase.DiphonBase.db[l].wav)

#wave = PtBase.DiphonBase.db['t+e'].wav

Px = PtAudio.Play(10)
Px.run(wave)