"""
BASIC PROJECT


Concepts we will use in this project:-

lists == To store groups of words like names ,actions and places.

random.choice() === To pick one item randomly from a list .

print() == To show the fake headline on screen.

input() == To ask the user if they want another headline 

while loop == To repeat the process until the user says "no".

string concatenation or f-strings == To form a sentences using selected words.
"""
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
#START
# 1 - IMPORT THE RANDOM MODULE
import random

#2-creating list of subjects,actions,objects and places
import random


subjects = ["Aliens", "Politicians", "Celebrities", "Scientists", "Cats", "Dogs"]
actions = ["discover", "ban", "invent", "eat", "dance with", "fight against"]
objects = ["chocolate", "robots", "flying cars", "AI", "pizza", "time machines"]
places = ["in New York", "on Mars", "in the White House", "at the zoo", "in space"]

# Step 3 generate a headlines
def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    place = random.choice(places)
    # print(f"{subject} {action} {obj} {place}")
    return f" BREAKING NEWS: {subject} {action} {obj} {place}!"

# Step 4 : run multiple time 
while True:
    print(generate_headline())
    user_input = input("Do you want another headline? (yes/no): ").strip()
    if user_input.lower() != "yes":
        break

print("Thanks for using  the Fake News Headline Generator !!")


