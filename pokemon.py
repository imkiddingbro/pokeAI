import time
import numpy as np 
import sys
import random

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
        
def remove(string):
    return string.replace(" ", "")        
class Pokemon:
    # Initializing Pokemon
    def __init__(self, name, types, moves, stats):
        self.name = name
        self.types = types
        self.moves = moves
        self.hp = stats['HP']
        self.attack = stats['ATTACK']
        self.defense = stats['DEFENSE']
        self.special_attack = stats['SPECIAL_ATTACK']
        self.special_defense = stats['SPECIAL_DEFENSE']
        self.speed = stats['SPEED']

        
    def fight(self, Pokemon2):
        
        # Variable Initialization
        player_start_health = self.hp
        opponent_start_health = Pokemon2.hp
        base_move_power = 50
        move_dmg = int
        
        # Effective Strings
        string_1_attack = '\nNot very effective...\n' 
        string_2_attack = '\nSuper effective!!\n'
        
        print("\n----POKEMON DUEL----")
        
        print(f"\n{remove(self.name)}", "| LVL",random.randint(1,100))
        print("TYPE |", self.types,"\n")
        
        print("HP/", self.hp)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("SPECIAL ATTACK/", self.special_attack)
        print("SPECIAL DEFENSE/", self.special_defense)
        print("SPEED/", self.speed)
        
        print("\nVS")
        
        print(f"\n{remove(Pokemon2.name)}","| LVL",random.randint(1,100))
        print("TYPE |", Pokemon2.types,"\n")
        
        print("HP/", Pokemon2.hp)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("SPECIAL ATTACK/", Pokemon2.special_attack)
        print("SPECIAL DEFENSE/", Pokemon2.special_defense)
        print("SPEED/", Pokemon2.speed)
        
        time.sleep(1.5)
        
        # The above code snippet is implementing a battle simulation between two Pokemon. It uses a
        # while loop to continue the battle until one of the Pokemon's health points (hp) drops below
        # 0. Within the loop, it displays the health of both Pokemon, allows the user to choose a
        # move, calculates the damage based on the move selected (physical or special), and then
        # pauses for 1 second before proceeding. The battle ends when either Pokemon's health drops
        # below 0.
        # While loop for battle, ends when pokemon drops below 0              
        while (self.hp > 0) and (Pokemon2.hp > 0):
            
            # Check for beginning of match and display health
            if Pokemon2.hp == opponent_start_health: 
                print(f"\n{self.name}\tHP ","|"*self.hp)
                print(f"{Pokemon2.name}\tHP ","|"*Pokemon2.hp,"\n")         
 
            # User chooses move
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('\nPick a move: '))
            
            if(index <= 2): # Physical Move Selected
                move_dmg = int(base_move_power* (self.attack/Pokemon2.defense))
            else: # Special Move Selected
                move_dmg = int(base_move_power*(self.special_attack/Pokemon2.special_defense)) 
            
            time.sleep(1)
            
            # Speed check for first turn
            if(self.speed >= Pokemon2.speed):
                
                print(f"\n{remove(self.name)}'s turn!")
                delay_print(f"\n{remove(self.name)} used {self.moves[index-1]}!")
                delay_print(string_1_attack)
            
                Pokemon2.hp -= move_dmg
                print(f"\n{remove(Pokemon2.name)} took",int(move_dmg),"damage")
                
                time.sleep(1)
                            
                if Pokemon2.hp <= 0:
                    delay_print("\n..." + remove(Pokemon2.name) + ' fainted.')
                    break
                
                print(f"\n{self.name}\tHP ","|"*int(self.hp))
                print(f"{Pokemon2.name}\tHP ","|"*int(Pokemon2.hp),"\n")
                
            # Pokemon2 AI's turn
                
            print(f"\n{remove(Pokemon2.name)}'s turn!")
                
                # If you wanted to play like an actual game, then this would implementation would be uncommented.
                
                #for i, x in enumerate(Pokemon2.moves):
                    #print(f"{i+1}.", x)
                #index = int(input('\nPick a move: '))
                
            time.sleep(1)
                
            # Calculate opponents lower defense stat
            if(self.defense>self.special_defense): # Lower Physical Defense
                delay_print(f"\n{remove(Pokemon2.name)} used {Pokemon2.moves[random.randint(2, 3)]}!")
                move_dmg = int(2*base_move_power*(Pokemon2.special_attack/self.special_defense)) # 2x for super effective
                self.hp -= move_dmg
                time.sleep(1)
                delay_print(string_2_attack)
                print(f"\n{remove(self.name)} took",int(move_dmg),"damage")
            else: # Lower Special Defense
                delay_print(f"\n{remove(Pokemon2.name)} used {Pokemon2.moves[random.randint(0, 1)]}!")
                move_dmg = int(2*base_move_power*(Pokemon2.attack/self.defense)) # 2x for super effective
                self.hp -= move_dmg
                time.sleep(1)
                delay_print(string_2_attack)
                print(f"\n{remove(self.name)} took",int(move_dmg),"damage")        
            
            time.sleep(1)
            
            print(f"\n{self.name}\tHP ","|"*int(self.hp))
            print(f"{Pokemon2.name}\tHP ","|"*int(Pokemon2.hp),"\n")
        
        # Battle has ended        
        money = random.randint(10, 1000)
        if(self.hp<=0): # User won battle
            delay_print("\n..." + remove(self.name) + ' fainted.\n')
            delay_print(f"\nYou paid the AI ${money}.\n")
        elif(Pokemon2.hp<=0): # AI won battle
            delay_print("\n..." + remove(Pokemon2.name) + ' fainted.\n')
            delay_print(f"\nThe Ai has paid you ${money}.\n")
            
