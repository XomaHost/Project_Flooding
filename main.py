import sys
import time
from scipy.optimize import minimize
from scipy.interpolate import CubicSpline
from scipy import integrate
from matplotlib import pyplot as plt
import numpy as np


data_in_Y = np.random.rand(10)*2
#data_in_Y = np.array([1.14, 2.57, 1.80, 0.02, 0.28, 0.24, 1.23, 0.91, 0.58, 1.41])
#data_in_Y = np.array([0.17, 2.1, 2.62, 0.43, 0.72, 2.25, 1.02, 2.72, 1.53, 2.97])
#data_in_Y = np.array([2, 1.8, 1.6, 1.4, 1.2, 1, 1, 1.3, 1.6, 2])
#data_in_Y = np.array([2.79494186, 2.52382158, 1.20701306, 2.39743015, 2.62776144, 2.45370954, 0.50185104, 2.69531928, 1.80515071, 1.00869593])
#data_in_Y = np.array([2.91372804, 1.80949204, 2.10589421, 2.60137063, 2.10389632, 0.76131113, 2.48825884, 1.30512281, 1.36386196, 0.13620369])


N = np.size(data_in_Y)
data_in_X = np.arange(0, np.size(data_in_Y), 1)

print(f'y = {data_in_Y}')
spline = CubicSpline(data_in_X, data_in_Y)
spline_reverse = CubicSpline(data_in_X, -data_in_Y)

plt.figure('Main')
dx = np.arange(data_in_X[0], data_in_X[np.size(data_in_X) - 1] + 0.1, 0.1)
plt.plot(data_in_X, data_in_Y, '.', markerfacecolor='black', markeredgecolor='black', markersize=7)
plt.plot(dx, spline(dx))

local_min = np.array([])
local_max = np.array([])

for i in data_in_X:
    temp = minimize(spline, i, method='L-BFGS-B', bounds=((np.min(data_in_X), np.max(data_in_X)),))
    local_min = np.append(local_min, temp.x)

    temp = minimize(spline_reverse, i, method='L-BFGS-B', bounds=((np.min(data_in_X), np.max(data_in_X)),))
    local_max = np.append(local_max, temp.x)

local_min = np.sort(local_min)
local_max = np.sort(local_max)
for i in range(np.size(local_min) - 2, -1, -1):
    if abs(local_min[i] - local_min[i + 1]) < 0.1:
        local_min = np.delete(local_min, i)

for i in range(np.size(local_max) - 2, -1, -1):
    if abs(local_max[i] - local_max[i + 1]) < 0.1:
        local_max = np.delete(local_max, i)

"""if local_min:
    print("Minimum not found")
    plt.plot()
    sys.exit()"""
while True:
    if local_min[np.size(local_min)-1] > local_max[np.size(local_max)-1]:
        local_min = np.delete(local_min, np.size(local_min)-1)
        continue
    if local_min[0] < local_max[0]:
        local_min = np.delete(local_min, 0)
        if np.size(local_min) == 0:
            print("Minimum not found")
            plt.plot()
            sys.exit()
        continue
    break
print(f'max = {local_max}')
print(f'min = {local_min}')

plt.plot(local_min, spline(local_min), 'xg')
plt.plot(local_max, spline(local_max), 'xr')

#=====
class Area:
    filled = False
    x_filling_left = float
    x_filling_right = float
    x_left_max = float
    x_right_max = float
    min = float
    S_fill = 0.0
    S_target = float

    def __init__(self, minimum, x_left_max, x_right_max, S):
        self.min = self.x_filling_left = self.x_filling_right = minimum
        self.x_left_max = x_left_max
        self.x_right_max = x_right_max
        self.S_target = S


def check(iterable):
    for element in iterable:
        if abs(element.S_target - element.S_fill) > precision_S:
            element.filled = False
        if not element.filled:
            return False
    return True

def square(x_left, x_right, spline):
    if abs(x_right - x_left) < 0.05:
        return (abs(area[i].x_filling_right - area[i].x_filling_left) + abs(x_right - x_left))*j*dh*0.5
    else:
        area[i].S_fill
        a = (spline(x_left) - spline(x_right)) / (x_left - x_right)
        #a = 0
        b = spline(x_right) - a * x_right
        def linear(x, a, b):
            return a * x + b
        return integrate.quad(linear, a=x_left, b=x_right, args=(a,b))[0] -\
               integrate.quad(spline, a=x_left, b=x_right)[0]


plt.show(block=False)
v = 0.5
dx_max = np.empty(0)
for i in range(0, np.size(local_max)-1, 1):
    dx_max = np.append(dx_max, local_max[i+1] - local_max[i])
