#7/15/2013 
#Problem to solve:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. 
#Find the sum of all the multiples of 3 or 5 below 1000.


def mult_array(base, max):
    print base
    print max
    divis = max / base
    print divis
    div_array = range(1,divis+1)
    print div_array
    output_array = []
    for dv in div_array:
        #print dv
        #print base
        #print base * dv
        #ouptut_1 = base * dv
        #print output_1
        output_array.append(base * dv)
    return output_array

base_3 = mult_array(3,999)

print base_3

base_5 = mult_array(5,999)

print base_5

base_3_5 = list(set(base_3) | set(base_5) )

print base_3_5

print sum(base_3_5)
