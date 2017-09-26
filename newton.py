import numpy as np
from divdiff import div_diff_class

# note! add function that addes new element to old ones
# div_diff_class contains value 


class div_diff_coefs:
    def __init__(self, x, f):
        self.coefs = np.array([div_diff_class(x[:i], f[:i]) for i in range(1, len(x)+1)])
        self.xgiven = x
    
    def __str__(self):
        return '\n'.join([str(c) for c in self.coefs])


class newton_poly:
    def __init__(self, x, coefs=0, x0=0, f0=0):
        self.f = coefs if coefs else div_diff_coefs(x0, f0)
        self.x = x
        self.image = np.array([self.get_newton_poly_value(x_i) for x_i in x])
        
    def get_newton_poly_value(self, x_i):
        result = (x_i - self.f.xgiven[-2])*self.f.coefs[-1].value
        n = len(self.x)
        for i in range(1, n):
            result = ( x_i - self.f.xgiven[n-1-i] ) * ( self.f.coefs[-i].value + result )
        return result+self.f.coefs[0].value
