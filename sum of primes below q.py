import math

##sum of primes below q

q=2000000

def primetruefalse(x):
    k = 1
    t = 1
   

    while True:
       
        if x%2.0==0 and x!=2:
##           print "Not Prime"
           t=0
        elif x%3.0==0 and x!=3:
##            print "Not Prime"
            t=0
        else:
            r=math.sqrt(x)
            r=math.ceil(x)
            
            while (6.0*k-1.0)<r:
                if x%(6.0*k+1.0)==0 and (6.0*k+1.0)!=x:
                   t=0
                   k=k+1
                elif x%(6.0*k-1.0)==0 and (6.0*k-1.0)!=x:
                   t=0
                   k=k+1
                else:
                    k=k+1            
        break
    return t

x=1
i=2
l=2

while i<q:
    x=x+2
    t = primetruefalse(x)
##    print t
    
    if t==1:
       l=l+x
    
    i=i+1
    
##    print i
##    print l

    
print l    
print i
