numbers = list(range(5,11))

print(numbers.index(6))

names = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo", "pablo"]

print(names.count("pablo"))
print(names.count("blue"))
print(names.count("pablin"))

names.reverse()
print(names)

names.sort()
print(names)

friends = ", ".join(names)
print(friends)