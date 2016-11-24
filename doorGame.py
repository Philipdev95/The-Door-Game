#-*- coding: utf-8 -*-
import time
class Doors:
    def __init__(self, doorNr, doorHp, playerHp):
        self.doorNr = doorNr
        self.doorHp = doorHp
        self.playerHp = playerHp
        
    def attack_door(self, doorNr):
        '''Om man som anvndare ska kunna attackera dörrar för att kunna öppna dem?'''
        pass

    
def one():
    print (35*"-")
    print (10*" " + " W E L C O M E ")
    time.sleep(0.4)
    print (10*" " + "    TO THE    ")
    time.sleep(0.4)
    print (10*" " + "  DOOR  GAME  ")
    time.sleep(0.4)
    print (35*"-")
    
    
    
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