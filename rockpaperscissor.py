#program that implements Rock paper scissor game

import random
input_dict = {0: "Rock",
              1: "Paper",
              2: "Scissor"}

list1 = [[1, 0], [0, 2], [2, 1]]
print("\n0. Rock \n1. Scissor \n2. Paper \n3.Quit")

ucount, ccount  = 0, 0

while True:
    listc = []
    computer = random.randint(0, 2)
    choice = int(input("Enter a choice"))
    if choice > 2:
        print("Game quits")
        if ucount == ccount: print("Draw")
        else:
            if ucount > ccount: print("User wins")
            else: print("Computer wins")
        exit()
    listc.append(choice)
    listc.append(computer)
    print("User selected:: " + input_dict[choice] + "\ncomputer selected::" + input_dict[computer])
    if (choice == computer): print("Draw")
    else:
        if listc in list1:
            print("User wins")
            ucount += 1
        else:
            print("Computer wins")
            ccount += 1








'''            
import random
input_dict = {0: "Rock",
              1: "Paper",
              2: "Scissor"}
com = random.randint(0, 2)
user = int(input("INPUT:: \n 0. For rock \n 1. For Paper \n 2. For scissor"))

if user > 2:
    print("Invalid")
    exit()

res = (3 + user - com) % 3
if res == 0: print("draw")
if res == 1: print("you win")
if res == 2: print("computer wins")

'''


