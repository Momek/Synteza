import PtBase
import PtAudio
import matplotlib.pyplot as plt
import numpy as np

print PtBase.DiphonBase.db['p+a'].show()
x= PtBase.DiphonBase.db['p+a'].wav
y= PtBase.DiphonBase.db['a+l'].wav
print PtBase.DiphonBase.db['a+l'].show()
z=PtBase.DiphonBase.db['l+_']
wave=0
wave = np.append(wave, x)
wave=np.append(wave,y)
#wave=np.append(wave,z)
Px = PtAudio.Play(10)
Px.run(wave)
# print len(x)
# print len(y)
# import matplotlib.pyplot as plt
# plt.plot(y)
# plt.show()