import math

n=10 ###### input number of digits here ######

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

def flr(x):
    if '.' in x:
        x=str(x)
        return x[:x.index('.')]
    else:
        return x

def add(a,b):
    a=str(a)
    b=str(b)
    l=list(str(int(dc(a,n).replace('.',''))+int(dc(b,n).replace('.',''))).zfill(n+1))
    l.insert(-n,'.')
    if l[0]+l[1]=='-.':
        l[1]='0.'
    return ''.join(l)

def sub(a,b):
    a=str(a)
    b=str(b)
    l=list(str(int(dc(a,n).replace('.',''))-int(dc(b,n).replace('.',''))).zfill(n+1))
    l.insert(-n,'.')
    if l[0]+l[1]=='-.':
        l[1]='0.'
    return ''.join(l)

def mul(a,b):
    a=str(a)
    b=str(b)
    l=list(str(int(dc(a,n).replace('.',''))*int(dc(b,n).replace('.',''))).zfill(2*n+1))[:-n]
    l.insert(-n,'.')
    if l[0]+l[1]=='-.':
        l[1]='0.'
    return ''.join(l)

def exp(x,n):
    y=x
    for i in range(int(n)-1):
        y=mul(y,x)
    return y

def ndiv(A,q):
    a=list(str(A))
    b=flr(str(q))
    B=len(b)
    
    if '.' in a:
        p=len(a)-a.index('.')-1
        a.remove('.')
        c=len(a)
    else:
        p=0
        c=len(a)
    
    a+=['0']*(n+B-p)
    if c-p>=B:
        l=[]
        for i in range(len(a)-B):
            s=''
            u=int(i>0)
            for j in range(-u,B):
                s+=a[i+j]
            l+=[str(int(s)//int(b))]
            z=str(int(s)%int(b)).zfill(B+u)
            for j in range(-u,B):
                a[i+j]=z[j+u]
        l.insert(c-p-B+1,'.')
    else:
        l=['0','.']+['0']*(p+B-c-1)
        for i in range(len(a)-B):
            s=''
            u=int(i>0)
            for j in range(-u,B):
                s+=a[i+j]
            l+=[str(int(s)//int(b))]
            z=str(int(s)%int(b)).zfill(B+u)
            for j in range(-u,B):
                a[i+j]=z[j+u]
    
    while 1:
        if l[0]=='0' and l[1]!='.':
            del l[0]
        else:
            break
    
    return ''.join(l[:l.index('.')+1+n])

def sin(x):
    x=str(x)
    y=0;z='';i=0
    while 1:
        y=add(y,mul(ndiv(exp(x,2*i+1),math.factorial(2*i+1)),(-1)**i))
        if z==y:
            break
        z=y
        i+=1
    return y