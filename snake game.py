# sanjay code 
import random
win=0
lose=0
counter=5
while(counter >0):
    print("\n WELCOME TO GAME WITH SANJAY\n")
    print(" plz select from menu to play the game\n"
          "snake,gun and water\n")
    list1=["snake","gun","water"]
    ran=random.choice(list1)

    string1=input("enter the string from above menu:")
    if ran=="water" and string1=="snake":
        print("you will win")
        win=win+1
        counter=counter-1


    elif ran == "gun" and string1 == "water":
     print("you will win")
     win = win + 1
     counter = counter - 1

    elif ran == "snake" and string1 == "gun":
        print("you will win")
        win = win + 1
        counter = counter - 1
    elif(ran==string1):
        print("you are in equal")
        counter = counter - 1
    else:
     lose = lose + 1
     print("you will lose")
     counter = counter - 1
    print(" chance left",counter)

print("\n-------------------------\n")
print("your score is ",win)
print("computer score is",lose)
if(win>lose):
    print("you won the match")
elif(win==lose):
    print("match is draw")
else:
    print("you lose the match")
