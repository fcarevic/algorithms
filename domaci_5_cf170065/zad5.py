import numpy as np
import scipy.optimize as so
import math as math
import matplotlib.pyplot as plot
def yout_f(win,x):
    w15 = win[0:5]
    w610 = win[5:10]
    hidden_output = [math.tanh(x * w) for w in w15]
    return  math.tanh(math.fsum([a * b for a, b in zip(hidden_output, w610)]))


def cost_f(win):
   if(max([math.fabs(w) for w in win])>10):
        return 1000000
   xin=np.arange(-1,1.1,0.1)
   result_array=[]
   for x in xin:
       yout = yout_f(win,x)
       expected_y= 0.5*math.sin(math.pi*x)
       result_array.append(math.pow(yout-expected_y,2))
   return math.sqrt(math.fsum(result_array))


while True:
    starting_point = np.random.uniform(low=-10, high=10, size=10)
    result = so.minimize(cost_f, starting_point, method="Nelder-Mead", options={'xtol':1e-15 , 'ftol':1e-8, 'maxfev':1e14, 'disp':True})
    if result.fun <= 1e-2:
        break
result_w=result.x
x=np.arange(-1,1.1,0.1)
y_t=[yout_f(result_w,x_) for x_ in x]
y = [0.5*math.sin(math.pi*x_) for x_ in x]
print(result)
for w in result_w:
    print('{:.15f}'.format(w))

plot.figure()
plot.grid()
plot.plot(x,y_t,"ro",label="Trained")
plot.plot(x,y,"b", label="Original")
plot.legend()
plot.show()

