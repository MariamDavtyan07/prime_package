def is_prime(n):
    if n <2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def prime_range(num):
    for x in range(2,num):
        if is_prime(x):
            yield x

def prime_factors(num):
    while num>1:
        for prime in prime_factors(num):
            num//=prime
            yield prime
            break
