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
    
    l=list(str(int(dc(a,n).replace('.',''))+int(dc(b,n).replace('.',''))).zfill(n+1))
    l.insert(-n,'.')
    
    return ''.join(l)

'''
while 1:
    a,b=input().split()
    print(add(a,b))
'''
