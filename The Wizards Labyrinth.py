#The Wizards Labyrinth Version 1.0

#The player must navigate through the labyrinth and make it to The Wizard, making many decisions along the way.

#Author: Jack Lawrence.

#4/23/18 - 5/24/18

import time

global Uname

global Sname

Uname = "dsjfjsopaijnf"

Sname = "akshfdjdks"

def menu():

    valid = False #sets up a loop to automatically return the user to the menu

    while valid == False:

        print('''

        1. New Adventure

        2. Continue Adventure

        3. View the intro again

        4. View Tutorial

        5. Quit 

        ''')

        print("")

        option = input("Select your option, [Enter '1', '2', '3' or '4'] ")

        if option == "1":

            new()

        if option == "2": 

            load()

        if option =="3":

            intro()

        if option =="4":

            tutorial()

        if option =="5":

            quit()

            

        elif option != "1" and option != "2" and option != "3" and option != "4" and option != "5": #Tells the user about options that are invalid

                print("")

                print(option,"Is not an available option, please enter a valid option.")

                print("")

        

def ask(text, choices): #not all functions will have this as of alpha, but they will as of beta.

    done = False

    while done == False:

        choice = input(text)

        if choice in choices:

            return choice

        if choice not in choices:

            print("Very funny... But",choice,"was not a given option.")

            print("")

            time.sleep(2)

def save(x):

   global Uname

   global Sname

   print (Uname)

   print (x)

   area = x 

   new1 = str(Sname+" "+area)  

   new2 = str(Uname+" "+area)

   file1 =open("save.txt","r")

   lines=file1.readlines()

   file1.close()

   file1=open("save.txt","w")

   for line in lines:

       splitline=line.split()

       if splitline[0]!=Uname and splitline[0] !=Sname:

           file1.write(line)

       elif splitline[0]==Uname:

           file1.write(new2)

           print("nerd")

           file1.write('\n')

       elif splitline [0] ==Sname:

           file1.write(new1)

           file1.write('\n')

    

   file1.close()

def load():

  global Sname

  Sname = input("Enter the name of your file ").title()

  file1 = open("save.txt","r",)

  lines=file1.readline()

  while lines:

      new = lines.split()

      if Sname == new[0]:

          print("")

          if new[1] == "1":

              firstA()

          if new[1] =="2a":

              secondA()

          if new[1] =="2b":

              secondB(x)

          if new[1] =="2h":

              second_hound(x)

          if new[1] =="2c":

              secondC(x)

          if new[1] =="3o":

              thirdIntro()

          if new[1] =="3a":

              thirdA()

          if new[1] =="3b":

              thirdB()

          if new[1] =="4a":

              fourthA()

          if new[1] =="4w":

              fourth_wall()

          if new[1] =="4s":

              fourth_spikes()

          if new[1] =="5a":

              fifthA()

          if new[1] =="wizard":

              the_wizard()

          file1.close() 

      lines=file1.readline()

  print("That isn't the name of a save file")



def tutorial():

    print("You will be asked to make many decisions throughout the course of the game.")

    print("")

    time.sleep(4)

    print("You must enter in the number that corresponds with the action you wish to take.")

    print("")

    time.sleep(4)

    print("Do the best you can to make it through the labyrinth, Good luck!")

    print("")

    time.sleep(4)

def intro():

    print("So they sent you to stop the Evil Wizard who has been plaguing the lands? You certainly don't look like much... but looks can be deceiving.")

    print("")

    time.sleep(5)

    print("Well in order to reach him, you'll have to go into the center of his labyrinth. There you will find his tower.")

    print("")

    time.sleep(5)

    print("But beware Adventurer! For this task is much more than just navigating a maze. The Wizard has set up many traps to trick adventurers.")

    print("")

    time.sleep(5)

    print("Even then, simply navigating the labyrinth is no easy task, for if you take one wrong turn you could be lost forever or find yourself staring into the face of a beast!")

    print("")

    time.sleep(8)

    print("Now go forth Adventurer! With your sword and your shield, get to The Wizard and spell his doom.")

    menu()

def new():

  global Uname

  Uname = input("Adventurer! What is your name? [Don't use spaces] [This will be your file name] ").title()

  area = ("1")

  file1 = open("save.txt","r",)

  lines=file1.readline()

  while lines:

      split = lines.split()

      if Uname == split[0]:

          print("Oh sorry it would appear that name is already in the obituary. It would be appreciated if you would go by something else")

          print("So I shall ask again.")

          print("")

          file1.close()

          new() 

      lines=file1.readline()    

  file1 = open("save.txt","a")

  file1.write(Uname)

  file1.write(" ")

  file1.write(area)

  file1.write('\n')

  file1.close()

  print("")

  firstA()

