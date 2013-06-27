import math

def get_prime_numbers(n):
    if n > 0:
        j = 3
        counter = 2
        while counter < n:
            c = int(math.sqrt(j)) + 1
            for i in range(2,c):
                if j % i == 0:
                    break
            else:
                counter += 1
            j += 1
    return (j-1)

get_prime_numbers(199)
