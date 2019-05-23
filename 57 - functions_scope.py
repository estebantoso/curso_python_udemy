total = 0

def sum():
    global total
    total += 1
    return total

print (sum())

name = "Rusty"

def greet():
    print(name)

greet()

###################################

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner