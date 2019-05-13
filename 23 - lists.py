shopping_list = []

while True:
    product = input("Add something to the cart? Type q to quit: ")
    if product == "q":
        break
    else:
        shopping_list.append(product)
print("YOUR FINAL GROCERY LIST")
for item in shopping_list:
    print(f"- {item}")