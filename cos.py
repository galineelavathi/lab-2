import numpy as np
import matplotlib.pyplot as mp
t=np.arange(0,10,0.03)
x1=np.cos(2*t*np.pi)
mp.plot(t,x1)
mp.title('sine wave')
mp.xlabel('time')
mp.ylabel('amplitude')
mp.show( )