#!/usr/bin/env python
""" generated source for module Selector """
# package: de.fhb.infm.knn.neuro
from random import Random

#from agent import Agent


# 
#  * A selector for the agent class that implements the greedy stategy!
#  * 
#  * @author Andy Klay 2014
#  
class Selector(object):
    """ generated source for class Selector """
    #  explorationfactor in percent
    explorationInPercent = 0
    epsilon = float()
    #agent = Agent()
    random =  Random()

    def __init__(self, agent, epsilon):
        """ generated source for method __init__ """
        super(Selector, self).__init__()
        self.agent = agent
        self.random = Random()
        self.explorationInPercent = int(((100 * epsilon) - 1))
        self.epsilon = epsilon

    # 
    # 	 * sets the explorationrate, how often the selector do a random move
    # 	 * 
    # 	 * @param epsilon
    # 	 
    def setEpsilon(self, epsilon):
        """ generated source for method setEpsilon """
        self.explorationInPercent = int(((100 * epsilon) - 1))
        self.epsilon = epsilon

    # 
    # 	 * get the explorationrate
    # 	 * 
    # 	 * @param epsilon
    # 	 
    def getEpsilon(self):
        """ generated source for method getEpsilon """
        return self.epsilon

    # 
    # 	 * Calculate next decision by greedy strategy
    # 	 * 
    # 	 * @param currentState
    # 	 * @param unoccupiedFieldSign
    # 	 * @return int field number to choose, error value = -1
    # 	 
    def getNextDecision(self, currentState, unoccupiedFieldSign, playerSign):
        """ generated source for method getNextDecision """
        #  build in expolration in depency of a factor
        randomChance = self.random.nextInt(99)
        randomDecision = False
        if randomChance < self.explorationInPercent:
            print "agent Random-Move"
            randomDecision = True
        #  1st count possible moves
        numberOfPossibleMoves = 0
        i = 0
        while len(currentState):
            if currentState[i] == unoccupiedFieldSign:
                numberOfPossibleMoves += 1
            i += 1
        possibleMoves = [None]*numberOfPossibleMoves
        fieldValue = [None]*numberOfPossibleMoves
        fieldNumbers = [None]*numberOfPossibleMoves
        possibilityCounter = 0
        #  2nd which moves are possible
        #  3rd get all values for all possible moves
        i = 0
        while len(currentState):
            if currentState[i] == unoccupiedFieldSign:
                fieldNumbers[possibilityCounter] = i
                if not randomDecision:
                    #  copy and set possible move in a state
                    possibleMoves[possibilityCounter] = currentState.clone()
                    possibleMoves[possibilityCounter][i] = playerSign
                    #self.agent.setInput(self.agent.stateToValues(currentState))
                    #fieldValue[possibilityCounter] = self.agent.responseValue()
                possibilityCounter += 1
            i += 1
        if randomDecision:
            return fieldNumbers[self.random.nextInt(possibilityCounter)]
        best = 0
        i = 0
        while len(possibleMoves):
            if fieldValue[i] >= fieldValue[best]:
                best = i
            i += 1
        if len(possibleMoves):
            return fieldNumbers[best]
        else:
            return -1


