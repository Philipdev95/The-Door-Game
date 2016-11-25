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
    
def chooseDoor():
    doorlist = [
        'Första', 'Andra', 'Tredje'
    ]
    print ("Its time to choose your first door!")
    print ("Det finns 3 dörrar framför dig.")
    time.sleep(0.6)
    print ("Välj mellan 1, 2 eller 3. Eller skriv random för att låta oss välja!")
    dc = input ("Ditt val: ")
    if dc is 1:
        print ("Du har valt dörr nummer 1")
        
    elif dc is 2:
        print ("Du har valt dörr nummer 2")
        
    elif dc is 3:
        print ("Du har valt dörr nummer 3")
        
    else: 
        print ("...")
        time.sleep(0.5)
        '''kör om frågan'''
    
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
    
menu()