if __name__ == '__main__':
    # Pokemon List
    list = []
    
    list.append(Pokemon('Eevee     ',
                        'Normal', 
                        ['Tackle | Physical', 'Take Down | Physical', 'Hyper Voice | Special', 'Hyper Beam | Special'],
                        {'HP':55,
                         'ATTACK':55,
                         'DEFENSE':50,
                         'SPECIAL_ATTACK':45,
                         'SPECIAL_DEFENSE':65, 
                         'SPEED':55}))
    
    list.append(Pokemon('Flareon   ',
                        'Fire', 
                        ['Flame Charge | Physical', 'Fire Fang | Physical', 'Ember | Special', 'Flamethrower | Special'],
                        {'HP':65,
                         'ATTACK':130,
                         'DEFENSE':60,
                         'SPECIAL_ATTACK':95,
                         'SPECIAL_DEFENSE':110, 
                         'SPEED':65}))
    
    list.append(Pokemon('Vaporeon  ',
                        'Water', 
                        ['Aqua Tail | Physical', 'Dive | Physical', 'Bubble | Special', 'Water Pulse | Special'],
                        {'HP':130,
                         'ATTACK':65,
                         'DEFENSE':60,
                         'SPECIAL_ATTACK':110,
                         'SPECIAL_DEFENSE':95, 
                         'SPEED':65}))
    
    list.append(Pokemon('Jolteon   ',
                        'Electric', 
                        ['Spark | Physical', 'Thunder Fang | Physical', 'Discharge | Special', 'Thunder | Special'],
                        {'HP':65,
                         'ATTACK':65,
                         'DEFENSE':60,
                         'SPECIAL_ATTACK':110,
                         'SPECIAL_DEFENSE':95, 
                         'SPEED':130}))
    
    list.append(Pokemon('Leafeon   ',
                        'Grass', 
                        ['Leaf Blade | Physical', 'Razor Leaf | Physical', 'Magical Leaf | Special', 'Frenzy Plant | Special'],
                        {'HP':65,
                         'ATTACK':110,
                         'DEFENSE':130,
                         'SPECIAL_ATTACK':60,
                         'SPECIAL_DEFENSE':65, 
                         'SPEED':95}))
    
    list.append(Pokemon('Glaceon   ',
                        'Ice', 
                        ['Avalanche | Physical', 'Ice Fang | Physical', 'Icy Wing | Special', 'Ice Beam | Special'],
                        {'HP':65,
                         'ATTACK':60,
                         'DEFENSE':110,
                         'SPECIAL_ATTACK':130,
                         'SPECIAL_DEFENSE':95, 
                         'SPEED':65}))
    
    list.append(Pokemon('Lucario   ',
                        'Fighting', 
                        ['Low Kick | Physical', 'Focus Punch | Physical', 'Focus Blast | Special', 'Aura Sphere | Special'],
                        {'HP':70,
                         'ATTACK':110,
                         'DEFENSE':70,
                         'SPECIAL_ATTACK':115,
                         'SPECIAL_DEFENSE':70, 
                         'SPEED':90}))
    
    list.append(Pokemon('Drapion   ',
                        'Poison', 
                        ['Cross Poison | Physical', 'Cross Poison | Physical', 'Sludge Bomb | Special', 'Venoshock | Special'],
                        {'HP':70,
                         'ATTACK':90,
                         'DEFENSE':110,
                         'SPECIAL_ATTACK':60,
                         'SPECIAL_DEFENSE':75, 
                         'SPEED':95}))
    
    list.append(Pokemon('Hippowdon ',
                        'Ground', 
                        ['Dig | Physical', 'Earthquake | Physical', 'Mud Bomb | Special', 'Earth Power | Special'],
                        {'HP':108,
                         'ATTACK':112,
                         'DEFENSE':118,
                         'SPECIAL_ATTACK':68,
                         'SPECIAL_DEFENSE':72, 
                         'SPEED':47}))
    
    list.append(Pokemon('Staraptor ',
                        'Flying', 
                        ['Aerial Ace | Physical', 'Brave Bird | Physical', 'Hurricane | Special', 'Air Slash | Special'],
                        {'HP':85,
                         'ATTACK':120,
                         'DEFENSE':70,
                         'SPECIAL_ATTACK':50,
                         'SPECIAL_DEFENSE':60, 
                         'SPEED':100}))
    
    list.append(Pokemon('Espeon    ',
                        'Psychic', 
                        ['Psychic Fangs | Physical', 'Zen Headbutt | Physical', 'Psychic | Special', 'Psybeam | Special'],
                        {'HP':65,
                         'ATTACK':65,
                         'DEFENSE':60,
                         'SPECIAL_ATTACK':130,
                         'SPECIAL_DEFENSE':95, 
                         'SPEED':110}))
    
    list.append(Pokemon('Kricketune',
                        'Bug', 
                        ['Pin Missile | Physical', 'Mega Horn | Physical', 'Bug Buzz | Special', 'Signal Beam | Special'],
                        {'HP':77,
                         'ATTACK':85,
                         'DEFENSE':51,
                         'SPECIAL_ATTACK':55,
                         'SPECIAL_DEFENSE':51, 
                         'SPEED':65}))
    
    list.append(Pokemon('Regirock  ',
                        'Rock', 
                        ['Smack Down | Physical', 'Rock Blast | Physical', 'Power Gem | Special', 'Ancient Power | Special'],
                        {'HP':80,
                         'ATTACK':100,
                         'DEFENSE':200,
                         'SPECIAL_ATTACK':50,
                         'SPECIAL_DEFENSE':100, 
                         'SPEED':50}))
    
    list.append(Pokemon('Gengar    ',
                        'Ghost', 
                        ['Astonish | Physical', 'Shadow Claw | Physical', 'Shadow Ball | Special', 'Ominous Wind | Special'],
                        {'HP':60,
                         'ATTACK':65,
                         'DEFENSE':60,
                         'SPECIAL_ATTACK':130,
                         'SPECIAL_DEFENSE':75, 
                         'SPEED':110}))
    
    list.append(Pokemon('Regidraco ',
                        'Dragon', 
                        ['Dragon Claw | Physical', 'Dragon Tail | Physical', 'Draco Meteor | Special', 'Dragon Pulse | Special'],
                        {'HP':200,
                         'ATTACK':100,
                         'DEFENSE':50,
                         'SPECIAL_ATTACK':100,
                         'SPECIAL_DEFENSE':50, 
                         'SPEED':80}))
    
    list.append(Pokemon('Umbreon   ',
                        'Dark', 
                        ['Crunch | Physical', 'Foul Play | Physical', 'Dark Pulse | Special', 'Snarl | Special'],
                        {'HP':95,
                         'ATTACK':65,
                         'DEFENSE':110,
                         'SPECIAL_ATTACK':60,
                         'SPECIAL_DEFENSE':130, 
                         'SPEED':65}))
    
    list.append(Pokemon('Registeel ',
                        'Steel', 
                        ['Gyro Ball | Physical', 'Bullet Punch | Physical', 'Flash Cannon | Special', 'Mirror Shot | Special'],
                        {'HP':80,
                         'ATTACK':75,
                         'DEFENSE':150,
                         'SPECIAL_ATTACK':75,
                         'SPECIAL_DEFENSE':150, 
                         'SPEED':50}))
    
    list.append(Pokemon('Sylveon   ',
                        'Fairy', 
                        ['Play Rough | Physical', 'Fairy Fang | Physical', 'Moonblast | Special', 'Fairy Wind | Special'],
                        {'HP':95,
                         'ATTACK':65,
                         'DEFENSE':65,
                         'SPECIAL_ATTACK':110,
                         'SPECIAL_DEFENSE':130, 
                         'SPEED':60}))
    
    # Beginning/Choosing your pokemon
    
    delay_print(f"Welcome to the PokeAi Battler.\n\n")
    
    for i, x in enumerate(list):
        print(f"{i+1}.", x.name, "|", x.types)
    num = int(input("\nPick a Pokemon: ")) 
    
    playerChoice = list[num-1].name   
    delay_print(f"\nYou have chosen {remove(playerChoice)}.")
    
    # Type Chart List for AI to pick Pokemon
    
    if list[num-1].types == 'Normal':
        # Choose fighting for super effective
        choice = 6
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Fire':
        # Choose water, ground, or rock for super effective
        choice = random.choice([2,8,12])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Water':
        # Choose electric or grass for super effective
        choice = random.choice([3,4])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Electric':
        # Choose ground for super effective
        choice = random.choice([8])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Grass':
        # Choose fire, ice, poison, flying, or bug for super effective
        choice = random.choice([1,5,7,9,11])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Ice':
        # Choose fire, fighting, rock, or steel for super effective
        choice = random.choice([1,6,12,16])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Fighting':
        # Choose flying, psychic, or fairy for super effective
        choice = random.choice([9,10,17])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Poison':
        # Choose ground or psychic for super effective
        choice = random.choice([8,10])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Ground':
        # Choose water, grass, or ice for super effective.
        choice = random.choice([2,4,5])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Flying':
        # Choose electric, ice, or rock for super effective
        choice = random.choice([3,5,12])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Psychic':
        # Choose bug, ghost, or dark for super effective
        choice = random.choice([11,13,15])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Bug':
        # Choose fire, flying, or rock for super effective
        choice = random.choice([1,9,12])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Rock':
        # Choose water, grass, fighting, ground, or steel for super effective
        choice = random.choice([2,4,6,8,16])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Ghost':    
        # Choose ghost or dark for super effective
        choice = random.choice([13,15])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Dragon':
        # Choose ice, dragon, or fairy for super effective
        choice = random.choice([5,14,17])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Dark':
        # Choose fighting, bug, or fairy for super effective
        choice = random.choice([6,11,17])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Steel':
        # Choose fire, fighting, or ground for super effective
        choice = random.choice([1,6,8,])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
        
    elif list[num-1].types == 'Fairy':
        # Choose poison or fairy for super effective
        choice = random.choice([7,16])
        aiChoice = list[choice].name
        delay_print(f"\n{remove(aiChoice)} is your opponent.\n")
        list[num-1].fight(list[choice])
    
    
    