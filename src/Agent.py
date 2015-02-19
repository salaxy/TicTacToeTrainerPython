#!/usr/bin/env python
from copy import deepcopy
import math
import pickle
from random import Random


# 
# This is a agent for reinforcement learning with a artificial neural net.
#
# @author Andy Klay 2014
#  
class Agent(object):

    #  5 + bias
    N_HIDDEN = 6
    N_OUTPUT = 1
    #  9 inputs + bias
    N_INPUT = 10
    
    biasInputLayer = 1
    biasHiddenLayer = 1
    
    weightsInputHidden = []
    weightsHiddenOutput = []
    lastActivationHidden = []
    lastActivationOutput = []
    lastInput = []
    targetSignal = float()
    
    alpha = 0.1
    beta = 0.2
    random = Random()
    
    explorationInPercent=0
    epsilon = float()

    #/**
    # * intializer with parameter setting
    # * 
    # * @param alpha
    # * @param beta
    # * @param epsilon
    # */
    #@__init__.register(object, float, float, float)
    def __init__(self, alpha = 0.1, beta = 0.2, epsilon = 0.0):

        self.initializeNetWeights()
        
        self.alpha = alpha
        self.beta = beta
        
        self.epsilon = epsilon
        self.explorationInPercent = int(((100 * epsilon) - 1))


    # 	 * set epsilon parameter, epsilon is the eploration rate of the agent
    # 	 * 
    # 	 * @param epsilon
    # 	 
    def setEpsilon(self, epsilon):
        self.epsilon = epsilon
        self.explorationInPercent = int(((100 * epsilon) - 1))

    # 
    # 	 * get paramter alpha, alpha is the learning rate of ANN between input and
    # 	 * hidden layer
    # 	 * 
    # 	 * @return
    # 	 
    def getAlpha(self):
        return self.alpha

    # 
    # 	 * get parameter beta, beta is the learning rate of ANN between hidden and
    # 	 * output layer
    # 	 * 
    # 	 * @return
    # 	 
    def getBeta(self):
        return self.beta

    # 
    # 	 * set paramter alpha, alpha is the learning rate of ANN between input and
    # 	 * hidden layer
    # 	 * 
    # 	 * @return
    # 	 
    def setAlpha(self, alpha):
        self.alpha = alpha

    # 
    # 	 * set parameter beta, beta is the learning rate of ANN between hidden and
    # 	 * output layer
    # 	 * 
    # 	 * @return
    # 	 
    def setBeta(self, beta):
        self.beta = beta

    # 
    # 	 * get parameter epsilon, epsilon is the eploration rate of the agent
    # 	 * 
    # 	 * @return
    # 	 
    def getEpsilon(self):
        return self.epsilon

    # 
    # 	 * input vector need a length of N_INPUT - 1
    # 	 * 
    # 	 * @param input
    # 	 
    def setInput(self, inputVector):
        """ generated source for method setInput """
        self.lastInput = [None]*self.N_INPUT

        for i in range(len(self.lastInput)-1):
            self.lastInput[i] = inputVector[i]
            
        #  BIAS neuron
        self.lastInput[self.N_INPUT - 1] = self.biasInputLayer

    # 
    # 	 * initialize testinput vector of 10 incl. BIAS neuron
    # 	 
    def initTestInput(self):
        """ generated source for method initTestInput """
        self.lastInput = [None]*10
        self.lastInput[0] = 1
        self.lastInput[1] = 0
        self.lastInput[2] = 0
        self.lastInput[3] = -1
        self.lastInput[4] = 0
        self.lastInput[5] = 1
        self.lastInput[6] = -1
        self.lastInput[7] = 0
        self.lastInput[8] = 1
        #  bias
        self.lastInput[9] = 1
        """  """
    # 
    # 	 * initializing arrays
    # 	 
    def initializeNetWeights(self):

        #self.random = Random()
        """ weight arrays init """
        self.weightsInputHidden = [ [ 0.0 for i in range(self.N_HIDDEN) ] for j in range(self.N_INPUT) ]
        #self.weightsHiddenOutput = [None]*self.N_HIDDEN
        self.weightsHiddenOutput = [ [ 0.0 for i in range(self.N_OUTPUT) ] for j in range( self.N_HIDDEN) ]
        #  Random initialize
        #  input>hidden
        #i = 0
        #while i < self.N_INPUT:
        #    j=0
        #    while j < self.N_HIDDEN:
        #        self.weightsInputHidden[i][j] = self.random.random() * 0.1
        #        if j == self.N_HIDDEN - 1:
        #            self.weightsInputHidden[i][j] = 0
        #        j += 1
        #    i += 1
        #i = 0
        for i in range(self.N_INPUT):
            for j in range(self.N_HIDDEN):
                self.weightsInputHidden[i][j] = self.random.random() * 0.1
        
        
        
        #while i < self.N_HIDDEN:
        #    j=0
        #    while j < self.N_OUTPUT:
        #        self.weightsHiddenOutput[i][j] = self.random.random() * 0.1
        #        j += 1
        #    i += 1
            
        for i in range(self.N_HIDDEN):
            for j in range(self.N_OUTPUT):
                self.weightsHiddenOutput[i][j] = self.random.random() * 0.1

    def responseValue(self):
        """ generated source for method responseValue """
        #activationHidden = [None]*self.N_HIDDEN 
        #bufferHidden = [None]*self.N_INPUT
        activationHidden = [ 0.0 for i in range(self.N_HIDDEN) ]
        bufferHidden = [ 0.0 for i in range(self.N_INPUT) ]
        
        #i = 0
        #while i < self.N_HIDDEN:
        #    j=0
        #    while j < self.N_INPUT:
        #        bufferHidden[j] = self.weightsInputHidden[j][i]
        #        j += 1
        #    if i == self.N_HIDDEN - 1:
        #        activationHidden[i] = self.biasHiddenLayer
        #    else:
        #        activationHidden[i] = self.activationFunction(bufferHidden, self.lastInput)
        #    i += 1
   
        for i in range(self.N_HIDDEN):
            for j in range(self.N_INPUT):
                    bufferHidden[j] = self.weightsInputHidden[j][i]
            if i == (self.N_HIDDEN - 1):
                activationHidden[i] = self.biasHiddenLayer
            else:
                activationHidden[i] = self.activationFunction(bufferHidden, self.lastInput) 
        
        activationOutput = [ 0.0 for i in range(self.N_OUTPUT)]
        bufferOutput = [ 0.0 for i in range(self.N_HIDDEN)]
        
        #i = 0
        #while i < self.N_OUTPUT:
        #    while j < self.N_HIDDEN:
        #        bufferOutput[j] = self.weightsHiddenOutput[j][i]
        #        j += 1
        #    activationOutput[i] = self.activationFunction(bufferOutput, activationHidden)
        #    i += 1
            
        for i in range(self.N_OUTPUT):
            for j in range(self.N_HIDDEN):
                bufferOutput[j] = self.weightsHiddenOutput[j][i]
            activationOutput[i] = self.activationFunction(bufferOutput, activationHidden)
                  
            
        self.lastActivationOutput = deepcopy(activationOutput)
        self.lastActivationHidden = deepcopy(activationHidden)
        return activationOutput[0]

    def getOutputDelta(self, targetSignal, outputSignal):
        """ generated source for method getOutputDelta """
        return targetSignal - outputSignal

    def learnByBackpropagation(self):
        """ generated source for method learnByBackpropagation """
        #bufferHiddenOutput = [None]*self.N_HIDDEN
        #bufferInputHidden = [None]*self.N_INPUT
        bufferHiddenOutput = [ [ 0.0 for i in range(self.N_OUTPUT) ] for j in range(self.N_HIDDEN) ]
        bufferInputHidden = [ [ 0.0 for i in range(self.N_HIDDEN) ] for j in range(self.N_INPUT)  ]    
        
        for k in range(self.N_OUTPUT):
            deltaOutput=self.getOutputDelta(self.targetSignal, self.lastActivationOutput[k])
            
            for i in range(self.N_HIDDEN):
                bufferHiddenOutput[i][k] = self.calcWeightOutputHidden(self.weightsHiddenOutput[i][k], self.alpha, self.lastActivationHidden[i], deltaOutput, self.lastActivationOutput[k])
                
        #k = 0
        #while k < self.N_OUTPUT:
        #    deltaOutput=self.getOutputDelta(self.targetSignal, self.outputSignal)
        #
        #    i=0
        #    while i < self.N_HIDDEN:
        #        bufferHiddenOutput[i][k] = self.calcWeightOutputHidden(self.weightsHiddenOutput[i][k], self.alpha, self.lastActivationHidden[i], deltaOutput, self.lastActivationOutput[k])
        #        i += 1
        #    k += 1  
            
        deltaOutputLayer = [ 0.0 for i in range(self.N_OUTPUT) ]
        
        #k = 0
        #while k < self.N_HIDDEN:
            
            #delta_hidden=self.getDeltaForHiddenNeuron(deltaOutputLayer, self.weightsHiddenOutput[k])
            
            #i=0
            #while i < self.N_INPUT:
                #if not (k == self.N_HIDDEN - 1):
                #    bufferInputHidden[i][k] = self.calcWeightHiddenInput(self.weightsInputHidden[i][k], self.beta, self.lastInput[i], delta_hidden)
                #i += 1
            #k += 1
            
        for k in range(self.N_HIDDEN):
            delta_hidden=self.getDeltaForHiddenNeuron(deltaOutputLayer, self.weightsHiddenOutput[k])
     
            for i in range(self.N_INPUT):
                if not (k == self.N_HIDDEN - 1):
                    bufferInputHidden[i][k] = self.calcWeightHiddenInput(self.weightsInputHidden[i][k], self.beta, self.lastInput[i], delta_hidden)
            
        self.weightsInputHidden = deepcopy(bufferInputHidden)
        self.weightsHiddenOutput = deepcopy(bufferHiddenOutput)

    def setTargetSignal(self, targetSignal):
        self.targetSignal = targetSignal

    def transferFunction(self, x):
        return float(math.tanh(x))

    def transferFunctionDerivate(self, x):
        return float(1.0) - (x * x)

    def calcWeightOutputHidden(self, oldWeight, learningRateAlpha, input, errorSignalDelta, old_output):
        w = oldWeight + learningRateAlpha * input * errorSignalDelta * self.transferFunctionDerivate(old_output)
        return w

    def calcWeightHiddenInput(self, oldWeight, learningRateAlpha, input, errorSignalDelta):
        w = oldWeight + learningRateAlpha * input * errorSignalDelta
        return w

    def getDeltaForHiddenNeuron(self, deltaBefore, weights):
        return self.weightedSum(deltaBefore, weights)

    def activationFunction(self, weights, activations):
        return self.transferFunction(self.weightedSum(weights, activations))

    def weightedSum(self, weights, activations):
        s = 0.0
        
        for i in range(len(weights)):
            s = s + weights[i] * activations[i]
        return s

    def printOutWeightTable(self):
        """ generated source for method printOutWeightTable """
        b = ""
        b = b + "weights_input_hidden" + "\n"
        #i = 0
        #while len(self.weightsInputHidden):
        #    j=0
        #    while len(self.weightsInputHidden[i]):
        #        b = b + "[" + str(self.weightsInputHidden[i][j]) + "]"
        #        j += 1
        #    b = b + "\n"
        #    i += 1
            
        for i in range(len(self.weightsInputHidden)):
            for j in range(len(self.weightsInputHidden[i])):
                b = b + "[" + str(self.weightsInputHidden[i][j]) + "]"
            b = b + "\n"
            
        b = b + "\n"
        b = b + "weights_hidden_output" + "\n"
        
        #i = 0
        #while len(self.weightsHiddenOutput):
        #    j=0
        #    while len(self.weightsHiddenOutput[i]):
        #        builder.append("[" + self.weightsHiddenOutput[i][j] + "]")
        #        j += 1
        #    builder.append("\n")
        #    i += 1
        
        
        for i in range(len(self.weightsHiddenOutput)):
            for j in range(len(self.weightsHiddenOutput[i])):
                b = b + "[" + str(self.weightsHiddenOutput[i][j]) + "]"
            b = b + "\n"

        print b

    def saveNetToFile(self, filePath):      
        f = open(filePath, "w+b")
        pickle.dump(self.weightsHiddenOutput, f)
        pickle.dump(self.weightsInputHidden, f)
        f.close()

    def loadNetFromFile(self, filePath):        
        f = open(filePath)
        self.weightsHiddenOutput = pickle.load(f)
        self.weightsInputHidden = pickle.load(f)
        f.close()

    @classmethod
    def stateToValues(cls, state):
        """ generated source for method stateToValues """
        values = [None]*9
        
        #i = 0
        #while len(state):
        for i in range(len(state)):
            if state[i]=='X':
                values[i] = 1.0
            elif state[i]=='O':
                values[i] = -1.0
            else:
                values[i] = 0.0
            #i += 1
        return values


    #      * Calculate next decision by greedy strategy
    #      * 
    #      * @param currentState
    #      * @param unoccupiedFieldSign
    #      * @return int field number to choose, error value = -1
    #      
    def getNextDecision(self, currentState, unoccupiedFieldSign, playerSign):
        #  build in expolration in depency of a factor
        randomChance = self.random.randrange(0,100,1)
        randomDecision = False
        if randomChance < self.explorationInPercent:
            print "Agent Random-Move"
            randomDecision = True
            
        #  1st count possible moves
        numberOfPossibleMoves = 0

        for i in range(len(currentState)):
            if currentState[i] == unoccupiedFieldSign:
                numberOfPossibleMoves += 1
                
        possibleMoves = [None]*numberOfPossibleMoves
        fieldValue = [None]*numberOfPossibleMoves
        fieldNumbers = [None]*numberOfPossibleMoves
        possibilityCounter = 0
        
        #  2nd which moves are possible
        #  3rd get all values for all possible moves
        for i in range(len(currentState)):
            if currentState[i] == unoccupiedFieldSign:
                fieldNumbers[possibilityCounter] = i
                
                if not randomDecision:
                    """ copy and set possible move in a state """
                    possibleMoves[possibilityCounter] = deepcopy(currentState)
                    possibleMoves[possibilityCounter][i] = playerSign

                    """calculate value of this state"""
                    self.setInput(Agent.stateToValues(currentState));
                    fieldValue[possibilityCounter] = self.responseValue()
                    
                possibilityCounter += 1
        if randomDecision:
            random = self.random.randrange(0,possibilityCounter,1)
            #print str(random)
            return fieldNumbers[random]
        
        best = 0
        for i in range(len(possibleMoves)):
            if fieldValue[i] >= fieldValue[best]:
                best = i
        if len(possibleMoves)>0:
            return fieldNumbers[best]
        else:
            return -1