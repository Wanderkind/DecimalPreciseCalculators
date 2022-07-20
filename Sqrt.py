n=400 ###### input number of digits here ######

from math import isqrt

def Sqrt(a):
    A=dc(a,2*n)
    p=A.index('.')
    P=p%2
    A=P*'0'+A
    u=t=0
    for I in range((p+P)//2):
        i=2*I
        r=int(A[i:i+2])+100*t
        z=-10*u+isqrt(100*u*u+r)
        t=r-(20*u+z)*z
        u=10*u+z
    U=str(u)
    for I in range(n):
        i=1+p+P+2*I
        r=int(A[i:i+2])+100*t
        z=-10*u+isqrt(100*u*u+r)
        t=r-(20*u+z)*z
        u=10*u+z
    return U+'.'+str(u)[len(U):]

'''
from math import sqrt
while 1:
    a=input()
    print(Sqrt(a))
    print(sqrt(float(a)))
'''
