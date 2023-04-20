def smallest_number(n):
    """
    Input: a number
    Computes the smallest number that can be formed with the digits of a given number
    Returns the computed number
    """
    minimum = 9
    copy = n
    while copy != 0:
        if minimum > copy % 10 != 0:
            minimum = copy % 10
        copy //= 10
    computed_nr = minimum
    for i in range(10):
        copy = n
        number_of_appearances = 0
        while copy != 0:
            if copy % 10 == i:
                number_of_appearances += 1
            copy //= 10
        if i == minimum:
            number_of_appearances -= 1
        for j in range(number_of_appearances):
            computed_nr = computed_nr * 10 + i
    if n != 0:
        return computed_nr
    else:
        return 0


x = int(input('x='))
print("the resulted number is...", smallest_number(x))
