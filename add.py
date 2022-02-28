n=10 ###### input number of digits here ######

def dc(a,n):
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

def add(a,b):
    
    A=int(float(a))
    B=int(float(b))
    a=dc(a,n)[len(str(A)):]
    b=dc(b,n)[len(str(B)):]
    
    S=''
    t=0
    for i in range(n,0,-1):
        s=int(a[i])+int(b[i])+t
        t=int(s>9)
        S=str(s%10)+S
    
    return str(A+B+t)+'.'+S

'''
while 1:
    a,b=input().split()
    print(add(a,b))
'''
