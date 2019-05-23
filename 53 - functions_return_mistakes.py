def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if not num % 2:
            total += num
    return total

print(sum_odd_numbers([1,2,2,1,3,5,6,8,9,10]))

