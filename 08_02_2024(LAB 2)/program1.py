import matplotlib.pyplot as pyt
import sympy as syms
import numpy as np
import math

ht = 5
hr = 3
f = 900*1000000
l = 3*100000000
l = l/f
k = 2*np.pi/l
E0 = 1
# d = 400
# d = syms.Rational(0.1, 10000)
d = np.linspace(0.1, 2000, 10000)

d1 = np.sqrt(np.square(ht - hr) + np.square(d))
d2 = np.sqrt(np.square(d) + np.square(ht + hr))

Etotal = (E0 * np.exp(-1j*d1*k))/d1 + (E0 * np.exp(-1j*d2*k))/d2
Etotal_abs = abs(Etotal)
pyt.plot(d,Etotal_abs)
pyt.show()

pyt.loglog(d, Etotal_abs)
pyt.show()
