# for num in range (1,10):
#     a = 1
#     while a <= num:
#         print("*", end = " ")
#         a += 1
#     print("\n")
    
# for num in range(1,10):
#     print("*" * num)

# cant = 3
# arr = [] 
# for i in range(cant):
#     arr.append(" ")
# print (arr)

# for num in range(1, cant + 1):
#     if i == (cant / 2 + 1):
#             arr[i] = "*"
#     else:
#         arr[i] = " "
# print (arr)
    

cant = 50
arr = [" "] * cant
centro = int(cant/2)
for fila in range (1, int((cant + 1)/2)):
    for a in range(cant):
        if (a > (centro - fila)) and (a < (centro + fila)):
            arr[a] = "*"
    for a in arr:
        print(a, end= " ")
    print("")
    

# for num in range(cant + 1):
#     arr[centro - num:centro + num] = "*"
#     print (arr)