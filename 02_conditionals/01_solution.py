# USER AGE CATEGORIZATION

user_age = input("Enter your age: ") # returns value in String and it needs to be changed

int_user_age = int(user_age) # Changes value to integer

if int_user_age < 13:
    print("Child")
elif int_user_age < 20:
    print("Teenager")
elif int_user_age < 60:
    print("Adult")
else:
    print("Senior")