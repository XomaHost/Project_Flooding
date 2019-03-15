import numpy
import interpolation
import optimization
import flooding
import time
from matplotlib import pyplot

start_time = int(round(time.time() * 1000))

coef = 1
v = 0.1
#data_in_y = numpy.random.rand(10*coef)*coef*2
#data_in_y = numpy.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.45, 0.37, 0.3, 0.2, 0.1])
data_in_y = numpy.array([1.1269689862619268, 1.5431244584800168, 0.8370225833975262, 0.5173791781536476, 1.1110267069859034, 1.0987147224051177, 0.07785358093265105, 0.38396909784135635, 1.8503065187093963, 1.4974254812592123])

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

main_graphic = pyplot.figure('Graphic')
main_graphic.subplots_adjust(left=0.07, right=0.96, top=0.95, bottom=0.05)
pyplot.plot(data_in_x, data_in_y, '.', markerfacecolor='black', markeredgecolor='black', markersize=7)
pyplot.plot(numpy.arange(data_in_x[0], data_in_x[-1], 0.01),
            interpolation_function[0](numpy.arange(data_in_x[0], data_in_x[-1], 0.01)))
pyplot.plot(extreme[0], interpolation_function[0](extreme[0]), 'xg')
pyplot.plot(extreme[1], interpolation_function[0](extreme[1]), 'xr')

areas = flooding.step_by_step_flooding(extreme, interpolation_function, v)

for i in areas:
    pyplot.plot([i.x_filling_left, i.x_filling_right],
                [interpolation_function[0](i.x_filling_left),
                 interpolation_function[0](i.x_filling_right)], 'b', linewidth=1)

    y2 = numpy.empty(0)
    for point in numpy.arange(i.x_filling_left, i.x_filling_right, 0.01):
        y2 = numpy.append(y2, interpolation_function[0](i.x_filling_left))
    pyplot.fill_between(numpy.arange(i.x_filling_left, i.x_filling_right, 0.01),
                        interpolation_function[0](numpy.arange(i.x_filling_left, i.x_filling_right, 0.01)),
                        y2,
                        color=(0, 0, 1), alpha=0.4)

print(f'Your code like shit did the task in: {(int(round(time.time() * 1000)) - start_time)/1000:.2f} seconds')
pyplot.show()
print(f'end.')
