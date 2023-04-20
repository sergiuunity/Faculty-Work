def greatest_power(nr):
    """
    Takes a natural number and determines the greatest number with the propriety that 2 to the power of that number
    is smaller or equal to n Returns the determined number
    """
    p = 0
    x = 1
    while x <= nr:
        p += 1
        x *= 2
    p -= 1
    return p


n = int(input('n='))
print(greatest_power(n))
