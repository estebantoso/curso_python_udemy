names = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo", "pablo"]

print(names)

partial_names = names[2:6:2]

print(partial_names)

partial_names = names[2:]

print(partial_names)

partial_names = names[-2:]

print(partial_names)

partial_names = names[0:]

partial_names.pop()

print(names)

print(partial_names)

print (names is partial_names)

print(names[1::4])
print(names[4::-1])