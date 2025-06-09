from turtledemo.paint import switchupdown

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input("You can go left or right.\nWhich direction would you like to go?"
                 "\nType L for left or R for right\n").lower()

if choice_1 == "l":
    choice_2 = input("You are at a river.\nYou can swim or wait for a boat."
                     "\nType swim or wait\n")
    if choice_2 == "wait":
        choice_3 = input("The boat took you to a castle.\n"
                         "There are three doors.\nChoose red, yellow, or blue\n")
        if choice_3 == "red":
            print("You were burned by fire. You are dead.")
        elif choice_3 == "blue":
            print("You were eaten by beasts. You are dead.")
        elif choice_3 == "yellow":
            print("Congratulations! You won!")
        else:
            print("You lost.")
    else:
        print("You were eaten by a kraken. You are dead.")
else:
    print("You fell off a cliff. You are dead.")