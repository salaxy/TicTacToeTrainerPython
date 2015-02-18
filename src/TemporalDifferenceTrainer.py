#!/usr/bin/env python
""" generated source for module TemporalDifferenceTrainer """
# package: de.fhb.infm.knn.neuro
#import java.io.BufferedWriter

from copy import deepcopy
import math
from nt import write
import os
import string

from agent import Agent
from environment import Environment
from player import RandomPlayer


#from randomPlayer import RandomPlayer
#import java.io.File
#import java.io.FileWriter
#import java.io.IOException
#import de.fhb.infm.knn.trainer.worldmodel.Environment
#import de.fhb.infm.knn.trainer.worldmodel.RandomPlayer
# 
#  * TD Trainer for a reinforcement agent
#  * 
#  * @author Andy Klay 2014
#  
class TemporalDifferenceTrainer(object):
    """ generated source for class TemporalDifferenceTrainer """
    LEARN_ROUNDS_AGENT = 1
    NUMBER_OF_FIELDS = 9
    game = Environment()
    agent = Agent()
    player = RandomPlayer()
    gamma = float()

    #  private float lambda;
    #  memory for td-learning
    lastStates = [None]*NUMBER_OF_FIELDS
    lastRewards = [None]*NUMBER_OF_FIELDS
    valueTable = [None]*NUMBER_OF_FIELDS
    stateCounter = 0

    #  for statistics
    winFactorTable = []
    remisFactorTable = []
    epsilonTable = []
    alphaTable = []
    betaTable = []
    wincounter = int()
    remiscounter = int()
    #lineSeparator = System.getProperty("line.separator")
    lineSeparator = ""

    # 
    # 	 * intializer without parameter setting and using gamma 1.0
    # 	 * 
    # 	 * @param game
    # 	 * @param agent
    # 	 * @param player
    # 	 
    #@overloaded
    #def __init__(self, game, agent, player):
    #    """ generated source for method __init__ """
    #    super(TemporalDifferenceTrainer, self).__init__()
    #    self.game = game
    #    self.agent = agent
    #    self.player = player
    #    self.gamma = 1.0
    #    #  this.lambda = 1.0f;

    # 
    # 	 * intializer with parameter setting
    # 	 * 
    # 	 * @param game
    # 	 * @param agent
    # 	 * @param player
    # 	 * @param gamma
    # 	 
    #@__init__.register(object, Environment, Agent, RandomPlayer, float)
    def __init__(self, game, agent, player, gamma = 1.0):
        """ generated source for method __init___0 """
        #  , float lambda) {
        super(TemporalDifferenceTrainer, self).__init__()
        self.game = game
        self.agent = agent
        self.player = player
        self.gamma = gamma
        #  this.lambda = lambda;
        
        if(os.name =="nt"):
            print " windows detected"
            self.lineSeparator = "\n"
        if(os.name == "posix"):
            self.lineSeparator = "\r\n"

    # 
    # 	 * Agent will be trained by a randomplayer
    # 	 * 
    # 	 * @param numberOfGames
    # 	 *            - number of games agent schould be trained
    # 	 
    def teachPassiveRandom(self, numberOfGames):
        """ generated source for method teachPassiveRandom """
        i = 0
        while i < numberOfGames:
            print "Play game nr.: " + str(i)
            self.initAll()
            #  1. Play a game
            #  remember all rewards and states
            self.playRandom()
            #  2. Do TD-Learning!
            #  3. Calculate neural net!
            #bis hier hin is alles gut ^^
            print "begin learning"
            self.doTDZeroLearning()
            print "end learning"
            #  4. prepare next game
            self.game.renewState()
            i += 1

    # 
    # 	 * inits the value tabels
    # 	 
    def initAll(self):
        """ generated source for method initAll """
        #  init value_function
        i = 0
        while i < 9:
            self.valueTable[i] = 0.0
            i += 1
        i = 0
        while i < 9:
            self.lastRewards[i] = 0.0
            i += 1

    # 
    # 	 * sets the game state counter while a gameplay for td learning of the agent
    # 	 * 
    # 	 * @param state_counter
    # 	 
    def setStateCounter(self, state_counter):
        """ generated source for method setStateCounter """
        self.stateCounter = state_counter

    # 
    # 	 * get reference to the last game states of a gameplay
    # 	 * 
    # 	 * @return
    # 	 
    def getLastStates(self):
        """ generated source for method getLastStates """
        return self.lastStates

    # 
    # 	 * get reference to the last rewards of a gameplay
    # 	 * 
    # 	 * @return
    # 	 
    def getLastRewards(self):
        """ generated source for method getLastRewards """
        return self.lastRewards

    # 
    # 	 * get reference to the last rewards
    # 	 * 
    # 	 * @return
    # 	 
    def getValueTable(self):
        """ generated source for method getValueTable """
        return self.valueTable

    # 
    # 	 * execute TD algorithm after a gameplay and train the agent
    # 	 * 
    # 	 
    def doTDZeroLearning(self):
        """ generated source for method doTDZeroLearning """
        r = self.lastRewards
        s = self.lastStates
        
        #  1. Fuehre das TD-Learning durch!
        #  Nicht-Inkrementeller TD-Lambda-Algortihmus
        #  fuer t=n-1 ... 0
        #  deduzierendes Lernen! Rueckswaerts vom Reward
        t = self.stateCounter - 1
        while t >= 0:
            n = self.stateCounter - t
            
            #  TD(0)-Algortithmn one-step TD-Error
            v_st = self.v(s[t])+ self.alpha(n) * (r[t + 1] + self.gamma * self.v(s[t+1]) - self.v(s[t]))
            self.valueTable[t] = self.valueTable[t] + self.alpha(n) * (r[t + 1] + self.gamma * self.valueTable[t + 1] - self.valueTable[t])
            self.learnV(self.lastStates[t], v_st)
            print str(v_st)
            print str(r[t + 1]) 
            print str(self.valueTable[t])
            print str(self.alpha(n))
            print str(t)
            t -= 1
            
        #  learn end reward
        self.learnV(self.lastStates[self.stateCounter], r[self.stateCounter])
        self.valueTable[self.stateCounter] = r[self.stateCounter]
        
        #  print out all rewards
        print "\n"
        print "Rewards: \n"
        
        i = 0
        while i <= self.stateCounter:
            print "[" + str(self.lastRewards[i]) + "] ",
            i += 1
        print "\n"
        
        print "Sollwerte: \n"
        #  print out all values
        i = 0
        while i <= self.stateCounter:
            print "[" + str(self.valueTable[i]) + "] ",
            i += 1
        print "\n"
        
        print "KNN: \n"
        #  gebe alle Values aus
        i = 0
        while i <= self.stateCounter:
            print "[" + str(self.v(s[i])) + "] ",
            i += 1
        print "\n"
        
        self.agent.printOutWeightTable()
        print "\n"

    # 
    # 	 * asking agent for a value
    # 	 * 
    # 	 * @param state
    # 	 * @param n
    # 	 * @return
    # 	 
    def v(self, state):
        """ generated source for method v """
        self.agent.setInput(Agent.stateToValues(state))
        return self.agent.responseValue()

    # 
    # 	 * the agent learn a value by backpropagation
    # 	 * 
    # 	 * @param state
    # 	 * @param n
    # 	 * @param input
    # 	 
    def learnV(self, state, targetSignal):
        """ generated source for method learnV """
        self.agent.setInput(Agent.stateToValues(state))
        self.agent.setTargetSignal(targetSignal)
        k = 0
        while k < self.LEARN_ROUNDS_AGENT:
            self.agent.responseValue()
            self.agent.learnByBackpropagation()
            k += 1

    # 
    # 	 * Alpha ist die lernrate, in diesem Fall als Funktion for 1 ... n 0.5,
    # 	 * 0.33333334, 0.25, 0.2, 0.16666667, 0.14285715, 0.125
    # 	 * 
    # 	 * @param n
    # 	 * @return
    # 	 
    def alpha(self, n):
        """ generated source for method alpha """
        return 1.0 / (n + 1.0)

    def playRandom(self):
        """ generated source for method playRandom """
        counter = 0
        while not self.game.isFinished():
            print "begin round A"
            #  Player X begins
            nextMoveX = self.player.getMove(self.game.getState(),'X') 
            self.game.moveX(nextMoveX)
            #  put it out to console
            print "X move: " + str(nextMoveX)
            print self.game.stateToString()
            #  save state
            self.lastStates[counter] = deepcopy(self.game.getState())
            self.lastRewards[counter] = deepcopy(self.game.getReward())
            #  check state, maybe break game if finished
            if self.game.isFinished():
                break
            counter += 1
            
            print "end round A"
            
            #  ****************************************************************************
            #  Player O follows
            print "begin round B"
            nextMoveO = self.player.getMove(self.game.getState(),'O') 
            self.game.moveO(nextMoveO)
            #  put it out to console
            print "O move: " + str(nextMoveO)
            print self.game.stateToString()
            
            #  save state
            self.lastStates[counter] = deepcopy(self.game.getState())
            self.lastRewards[counter] = deepcopy(self.game.getReward())
            
            #  check state, maybe break game if finished
            if self.game.isFinished():
                break
            counter += 1
            
            print "end round B"
            
        #  count how many states in this game recently has existed
        self.stateCounter = counter

    # 
    # 	 * sets the gamma value for degrading the learning of states in the past
    # 	 * 
    # 	 * @param gamma
    # 	 
    def setGamma(self, gamma):
        """ generated source for method setGamma """
        self.gamma = gamma

    # 
    # 	 * teach an agent with different positions and parameters by online learning
    # 	 * and and save statistics
    # 	 * 
    # 	 * @param name
    # 	 *            - file desciption
    # 	 * @param numberOfGames
    # 	 * @param alphaAtStart
    # 	 * @param betaAtStart
    # 	 * @param gamma
    # 	 * @param lambda
    # 	 * @param epsilonAtStart
    # 	 * @param agentPlayFirst
    # 	 *            - postion of agent, tue - play first, false -play as secound
    # 	 *            player
    # 	 * @param isLearning
    # 	 *            - false means the agent doesnt learn and is only playing,
    # 	 *            playing is for tests only
    # 	 
    def teachActiveAndSaveStatistics(self, name, numberOfGames, alphaAtStart, betaAtStart, gamma, lambda_, epsilonAtStart, agentPlayFirst, isLearning, isAgentVsAgent):
        """ generated source for method teachActiveAndSaveStatistics """
        self.winFactorTable = [None]*numberOfGames
        self.remisFactorTable = [None]*numberOfGames
        self.alphaTable = [None]*numberOfGames
        self.betaTable = [None]*numberOfGames
        self.epsilonTable = [None]*numberOfGames
        self.wincounter = 0
        self.remiscounter = 0
        #  Environment Parameters
        self.game.setAgentPlayerX()
        #  Agent(ANN) Parameters
        if isLearning:
            name = "net" + numberOfGames + "_a" + alphaAtStart + "_b" + betaAtStart + "g_" + gamma + "e_" + epsilonAtStart
            self.agent.setAlpha(alphaAtStart)
            self.agent.setBeta(betaAtStart)
            self.agent.setEpsilon(epsilonAtStart)
        #  TD Parameters
        self.setGamma(gamma)
        #  trainer.setLambda(lambda);
        i = 0
        while i < numberOfGames:
            print "Play game nr.: " + str(i)
            self.initAll()
            #  1. Play a game
            #  remember all rewards and states
            if isAgentVsAgent:
                self.playAgentVsAgent(agentPlayFirst)
            else:
                self.playAgentVsRandom(agentPlayFirst)
            self.calculateStatistic(i)
            if isLearning:
                #  2. Do TD-Learning!
                #  3. Calculate neural net!
                self.doTDZeroLearning()
            #  4. prepare next game
            self.game.renewState()
            #  shrink epsilon in depence of number of games
            if isLearning:
                self.agent.setEpsilon(self.calculateNextEpsilon(i, epsilonAtStart))
                self.agent.setAlpha(self.calculateNextAlpha(i, alphaAtStart))
                self.agent.setBeta(self.calculateNextBeta(i, betaAtStart))
                self.alphaTable[i] = self.agent.getAlpha()
                self.betaTable[i] = self.agent.getBeta()
                self.epsilonTable[i] = self.agent.getEpsilon()
                print self.agent.getEpsilon()
                print self.agent.getAlpha()
                print self.agent.getBeta()
            i += 1
            
        #  save after training
        if isLearning:
            #  save Agent to File
            self.agent.saveNetToFile(name + ".net")
            
        #output = ""
        output = "name: " + name + self.lineSeparator
        output += "numberOfGames: " + str(numberOfGames) + self.lineSeparator
        output += "agentPlayFirst: " + str(agentPlayFirst) + self.lineSeparator
        output += "alpha: " + str(alphaAtStart) + self.lineSeparator
        output += "beta: " + str(betaAtStart) + self.lineSeparator
        output += "epsilon: " + str(epsilonAtStart) + self.lineSeparator
        output += "gamma: " + str(gamma) + self.lineSeparator
        output += "lambda: " + str(lambda_) + self.lineSeparator
        output += "winfactors: " + self.lineSeparator
        
        for i in range(len(self.winFactorTable)):
            output += str(self.winFactorTable[i]) + self.lineSeparator
        output += self.lineSeparator
        output += "remisFactor:"
        output += str(self.remisFactorTable[len(self.remisFactorTable)-1]) + self.lineSeparator
        print output
        
        #  save winning rate to textfile
        self.writeStringToFile(name + "_TestWith" + str(numberOfGames) + str(agentPlayFirst) + ".txt", string.replace(output,'.',','))
        
        #  save parameter tables to textfiles
        if isLearning:    
            output = ""
            for i in range(len(self.alphaTable)):
                output += str(self.alphaTable[i]) + self.lineSeparator
            self.writeStringToFile(name + "_AlphaTable" + str(numberOfGames) + ".txt", string.replace(output,'.',','))
            
            output = ""
            for i in range(len(self.betaTable)):
                output += str(self.betaTable[i]) + self.lineSeparator
            self.writeStringToFile(name + "_BetaTable" + str(numberOfGames) + ".txt", string.replace(output,'.',','))
            
            output = ""
            for i in range(len(self.epsilonTable)):
                output += str(self.epsilonTable[i]) + self.lineSeparator
                
            self.writeStringToFile(name + "_EpsilonTable" + str(numberOfGames) + ".txt", string.replace(output,'.',','))

    # 
    # 	 * epsilonStart fall down through this function from start value againt zero
    # 	 * like a exp function
    # 	 * 
    # 	 * @param n
    # 	 * @param epsilonStart
    # 	 * @return
    # 	 
    def calculateNextEpsilon(self, n, epsilonStart):
        """ generated source for method calculateNextEpsilon """
        return float((math.pow(0.96, (n / 100.0) + 1) * epsilonStart))

    # 
    # 	 * betaAtStart fall down through this function from start value againt zero
    # 	 * like a exp function
    # 	 * 
    # 	 * @param n
    # 	 * @param epsilonStart
    # 	 * @return
    # 	 
    def calculateNextBeta(self, n, betaAtStart):
        """ generated source for method calculateNextBeta """
        return float((math.pow(0.98, (n / 100.0) + 1) * betaAtStart))

    # 
    # 	 * alphaAtStart fall down through this function from start value againt zero
    # 	 * like a exp function
    # 	 * 
    # 	 * @param n
    # 	 * @param epsilonStart
    # 	 * @return
    # 	 
    def calculateNextAlpha(self, n, alphaAtStart):
        """ generated source for method calculateNextAlpha """
        return float((math.pow(0.98, (n / 100.0) + 1) * alphaAtStart))

    # 
    # 	 * calculates the statistic rates
    # 	 * 
    # 	 * @param i
    # 	 
    def calculateStatistic(self, i):
        """ generated source for method calculateStatistic """
        if self.game.getReward() == 1:
            self.wincounter += 1
        if self.game.getReward() == 0.5:
            self.remiscounter += 1
        self.winFactorTable[i] = self.wincounter / float((i + 1))
        self.remisFactorTable[i] = self.remiscounter / float((i + 1))

    # 
    # 	 * play a game with an active agent
    # 	 * @param agentIsFirst - which position the agent is
    # 	 
    def playAgentVsRandom(self, agentIsFirst):
        """ generated source for method playAgentVsRandom """
        counter = 0
        while not self.game.isFinished():
            #  Player X begins
            if agentIsFirst:
                nextMoveA = self.agent.getNextDecision(self.game.getState(), '-', 'X')
                self.game.moveX(nextMoveA)
            else:
                nextMoveA = self.player.getMove(self.game.getState(), 'O')
                self.game.moveO(nextMoveA)
                #  its for RandomRandom test
                #  nextMoveA = player.doRandomMove(game.getState(), 'X');
                #  game.moveX(nextMoveA);
            #  put it out to console
            print "X move: " + str(nextMoveA)
            print self.game.stateToString()
            #  push state and reward to trainer
            self.getLastStates()[counter] = deepcopy(self.game.getState())
            self.getLastRewards()[counter] = self.game.getReward()
            if self.game.isFinished():
                break
            counter += 1
            if agentIsFirst:
                nextMoveB = self.player.getMove(self.game.getState(), 'O')
                self.game.moveO(nextMoveB)
            else:
                nextMoveB = self.agent.getNextDecision(self.game.getState(), '-', 'X')
                self.game.moveX(nextMoveB)
            print "O move: " + str(nextMoveB)
            print self.game.stateToString()
            self.getLastStates()[counter] = deepcopy(self.game.getState())
            self.getLastRewards()[counter] = self.game.getReward()
            if self.game.isFinished():
                break
            counter += 1
        self.setStateCounter(counter)

    def playAgentVsAgent(self, trainOnPlayerA):
        """ generated source for method playAgentVsAgent """
        counter = 0
        while not self.game.isFinished():
            if trainOnPlayerA:
                nextMoveA = self.agent.getNextDecision(self.game.getState(), '-', 'X')
                self.game.moveX(nextMoveA)
            else:
                nextMoveA = self.agent.getNextDecision(self.game.getState(), '-', 'O')
                self.game.moveO(nextMoveA)
            print "X move: " + nextMoveA
            print self.game.stateToString()
            self.getLastStates()[counter] = self.game.getState().clone()
            self.getLastRewards()[counter] = self.game.getReward()
            if self.game.isFinished():
                break
            counter += 1
            if trainOnPlayerA:
                nextMoveB = self.agent.getNextDecision(self.game.getState(), '-', 'O')
                self.game.moveO(nextMoveB)
            else:
                nextMoveB = self.agent.getNextDecision(self.game.getState(), '-', 'X')
                self.game.moveX(nextMoveB)
            print "O move: " + nextMoveB
            print self.game.stateToString()
            self.getLastStates()[counter] = self.game.getState().clone()
            self.getLastRewards()[counter] = self.game.getReward()
            if self.game.isFinished():
                break
            counter += 1
        self.setStateCounter(counter)

    def writeStringToFile(self, filePath, content):
        """ generated source for method writeStringToFile """
        
        f = open(filePath, 'w')
        print "attention writing dends on os"
        f.write(content)
        
        #try:
        #    writer.write(content)
        #    writer.close()
        #except IOException as e:
        #    print e.getMessage()