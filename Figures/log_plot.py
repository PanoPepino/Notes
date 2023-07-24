import numpy as np
import matplotlib.pyplot as plt
import unicodedata as ud

def radiation(x):
    return 10/x**4

def matter(x):
    return 10/x**3

def dark_energy():
    return 10/x**2

x = np.linspace(-10, 10, 10000)
y_r = radiation(x)
y_m = matter(x)
y_d = dark_energy()
y_d = np.ones(10000)

plt.figure()
plt.plot(x, y_r, 'r.', markersize = 0.5, label = 'Radiation')
plt.plot(x, y_m, 'g.', markersize = 0.5,label = 'Matter')
plt.plot(x, y_d, 'b.', markersize = 0.5,label = 'Dark energy')
plt.axis

#plt.xlabel('log (a)')
#plt.ylabel('log (\u03C1)')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xticks([])
plt.yticks([])
plt.savefig('Svgs/densities.png')