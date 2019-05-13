# ask for age
age = input("how old are you?: " )
if age.isnumeric():                  #if age != "":
    age = int(age)
    if age >= 18 and age < 21:
        # 18-21 wristband
        print("you can enter, but need a wristband")
    elif age >= 21:
        # 21+ drink, normal entry
        print("you are good to enter and can drink!")
    else:
        # too young, sorry
        print("you can't come in, little one! :(")
else:
    print("please enter age!")