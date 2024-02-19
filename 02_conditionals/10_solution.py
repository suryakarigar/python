import random

pet_species = ["Dog", "Cat"]

pet_age = 2

random_pet = random.choice(pet_species)

if pet_age <= 2 :
    if random_pet == "Dog" :
        pet_food = "Puppy Food"
    elif random_pet == "Cat" :
        pet_food = "Kitten Food"
elif pet_age >= 2 :
    if random_pet == "Dog" :
        pet_food = "Dog Food"
    elif random_pet == "Cat" :
        pet_food = "Senior Cat Food"
        
print("Pet is", random_pet,"its age is",pet_age,"years","and its food is",pet_food)