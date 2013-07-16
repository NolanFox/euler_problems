#7/15/2013
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#int_test = 1
int_test = 691980
int_range = range(1,21)
print int_range
n = 0
while n < 10:
    #print n
    #print "int_test"
    print int_test
    for int_item in int_range:
        #print "int_item"
        #print int_item
        if int_test % int_item == 0:
            n = n + 1
            #print "n                              n"
            #print n
            if n == 20:
                break
        else:
            n = 0
            int_test = int_test + 1
            break
print "Above is the solution"
