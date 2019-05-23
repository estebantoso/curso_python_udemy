noises = {
    "pig": "oink",
    "duck": "quack",
    "cat": "meow",
    "dog": "woof",
}

def speak(animal):
    return noises.get(animal, "?")