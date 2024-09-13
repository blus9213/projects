#The goalkeeper agent we are making can realistically only move in two directions to cover the goal
state = ['left', 'right','up','down'] #The state space for the goalkeeper agent
#The possible moves a player can make to score a goal
percept = ['player shooting left', 'player shooting right','player shooting up','player shooting down']


def action(percept):
    #This function defines the actions for the goalkeeper agent provided the given percepts"""
    return state[percept]

#Driver code for demonstration

print("Enter what the player is doing: ")
print("1. player shooting left")
print("2. player shooting right")
print("3. player shooting up")
print ("4.player shooting down")
var = int(input())


print(f"The goalkeeper agent moves {action(var-1)} to block the football !!")


