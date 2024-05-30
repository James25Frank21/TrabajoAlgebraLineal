import numpy as np
import matplotlib.pyplot as plt

v , r  =  0, 70
kp = 0.2
ki = 0.5
kd = 0
x = np.arange(0,10,0.1)
iota = 0.01
l = []
E = 0
eold = 0
for i in x:
    l.append(v)
    enew = r - v
    e_dot = enew - eold
    E += enew
    u = kp*enew  + ki*E +kd*e_dot
    eold = enew
    acel = u - iota*v
    v = v + acel
y = np.array(l)
plt.plot(x, y)
plt.show()


