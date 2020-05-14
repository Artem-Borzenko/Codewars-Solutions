#  In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

def square_digits(num):
    r = ''
    for l in str(num):
        r = r + str((int(l))**2)
    return int(r)
