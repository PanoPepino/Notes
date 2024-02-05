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
my_colors = {"red" : "#9b0808",
            "green" : "#006111",
            "blue":"#0051CF",
            "white": "#FFF5F0"}

plt.figure()
plt.plot(x, y_r, color=my_colors['red'], marker='.',  markersize = 0.5, linewidth = 0,label = 'Radiation')
plt.plot(x, y_m, color=my_colors['green'], marker='.', markersize = 0.5, linewidth = 0, label = 'Matter')
plt.plot(x, y_d, color=my_colors['blue'], marker='.', markersize = 0.5, linewidth = 0, label = 'Dark energy')
plt.axis

#plt.xlabel('log (a)')
#plt.ylabel('log (\u03C1)')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xticks([])
plt.yticks([])
plt.savefig('Svgs/densities.svg', dpi = 300)