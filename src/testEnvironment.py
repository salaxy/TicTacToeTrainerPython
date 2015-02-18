'''
Created on 18.02.2015

@author: Salaxy
'''
from environment import Environment


if __name__ == '__main__':
    
    
    game = Environment()
    game.renewState()  
    game.setAgentPlayerX()
    
    game.moveX(8)   
    game.isFinished()
    game.getReward()   
    print game.stateToString()
    
    game.moveX(0)
    game.moveX(4)
    print game.stateToString()
    print str(game.isFinished())
    
    pass