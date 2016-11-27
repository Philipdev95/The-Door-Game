#-*- coding: utf-8 -*-
import time
import random


'''
class Doors:
    def __init__(self, doorNr, doorHp, playerHp):
        self.doorNr = doorNr
        self.doorHp = doorHp
        self.playerHp = playerHp
        
    def attack_door(self, doorNr):
        Om man som anvndare ska kunna attackera dörrar för att kunna öppna dem?
        pass
'''
def openDoor(num):
    #treasure or nah
    skattchans = [
        "en SKATT!", 
        "fler dörrar.", 
        "fler dörrar.", 
        "fler dörrar.",
        "fler dörrar."
    ]
    ton = random.choice(skattchans)
    if ton == " fler dörrar.":
        print ("Du öppnar dörr nr " + str(num) + ".")
        print ("Bakom dörren finns...")
        time.sleep(0.3)
        print (".")
        time.sleep(0.3)
        print (".")
        time.sleep(0.3)
        print (".")
        time.sleep(0.3)
        print ("..." + str(ton))
        

def chooseDoor():
    doorlist = [
        1, 2, 3
    ]
    print ("Its time to choose your first door!")
    print ("Det finns 3 dörrar framför dig.")
    time.sleep(0.6)
    print ("Välj mellan 1, 2 eller 3. Eller skriv random för att låta oss välja!")
    doorChoice(doorlist)
    
def doorChoice(doorlist):
    dc = input ("Ditt val: ")
    if dc is 1 or dc == 2 or dc == 3:
        print ("Du har valt dörr nummer " + str(dc))
        openDoor(dc)
    elif dc is "random":
        rVal = random.choice(doorlist)
        if rVal is 1 or rVal == 2 or rVal == 3:
            print ("Vi har valt dörr nummer " + str(rVal))
            openDoor(rVal)
    else:
        print ("...")
        time.sleep(0.5)
        print (30*"#")
        print ("Nånting gick fel")
        print (30*"#")
        doorChoice()
    #print (random.choice(doorlist))
    
def one():
    print (35*"-")
    print (10*" " + " W E L C O M E ")
    time.sleep(0.4)
    print (10*" " + "    TO THE    ")
    time.sleep(0.4)
    print (10*" " + "  DOOR  GAME  ")
    time.sleep(0.4)
    print (35*"-")
    time.sleep(1.5)
    chooseDoor()
    
    
def menu():
    print ("1. Starta Spelet")
    print ("2. Statistik")
    print ("3. Avsluta")
    menuval()
def menuval():
    mv = input("Ditt val: ")
    if mv is 1:
        one()
    elif mv is 2:
        two()
    elif mv is 3:
        exit()
    else:
        time.sleep(0.5)
        print ("Oj! Vad har hänt?")
        time.sleep(0.5)
        print ("Försök igen!")
        time.sleep(0.5)
        menu()
menu()