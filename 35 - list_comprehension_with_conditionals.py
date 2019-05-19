numbers = list(range(1,7))

evens = [num for num in numbers if num % 2 == 0]
#odds = [num for num in numbers if num % 2 == 1]

odds = [num for num in numbers if num not in evens]
print (evens)
print (odds)

aux = [num*2 if num % 2 == 0 else num/2 for num in numbers]

print(aux)

with_vowels = "This is so much fun!"

new_string = "".join(letter for letter in with_vowels  if letter not in "aeiou")

print(new_string)

word = "Locas"
print(word[::-1])