from random import randint

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890"

"""
This function takes an input of a String and outputs the String
without numbers and punctuation.
"""
def clean( input ):
  clean = ""
  for character in input:
    if character in alphabet:
      clean += character
  return clean.lower()

short_map = {
    "h" : "help",
    "n" : "north",
    "s" : "south",
    "e" : "east",
    "w" : "west",
    "l" : "look",
    "i" : "inventory"
}

def short( command ):
    command = clean(command)
    if command in short_map:
        return short_map[command]
    return command

scenes = {
    "Town_Square" : {
        "description" : "This is a town square. There are villagers milling about. There is a clock tower in the center.",
        "commands" : [ "north", "south", "east", "west", "look", "attack villager" ] ,
    },
    "hallway" : {
        "description" : "You find yourself in a long hallway. At the north end is a goblin, it may be dead already.",
        "commands" : [ "north", "south", "look", "attack" ],
    },
    "vault" : {
        "description" : "Behind the dead goblin, you find a big vault. The only interesting feature is a big button on the front that says \"Do not press me.\"",
        "commands" : [ "south", "press button" ],
    },
    "Great_Hall" : {
        "description" : "You enter the Great Hall, inside is a long table with chairs all around it. At the head sits a depressed man, who seems to be a Baron. There are rooms all arund the hall.",
        "commands" : [ "north", "south", "look", "talk to baron" ],
    }
}

playerScene = "Town_Square"
playerHealth = 100
playerPoints = 0
playerHasKilledGoblin = False

# The brains of the operation
def runScene():

    # Make sure the player is alive
    if( playerHealth > 0 ):
        # Print the current scene's description
        print( scenes[playerScene]["description"] )
        print( "" )
        # Accept input from the user
        command = short(input("What would you like to do: "))
        print( "" )

        # If our command is help, print the list of commands available
        if( command == "help" ):
            print( scenes[playerScene]["commands"] )
            print( "" )
            runScene()
        # Check if the command is in the list of available commands, run it if it is
        elif( command in scenes[playerScene]["commands"] ):
            runCommand( playerScene, command )
        # Uh, we don't understand that command, let the player know and move on
        else:
            print("Sorry, this scene does not support that command.")
            print( "" )
            runScene()
    # Our player is dead
    else:
        print( "You've lost the game, you are terrible. And dead." )
        print( "" )

# Defining all the logic and command responses
def runCommand(scene,command):

    # These are global variables which we want to modify globally
    global playerScene, playerHealth, playerPoints, playerHasKilledGoblin

    # Our start scene and each command available
    if( scene == "Town_Square" ):
        if( command == "north" ):
            print( "You go north." )
            print( "" )
            playerScene = "Great_Hall"
            runScene()
        elif( command == "south" ):
            print( "You go south." )
            print( "" )
            playerScene = "Wall"
            runScene()
        elif( command == "west" ):
            print( "You go west." )
            print( "" )
            print( "You are stopped at the city wall, you can't go further. You return to the town square." )
            runScene()
        elif( command == "east" ):
            print( "You go east." )
            print( "" )
            playerScene = "Inn"
            runScene()
        elif( command == "attack villager" ):
            print( "You attack the nearest villager." )
            print( "" )
            runScene()
    # The hallway scene
    elif( scene == "hallway" ):
        if( command == "south" ):
            print( "Like a total wuss, you run back to the room your started in." )
            print( "" )
            playerScene = "start"
            runScene()
        elif( command == "north" ):
            # A little logic based on whether the player has killed the goblin
            if( playerHasKilledGoblin ):
                print( "You can proceed." )
                print( "" )
                playerScene = "vault"
                runScene()
            else:
                print( "You attempt to pass the goblin, but he attacks you and you get hurt." )
                print( "" )
                playerHealth = playerHealth - 50
                runScene()
        elif( command == "attack" ):
            print( "Like a maniac you attack the goblin, it was an easy fight and you kill the goblin. You got 100 points!" )
            print( "" )
            playerHasKilledGoblin = True
            playerPoints = playerPoints + 100
            runScene()
        elif( command == "look" ):
            print( "You take your time to look around. While you sit there like an idiot, the goblin attacks and hurts you." )
            print( "" )
            playerHealth = playerHealth - 50
            runScene()

    # The vault scene
    elif( scene == "Great_Hall" ):
        if( command == "south" ):
            print( "You return to the town square." )
            print( "" )
            playerScene = "Town_Square"
            runScene()
        elif( command == "talk to baron" ):
            print( "You approach the depressed man. He seem to be a baron. He asks you for help. He needs someone to deliver to the head of the Red Knights a sealed message." )
            scenes["Great_Hall"]["commands"].append("take paper");
            print( "" )
            playerScene = "Town_Square"
            runScene()
        elif( command == "press button" ):
            print( "You hear a loud voice shout \"Time to open the Vault!\" Followed by a loud cranking sound." )
            print( "" )
            randoCalrissian = randint(1,10)
            print( "Your random number is " + str(randoCalrissian) )
            print( "" )
            if( randoCalrissian > 8 ):
                print( "You have won the game! A million points is awarded to you!" )
                print( "" )
                playerPoints = playerPoints + 1000000
            else:
                print( "Nothing else happens and you feel slightly hurt." )
                print( "" )
                runScene()
    else:
        print( "Scene not found, error." )

# The opening description for the game, along with some simple instructions
print("Welcome to Interactive Fiction Starter: The Game!\n\nYour task is to navigate through these rooms and discover all the secrets you can.")
print( "" )
print( "If you need help at any time, type help." )
print( "" )

# Let's go right into the game, this function is recursive and will keep calling itself until we win or lose
runScene()

# We broke out of the "game loop" so let's output the final score
print( "Your final score is: " + str(playerPoints) )
print( "" )
print( "Thanks for playing!" )
