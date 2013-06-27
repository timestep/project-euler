a,b = 0,0
while b < 1000:
    print b,
    print a,
    b = b+1
    
    if b%3 == 0:
        a = b+a
    elif b%5 == 0:
        a = b+a
    
    
    
