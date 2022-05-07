import random


#lists
destinations = ["New York", "Orlando",  "Honolulu", "San Diego", "Paris", "Shanghai"]
restaurants = ["McDonald's", "Taco Bell", "KFC", "Albertos Mexican Food", "Pizza hut", "Panda Express"]
transportation = ["a private Jet", "an Uber", "a bullet train", "a Lambroghini rental car"]  
entertainment = ["watching a show", "going to a ballet", "mountain biking", "surfing", "roller blading", "site seeing"]
day_trip = ["xxxx"]  #['xxxx', 'destination, 'restaurant', 'transporation, 'entertainent']

#variables
random_destination = random.choice(destinations)
random_restaurant = random.choice(restaurants)
random_transportation = random.choice(transportation)
random_entertainment = random.choice(entertainment)


print("Welcome to your day trip planner!")

# destination selection

def place(answer):
    random_destination = random.choice(destinations)
    day_trip.append (random_destination)
    
    print(" ")
    print("We have selected" + " " + (day_trip[1]) + " " + "as your destination.")
    print(" ")

    while True: 
        answer = (input("Are you happy with this?"))
        if answer == "yes":
            print(" ")
            print("Truly a wonderful place!")
            print(" ")
            break
        elif answer =="no": 
            day_trip.pop()                                          #removes last random value
            random_destination = random.choice(destinations)
            day_trip.append (random_destination)
            print(" ")
            print("Sorry to hear that." + " " + "We've rebooked you to" + " " + random_destination + " " + "instead.")
            print(" ")
            continue
        else: 
            print("Enter yes or no")
            break   

place("yes" or "no")

print ("We've go you booked for" + " " + day_trip[1] + "!")

# meal selection

def food(answer):
    random_restaurant = random.choice(restaurants)
    day_trip.append (random_restaurant)

    print(" ")
    print("We have booked a table at" + " " + (day_trip[2]) + " " + "for a perfect meal.")
    print(" ")

    while True: 
        answer = (input("Are you happy with this?"))
        if answer == "yes":
            print(" ")
            print("A gastronomic adventure like no other!")
            print(" ")
            break
        elif answer =="no": 
            day_trip.pop()
            random_restaurant = random.choice(restaurants)
            day_trip.append (random_restaurant)
            print(" ")
            print("Sorry to hear that." + " " + "We've rebooked you eat at" + " " + random_restaurant + " " + "instead.")
            print(" ")
            continue
        else: 
            print("Enter yes or no")
            break   

food("yes" or "no")

print("You are confirmed for" + " " + day_trip[2] + "!")

# transportation selector

def transport(answer):
    random_transportation = random.choice(transportation)
    day_trip.append (random_transportation)
    print(" ")
    print("For your mode of transportation we have chosen" + " " + (day_trip[3]) + " " + "for you.")
    print(" ")
    while True: 
        answer = (input("Are you happy with this?"))
        if answer == "yes":
            print(" ")
            print("Lets go!!")
            print(" ")
            break
        elif answer =="no": 
            day_trip.pop()
            random_transportation = random.choice(transportation)
            day_trip.append (random_transportation)
            print(" ")
            print("Maybe a bit too slow for you I guess..." + " " + "How about" + " " + random_transportation + " " + "instead?")
            print(" ")
            continue
        else: 
            print("Enter yes or no")
            break   

transport("yes" or "no")

print("You are confirmed for" + " " + day_trip[3] + " " + "on your day trip.")

# entertainment

def to_do(answer):
    random_entertainment = random.choice(entertainment)
    day_trip.append (random_entertainment)
    
    print("For your enjoyment we have booked an afternoon" + " " + (day_trip[4]) + " " + "for you.")
    print(" ")
    while True: 
        answer = (input("Are you happy with this?"))
        if answer == "yes":
            print(" ")
            print("Lets go!!")
            print(" ")
            break
        elif answer =="no": 
            day_trip.pop()
            random_entertainment = random.choice(entertainment)
            day_trip.append (random_entertainment)
            print(" ")
            print("Maybe a bit too slow for you I guess..." + " " + "How about" + " " + random_entertainment + " " + "instead?")
            print(" ")
            continue
        else: 
            print("Enter yes or no")
            break   

to_do("yes" or "no")

print("You are confirmed for" + " " + day_trip[4] + " " + "on your day trip.")

print(" ")

print("To comfirm, here is your itinerary for the day. You will be visiting the city of" + " " + day_trip[1] + ".")

print(" ")

print("You will be enjoying a wonderful meal at" + " " + day_trip[2] + ".")

print(" ")

print("For your transporation, we have booked" + " " + day_trip[3] + ".")

print(" ")

print("And finally, for your day's entertainment, you will be spending the rest of the day" + " " + day_trip[4])

print(" ")

confirmation = input("Are you happy with this Itinerary?")
if confirmation == ("yes"):
    print(" ")
    print("Enjoy your special trip!")
else:
    print(" ")
    print("Ok... let's start over")
    print(" ")
    print("Welcome... AGAIN to your day trip planner.")
    print(" ")
    place("yes" or "no")
    

