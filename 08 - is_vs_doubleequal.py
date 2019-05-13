a = [1, 2, 3]
b = [1, 2, 3]

print (a == b)
print (a is b)

c = b

print (b is c)

d = b.copy()

print (d is b)