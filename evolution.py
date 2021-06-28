from game import Board
from NeuralNet import NeuralNetwork
import time
import ast
import numpy as np
import copy
import os
clear = lambda : os.system('clear')
def sigmoid(x):
    return 1/(1+np.exp(-x))
def evolution(generations, snakes):
    """
    This function looks for text files in generations folder to see if there are any neural networks to start the evolution from.
    If there are no files in generations file then it creates neural networks with random weights and uses those networks to make
    decisions in the game. Everytime a 'snake' plays the game, it's gameplay results are put in a fitness function. Then the weights
    of every snake, and its fitness results are saved in a .txt file in the generations folder. Then the file is opened and the best
    200 snakes are mutated (every weight is randomly changed with %c chance) into 4 different snakes. The cycle countinues by making the 
    1000 snakes in every generation.
    """
    import glob, os
    os.chdir("generations/")
    files=(glob.glob("*.txt"))
    if len(files)>0:
        import re
        last_g=[]
        for i in range(len(files)):
            last_g.append(int(re.findall(r'\d+',files[i])[0]))
        g=max(last_g)+1
    else:
        g=0
    print("starting from: ", g)
    for a in range(g,g+generations):
        losses=[]
        def snake(frames, b,n):
                    start=time.time()
                    while frames>0:
                        b.render()
                        b.move(n.predict(b.values()))
                        if b.game_over==True:
                            break
                        frames-=1
                    end=time.time()
                    t=end-start
                    def fitness():
                        if b.game_over==True:
                            go=-100
                        else:
                            go=200
                        return len(b.player_cords)*30-b.frames_not_eaten/10+go+b.turns
                    return fitness()
        generation=[]
        if a==0:
            for s in range(snakes):
                board=Board(10)
                nn=NeuralNetwork()
                fitness=snake(500,board,nn)
                generation.append([fitness, nn.weights])
                losses.append(fitness)
            path=f""
            f = open(f"generation{a}.txt", "w+")
            f.write(f"[{generation}]")
            f.close()
        if a>0:
            path=f""
            f = open(f"generation{a-1}.txt", "r")
            content=f.read()
            dictionary = ast.literal_eval(content)
            f.close()
            scores=list()
            for i in dictionary[0]:
                scores.append(i[0])
            best_fit=[]
            for x in range(200):
                index=scores.index(max(scores))
                best_fit.append(dictionary[0][index][1])
                scores.pop(index)
                dictionary[0].pop(index)
            
            def mutate(network,n,c):
                output=[]
                for i in range(n):
                    sample=copy.deepcopy(network)
                    for layer in range(len(sample)):
                        for sub_layer in range(len(sample[layer])):
                            for weight in range(len(sample[layer][sub_layer])):
                                chance=np.random.randint(0,1000)
                                if chance < c:
                                    sample[layer][sub_layer][weight]=np.random.rand()
                    output.append(sample)
                return output
            
            tmp=[]
            for best in best_fit:
                tmp.append(best)
                mutants=mutate(best,4,10)
                for mutant in mutants:
                    tmp.append(mutant)
            for t in tmp:
                board=Board(10)
                nn=NeuralNetwork()
                nn.load_weights(t)
                fitness=snake(500,board,nn)
                generation.append([fitness, nn.weights])
                losses.append(fitness)
            path=f""
            f = open(f"generation{a}.txt", "w")
            f.write(f"[{generation}]")
            f.close()

        mean=0
        for loss in losses:
            mean+=loss
        mean=mean/(len(losses))
        print(f"{a}. fitness: ", mean,)
evolution(200,1000)
