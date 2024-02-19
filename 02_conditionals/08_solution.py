# Password checker

user_password = str(input("Enter your password: "))

# password_length = len(user_password)                  # MY WAY to check length

# MY WAY

# if password_length < 6 :
#     print("Weak Password")
# elif password_length <= 10 : 
#     print("Medium Password")
# else :
#     print("Strong Password")

# GURUJI WAY

if len(user_password) < 6 :
    strength = "Weak"
elif len(user_password) <= 10 : 
    strength = "Medium"
else :
    strength = "Strong"

print("Password strength is",strength)