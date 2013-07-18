#Jul 17 2013
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_sq_diff(n1, n_max):
    range_array = range(n1, n_max + 1)
    print "range check"
    range_sum = sum(range_array)
    print "range sum"
    sq_sum = range_sum**2
    print "square sum"
    print sq_sum
    sum_sq = 0
    for n in range_array:
        sum_sq = sum_sq + n**2
        print "sum square"
        print sum_sq
    sum_sq_diff = sq_sum - sum_sq
    print "square sum less sum square"
    print sum_sq_diff

sum_sq_diff(1,100)