def firstA():

    print("You Arrive at the entrance to the labyrinth, its monolithic doors standing in front of you. An overwhelming dark aura washes over you, sending shivers down your back. There is still time to turn back though.")

    time.sleep(10)

    print("")

    flee = ask("Will you flee now? Knowing what your up against? [1] Or will you push forward and remain vigilant, even if it means never returning home? [2] ",["1","2"])

                                                                                                                                                                    

    if flee == "2":

        print("")

        secondA()

    if flee == "1":

        print("")

        print("And so you fled, running from the overwhelmingly powerful aura.")

        time.sleep(4)

        print("You ran to the hills, built a house and lived out the rest of your days, letting nature supply you with all you need.")

        time.sleep(7)

        print("Eventually, The Wizard reigned supreme over the land you used to call home. But that didn't matter to you anymore.")

        time.sleep(8)

        print("")

        print("The End...")

        time.sleep(5)

def secondA():

    save("2a")

    print()

    print("You open the doors and walk through.")

    time.sleep(3)

    print("The doors suddenly close behind you, making a loud noise.")

    time.sleep(5)

    print("You attempt to open them again, to no avail. You're stuck here now.")

    time.sleep(5)

    secondB(0)

def secondB(x):

    save("2b")

    HH = x

    print("")

    print("You see two different hallways, one on the left, the other on the right.")

    way = ask("Go left [1] or right? [2] ",["1","2"])

    if way =="1":

        second_hound(HH)

    if way =="2":

        secondC(HH)

def second_hound(x):

     save("2h")

     HH= x

     print(HH)

     print("")

     print("You turn the corner and find yourself face to face with a massive beast that emits a dark presence. It is a Hellhound.")

     time.sleep(7)

     print("")

     hound = ask("Will you run away? [1] Or attempt to slay the beast? [2] ",["1","2"]) 

     if hound =="1":

        print("")

        print("You ran away, a wise decision.")

        print("")

        time.sleep(4)

        secondB(HH)

     if hound =="2":

        if HH ==(1):

             print("You thrust your sword into the beast, it lets out a roar of pain before disintegrating.")

             time.sleep(4) 

             thirdIntro()

        if HH==(0):

             print("")

             print("As was to be expected, The Hound wasted no time in eating you.")

             time.sleep(6)

             print("")

             print("Game over...")

def secondC(x):

        save("2c")

        HH=x

        print("")

        print("You turn the corner only to find a dark, empty room.")

        time.sleep(4)

        print("You get a bad feeling about this room.")

        time.sleep(2)

        go = ask("Do you turn back? [1] Or investigate the dark room? [2] ",["1","2"])

        if go =="1":

            print("")

            print("You turned back, returning to the split in the hallways.")

            time.sleep(5)

            secondB(HH)

        if go =="2":

            if HH ==(0):

                print("")

                print("You investigate the room. You notice something in a corner.")

                time.sleep(6)

                print("It is a demon slaying enchantment, it gives your sword the ability to slay demons with ease!")

                print("Other than that however, the room is empty")

                time.sleep(10)

                print("")

                print("You return to the split in the hallways.")

                time.sleep(4)

                secondB(1)

            if HH==(1):

                print("")

                print("You investigate the room. You've already seen all there is too it.")

                time.sleep(6)

                print("")

                print("You return to the split in the hallways.")

                secondB(HH)

def thirdIntro(): #around this time i stopped caring about having sleeps, i'll do those in beta. along with fixing any spelling/grammar errors or just general script touch ups.

    save("3o")

    print("")

    print("With the Hellhound dead you push forward, deeper into the labyrinth.")
    time.sleep(4)
    print("The deeper into its winding halls you go, the darker it becomes.")
    time.sleep(4)
    print("However, the path is slowly becoming lighter...")
    time.sleep(3)
    print("You arrive at the light source, its a pit of lava!")
    time.sleep(3)
    thirdA()

def thirdA():

    save("3a")

    print("You don't spot any way over it, but it may be possible to jump it!")
    print("")
    jump = ask("Will You jump it? [1] or will You further investigate the room? [2] ", ["1","2"])

    if jump == "1":                                                                            

        print("")
        
        print("You decide to jump it. Surprisingly you actually make the jump!")
        time.sleep(4)
        print("You push forward, having made the jump, toward whatever challenge will face You next!")
        time.sleep(5)
        fourthIntro()

    if jump == "2":

        thirdB()

    

