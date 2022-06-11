from cmath import sqrt
from math import sqrt as sqrt2


class QuadEq:
    def __init__(self,coeff_a,coeff_b,coeff_c):
        self.coeff_a = coeff_a
        self.coeff_b = coeff_b
        self.coeff_c = coeff_c

    def expression(self):
        print(str(self.coeff_a)+"x^2 + "+str(self.coeff_b)+"x + "+str(self.coeff_c)+" = 0")

    def solution(self):
        roots = []
        discr = self.coeff_b**2 - 4*self.coeff_a*self.coeff_c
        if discr >= 0:
            discr_sol = sqrt2(discr)
        else:
            discr_sol = sqrt(discr)
        
        roots.append((-self.coeff_b+discr_sol)/(2*self.coeff_a))
        roots.append((-self.coeff_b-discr_sol)/(2*self.coeff_a))
        return roots