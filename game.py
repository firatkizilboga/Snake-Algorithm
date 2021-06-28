import numpy as np
class Board():
    def __init__(self, size):
        #Initializes the game board
        self.size=size
        self.apple_cords=[]# y,x
        self.player_cords=[[5,5]]
        self.direction="w"
        self.game_over=False
        self.turns=0
        self.frames_not_eaten=0
        for i in range(1):
            apple=[np.random.randint(size),np.random.randint(size)]
            for cord in self.player_cords:
                if apple==cord or (apple in self.apple_cords):
                    self.__create_apple(self.size,len(self.apple_cords)-1)
                    break
            self.apple_cords.append(apple)
    def __create_apple(self, size,a):
        #creates an apple at a random location in the game board
        apple=[np.random.randint(size),np.random.randint(size)]
        for cord in self.player_cords:
            if (apple==cord):
                self.__create_apple(self.size,a)
                break
            if apple in self.apple_cords:
                self.__create_apple(self.size,a)
                break
        try:
            self.apple_cords.pop(a)
        except:
            pass
        finally:
            self.apple_cords.append(apple)
    
    def move(self,direction):
        #direction=input()
        x=self.direction
        head=self.player_cords[len(self.player_cords)-1]
        if self.direction=="w":
            if direction=="a":
                self.player_cords.append([head[0],head[1]-1])
                self.direction="a"
            if direction=="w":
                self.player_cords.append([head[0]-1,head[1]])
                self.direction="w"
            if direction=="d":
                self.player_cords.append([head[0],head[1]+1])
                self.direction="d"
        elif self.direction=="s":
            if direction=="a":
                self.player_cords.append([head[0],head[1]+1])
                self.direction="d"
            if direction=="w":
                self.player_cords.append([head[0]+1,head[1]])
                self.direction="s"
            if direction=="d":
                self.player_cords.append([head[0],head[1]-1])
                self.direction="a"
        elif self.direction=="a":
            if direction=="a":
                self.player_cords.append([head[0]+1,head[1]])
                self.direction="s"
            if direction=="w":
                self.player_cords.append([head[0],head[1]-1])
                self.direction="a"
            if direction=="d":
                self.player_cords.append([head[0]-1,head[1]])
                self.direction="w"
        elif self.direction=="d":
            if direction=="a":
                self.player_cords.append([head[0]-1,head[1]])
                self.direction="w"
            if direction=="w":
                self.player_cords.append([head[0],head[1]+1])
                self.direction="d"
            if direction=="d":
                self.player_cords.append([head[0]+1,head[1]])
                self.direction="s"
        if x!=self.direction:
            self.turns+=1

        def __eat():
            for apple in range(len(self.apple_cords)):
                if self.player_cords[len(self.player_cords)-1]==self.apple_cords[apple]:
                    a=apple
                    return True, a
            a=apple
            return False, a
        c, a = __eat()
        if c==True:
            self.__create_apple(self.size,a)
        else:
            self.frames_not_eaten+=1
            self.player_cords.pop(0)
        for i in self.player_cords[len(self.player_cords)-1]:
            if i < 0 or i>=self.size:
                self.game_over=True
        for cord in range(len(self.player_cords)-1):
            if self.player_cords[cord]==self.player_cords[len(self.player_cords)-1]:
                self.game_over=True
    def render(self):
        #renders the board in the terminal represented in a matrix.
        b=np.zeros((self.size,self.size))
        for cord in self.apple_cords:
            cord=tuple(cord)
            b[cord]=3
        for cord in self.player_cords:
            cord=tuple(cord)
            b[cord]=1
        return b
    def values(self):
        #returns the values that will be the input of the neural network (The types and distances of objects that the snake can see in three directions.)
        output=[]
        b=self.render()
        head=self.player_cords[len(self.player_cords)-1]
        #forward left right
        if self.direction=="w":
            for n in range(10):
                v=[head[0]-1-n,head[1]]
                if (-1 or self.size+1) in v:
                    output.append([1,0,n/10])
                    break
                else:
                    try:
                        if  b[v[0],v[1]]==1:
                            output.append([1,0,n/10])
                            break
                        elif  b[v[0],v[1]]==3:
                            output.append([0,1,n/10])
                            break
                    except IndexError:
                            output.append([1,0,n/10])
                            break
            for n in range(10):
                v=[head[0],head[1]-1-n]
                if (-1 or self.size+1) in v:
                    output.append([1,0,n/10])
                    break
                else:
                    try:
                        if  b[v[0],v[1]]==1:
                            output.append([1,0,n/10])
                            break
                        elif  b[v[0],v[1]]==3:
                            output.append([0,1,n/10])
                            break
                    except IndexError:
                            output.append([1,0,n/10])
                            break
            for n in range(10):
                v=[head[0],head[1]+1+n]
                if (-1 or self.size+1) in v:
                    output.append([1,0,n/10])
                    break
                else:
                    try:
                        if  b[v[0],v[1]]==1:
                            output.append([1,0,n/10])
                            break
                        elif  b[v[0],v[1]]==3:
                            output.append([0,1,n/10])
                            break
                    except IndexError:
                            output.append([1,0,n/10])
                            break
        elif self.direction=="s":
                    
            for n in range(10):
                v=[head[0]+1+n,head[1]]
                if (-1 or self.size+1) in v:
                    output.append([1,0,n/10])
                    break
                else:
                    try:
                        if  b[v[0],v[1]]==1:
                            output.append([1,0,n/10])
                            break
                        elif  b[v[0],v[1]]==3:
                            output.append([0,1,n/10])
                            break
                    except IndexError:
                            output.append([1,0,n/10])
                            break
            for n in range(10):
                v=[head[0],head[1]+1+n]
                if (-1 or self.size+1) in v:
                    output.append([1,0,n/10])
                    break
                else:
                    try:
                        if  b[v[0],v[1]]==1:
                            output.append([1,0,n/10])
                            break
                        elif  b[v[0],v[1]]==3:
                            output.append([0,1,n/10])
                            break
                    except IndexError:
                            output.append([1,0,n/10])
                            break
            for n in range(10):
                v=[head[0],head[1]-1-n]
                if (-1 or self.size+1) in v:
                    output.append([1,0,n/10])
                    break
                else:
                    try:
                        if  b[v[0],v[1]]==1:
                            output.append([1,0,n/10])
                            break
                        elif  b[v[0],v[1]]==3:
                            output.append([0,1,n/10])
                            break
                    except IndexError:
                            output.append([1,0,n/10])
                            break
        elif self.direction=="a":
            for n in range(10):
                v=[head[0],head[1]-1-n]
                if (-1 or self.size+1) in v:
                    output.append([1,0,n/10])
                    break
                else:
                    try:
                        if  b[v[0],v[1]]==1:
                            output.append([1,0,n/10])
                            break
                        elif  b[v[0],v[1]]==3:
                            output.append([0,1,n/10])
                            break
                    except IndexError:
                            output.append([1,0,n/10])
                            break
            for n in range(10):
                v=[head[0]+1+n,head[1]]
                if (-1 or self.size+1) in v:
                    output.append([1,0,n/10])
                    break
                else:
                    try:
                        if  b[v[0],v[1]]==1:
                            output.append([1,0,n/10])
                            break
                        elif  b[v[0],v[1]]==3:
                            output.append([0,1,n/10])
                            break
                    except IndexError:
                            output.append([1,0,n/10])
                            break
            for n in range(10):
                v=[head[0]-1-n,head[1]]
                if (-1 or self.size+1) in v:
                    output.append([1,0,n/10])
                    break
                else:
                    try:
                        if  b[v[0],v[1]]==1:
                            output.append([1,0,n/10])
                            break
                        elif  b[v[0],v[1]]==3:
                            output.append([0,1,n/10])
                            break
                    except IndexError:
                            output.append([1,0,n/10])
                            break
        elif self.direction=="d":
            for n in range(10):
                v=[head[0],head[1]+1+n]
                if (-1 or self.size+1) in v:
                    output.append([1,0,n/10])
                    break
                else:
                    try:
                        if  b[v[0],v[1]]==1:
                            output.append([1,0,n/10])
                            break
                        elif  b[v[0],v[1]]==3:
                            output.append([0,1,n/10])
                            break
                    except IndexError:
                            output.append([1,0,n/10])
                            break
            for n in range(10):
                v=[head[0]-1-n,head[1]]
                if (-1 or self.size+1) in v:
                    output.append([1,0,n/10])
                    break
                else:
                    try:
                        if  b[v[0],v[1]]==1:
                            output.append([1,0,n/10])
                            break
                        elif  b[v[0],v[1]]==3:
                            output.append([0,1,n/10])
                            break
                    except IndexError:
                            output.append([1,0,n/10])
                            break
            for n in range(10):
                v=[head[0]+1+n,head[1]]
                if (-1 or self.size+1) in v:
                    output.append([1,0,n/10])
                    break
                else:
                    try:
                        if  b[v[0],v[1]]==1:
                            output.append([1,0,n/10])
                            break
                        elif  b[v[0],v[1]]==3:
                            output.append([0,1,n/10])
                            break
                    except IndexError:
                            output.append([1,0,n/10])
                            break
        return output
"""

frames=500
clear = lambda : os.system('clear')
import os
b=Board(10)
while frames>0:
    clear()
    print(b.render())
    print(b.values())
    b.move(1)
    print(b.turns)
    if b.game_over==True:
        print("game over")
        break
    frames-=1
"""