import random
print("Please to meet you. We are going to play rock, paper and scissors")
user = input("Enter rock, paper or scissors: ")
hsign = ["rock","paper","scissors"]

value = random.choice(hsign)
print(value)
#print(type(value)) checker
#print(hsign[0]) checker
#print(hsign[1]) checker
#print(hsign[2]) checker

if user == hsign[0] and value == hsign[0]:
    print("We both made a", hsign[0], ", its a draw...")
elif user == hsign[0] and value == hsign[1]:
    print ("Oh I lost as I made", hsign[1],", you won!")
elif user == hsign[0] and value == hsign[2]:
    print("Oh I have won as I made", hsign[2], ", yay!")
elif user == hsign[1] and value ==hsign[1]:
    print ("We both made a", hsign[1],", its a draw...")
elif user == hsign[1] and value == hsign[0]:
    print ("Oh I lost as I made", hsign[1],", you won!")
elif user == hsign[1] and value == hsign[2]:
    print("Oh I have won as I made", hsign[2], ", yay!")
elif user == hsign[2] and value == hsign[2]:
    print("We both made a", hsign[2], ", its a draw...")
elif user == hsign[2] and value == hsign[0]:
    print("Oh I lost as I made", hsign[0], ", you won!")
elif user == hsign[2] and value == hsign[1]:
    print("Oh I have won as I made", hsign[1], ", yay!")
else:
    print("Text Error")
