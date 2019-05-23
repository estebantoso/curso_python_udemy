def intersection(list_a, list_b):
    a = [val for val in set(list_a) & set(list_b)]
    return a

print(intersection([2,3,4,3,2,3,5,7],[7,9,7,6,6,7,4,3,2]))