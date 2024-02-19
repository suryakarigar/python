# Weather activity checker

# weather = "Sunny"
weather = str.capitalize(input("Enter a weather:"))

if weather == "Sunny" :
    activity = "Go for a walk"
elif weather == "Rainy" :
    activity = "Take a cup of tea and read a book"
elif weather == "Snowy" :
    activity = "Build a snowman"

print(activity)