instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

print(instructor.pop("owns_dog"))
print(instructor)

print(instructor.popitem())
print(instructor)

first = dict(a=1, b=2, c=3)

second = {}

second.update(first)

print(second)