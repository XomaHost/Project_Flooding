from scipy.interpolate import Rbf


def scipy_rbf(data_in_x, data_in_y):
    spline = Rbf(data_in_x, data_in_y)
    spline_reverse = Rbf(data_in_x, -data_in_y)
    return spline, spline_reverse

