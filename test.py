#use this script to see how the best snake in a generation plays the game
from game import Board
from NeuralNet import NeuralNetwork
import ast
import time
import os
path=f"generations"
#change the variable below (gen) to pick a generation
gen=288
f = open(f"{path}/generation{gen}.txt", "r")
content=f.read()
dictionary = ast.literal_eval(content)
f.close()
scores=[]
for i in dictionary[0]:
    scores.append(i[0])
index=scores.index(max(scores))
weights=(dictionary[0][index][1])
clear = lambda : os.system('clear')
b=Board(10)
n=NeuralNetwork()
n.load_weights(weights)

#change the variable below (frames) to determine length of the game
frames=500
while frames>0:
    clear()
    print(b.render())
    b.move(n.predict(b.values()))
    print("score: ", len(b.player_cords)-1)
    if b.game_over==True:
        print("game over")
        break
    frames-=1
    time.sleep(0.2)
