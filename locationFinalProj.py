game = True
game_time = True
import time
location = "Town_square"
name = "Maeth"

while game == True:
    if location == "Town_square":
        if game_time == True:
            print("A magical knight battles a warlord. The crowd arround you cheers. The sun beat down relentlessly.")
            print("*Kaboom*")
            print("--------------")
            time.sleep(0.5)
            print("--------------")
            time.sleep(1)
            print("Find me " + name + " for you are of pure heart.")
            print("--------------")
            time.sleep(2)
            print("--------------")
            game_time = False
        if game == True:
            print("")
            print("Criaf, your friend from hometown stands above you.")
            input(name + ", are you okay?")
            follow_him = input("That explosion was crazy! I think we should head to the inn before something bad happens. What do you think? ")
            if follow_him == "ok" or "yes" or "follow":
                print("You follow him.")
                location = "inn"
                criaf_location = "inn"
            elif follow_him == "look":
                print("The town square is in chaos, people are running from the arena. The knight, and warlord are nowhere to be found. ")
                print("Criaf heads back to the inn to the east")
                criaf_location = "inn"
            elif follow_him == "no":
                print("Ok, maeth, I will see you there later.")
                print("Criaf heads back to the inn to the east.")
                criaf_location = "inn"
            elif
    if location == "inn":
        print("You approach a large inn.")
        char_inn = input("")
        if char_do == "n":
