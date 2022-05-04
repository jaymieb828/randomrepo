#Day Trip Generator


#lists

# destinations = ["New York", "Orlando",  "Honolulu", "San Diego", "Paris", "Shanghai"]

# restaurants = ["McDonald's", "Taco Bell", "KFC", "Albertos Mexican Food", "Pizza hut", "Panda Express"]

# transportation = ["Private Jet", "Uber", "Bullet train", "Lambroghini rental car"]  

# entertainment = ["A Show", "Gator wrestling", "Mountain biking", "Surfing", "Roller Blading", "Sight seeing"]

import random

destinations = ["New York", "Orlando",  "Honolulu", "San Diego", "Paris", "Shanghai"]

print ("Welcome to your day trip planner!" + " We have selected " + (random.choice(destinations) + " as your destination. "))

# Yes = True
# yes = True
# No = False
# no = False

def yes_or_no  (input("Are you happy with this choice we made for you?")):
    if yes_or_no is "No" or "no":   
        print(("I'm sorry to hear that." + " " + "How about" + " " + (random.choice(destinations) + " " + "instead?")))



