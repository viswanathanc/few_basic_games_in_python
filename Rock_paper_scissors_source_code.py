#Setting up essential components
import random
possible_entities = ['Rock','Paper','Scissors']

class entity_in:
    def __init__(self,entity):
        self.entity = entity
        
    def __eq__(self,other):
        if self.entity == other.entity:
            return True
        else:
            return False
        
    def __str__(self):
        return self.entity
        
r = entity_in("Rock")
p = entity_in("Paper")
s = entity_in("Scissors")

def take_user_input():
    user_input = input("Its your turn! Type one of the following:\nRock\nPaper\nScissors\n\t")
    user_entity = entity_in(user_input)
    return user_entity
    
def take_comp_input():
    comp_input = random.choice(possible_entities)
    comp_entity = entity_in(comp_input)
    print("\nComputer returns {}".format(comp_input))
    return comp_entity

#setting Game rules
def compare_n_reward(p1,p2,entity_1,entity_2):
    if entity_1 == entity_2:
        print("Both returned same!")
    elif entity_1 == r and entity_2 == s:
        print("{}'s Rock crashes {}'s Scissors!".format(p1,p2))
    elif entity_2 == r and entity_1 == s:
        print("{}'s Rock crashes {}'s Scissors!".format(p2,p1))
    elif entity_1 == p and entity_2 == r:
        print("{}'s Paper covers {}'s Rock!".format(p1,p2))
    elif entity_2 == p and entity_1 == r:
        print("{}'s Paper covers {}'s Rock!".format(p2,p1))
    elif entity_1 == s and entity_2 == p:
        print("{}'s Scissors cuts {}'s Paper".format(p1,p2))
    elif entity_2 == s and entity_1 == p:
        print("{}'s Scissors cuts {}'s Paper".format(p2,p1))
        
def play_a_trial_with_comp(p1,p2):
    u = take_user_input()
    c = take_comp_input()
    compare_n_reward(p1,p2,u,c)

def play():
    single = input("\n\tSingle player or multiple? Type 'True' or 'False'\n\t")
    if single:
        p1 = input("\n\tType your Username:")
        p2 = "Computer"    
        play_a_trial_with_comp(p1,p2)
    else:
        print("Multiplayer is not enables in this version.")