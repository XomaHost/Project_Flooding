import sys
from scipy.optimize import minimize
from scipy.interpolate import Rbf, CubicSpline
from scipy import integrate
from matplotlib import pyplot as plt
import numpy as np
import time
a = time.time()
time.sleep(1)
print(f'{(time.time()-a)}')

"""
data_in_Y = np.random.rand(10)*3
#data_in_Y = np.array([1.14, 2.57, 1.80, 0.02, 0.28, 0.24, 1.23, 0.91, 0.58, 1.41])
#data_in_Y = np.array([0.17, 2.1, 2.62, 0.43, 0.72, 2.25, 1.02, 2.72, 1.53, 2.97])
#data_in_Y = np.array([2, 1.8, 1.6, 1.4, 1.2, 1, 1, 1.3, 1.6, 2])
#data_in_Y = np.array([2.79494186, 2.52382158, 1.20701306, 2.39743015, 2.62776144, 2.45370954, 0.50185104, 2.69531928, 1.80515071, 1.00869593])
#data_in_Y = np.array([2.91372804, 1.80949204, 2.10589421, 2.60137063, 2.10389632, 0.76131113, 2.48825884, 1.30512281, 1.36386196, 0.13620369])
#data_in_Y = np.array([2.91372804, 1.80949204, 2.10589421, 2.60137063, 2.10389632, 0.76131113, 2.48825884, 1.30512281, 1.36386196, 0.13620369])

N = np.size(data_in_Y)
data_in_X = np.arange(0, np.size(data_in_Y), 1)

print(f'y = {data_in_Y}')
print('([', end='')
for i in data_in_Y:
    print(f'{i}, ', end='')
print('])')

plt.figure('Main')
plt.plot(data_in_X, data_in_Y, '.', markerfacecolor='black', markeredgecolor='black', markersize=7)

dx = np.arange(data_in_X[0], data_in_X[np.size(data_in_X) - 1] + 0.1, 0.1)

spline = Rbf(data_in_X, data_in_Y)
plt.plot(dx, spline(dx), color='blue', linewidth=1, linestyle=':')
spline = Rbf(data_in_X, data_in_Y, function='inverse')
plt.plot(dx, spline(dx), color='green', linewidth=1, linestyle=':')
spline = Rbf(data_in_X, data_in_Y, function='gaussian')
plt.plot(dx, spline(dx), color='cyan', linewidth=1, linestyle=':')
spline = Rbf(data_in_X, data_in_Y, function='cubic')
plt.plot(dx, spline(dx), color='magenta', linewidth=1, linestyle=':')
spline = Rbf(data_in_X, data_in_Y, function='quintic')
plt.plot(dx, spline(dx), color='yellow', linewidth=1, linestyle=':')
spline = Rbf(data_in_X, data_in_Y, function='thin_plate')
plt.plot(dx, spline(dx), color='black', linewidth=1, linestyle=':')

spline = CubicSpline(data_in_X, data_in_Y)
plt.plot(dx, spline(dx), color='red', linewidth=1, linestyle='--')

plt.show()"""
"""
a = ['Mary', 'had', 'a', 'little', 'lamb']
i = 0
while i < len(a):
    print(i, a[i])
    if a[i] == 'a':
        a.remove(a[i])
        i -= 1
    i += 1


user_0 = {'username': 'Efermi', 'first': 'Enrico', "last": "Fermi"}
key = user_0.items()
"""