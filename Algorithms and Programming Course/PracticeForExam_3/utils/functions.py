def custom_filter(given_list, criterion):
    new_list = []
    for item in given_list:
        if criterion(item):
            new_list.append(item)
    return new_list
