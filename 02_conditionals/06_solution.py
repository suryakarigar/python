# Choose a mode of transportation

distance = int(input("Enter distance: "))

if distance < 3 :
    transport = "Walk"
elif distance <= 15 :
    transport = "Bike"
else :
    transport = "Car"

print("Take a",transport)