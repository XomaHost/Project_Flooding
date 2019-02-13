import numpy
import interpolation
import optimization
import flooding
import time
from matplotlib import pyplot

start_time = int(round(time.time() * 1000))

coef = 4
#data_in_y = numpy.random.rand(10*coef)*coef
#data_in_y = numpy.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.45, 0.37, 0.3, 0.2, 0.1])
data_in_y = numpy.array([0.25333755672135716, 0.09191943705452665, 3.6858318962991685, 3.841924713403265, 1.7287496035511016, 2.645662254264335, 1.3004685701279608, 1.6570892217112094, 0.5209757996785762, 1.0797032590219127, 0.8990589346291595, 1.2883778447593146, 2.418714272412915, 0.7075762489797373, 2.2117370456137353, 2.498012856891847, 3.1291040175279323, 1.4447830655258578, 2.472143374260919, 1.288990445550819, 2.4809196007171654, 3.6408199126341394, 0.5989716780060945, 3.453320046517728, 3.7886142842259005, 2.047322037646502, 3.8063475213327966, 1.1852492929737828, 1.405975628294886, 2.3546899876459553, 3.2090791736401, 3.665102812100728, 0.21303633351718876, 0.5665445913589728, 3.6650362786220665, 3.471896895918178, 2.631420885377288, 3.0180796166477095, 1.5430967072929378, 0.42851034193277115])


data_in_x = numpy.arange(0, numpy.size(data_in_y) * coef, 1 * coef)

print('data_in_y = numpy.array([', end='')
i = 0
while i < numpy.size(data_in_y)-1:
    print(f'{data_in_y[i]}, ', end='')
    i += 1
print(f'{data_in_y[i]}])')

interpolation_function = interpolation.scipy_rbf(data_in_x, data_in_y)
extreme = optimization.scipy_minimize(interpolation_function)

print(f'max = {extreme[1]}')
print(f'min = {extreme[0]}')

pyplot.plot(data_in_x, data_in_y, '.', markerfacecolor='black', markeredgecolor='black', markersize=7)
pyplot.plot(numpy.arange(data_in_x[0], data_in_x[-1], 0.01),
            interpolation_function[0](numpy.arange(data_in_x[0], data_in_x[-1], 0.01)))
pyplot.plot(extreme[0], interpolation_function[0](extreme[0]), 'xg')
pyplot.plot(extreme[1], interpolation_function[0](extreme[1]), 'xr')

flooding.standart_flooding(extreme, interpolation_function, v=2.2)
print(f'Your code like shit did the task in: {(int(round(time.time() * 1000)) - start_time)/1000:.2f} seconds')
pyplot.show()
print(f'end.')
