def check_base_10_digits(n1, n2):
    """
    Takes two numbers and verifies if the same digits are used to write them in base 10
    Return True if the condition is meet and False if it is not
    """
    n1_digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    n2_digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while n1 != 0:
        n1_digits[n1 % 10] = 1
        n1 //= 10
    while n2 != 0:
        n2_digits[n2 % 10] = 1
        n2 //= 10
    condition = True
    for i in range(10):
        if n1_digits[i] != n2_digits[i]:
            condition = False
    return condition


x = int(input('x='))
y = int(input('y='))
print(check_base_10_digits(x, y))
