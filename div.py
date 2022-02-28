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

def div(a,b):
    l=list(str(int(int(dc(a,n).replace('.',''))*10**n/int(dc(b,n).replace('.','')))).zfill(n+1))
    l.insert(-n,'.')
    if l[0]+l[1]=='-.':
        l[1]='0.'
    return ''.join(l)

'''
while 1:
    A,b=input().split()
    print(div(A,b))
'''
