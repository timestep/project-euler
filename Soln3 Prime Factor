import math

##Find the largest prime factor of a composite number.

x = 100000 ## Number Here
k = 1
t = 1
l = 0.0
i = 0

while True:
   
    if x%2.0==0:
        print "Not Prime"
        x=x/2
        t=0
        l=2
    elif x%3.0==0:
        x=x/3
        print "Not Prime"
        t=0
        l=3
    else:
        r=math.sqrt(x)
        r=math.ceil(x)
        
        while (6.0*k-1.0)<r:
            r=math.sqrt(x)
            r=math.ceil(x)

            if x%2.0==0:
               x=x/2
               
            elif x%3.0==0:
               x=x/3
               
            elif x%(6.0*k+1.0)==0 and (6.0*k+1.0)!=x:
               t=0
               l=(6.0*k+1.0)
               x=x/l
               k=k+1
               
            elif x%(6.0*k-1.0)==0 and (6.0*k-1.0)!=x:
               t=0
               l=(6.0*k-1)
               x=x/l
               k=k+1
               
            else:
                k=k+1

    break

print l

     
