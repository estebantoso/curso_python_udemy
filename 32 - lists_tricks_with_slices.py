names = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo", "pablo"]
print(names)

names_modified = names[::-1]
print (names_modified)

names_modified[1:3] = ["a", "b"]
print(names_modified)

print(names)

print(names[3][::-1])