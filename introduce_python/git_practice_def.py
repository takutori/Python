import numpy as np



def plus(x,y):
    return x+y

class vector_space():
    def __init__(self,x,y):
        self.x = x;
        self.y = y;


    def plus(self):
        return self.x+self.y

    def mainus(self):
        return self.x-self.y

    def tiems(self):
        return self.x*self.y
