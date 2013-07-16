#7/15/2013
#Find the largest palindrome made from the product of two 3-digit numbers.


three_digits = range( 100, 999 )
three_digit_mult = []
while len(three_digits) > 1:
    mult_digit = three_digits[0]
    three_digits.remove(mult_digit)
    for left_digit in three_digits:
        three_digit_mult.append(mult_digit * left_digit )
three_digit_mult = list(set(three_digit_mult))
print three_digit_mult
palindrome_array = []
for test_digit in three_digit_mult:
    digit_string = str(test_digit)
    if digit_string == digit_string[::-1]:
        palindrome_array.append(test_digit)
print palindrome_array
print max(palindrome_array)
