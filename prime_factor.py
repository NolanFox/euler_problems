#7/15/2013
#What is the largest prime factor of the number 600851475143 ?

def factors(n):
    return list(reduce(list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def isprime(n):
    factor_count = len(factors(n))
    if factor_count < 2:
        return False
    elif factor_count > 2:
        return False
    else:
        return True


def largest_prime_factor(n):
    all_factors = factors(n)
    print all_factors
    prime_factors = []
    for fct in all_factors:
        if isprime(fct):
            print "Prime"
            print fct
            prime_factors.append(fct)
        else:
            print "Not Prime"
            print fct
    print prime_factors
    print max(prime_factors)

largest_prime_factor(600851475143)
