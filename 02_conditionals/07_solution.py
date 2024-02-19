# Customize coffee order with extra espresso shot option

coffee_size = "Medium"
espresso = False

# One way

# if coffee_size == "Medium" :
#     if espresso :
#         print("Coffee with extra shot")
#     if not espresso :
#         print("Regular coffee")

# Guruji way

if espresso :
    if coffee_size == "Medium" :
        # print(f"Here's your {coffee_size} coffee with extra shot") my way
        coffee = f"Here's your {coffee_size} coffee with extra shot"

elif not espresso :
    if coffee_size == "Medium" :
        # print(f"Here's your regular {coffee_size} coffee") my way
        coffee = f"Here's your regular {coffee_size} coffee"

print(coffee)