#!/usr/bin/env python
from numpy import char

from TemporalDifferenceTrainer import TemporalDifferenceTrainer
from agent import Agent
from environment import Environment
from player import RandomPlayer
from copy import deepcopy

#
#  Its a felxible human vs random or learnign agent mode playing
#  in console of your system
# 
#  @author Andy Klay 2014
#
class StartHumanConsolePlay(object):
    
    game = Environment()
    agent = Agent()
    randomPlayer = RandomPlayer()
    trainer = TemporalDifferenceTrainer(game, agent, None, 1.0)
    TRAINED_NET_FILE_NAME = "random_learning_without_playing.save"

    # 
    # 	 * @param args
    # 	 
    @classmethod
    def main(cls, args):
        #  load ANN state optional
        #cls.train()
        #cls.agent.loadNetFromFile(cls.TRAINED_NET_FILE_NAME)
        cls.agent.setEpsilon(0.05)
        #  lets start
        cls.startHumanVsAgent(True)

    # 
    # 	 * start a game with human gameplay against random or agent player
    # 	 * @param isLearning
    # 	 
    @classmethod
    def startHumanVsAgent(cls, isLearning):
        
        print "Neues Spiel gestartet!"
        humanBegins = False
        isAgainstRandom = False
        whoBeginInputValid = True
        whichSignInputValid = True
        whichEnemyValid = True
        agentSign = 'X'
        humanSign = 'O'
        playerA = "AGENT"
        playerB = "DU"
        
        #  Ask which enemy should used
        while whichEnemyValid:
            decision =  raw_input("Moechten Sie gegen Random (R) oder einen Agenten (A) spielen? \n")
            print decision
            if decision == 'R':
                isAgainstRandom = True
                print "Sie spielen gegen Random!"
                playerA = "RANDOM"
            else:
                print "Sie spielen gegen den Agenten!"
            whichEnemyValid = False
            
        #  Ask who should begin the game
        while whoBeginInputValid:
            decision =  raw_input("Moechten Sie beginnen? Ja (J) oder NEIN (N) \n")
            
            if decision == 'J':
                humanBegins = True
                print "Sie beginnen!"
                playerA = "DU"
                if isAgainstRandom:
                    playerB = "RANDOM"
                else:
                    playerB = "AGENT"
            else:
                print "Der Agent beginnt!"
            whoBeginInputValid = False
        if humanBegins:
            cls.game.setAgentPlayerX()
        else:
            cls.game.setAgentPlayerO()
            
        #  choose the player sign
        while whichSignInputValid:
            print "Mit welchem Zeichen moechten Sie spielen? \n"
            decision =  raw_input("O oder X?\n")
            
            if decision == 'X':
                agentSign = 'O'
                humanSign = 'X'
                print "Sie spielen mit X!"
                cls.game.setAgentPlayerO()
            else:
                print "Sie spielen mit O!"
                cls.game.setAgentPlayerX()
                agentSign = 'X'
                humanSign = 'O'
            whichSignInputValid = False
            
        #  begin the game
        print "Das Spiel beginnt!"
        playAgain = True

        while playAgain:
            counter = 0            
            print cls.game.stateToString()
            
            while not cls.game.isFinished():
                if humanBegins:
                    cls.playHumanTurn(humanSign)
                else:
                    if isAgainstRandom:
                        cls.playRandomTurn(agentSign)
                    else:
                        cls.playAgentTurn(agentSign)
                        
                #  push state and reward to trainer
                cls.trainer.getLastStates()[counter] = deepcopy(cls.game.getState())
                cls.trainer.getLastRewards()[counter] = cls.game.getReward()
                
                #  check state, maybe break game if finished
                if cls.checkGameState(cls.game, playerA):
                    break
                counter += 1
                
                #  ****************************************************************************
                if humanBegins:
                    if isAgainstRandom:
                        cls.playRandomTurn(agentSign)
                    else:
                        cls.playAgentTurn(agentSign)
                else:
                    cls.playHumanTurn(humanSign)
                    
                #  push state and reward to trainer
                cls.trainer.getLastStates()[counter] = deepcopy(cls.game.getState())
                cls.trainer.getLastRewards()[counter] = cls.game.getReward()
                
                #  check state, maybe break game if finished
                if cls.checkGameState(cls.game, playerB):
                    break
                counter += 1
            #  count how many states in this game recently has existed
            cls.trainer.setStateCounter(counter)
            #  agent learning
            if isLearning and not isAgainstRandom:
                cls.trainer.doTDZeroLearning()
            #  set back gamestate
            cls.game.renewState()
            print "Moechten Sie ein weiteres Spiel spielen?"
            
            decision =  raw_input("Ja (J) oder NEIN (N) \n")
            
            if decision == 'N':
                playAgain = False

    @classmethod
    def playAgentTurn(cls, playerSign):
        print "AGENT spielt!"
        #  Player X begins - TRAINED AGENT
        nextMove = cls.agent.getNextDecision(cls.game.getState(), '-', playerSign)
        if playerSign == 'O':
            cls.game.moveO(nextMove)
        else:
            cls.game.moveX(nextMove)
        print "AGENT entscheidet fuer " + str(nextMove) + "."
        print cls.game.stateToString()

    @classmethod
    def playRandomTurn(cls, playerSign):
        print "RANDOM spielt!"
        nextMove = cls.randomPlayer.getMove(cls.game.getState(), playerSign)
        if playerSign == 'O':
            cls.game.moveO(nextMove)
        else:
            cls.game.moveX(nextMove)
        print "RANDOM entscheidet fuer " + str(nextMove) + "."
        print cls.game.stateToString()

    @classmethod
    def playHumanTurn(cls, playerSign):
        #  Player O follows - HUMAN
        print "Sie sind dran!"
        nextMove = 0
        
        decisionValid = False
        while not decisionValid:
            
            humanDecision =  int(raw_input("Waehle zwischen 1 und 9: \n"))-1
            
            if cls.game.isPossibleMove(humanDecision, playerSign):
                decisionValid = True
                nextMove = humanDecision
            else:
                print "Dieser Zug ist nicht moeglich!"
                print "Bitte waehlen sie einen anderen!"
        if playerSign == 'O':
            cls.game.moveO(nextMove)
        else:
            cls.game.moveX(nextMove)
        print "Sie entschieden fuer " + str(nextMove) + "."
        print cls.game.stateToString()

    @classmethod
    def checkGameState(cls, game, who):
        """ generated source for method checkGameState """
        finished = False
        if game.isFinished():
            finished = True
            if game.isUndecided():
                print "Unentschieden!"
            else:
                print who + " gewinnt!"
        else:
            finished = False
        return finished

    @classmethod
    def train(cls):
        """ generated source for method train """
        agent = Agent(0.1, 0.1, 0.0)
        trainer = TemporalDifferenceTrainer(cls.game, agent, cls.randomPlayer)
        trainer = TemporalDifferenceTrainer(cls.game, agent, cls.randomPlayer, 1.0)
        trainer.teachPassiveRandom(100000)
        agent.saveNetToFile(cls.TRAINED_NET_FILE_NAME)


if __name__ == '__main__':
    import sys
    StartHumanConsolePlay.main(sys.argv)

