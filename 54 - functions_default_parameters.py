def exponent(num, power=2):
    return num ** power

print(exponent(2))
print(exponent(2, 5))

def add(a,b):
    return(a+b)

def subtract(a,b):
    return(a-b)

def math(a, b, fn=add):
    return fn(a,b)

print(math(2,2))

print(math(2,2,subtract))