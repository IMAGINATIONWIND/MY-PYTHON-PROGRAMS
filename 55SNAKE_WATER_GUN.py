
# BUNCH OF HEADACHE I JUST CREATED


# import random as r 
# import numpy as np


# def res (player , computer) :
# # for this i tried list , dict and other data types also but array is the simplest
#     outcome = np.array([
#     ["D", "W", "L"],  
#     ["L", "D", "W"],  
#     ["W", "L", "D"]   
#     ])
    
#     choices = np.array(["Snake", "Water", "Gun"])

#     player_index: int = np.where(choices == player)[0][0]
#     computer_index: int = np.where(choices == computer)[0][0]



# def s_w_g ():

 
#     print (" WELCOME TO THIS GAME\n         OF           \n SNAKE,WATER & GUN")
#     player: str = input("Enter your choice (S for Snake, W for Water, G for Gun): ")
#     a = player.lower()
#     if a == "S" : 
#         a = 0
#     elif a == 'W' :
#         a = 1
#     elif a == 'G' :
#         a = 2
#     computer: str = r.randint(0,2)
    
    
    
    
# s_w_g()

# CORRECT ANSWER


import numpy as np
import random

# numpy.ndarray of strings (3x3 outcome matrix)
# Rows = Player, Columns = Computer
outcome = np.array([
    ["D", "W", "L"],  # Player = S
    ["L", "D", "W"],  # Player = W
    ["W", "L", "D"]   # Player = G
])

# numpy.ndarray of strings (choices)
choices = np.array(["S", "W", "G"])

# str
player: str = input("Enter your choice (S for Snake, W for Water, G for Gun): ").upper()
computer: str = random.choice(choices)

# int
player_index: int = np.where(choices == player)[0][0]
computer_index: int = np.where(choices == computer)[0][0]

# str
result: str = outcome[player_index, computer_index]

print(f"Player: {player}, Computer: {computer}, Result: {result}")

# ALLL THE BEST