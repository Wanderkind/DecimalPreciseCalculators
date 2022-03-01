def flr(x):
    if '.' in x:
        x=str(x)
        return x[:x.index('.')]
    else:
        return x
