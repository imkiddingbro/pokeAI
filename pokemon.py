import time
import numpy as np 
import sys
import random

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
        
        
class Pokemon:
    def __init__(self, name, types, moves, EVs, health = '===================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20
        
    def fight(self, Pokemon2):
        print("\n----POKEMON DUEL----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))
        
        time.sleep(2)
        
        # Only considering 3 Pokemon types -> Fire, Water, Grass
        
        version = ['Fire', 'Water', 'Grass']
        
        for i,k in enumerate(version):
            if self.types == k:
                if self.types == k:
                    # For if both pokemon are the same types ----> Irrelevant for the project
                    if Pokemon2.types == k:
                        string_1_attack = '\nNot very effective...\n'
                        string_2_attack = '\nNot very effective...\n'

                    # Pokemon2 is STRONG
                    if Pokemon2.types == version[(i+1)%3]:
                        Pokemon2.attack *= 2
                        Pokemon2.defense *= 2
                        self.attack /= 2
                        self.defense /= 2
                        string_1_attack = '\nNot very effective...\n'
                        string_2_attack = '\nSuper effective!!\n'
                        
                    # Pokemon2 is WEAK
                    if Pokemon2.types == version[(i+2)%3]:
                        self.attack *= 2
                        self.defense *= 2
                        Pokemon2.attack /= 2
                        Pokemon2.defense /= 2
                        string_1_attack = '\nSuper Effective!!\n'
                        string_2_attack = '\nNot very effective...\n'
                        
            while (self.bars > 0) and (Pokemon2.bars > 0):
                print(f"\n{self.name}\t\tHLTH\t{self.health}") 
                print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}")         
                
                print(f"\nGo {self.name}!")
                for i, x in enumerate(self.moves):
                    print(f"{i+1}.", x)
                index = int(input('\nPick a move: '))
                delay_print(f"\n{self.name} used {self.moves[index-1]}!")
                time.sleep(1)
                delay_print(string_1_attack)
                
                Pokemon2.bars -= self.attack
                Pokemon2.health = ""
                
                for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                    Pokemon2.health += "="
                    
                time.sleep(1)
                print(f"\n{self.name}\t\tHLTH\t{self.health}") 
                print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}")
                
                if Pokemon2.bars <= 0:
                    delay_print("\n..." + Pokemon2.name + ' fainted.')
                    break
                
                # Pokemon2 AI's turn
                
                print(f"\nGo {Pokemon2.name}!")
                
                # If you wanted to play like an actual game, then this would implementation would be uncommented.
                
                #for i, x in enumerate(Pokemon2.moves):
                    #print(f"{i+1}.", x)
                #index = int(input('\nPick a move: '))
                
                delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[random.randint(0, 3)]}!")
                time.sleep(1)
                delay_print(string_2_attack)
                
                self.bars -= Pokemon2.attack
                self.health = ""
                
                for j in range(int(self.bars+.1*self.defense)):
                    self.health += "="
                    
                time.sleep(1)
                print(f"\n{self.name}\t\tHLTH\t{self.health}") 
                print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}")
                
                if self.bars <= 0:
                    delay_print("\n..." + self.name + ' fainted.\n')   
                    break
                
        money = random.randint(10, 1000)
        delay_print(f"\nThe Ai has paid you ${money} as a consolation prize.\n")
            
if __name__ == '__main__':
    
    list = []
    
    list.append(Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE':8}))
    list.append(Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'], {'ATTACK':10, 'DEFENSE':10}))
    list.append(Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'], {'ATTACK':8, 'DEFENSE':12}))
    
    list.append(Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'], {'ATTACK':6, 'DEFENSE':5}))
    list.append(Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'], {'ATTACK':5, 'DEFENSE':5}))
    list.append(Pokemon('Ivysaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'], {'ATTACK':4, 'DEFENSE':6}))
    
    list.append(Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'], {'ATTACK':4, 'DEFENSE':2}))
    list.append(Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'], {'ATTACK':3, 'DEFENSE':3}))
    list.append(Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'], {'ATTACK':2, 'DEFENSE':4}))
    
    # Choosing your pokemon
    
    delay_print(f"Welcome to the PokeAi Battler.\n\n")
    
    for i, x in enumerate(list):
        print(f"{i+1}.", x.name)
    num = int(input("\nPick a Pokemon: ")) 
    playerChoice = list[num-1].name   
    delay_print(f"\nYou have chosen {playerChoice}.")
    
    # Ai choosing
    
    if list[num-1].types == 'Fire':
        aiChoice = list[num].name
        delay_print(f"\n{aiChoice} is your opponent.\n")
        list[num-1].fight(list[num])
    elif list[num-1].types == 'Water':
        aiChoice = list[num].name
        delay_print(f"\n{aiChoice} is your opponent.\n")
        list[num-1].fight(list[num])
    elif list[num-1].types == 'Grass':
        aiChoice = list[num-3].name
        delay_print(f"\n{aiChoice} is your opponent.\n")
        list[num-1].fight(list[num-3])
    
    
    