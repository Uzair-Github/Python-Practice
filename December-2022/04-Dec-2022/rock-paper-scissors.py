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

#rock vs rock
if user == hsign[0] and value == hsign[0]:
    print("We both made a", hsign[0], ", its a draw...")
#rock vs paper
elif user == hsign[0] and value == hsign[1]:
    print ("Oh I lost as I made", hsign[1],", you won!")
#rock vs scissors
elif user == hsign[0] and value == hsign[2]:
    print("Oh I have won as I made", hsign[2], ", yay!")
#paper vs paper
elif user == hsign[1] and value ==hsign[1]:
    print ("We both made a", hsign[1],", its a draw...")
#paper vs rock
elif user == hsign[1] and value == hsign[0]:
    print ("Oh I lost as I made", hsign[0],", you won!")
#paper vs scissors
elif user == hsign[1] and value == hsign[2]:
    print("Oh I have won as I made", hsign[2], ", yay!")
#scissors vs scissors
elif user == hsign[2] and value == hsign[2]:
    print("We both made a", hsign[2], ", its a draw...")
#scissors vs rock
elif user == hsign[2] and value == hsign[0]:
    print("Oh I lost as I made", hsign[0], ", you won!")
#scissors vs paper
elif user == hsign[2] and value == hsign[1]:
    print("Oh I have won as I made", hsign[1], ", yay!")
else:
    print("Text Error")
