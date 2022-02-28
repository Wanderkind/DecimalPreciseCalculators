def dc(a,n):
    n=int(n)
    if '.' in a:
        P=n-len(a)+a.index('.')+1
        if P>0:
            a+='0'*P
        if P<0:
            a=a[:P]
    else:
        a+='.'+'0'*n
    return a
