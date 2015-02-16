#!/usr/bin/env python
""" generated source for module StartHumanConsolePlay """
# package: de.fhb.infm.knn.trainer
import de.fhb.infm.knn.neuro.Agent

import de.fhb.infm.knn.neuro.TemporalDifferenceTrainer

import de.fhb.infm.knn.system.In

import de.fhb.infm.knn.trainer.worldmodel.RandomPlayer

import de.fhb.infm.knn.trainer.worldmodel.Environment

# 
#  * Its a felxible human vs random or learnign agent mode playing in console of
#  * your system
#  * 
#  * @author Andy Klay 2014
#  
class StartHumanConsolePlay(object):
    """ generated source for class StartHumanConsolePlay """
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
        """ generated source for method main """
        #  load ANN state optional
        train()
        cls.agent.loadNetFromFile(cls.TRAINED_NET_FILE_NAME)
        cls.agent.setEpsilon(0.05)
        #  lets start
        startHumanVsAgent(True)

    # 
    # 	 * start a game with human gameplay against random or agent player
    # 	 * @param isLearning
    # 	 
    @classmethod
    def startHumanVsAgent(cls, isLearning):
        """ generated source for method startHumanVsAgent """
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
            print "Moechten Sie gegen Random (R) oder einen Agenten (A) spielnen?"
            if decision == 'R':
                isAgainstRandom = True
                print "Sie spielen gegen Random!"
                playerA = "RANDOM"
            else:
                print "Sie spielen gegen den Agenten!"
            whichEnemyValid = False
        #  Ask who should begin the game
        while whoBeginInputValid:
            print "Moechten Sie beginnen? Ja (J) oder NEIN (N)"
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
            print "Mit welchem Zeichen moechten Sie spielen?"
            print "O oder X?"
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
            print cls.game.stateToString()
            while not cls.game.isFinished():
                if humanBegins:
                    playHumanTurn(humanSign)
                else:
                    if isAgainstRandom:
                        playRandomTurn(agentSign)
                    else:
                        playAgentTurn(agentSign)
                #  push state and reward to trainer
                cls.trainer.getLastStates()[counter] = cls.game.getState().clone()
                cls.trainer.getLastRewards()[counter] = cls.game.getReward()
                #  check state, maybe break game if finished
                if checkGameState(cls.game, playerA):
                    break
                counter += 1
                #  ****************************************************************************
                if humanBegins:
                    if isAgainstRandom:
                        playRandomTurn(agentSign)
                    else:
                        playAgentTurn(agentSign)
                else:
                    playHumanTurn(humanSign)
                #  push state and reward to trainer
                cls.trainer.getLastStates()[counter] = cls.game.getState().clone()
                cls.trainer.getLastRewards()[counter] = cls.game.getReward()
                #  check state, maybe break game if finished
                if checkGameState(cls.game, playerB):
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
            print "Ja (J) oder NEIN (N)"
            if decision == 'N':
                playAgain = False

    @classmethod
    def playAgentTurn(cls, playerSign):
        """ generated source for method playAgentTurn """
        print "AGENT spielt!"
        #  Player X begins - TRAINED AGENT
        nextMove = cls.agent.getNextDecision(cls.game.getState(), '-', playerSign)
        if playerSign == 'O':
            cls.game.moveO(nextMove)
        else:
            cls.game.moveX(nextMove)
        print "AGENT entscheidet fuer " + nextMove + "."
        print cls.game.stateToString()

    @classmethod
    def playRandomTurn(cls, playerSign):
        """ generated source for method playRandomTurn """
        print "RANDOM spielt!"
        nextMove = cls.randomPlayer.getMove(cls.game.getState(), playerSign)
        if playerSign == 'O':
            cls.game.moveO(nextMove)
        else:
            cls.game.moveX(nextMove)
        print "RANDOM entscheidet fuer " + nextMove + "."
        print cls.game.stateToString()

    @classmethod
    def playHumanTurn(cls, playerSign):
        """ generated source for method playHumanTurn """
        #  Player O follows - HUMAN
        print "Sie sind dran!"
        print "Waehle zwischen 1 und 9."
        nextMove = 0
        decisionValid = False
        while not decisionValid:
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
        print "Sie entschieden fuer " + nextMove + "."
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

