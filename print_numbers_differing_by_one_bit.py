# Given n, output the numbers from 0 to 2^n-1 (inclusive) in n-bit binary form, 
# in such an order that adjacent numbers in the list differ by exactly 1 bit.


def print_nums(n):
    prefix = 0
    while prefix <= n:
        carry = 0
        while carry < n - prefix:
            buf = [1] * prefix
            buf.extend([0] * (n - prefix))
            if carry > 0:
                buf[n - carry] = 1
            print ''.join(map(str, buf))
            carry += 1
        prefix += 1


print_nums(10)