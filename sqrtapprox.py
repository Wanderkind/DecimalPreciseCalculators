# clumsy!

n=400 ###### input number of digits here ######

def sqrtapprox(a):
    A=list(dc(a,n))
    A.remove('.')
    k=(len(A)-1)//2
    i=int(''.join(A))
    l=10**k
    r=10*l
    for _ in range(800):
        t=(l+r)//2
        if t*t>i:
            r=t
        else:
            l=t
    T=list(str(ndiv(t,10**(n//2))))
    return ''.join(T)

'''
from math import sqrt
while 1:
    a=input()
    print(sqrtapprox(a))
    print(sqrt(float(a)))
'''
