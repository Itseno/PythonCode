game = True
game_time = True
location = "Town_square"
name = "John"

while game == True:
    if location == "Town_square":
        if game_time == True:
            print("A magical knight battles a warlord. The crowd arround you cheers. The sun beat down relentlessly.")
            print("*Kaboom*")
            print("--------------")
            print("Find me " + name + " for you are of pure heart.")
            print("--------------")
            game_time = False
        if game == True:
            print(name + ", are you okay?")
            print("")
            print("Criaf, your friend from hometown stands above you.")
            follow_him = input(name + ", are you okay? Let's head back to the inn.")
            if follow_him == "ok":
                print("You follow him.")
                location = "inn"
            elif follow_him == "look":
                print("The town square is in chaos, people are running from the arena. The knight, and warlord are nowhere to be found.")
                print("John heads back to the inn to the east.")
            elif follow_him == "No":
                print("What? Please John.")
    if location == "inn":
        print("You approach an inn.")
