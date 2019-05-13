for guion in "12-345///asvds6789-x":
    if guion == "-" or guion == "/" or guion.isalpha():
        continue
    print(guion, end = "")