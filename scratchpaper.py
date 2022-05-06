
from gc import collect
import random


destinations = ["New York", "Orlando",  "Honolulu", "San Diego", "Paris", "Shanghai"]
restaurants = ["McDonald's", "Taco Bell", "KFC", "Albertos Mexican Food", "Pizza hut", "Panda Express"]
transportation = ["Private Jet", "Uber", "Bullet train", "Lambroghini rental car"]  
entertainment = ["A Show", "A ballet", "Mountain biking", "Surfing", "Roller Blading", "Sight seeing"]
confirmation = []

chow = (random.choice(restaurants)) 
    
print (chow)

    

print ("Welcome to your day trip planner!" + " We have selected " + (random.choice(destinations) + " as your destination. "))

def place(answer):
    while True: 
        answer = (input("Are you happy with this destination?"))
        if answer == "yes":
            print("That's a beautiful place to visit!")
            return confirmation [0]
            break
        elif answer =="no": 
            (input(("I'm sorry to hear that." + " " + "How about" + " " + (random.choice(destinations)) + " " + "instead?")))
            continue
        else: 
            print("Enter yes or no")
            break   

place("yes" or "no")



print ("We hope you enjoy your stay.")
print ("Next we have planned a wonderful meal at" + " " + (random.choice(restaurants) + "."))
print ("A fine meal to enjoy for sure!")


def food(answer):
    while True: 
        answer = (input("Are you happy with this meal selection?"))
        if answer == "yes":
            break 
        elif answer =="no": 
            (input(("I'm sorry to hear that." + " " + "How about" + " " + (random.choice(restaurants)) + " " + "instead?")))
            continue
        else: 
            print("Enter yes or no")
            break   

food("yes" or "no")  

print("Excellent choice!")
print("for your mode of transportation we have chosen" + " " + (random.choice(transportation) + " " + "for you."))
        
def transport(answer):
    while True: 
        answer = (input("Are you happy with this mode of transport?"))
        if answer == "yes":
            break 
        elif answer =="no": 
            (input(("Agreed, that selection was lame." + " " + "How about" + " " + (random.choice(transportation)) + " " + "instead?")))
            continue
        else: 
            print("Enter yes or no")
            break   

transport("yes" or "no")

print ("This day trip is looking awesome!")
print ("Up next, we've selected" + " " + (random.choice(entertainment)) + " " + "for you.")

def fun_stuff(answer):
    while True: 
        answer = (input("Are you feeling this choice?"))
        if answer == "yes":
            break 
        elif answer =="no": 
            (input(("Agreed, that selection was not a good fit." + " " + "How about" + " " + (random.choice(transportation)) + " " + "instead?")))
            continue
        else: 
            print("Enter yes or no")
            break   

fun_stuff("yes" or "no")
