def partition(list_a, fn):
    truthy_list = []
    falsy_list = []
    for val in list_a:
        if fn(val):
            truthy_list.append(val)
        else:
            falsy_list.append(val)
    return [truthy_list, falsy_list]

