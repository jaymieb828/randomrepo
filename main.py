import random

destinations = ["New York", "Orlando",  "Honolulu", "San Diego", "Paris", "Shanghai"]
restaurants = ["McDonald's", "Taco Bell", "KFC", "Albertos Mexican Food", "Pizza hut", "Panda Express"]
transportation = ["Private Jet", "Uber", "Bullet train", "Lambroghini rental car"]  
entertainment = ["A Show", "A ballet", "Mountain biking", "Surfing", "Roller Blading", "Sight seeing"]

print ("Welcome to your day trip planner!" + " We have selected " + (random.sample(destinations) + " as your destination. "))

def place(answer): #destination selector
    while True: 
        answer = (input("Are you happy with this destination?"))
        if answer == "yes":
            print("That's a beautiful place to visit!")
            break
        elif answer =="no": 
            (input(("I'm sorry to hear that." + " " + "How about" + " " + (random.sample(destinations)) + " " + "instead?")))
            continue
        else: 
            print("Enter yes or no")
            break   
   
place("yes" or "no")

print ("We hope you enjoy your stay.")
print ("Next we have planned a wonderful meal at" + " " + (random.sample(restaurants) + "."))
print ("A fine meal to enjoy for sure!")


def food(answer): #meal selector
    while True: 
        answer = (input("Are you happy with this meal selection?"))
        if answer == "yes":
            break 
        elif answer == "no": 
            (input(("I'm sorry to hear that." + " " + "How about" + " " + (random.sample(restaurants)) + " " + "instead?")))
            continue
        else: 
            print("Enter yes or no")
            break   

food("yes" or "no")  

print("Excellent choice!")
print("for your mode of transportation we have chosen" + " " + (random.sample(transportation) + " " + "for you."))
        
def transport(answer): #transportation selector
    while True: 
        answer = (input("Are you happy with this mode of transport?"))
        if answer == "yes":
            break 
        elif answer =="no": 
            (input(("Agreed, that selection was lame." + " " + "How about" + " " + (random.sample(transportation)) + " " + "instead?")))
            continue
        else: 
            print("Enter yes or no")
            break   

transport("yes" or "no")

print ("This day trip is looking awesome!")
print ("Up next, we've selected" + " " + (random.sample(entertainment)) + " " + "for you.")

def fun_stuff(answer): #entertainment selector
    while True: 
        answer = (input("Are you feeling this choice?"))
        if answer == "yes":
            break 
        elif answer =="no": 
            (input(("Agreed, that selection was not a good fit." + " " + "How about" + " " + (random.sample(entertainment)) + " " + "instead?")))
            continue
        else: 
            print("Enter yes or no")
            break   

fun_stuff("yes" or "no")

input("Once you are happy with these selections, please confirm your daytrip as complete by typing 'Complete'")
if(input == "Complete"):
    print("We're glad you enjoyed your day trip")
else:
    print("Maybe you'll need to hire a better day trip planner.")


# #destination function

# # def get_random_destination(rand_des):
# #     rand_des = random.randrange(len(destinations))
# #     rand_loc = destinations[rand_des]
# #     print (rand_loc)
# #     return



