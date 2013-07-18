#7/17/2013
#What is the 10 001st prime number?


def factors(n):
    return list(reduce(list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def isprime(n):
    factor_count = len(factors(n))
    if n == 1:
        return False
    elif factor_count < 2:
        return False
    elif factor_count > 2:
        return False
    else:
        return True

def prime_num(n):
    x = 0
    prime_cnt = 0
    while prime_cnt < n:
        x = x + 1
        if isprime(x):
            prime_cnt = prime_cnt + 1
            print x
    print "count of primes"
    print prime_cnt

prime_num(10001)
