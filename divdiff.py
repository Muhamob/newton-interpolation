
class div_diff_class:
    def __init__(self, x, f, value = 0):
        self.value = value if value else self.div_diff(x, f)
        self.n = len(x)
        
    def div_diff(self, x, f):
        if len(f) == 1: return f[0]
        sum = 0
        for i, value in enumerate(f):
            pi = 1
            for j in x:
                if x[i] == j : continue
                pi *= x[i] - j
            sum += value/ pi
        return sum

    def __str__(self):
        return 'f(x0...x{1}) = {0}'.format(self.value, self.n-1)