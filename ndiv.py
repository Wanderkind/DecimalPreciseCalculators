n=10 ###### input number of digits here ######

def flr(x):
    if '.' in x:
        x=str(x)
        return x[:x.index('.')]
    else:
        return x

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

'''
while 1:
    A,b=input().split()
    print(ndiv(A,b))
'''
