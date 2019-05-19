numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key,value in numbers.items()}

print(squared_numbers)

a = {num: num ** 2 for num in [1, 2, 3, 4, 5]}

print(a)

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(len(str1))}
print(combo)

instructor = {
    "name": "colt",
    "city": "san francisco",
    "color": "purple"
}

yelling_instructor = {key.upper(): value.upper() for key, value in instructor.items()}
print(yelling_instructor)

num_list = [1, 2, 3, 4]

numbers = {num: ("odd" if num % 2 else "even") for num in num_list }
print(numbers)
