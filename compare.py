n=100 ###### input number of digits here ######

def dc(a,n):
    a=str(a)
    n=int(n)
    if '.' in a:
        p=n-len(a)+a.index('.')+1
        if p>0:
            a+='0'*p
        if p<0:
            a=a[:p]
    else:
        a+='.'+'0'*n
    return a

def compare(a, b): # is a greater than b?
    
    p = a.index('.')
    q = b.index('.')
    
    A = int(a[:p])
    B = int(b[:q])
    if A > B:
        return True
    if A < B:
        return False
    
    return int(dc(a, n)[p+1:]) > int(dc(b, n)[q+1:])
