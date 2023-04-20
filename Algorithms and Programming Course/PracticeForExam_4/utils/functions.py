def general_filter(new_list, criterion):
    output = []
    for item in new_list:
        if criterion(item):
            output.append(item)
    return output
