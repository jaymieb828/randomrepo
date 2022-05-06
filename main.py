import random


#lists
destinations = ["New York", "Orlando",  "Honolulu", "San Diego", "Paris", "Shanghai"]
restaurants = ["McDonald's", "Taco Bell", "KFC", "Albertos Mexican Food", "Pizza hut", "Panda Express"]
transportation = ["Private Jet", "Uber", "Bullet train", "Lambroghini rental car"]  
entertainment = ["a show", "a ballet", "mountain biking", "surfing", "roller blading", "sight seeing"]
day_trip = ["xxxx"]  #['xxxx', 'destination, 'restaurant', 'transporation, 'entertainent']

#variables
random_destination = random.choice(destinations)
random_restaurant = random.choice(restaurants)
random_transportation = random.choice(transportation)
random_entertainment = random.choice(entertainment)


print("Welcome to your day trip planner!")



def place(answer):
    print("We have selected" + " " + random.choice(destinations) + " " + "as your destination.")
    while True: 
        answer = (input("Are you happy with this ?"))
        if answer == "yes":
            print("Truly a wonderful place!")
            return
            break
        elif answer =="no": 
            (input(("Sorry to hear that." + " " + "How about" + " " + random.choice(destinations) + " " + "instead?")))
            random_destination = random.choice(destinations)
            continue
        else: 
            print("Enter yes or no")
            break   

place("yes" or "no")

day_trip.append (random_restaurant)
print ("We've go you booked for" + " " + day_trip[1] + "!")
print("We hope you enjoy your meal.")

# meal selection

print("A fine meal to enjoy for sure!")

def food(answer):
    print("Next we have planned a wonderful meal at" + " " + random.choice(restaurants)+ ".")
    while True: 
        answer = (input("Are you happy with this destination?"))
        if answer == "yes":
            print("That's a beautiful place to visit!")
            return
            break
        elif answer =="no": 
            (input(("I'm sorry to hear that." + " " + "How about" + " " + random.choice(restaurants) + " " + "instead?")))
            random_restaurant = random.choice(restaurants)
            continue
        else: 
            print("Enter yes or no")
            break   

day_trip.append (random_restaurant)
print ("We've go you booked for" + " " + day_trip[2] + "!")
print("We hope you enjoy your meal.")
food("yes" or "no")






# def food(answer): #meal selector
#     while True: 
#         answer = (input("Are you happy with this meal selection?"))
#         if answer == "yes":
#             break 
#         elif answer == "no": 
#             (input(("I'm sorry to hear that." + " " + "How about" + " " + random.choice(restaurants) + " " + "instead?")))
#             continue
#         else: 
#             print("Enter yes or no")
#             break   

# food("yes" or "no")  

# print("Excellent choice!")
# print("for your mode of transportation we have chosen" + " " + random_transportation + " " + "for you.")
        
# def transport(answer): #transportation selector
#     while True: 
#         answer = (input("Are you happy with this mode of transport?"))
#         if answer == "yes":
#             break 
#         elif answer =="no": 
#             (input(("Agreed, that selection was lame." + " " + "How about" + " " + random.choice(transportation) + " " + "instead?")))
#             continue
#         else: 
#             print("Enter yes or no")
#             break   
    
# transport("yes" or "no")

# print ("This day trip is looking awesome!")
# print ("Up next, we've selected" + " " + random_entertainment + " " + "for you.")

# def fun_stuff(answer): #entertainment selector
#     while True: 
#         answer = (input("Are you feeling this choice?"))
#         if answer == "yes":
#             break 
#         elif answer =="no": 
#             (input(("Agreed, that selection was not a good fit." + " " + "How about" + " " + random.choice(entertainment) + " " + "instead?")))
#             continue
#         else: 
#             print("Enter yes or no")
#             break   

# fun_stuff("yes" or "no")

# input("Once you are happy with these selections, please confirm your daytrip as complete by typing 'Complete'")
# if(input == "Complete"):
#     print("We're glad you enjoyed your day trip")
# else:
#     print("Maybe you need to hire a better day trip planner.")


# # #destination function

# # # def get_random_destination(rand_des):
# # #     rand_des = random.randrange(len(destinations))
# # #     rand_loc = destinations[rand_des]
# # #     print (rand_loc)
# # #     return



