from tkinter import *
import random

winRoll = Tk()
#set geometry and other features
winDice = Tk()
#set geometry and other features

#variables
dAmountA = 5
dAmountB = 5
num_sides = StringVar() #put num_sides next to the dropdown list
num_sides.set("6 sides")

#Die Values
d_1A_Val = 0
d_2A_Val = 0
d_3A_Val = 0
d_4A_Val = 0
d_5A_Val = 0
d_1B_Val = 0
d_2B_Val = 0
d_3B_Val = 0
d_4B_Val = 0
d_5B_Val = 0

#All functions for the program

def rollDice():
    #function for rolling dice
    randomListA =[]
    randomListA.clear()
    randomListB = []
    randomListB.clear()
    
    dCounterA = dAmountA
    dCounterB = dAmountB
    
    
    if num_sides == "2 sides":
        sides = 2
    elif num_sides == "3 sides":
        sides = 3
    elif num_sides == "4 sides":
        sides = 4
    elif num_sides == "8 sides":
        sides = 8
    elif num_sides == "10 sides":
        sides = 10
    elif num_sides == "12 sides":
        sides = 12
    else:
        sides = 6
    

    dCounterA = dAmountA    
    while dCounterA > 0:
        randomListA.append(random.randint(1,sides))
        dCounterA -= 1
        
    dCounterB = dAmountB
    while dCounterB > 0:
        randomListB.append(random.randint(1,sides))
        dCounterB -= 1
        
    print(randomListA[0])
    print(randomListB[0])
    
    
    if randomListA[0] > 0:
        d_1A_Val = randomListA[0]
        dLabel1.config(text=d_1A_Val)

def clearAll():
    # brings all fields to default values, just like starting a new program
    return



def change_Num_Dice():
    #increases or decreases the number of dice for either Row A or B
    return








#Widgets for Dice Window Row A
plus_RowA_button = Button(winDice, text="+").grid(row=0, column=7)
minus_RowA_button = Button(winDice, text="-").grid(row=0, column=5)
dice_RowA_label = Label(winDice, text="# of dice first row").grid(row=0, column=6)
tvalue_RowA_label = Label(winDice, text="Total Value").grid(row=2, column=6)

#Widgets for Dice Window Row B
plus_RowB_Button = Button(winDice, text="+").grid(row=3, column=7)
minus_RowB_Button = Button(winDice, text="-").grid(row=3, column=5)
dice_RowB_label = Label(winDice, text="# of dice second row").grid(row=3, column=6)
tvalue_RowB_label = Label(winDice, text="Total value").grid(row=5, column=6)

#Labels for all 10 dice in Dice Window
dLabel1 = Label(winDice, text=d_1A_Val).grid(row=0, column=0)
dLabel2 = Label(winDice, text=d_2A_Val).grid(row=0, column=1)
dLabel3 = Label(winDice, text=d_3A_Val).grid(row=0, column=2)
dLabel4 = Label(winDice, text=d_4A_Val).grid(row=0, column=3)
dLabel5 = Label(winDice, text=d_5A_Val).grid(row=0, column=4)
dLabel6 = Label(winDice, text=d_1B_Val).grid(row=3, column=0)
dLabel7 = Label(winDice, text=d_2B_Val).grid(row=3, column=1)
dLabel8 = Label(winDice, text=d_3B_Val).grid(row=3, column=2)
dLabel9 = Label(winDice, text=d_4B_Val).grid(row=3, column=3)
dLabel0 = Label(winDice, text=d_5B_Val).grid(row=3, column=4)

#Widgets on Roll Window
myButton1 = Button(winRoll, text="ROLL DICE", command=rollDice).grid(row=2, column=2)
myButton2 = Button(winRoll, text="Clear All", command=clearAll).grid(row=1, column=2)
sidesDrop = OptionMenu(winRoll, num_sides, "2 sides", "3 sides", "4 sides", "6 sides", "8 sides", "10 sides", "12 sides").grid(row=0, column=0)


#Main loop of program
winDice.mainloop()