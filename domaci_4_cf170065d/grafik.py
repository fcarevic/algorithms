import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
plt.figure()
x=np.arange(0,20,0.01)
y1=sp.spherical_jn(1,x)
y2=sp.spherical_jn(2,x)
plt.plot(x,y1,'b',label='J1 - First order Bessel')
plt.plot(x,y2,'r',label='J2 - Second order Bessel')
plt.grid()
plt.legend()
plt.show()
