#Day Trip Generator


#lists

from random import random


# destinations = ["New York", "Orlando",  "Honolulu", "San Diego", "Paris", "Shanghai"]

# restaurants = ["McDonald's", "Taco Bell", "KFC", "Albertos Mexican Food", "Pizza hut", "Panda Express"]

# transportation = ["Private Jet", "Uber", "Bullet train", "Lambroghini rental car"]  

# entertainment = ["A Show", "Gator wrestling", "Mountain biking", "Surfing", "Roller Blading", "Sight seeing"]



import random

destinations = ["New York", "Orlando",  "Honolulu", "San Diego", "Paris", "Shanghai"]

print ("Welcome to your day trip planner!" + " We have selected " + (random.choice(destinations) + " as your destination. "))

yes_or_no = (input("Are you happy with this choice we made for you?"))
if "No" or "no":
    print("I'm sorry to hear that." + " " + "How about" + " " + (random.choice(destinations) + " " + "instead?"))
elif "Yes" or "yes":
    print("Thats wonderul, let's move on...")

    