def thirdB():

    save("3b")

    print("")

    print("You decide to further investigate. You see a pressure plate on the wall.")
    print("")
    time.sleep(2)
    press = ask("Will you press it? [1] Or leave it be? [2] ")

    if press == "2":

        print("You decide not to press it and further investigate... However there isn't much of anything else.")
        time.sleep(6)
        print("So you turn your attention back toward the pit of lava.")
        time.sleep(3)
        print("")

        thirdA()

    if press == "1":

        print("You decide to press it. You notice the ground shaking and the lava moving. However, the lava isn't moving down, it's moving up!")
        time.sleep(6)
        print("The lava quickly floods the room, completely submerging you.")
        time.sleep(4)
        print("")
        print("Game over...")
        time.sleeep(5)
def fourthIntro():

    print("As you walk further down the winding halls you come to a split.")
    time.sleep(3)
    fourthA()

def fourthA():

    save("4a")

    print("")

    split =ask("Will you go left? [1] Or will you go right? [2] ", ["1","2"])

    if split == "1":

        fourth_spikes()

    if split == "2":

        fourth_wall()



def fourth_wall():

    save("4w")

    print("")

    print("You go right, finding nothing but a dark dead end, however it may still be worth investigating the room.")
    time.sleep(3)
    wall = ask("Will you investigate the room? [1] or will you go back to the split? [2] ", ["1","2"])

    if wall == "1":

        print("")

        print("You search around the room and find nothing... that is until you bump into one of the walls and notice that part of youe body went through it!")
        time.sleep(6)
        print("You walk through the wall and after a short hallway you find a massive wooden door... it's the door to The Wizards Tower!")
        time.sleep(5)
        print("You open the door, it creeks as you do...")
        time.sleep(3)
        print("You look above and see a spiral staircase leading to the top.")
        time.sleep(4)
        fifthA()

    if wall == "2":

        print("")

        print("You turned back, not wanting to risk going into the dark.")
        time.sleep(3)
        print("You arrive back at the split.")
        time.sleep(2)
        fourthA()

    

        

def fourth_spikes():

    save("4s")

    print("")

    print("You go left, and down the hall you find a pit of spikes that appears to be a similar size to the pit of lava.")
    time.sleep(3)
    jump = ask("Will you jump over the pit of spikes [1] or go back to the split? [2] ", ["1","2"])

    if jump == "1":

        print("")

        print("You attempt to jump over the pit, thinking it'd be the same as with the lava.")
        time.sleep(4)
        print("But before your very eyes you see the size of the spike pit nearly triple!")
        time.sleep(4)
        print("What you saw before was merely an illusion created by The Wizard!")
        time.sleep(4)
        print("You fall into the spikes and die a painful and slow death...")
        time.sleep(3)
        print("")
        print("Game Over...")
        time.sleep(5)
    if jump == "2":

        print("")

        print("Something felt peculiar about that pit, so you decided to turn back to the split.")
        time.sleep(4)
        print("You arrive back at the split")
        time.sleep(3)
        fourthA()

    

def fifthA():

    save("5a")

    print("")
   
    print("Slowly you climb the spiral staircase...")
    time.sleep(3)
    print("The air feels as if it's getting heavier")
    time.sleep(2)
    print("The Wizards power can be felt at full force, it's overwhelming.")
    time.sleep(4)
    print("Finally you reach the top.")
    time.sleep(1)
    print("You and the wizard meet face to face, his big red robe and cloak hide his appearance.")
    time.sleep(5)
    print('"Hello... I have been watching you carefully, no other adventurer has been able to reach me."')
    time.sleep(5)
    print('"And for that I give to you an opportunity..."')
    time.sleep(2)
    print('"Join me and together we will rule supreme over this world."')
    time.sleep(3)
    wiz = ask("Will you join The Wizard [1] or raise your weapon to fight him? [2] ", ["1","2"])

    if wiz == "1":

        print("You decided to take The Wizard up on his offer.")
        time.sleep(3)
        print("With The Wizard's magic and your strength nobody could stop you.")
        time.sleep(4)
        print("In a matter of years you two reigned supreme over the entire world.")
        time.sleep(5)
        print("")
        print("The End...")
        time.sleep(8)
    if wiz == "2":

        the_wizard()

def the_wizard():

    save("wizard")

    print("")

    print("You raise your weapon, ready to fight.")
    time.sleep(3)
    print('"So that\'s how it is... A shame."')
    time.sleep(2)
    print('"Well so be it! Prepare to di-"')
    time.sleep(1)
    print("While The Wizard was talking you stabbed him in the heart.")
    time.sleep(2)
    print('"GAAAAAH. I *huff* was a fool *cough* and in my arrogance I let my guard down."')
    time.sleep(4)
    print("The Wizard starts coughing up blood and moments later he dies...")
    time.sleep(2)
    print("")

    print("You return home, celebrated as a hero, with praise from the town.")
    time.sleep(3)
    print("You see the people of the town happy, knowing that they no longer have to worry about The Wizard.")
    time.sleep(4)
    print("")

    print("The End.")
    time.sleep(6)
intro()
