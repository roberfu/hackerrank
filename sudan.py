def sudan(n,y,x):
    if (n==0):
        return x+y
    if (y==0):
        return x
    return sudan(n-1,sudan(n,x,y),sudan(n,x,y)+y+1)

print(sudan(1,1,1)) # error: needs verification
    





