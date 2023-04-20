def check_prime(nr):
    """
    Takes a given number and checks if it is prime
    Returns True if the number is prime and False if it is not
    """
    d = 0
    for i in range(2, nr // 2 + 1):
        if nr % i == 0:
            d += 1
    if d == 0:
        return True
    else:
        return False


def nearest_prime(x):
    """
    Input: an integer
    Computes the nearest prime number to a given number
    Returns the requested number
    """
    if x < 2:
        return 2
    else:
        left, right = x-1, x+1
        is_prime = False
        while not is_prime:
            is_prime = check_prime(left)
            left -= 1
        left += 1
        is_prime = False
        while not is_prime:
            is_prime = check_prime(right)
            right += 1
        right -= 1
        if right - x > x - left:
            return left
        else:
            return right


n = int(input('n='))
m = nearest_prime(n)
print(m)
