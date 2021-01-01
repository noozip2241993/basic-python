def check_integers(n1,n2):
    """Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5."""
    if n1 ==n2 or n1+n2 == 5 or abs(n1-n2) ==5:
        return True
    else:
        return False
print(check_integers(9,2))