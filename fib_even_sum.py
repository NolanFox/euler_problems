#7/15/2013
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


def fib_even_sum(max_number):
    fib_array = [ 1 , 2 ]
    n = 1
    fib_new = 2
    while fib_new < max_number:
        fib_new = fib_array[ n - 1 ] + fib_array[n]
        fib_array.append(fib_new)
        n = n + 1
    print fib_array
    fib_even = []
    for fib in fib_array:
        if fib % 2 == 0:
            fib_even.append(fib)
        else:
            print "not even"
    print fib_even
    print sum(fib_even)





fib_even_sum(4000000)
