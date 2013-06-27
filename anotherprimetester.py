import math,time

q=6

for x in range(3,q):

    u=math.sqrt(x)
    u=math.ceil(x)
    u=int(u)
    
    for q in range(2,u):
        if x%q == 0:
            t=0
        else:
            t=1
   
print t
