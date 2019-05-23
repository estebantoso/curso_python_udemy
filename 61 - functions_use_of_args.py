def sum_all_nums(num1, num2, num3):
    return num1 + num2 + num3

print(sum_all_nums(4,6,9))

def sum_all_nums_better(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums_better(4,6,9,30))