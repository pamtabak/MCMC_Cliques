import numpy as np

def exponential(T_0, t, params_dict):
    return T_0 * np.power(params_dict['beta'], t)

def linear(T_0, t, params_dict):
    return T_0 - params_dict['beta'] * t

def logarithmic(T_0, t, params_dict):
    return params_dict['a'] / np.log(t + params_dict['b'])
