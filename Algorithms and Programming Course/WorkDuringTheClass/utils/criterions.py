# lambda value: value % 2 == 0
def is_even(value):
    """
    Defines if a given number is even.
    :param value: given number
    :type: int
    :return: if the number is even
    :rtype: bool
    """
    return value % 2 == 0


def is_armstrong(value):
    """
    Defines if a given number is Armstrong number.
    :param value: given number
    :type: int
    :return: if the number is Armstrong number
    :rtype: bool
    """
    s = 0
    copy = value
    while value > 0:
        s = s + (value % 10) ** 3
        value = value // 10
    return s == copy


def is_prime(value):
    """
    Defines if a given number is prime.
    :param value: given number
    :type: int
    :return: if the number is prime
    :rtype: bool
    """
    if value <= 1:
        return False
    for i in range(2, value):
        if value % i == 0:
            return False
    return True


def is_perfect_square(value):
    """
    Defines if the given number is a perfect square.
    :param value: given number
    :type: int
    :return: if the number is perfect square
    :rtype: bool
    """
    if value >= 0:
        return int(value ** (1/2)) ** 2 == value
    return False


# lambda value: is_armstrong(value) and is_even(value)
def criterion_i_2(value):
    """
    Defines if a given number is Armstrong number and even.
    :param value: given number
    :type: int
    :return: if the number is Armstrong number and even
    :rtype: bool
    """
    return is_armstrong(value) and is_even(value)


# lambda value: is_armstrong(value) or is_even(value) or is_prime(value) or is_prefect_square(value)
def criterion_i_3(value):
    """
    Defines if a given number is Armstrong number and even.
    :param value: given number
    :type: int
    :return: if the number is Armstrong number and even
    :rtype: bool
    """
    return is_armstrong(value) or is_even(value) or is_prime(value) or is_perfect_square(value)
