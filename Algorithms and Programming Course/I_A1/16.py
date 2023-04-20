def compare_figures():
    """
    Reads numbers with at least 2 digits until 0 is given and computes the amount of numbers that have the unit
    figure smaller than the tens figure Returns the computed number
    """
    nr = 0
    x = int(input('...'))
    while x != 0:
        if x % 10 < x // 10 % 10:
            nr += 1
        x = int(input('...'))
    return nr


print(compare_figures())
