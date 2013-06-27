i = 0
x = [1,1]
y = 0

while x[i]<4000000:

    

    if x[i]%2 == 0:
        y=x[i]+y
        x[i]=x[i-2]+x[i-1]
        i=i+1
    else:
        x[i]=x[i-2]+x[i-1]
        i=i+1
    
print x[i]    
