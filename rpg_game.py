import random

# define the game variables
player_name = input("What is your name? ")
player_health = 100
monster_name = "Evil Goddess"
monster_health = 100

# define the game functions
def attack(target):
    damage = random.randint(1, 15)
    print(f"{player_name} attacks {target} for {damage} damage!")
    return damage

# start the game loop
while player_health > 0 and monster_health > 0:
    # print the current game status
    print(f"{player_name} (health: {player_health}) vs {monster_name} (health: {monster_health})")
    
    # ask the player what they want to do
    action = input("What do you want to do? (attack or defend) ")
    
    # handle the player's choice
    if action == "attack":
        damage = attack(monster_name)
        monster_health -= damage
    elif action == "defend":
        print(f"{player_name} defends!")
    else:
        print("Invalid action.")
        continue
    
    # handle the monster's turn
    if monster_health > 0:
        damage = attack(player_name)
        player_health -= damage
    
# print the final game result
if player_health > 0:
    print(f"{player_name} wins!")
else:
    print(f"{monster_name} wins!")

    