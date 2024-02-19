# Movie ticket pricing based on age
import random

userage = input("Enter your age: ")
int_userage = int(userage)

# MY WAY

# adult_regular = 12
# child_regular = 8
# adult_discount = 10
# child_discount = 6

# GURUJI WAY
price = 12 if int_userage >= 18 else 8

days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
random_day = random.choice(days)

# MY WAY

# if random_day == "wednesday" :
#     if int_userage < 18 :
#         print(f"It's Wednesday. You've got a discount, ticket price: ${child_discount}")
#     elif int_userage >= 18 : 
#         print(f"It's Wednesday. You got a discount, ticket price: ${adult_discount}")
# else :
#     if int_userage < 18 :
#         print(f"Your ticket price: ${child_regular}")
#     elif int_userage >= 18 : 
#         print(f"Your ticket price: ${adult_regular}")

# GURUJI WAY

if random_day == "wednesday" :
    # price = price - 2
    price -= 2
    print(f"Discounted ticket price: ${price}")
else :
    print(f"Regular ticket price: ${price}")