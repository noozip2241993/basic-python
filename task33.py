def sum_three_given_numbers(n1,n2,n3):
    """ Write a Python program to sum of three given integers. However, if two values are equal sum will be zero"""
    if n1 == n2 or n1==n3:
        return 0
    else:
        return n1+n2+n3
print(sum_three_given_numbers(3,1,3))