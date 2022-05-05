#Day Trip Generator


#lists

# destinations = ["New York", "Orlando",  "Honolulu", "San Diego", "Paris", "Shanghai"]

# restaurants = ["McDonald's", "Taco Bell", "KFC", "Albertos Mexican Food", "Pizza hut", "Panda Express"]

# transportation = ["Private Jet", "Uber", "Bullet train", "Lambroghini rental car"]  

# entertainment = ["A Show", "Gator wrestling", "Mountain biking", "Surfing", "Roller Blading", "Sight seeing"]

# import random


# destinations = ["New York", "Orlando",  "Honolulu", "San Diego", "Paris", "Shanghai"]
# restaurants = ["McDonald's", "Taco Bell", "KFC", "Albertos Mexican Food", "Pizza hut", "Panda Express"]

# print ("Welcome to your day trip planner!" + " We have selected " + (random.choice(destinations) + " as your destination. "))

# def yes_or_no(answer):
#     answer = (input("Are you happy with this destination?"))
#     while answer == "no":
#         print (input(("I'm sorry to hear that." + " " + "How about" + " " + (random.choice(destinations) + " " + "instead?"))))
#         return (answer)
#     if answer == "yes":
#         print ("Wonderful!")
#         return True
   
# yes_or_no ("yes" or "no")

    

# print ("Great choice! We hope you enjoy your visit. We have planned a wonderful meal at" + " " + (random.choice(restaurants) + "."))
# print ("A fine meal to enjoy for sure!")

# def food(answer):
#     answer = (input("Are you happy with this meal selection?"))
#     while answer == "no":
#         input(("I'm sorry to hear that." + " " + "How about" + " " + (random.choice(restaurants) + " " + "instead?")))
#     if answer == "yes":
#         print("Great! let's move on.")
#         return False
        
# food("yes" or "no")

import random
from tracemalloc import Snapshot

destinations = ["New York", "Orlando",  "Honolulu", "San Diego", "Paris", "Shanghai"]
restaurants = ["McDonald's", "Taco Bell", "KFC", "Albertos Mexican Food", "Pizza hut", "Panda Express"]

print ("Welcome to your day trip planner!" + " We have selected " + (random.choice(destinations) + " as your destination. "))

def yes_or_no(answer):
    while True: 
        answer = (input("Are you happy with this destination?"))
        if answer == "yes":
            continue
        elif answer =="no": 
            (input(("I'm sorry to hear that." + " " + "How about" + " " + (random.choice(destinations) + " " + "instead?"))))
            break
        else: 
            print("Enter yes or no")

yes_or_no ("yes" or "no")

print("wonderful! Let's continue.")

    
   
