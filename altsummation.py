import math,time

##sum of primes below q

q = 100

t = 1
l = 2   
tt=time.time()
for x in range(3,q+1):

        
    
##  x=x+2
           
    if x%2.0==0 and x!=2:
##           print "Not Prime"
        t=0
    elif x%3.0==0 and x!=3:
##            print "Not Prime"
        t=0
    else:
        r=math.sqrt(x)
        r=math.ceil(x)
        k = 1
        while (6.0*k-1.0)<r:
            if x%(6.0*k+1.0)==0 and (6.0*k+1.0)!=x:
               t=0
               k=k+1
            elif x%(6.0*k-1.0)==0 and (6.0*k-1.0)!=x:
               t=0
               k=k+1
            else:
                k=k+1

    if t==1:
        l=l+x
##        print x
##        print l
       
    else:
        t=1
        

print x    
print l    
print time.time()-tt
