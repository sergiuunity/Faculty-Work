def general_filter(my_l, criterion):
    new_l = []
    for item in my_l:
        if criterion(item):
            new_l.append(item)
    return new_l

