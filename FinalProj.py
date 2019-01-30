from random import *

mon_def = 9
mon_health = randint(10,12)
print("Monster Start Health:" + str(mon_health))
p_dex = randint(1, 3)
p_str = randint(1, 3)
print("Player Strength: " + str(p_str))
p_con = randint(1, 3)
p_int = randint(1, 3)
p_wis = randint(1, 3)
p_cha = randint(1, 3)

roll_20 = randint(1,20)
input = input("do you want to attack?")
while (input) == "a":
    input_2 = input("Do you want to attack?")
    if input_2 is "a":
        roll_20 = int(randint(1,20))
        p_attack = roll_20 + p_str
        print("Roll 20: " + str(roll_20))
        print("Player Strength: " + str(p_str))
        if p_attack > mon_def:
            roll_8 = randint(1,8)
            print("You dealt " + str(roll_8) + " damage!")
            mon_health = mon_health - roll_8
            print("Monster Health: " + str(mon_health))
        else:
            print("You missed!")
