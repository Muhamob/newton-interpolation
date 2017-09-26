import numpy as np
import matplotlib.pyplot as plt
import partitions as pt
import newton


def test_for_class_impl(start=0, stop=5, h=.13):
    x = pt.cheb(start, stop, int((stop-start)/h))
    f_x = lambda x: x*np.sin(x**2)
    f = f_x(x)
    #coefs = newton.div_diff_coefs(x, f)
    x_inter = np.arange(start+.1, stop-.01, h)
    f_interpol = newton.newton_poly(x_inter, x0 = x, f0 = f)
    plt.plot(x, f, label='true')
    plt.plot(x_inter, f_interpol.image, label='class')
    
    
  
test_for_class_impl()
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
