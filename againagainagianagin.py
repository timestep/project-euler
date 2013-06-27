import time, math

s = time.time()
def IsPrime( n ):
	if n == 2:
		return 1
	elif n % 2 == 0:
		return 0
	
	i = 3
	range = int( math.sqrt(n) ) + 1
	while( i < range ):
		if( n % i == 0):
			return 0
		i += 1
	return 1

q=2000000
T = 3
l=2
while T<q:
	if IsPrime(T):
		l=l+T
	T+=2
	
print T-2
print l
print time.time() - s
