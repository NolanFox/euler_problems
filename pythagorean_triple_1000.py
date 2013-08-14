#August 11, 2013
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.


def sum_two(n):
    if n < 2:
        print "no two natural numbers sum since less than 2"
    else:
        output_array = []
        iter_cnt = 1
        half_n = (n * 1.0) / 2
        while iter_cnt < half_n:
            n_0 = n - iter_cnt
            sum_pair = [iter_cnt , n_0]
            output_array = output_array.append(sum_pair)
        return output_array

sum_two(5)

#def sum_three(n):

