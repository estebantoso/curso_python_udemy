instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

print (instructor)

#instructor.clear()
#print (instructor)

ins = instructor.copy()
print (ins is instructor)

a = {}.fromkeys("a", [1, 2, 3, 4, 5])

print(a)

# GET

print(instructor.get("name"))


