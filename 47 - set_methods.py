a = set({2,3,4,4,4,4})

print(a)

a.add(26)

print(a)

a.remove(4)

print(a)

math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Oliver", "James"}

a = math_students | biology_students

print(a)

b = math_students & biology_students

print(b)