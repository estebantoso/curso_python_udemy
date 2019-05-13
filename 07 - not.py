age = int(input("how old are you?: "))

if not((age >=2 and age <= 8) or age >=65):
    print("you must pay 10 dollar")
else:
    print("you must pay 2 or 5 dollar")