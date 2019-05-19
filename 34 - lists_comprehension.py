nums = [1, 2, 3]

print([x*10 for x in nums])
print([x/2 for x in nums])

name = "colt"

print([char.upper() for char in name])

generic_list = ["", 0, [], 1]

bool_list = [bool(val) for val in generic_list]

print(bool_list)

colors = ["orange", "yellow", "green", "blue", "red"]

colors = [color[0].upper() + color[1:] for color in colors]

print(colors)
