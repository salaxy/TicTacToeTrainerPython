'''
Created on 18.02.2015

@author: Salaxy
'''
#from player import player
from TemporalDifferenceTrainer import TemporalDifferenceTrainer
from agent import Agent
from environment import Environment
from player import RandomPlayer


if __name__ == '__main__':
    
    game = Environment()
    player = RandomPlayer()
    agent = Agent()
    trainer = TemporalDifferenceTrainer(game, agent, player)
    trainer.teachPassiveRandom(10)
    
    
    trainer.teachActiveAndSaveStatistics("path", 10000, 0.0, 0.0, 0.0, 0.0, 0.0, True, False, False)
    
    
    pass