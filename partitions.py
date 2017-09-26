import numpy as np


def cheb(a, b, n):
    # chebishev distribution
    # provides minimal error in newton interpolation
    return np.array([0.5*(a+b)+0.5*(b-a)*np.cos( (np.pi/2)*(2*k+1)/(n+1) ) for k in range(n)])


def uniform_distribution(a, b, n):
    # a and b are included
    return np.array([(a+(b-a)*k/n) for k in range(n+1)])