S_target = dx_max * v
epsilon = 0.003*(np.max(local_max) - np.min(local_min))
precision_S = 0.02
area = np.array([Area(local_min[i], local_max[i], local_max[i+1], S_target[i]) for i in range(np.size(local_min))])
i = 0
while not check(area):
    if i >= np.size(area): i = 0
    dh = (np.max(local_max) - np.min(local_min))/200
    h = spline(area[i].x_filling_left)
    j = 1
    while True:
            h += dh

            x = x_left = area[i].x_filling_left
            if x <= area[i].x_left_max:
                    area[i].filled = True
            while x > area[i].x_left_max and not area[i].filled:
                if abs(spline(x) - h) <= abs(epsilon):
                    x_left = x
                    break
                else:
                    x -= epsilon/4
                if x <= area[i].x_left_max:
                    area[i].filled = True
                    area[i].x_filling_left = x_left = area[i].x_left_max
                    area[i].S_fill = square(x_left, x_right, spline)

                    """while abs(spline(area[i].x_filling_right) - spline(area[i].x_filling_left)) > abs(epsilon):
                        if spline(area[i].x_filling_right) > spline(area[i].x_filling_left):
                            area[i].x_filling_right -= epsilon/2
                        else:
                            area[i].x_filling_right += epsilon/2"""

                    if i == 0:
                        area[i].S_target -= (area[i].S_target - area[i].S_fill)
                        print('Void on the left')
                        continue
                    area[i-1].filled = False
                    area[i-1].S_target += (area[i].S_target - area[i].S_fill)
                    area[i].S_target -= (area[i].S_target - area[i].S_fill)
                    print('Overflow to the left')

            x = x_right = area[i].x_filling_right
            if x >= area[i].x_right_max:
                    area[i].filled = True
            while x < area[i].x_right_max and not area[i].filled:
                if abs(spline(x) - h) <= abs(epsilon):
                    x_right = x
                    break
                else:
                    x += epsilon/4
                if x >= area[i].x_right_max:
                    area[i].filled = True
                    area[i].x_filling_right = x_right = area[i].x_right_max
                    area[i].S_fill = square(x_left, x_right, spline)

                    #print(f'{spline.solve(spline(area[i].x_right_max))}')
                    """while abs(spline(area[i].x_filling_right) - spline(area[i].x_filling_left)) > abs(epsilon):
                        if spline(area[i].x_filling_left) > spline(area[i].x_filling_right):
                            area[i].x_filling_left += epsilon/2
                        else:
                            area[i].x_filling_left -= epsilon/2"""

                    if i == np.size(area)-1:
                        area[i].S_target -= (area[i].S_target - area[i].S_fill)
                        print('Void on the right')
                        continue
                    area[i+1].filled = False
                    area[i+1].S_target += (area[i].S_target - area[i].S_fill)
                    area[i].S_target -= (area[i].S_target - area[i].S_fill)
                    print('Overflow to the right')

            area[i].S_fill = square(x_left, x_right, spline)
            if abs(area[i].S_fill - area[i].S_target) < precision_S or area[i].filled:
                area[i].x_filling_right = x_right
                area[i].x_filling_left = x_left
                area[i].filled = True
                plt.plot([area[i].x_filling_left, area[i].x_filling_right],
                         [spline(area[i].x_filling_left),spline(area[i].x_filling_right)], 'k--')
                plt.draw()
                i += 1
                break
            elif abs(area[i].S_fill - area[i].S_target) > precision_S and area[i].S_fill > area[i].S_target:
                h -= dh
                dh /= 2
                j += 1
                continue
            elif abs(area[i].S_fill - area[i].S_target) >= precision_S and area[i].S_fill < area[i].S_target:
                area[i].x_filling_right = x_right
                area[i].x_filling_left = x_left
                plt.plot([area[i].x_filling_left, area[i].x_filling_right],
                         [spline(area[i].x_filling_left),spline(area[i].x_filling_right)], 'b--', linewidth=1)
                plt.draw()
                j += 1
                continue
    k = 0
    while k < np.size(area)-1:
        if area[k].x_filling_right == area[k+1].x_filling_left:
            area[k].x_filling_right = area[k+1].x_filling_right
            area[k].x_right_max = area[k+1].x_right_max
            area[k].S_target += area[k+1].S_target
            area = np.delete(area, k+1)
            print(f'{k+1} joining with {k}')
        k += 1


#=====
print('end?')
plt.show()
input('end.')

