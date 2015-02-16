#!/usr/bin/env python
""" generated source for module Agent """
# package: de.fhb.infm.knn.neuro
import java.io.FileInputStream

import java.io.FileOutputStream

import java.io.IOException

import java.io.ObjectInputStream

import java.io.ObjectOutputStream

import java.util.Random

# 
#  * This is a agent for reinforcement learning with a artificial neural net.
#  * 
#  * @author Andy Klay 2014
#  
class Agent(object):
    """ generated source for class Agent """
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
    selector = Selector()
    random = Random()

    # 
    # 	 * intializer
    # 	 
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        initializeNetWeights()
        self.selector = Selector(self, 0.0)

    # 
    # 	 * intializer with parameter setting
    # 	 * 
    # 	 * @param alpha
    # 	 * @param beta
    # 	 * @param epsilon
    # 	 
    @__init__.register(object, float, float, float)
    def __init___0(self, alpha, beta, epsilon):
        """ generated source for method __init___0 """
        initializeNetWeights()
        self.selector = Selector(self, epsilon)
        self.alpha = alpha
        self.beta = beta

    # 
    # 	 * set epsilon parameter, epsilon is the eploration rate of the agent
    # 	 * 
    # 	 * @param epsilon
    # 	 
    def setEpsilon(self, epsilon):
        """ generated source for method setEpsilon """
        self.selector.setEpsilon(epsilon)

    # 
    # 	 * get paramter alpha, alpha is the learning rate of ANN between input and
    # 	 * hidden layer
    # 	 * 
    # 	 * @return
    # 	 
    def getAlpha(self):
        """ generated source for method getAlpha """
        return self.alpha

    # 
    # 	 * get parameter beta, beta is the learning rate of ANN between hidden and
    # 	 * output layer
    # 	 * 
    # 	 * @return
    # 	 
    def getBeta(self):
        """ generated source for method getBeta """
        return self.beta

    # 
    # 	 * set paramter alpha, alpha is the learning rate of ANN between input and
    # 	 * hidden layer
    # 	 * 
    # 	 * @return
    # 	 
    def setAlpha(self, alpha):
        """ generated source for method setAlpha """
        self.alpha = alpha

    # 
    # 	 * set parameter beta, beta is the learning rate of ANN between hidden and
    # 	 * output layer
    # 	 * 
    # 	 * @return
    # 	 
    def setBeta(self, beta):
        """ generated source for method setBeta """
        self.beta = beta

    # 
    # 	 * get parameter epsilon, epsilon is the eploration rate of the agent
    # 	 * 
    # 	 * @return
    # 	 
    def getEpsilon(self):
        """ generated source for method getEpsilon """
        return self.selector.getEpsilon()

    # 
    # 	 * input vector need a length of N_INPUT - 1
    # 	 * 
    # 	 * @param input
    # 	 
    def setInput(self, input):
        """ generated source for method setInput """
        self.lastInput = [None]*N_INPUT
        i = 0
        while i < len(length):
            self.lastInput[i] = input[i]
            i += 1
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

    # 
    # 	 * initializing arrays
    # 	 
    def initializeNetWeights(self):
        """ generated source for method initializeNetWeights """
        self.random = Random()
        #  weight arrays init
        self.weightsInputHidden = [None]*N_INPUT
        self.weightsHiddenOutput = [None]*N_HIDDEN
        #  Random initialize
        #  input>hidden
        i = 0
        while i < self.N_INPUT:
            while j < self.N_HIDDEN:
                self.weightsInputHidden[i][j] = self.random.nextFloat() * 0.1
                if j == self.N_HIDDEN - 1:
                    self.weightsInputHidden[i][j] = 0
                j += 1
            i += 1
        i = 0
        while i < self.N_HIDDEN:
            while j < self.N_OUTPUT:
                self.weightsHiddenOutput[i][j] = self.random.nextFloat() * 0.1
                j += 1
            i += 1

    def responseValue(self):
        """ generated source for method responseValue """
        activationHidden = [None]*N_HIDDEN
        bufferHidden = [None]*N_INPUT
        i = 0
        while i < self.N_HIDDEN:
            while j < self.N_INPUT:
                bufferHidden[j] = self.weightsInputHidden[j][i]
                j += 1
            if i == self.N_HIDDEN - 1:
                activationHidden[i] = self.biasHiddenLayer
            else:
                activationHidden[i] = activationFunction(bufferHidden, self.lastInput)
            i += 1
        activationOutput = [None]*N_OUTPUT
        bufferOutput = [None]*N_HIDDEN
        i = 0
        while i < self.N_OUTPUT:
            while j < self.N_HIDDEN:
                bufferOutput[j] = self.weightsHiddenOutput[j][i]
                j += 1
            activationOutput[i] = activationFunction(bufferOutput, activationHidden)
            i += 1
        self.lastActivationOutput = activationOutput.clone()
        self.lastActivationHidden = activationHidden.clone()
        return activationOutput[0]

    def getOutputDelta(self, targetSignal, outputSignal):
        """ generated source for method getOutputDelta """
        return targetSignal - outputSignal

    def learnByBackpropagation(self):
        """ generated source for method learnByBackpropagation """
        bufferHiddenOutput = [None]*N_HIDDEN
        bufferInputHidden = [None]*N_INPUT
        k = 0
        while k < self.N_OUTPUT:
            while i < self.N_HIDDEN:
                bufferHiddenOutput[i][k] = calcWeightOutputHidden(self.weightsHiddenOutput[i][k], self.alpha, self.lastActivationHidden[i], deltaOutput, self.lastActivationOutput[k])
                i += 1
            k += 1
        deltaOutputLayer = [None]*N_OUTPUT
        k = 0
        while k < self.N_HIDDEN:
            while i < self.N_INPUT:
                if not (k == self.N_HIDDEN - 1):
                    bufferInputHidden[i][k] = calcWeightHiddenInput(self.weightsInputHidden[i][k], self.beta, self.lastInput[i], delta_hidden)
                i += 1
            k += 1
        self.weightsInputHidden = bufferInputHidden
        self.weightsHiddenOutput = bufferHiddenOutput

    def setTargetSignal(self, targetSignal):
        """ generated source for method setTargetSignal """
        self.targetSignal = targetSignal

    def transferFunction(self, x):
        """ generated source for method transferFunction """
        return float(Math.tanh(x))

    def transferFunctionDerivate(self, x):
        """ generated source for method transferFunctionDerivate """
        return float(1.0) - (x * x)

    def calcWeightOutputHidden(self, oldWeight, learningRateAlpha, input, errorSignalDelta, old_output):
        """ generated source for method calcWeightOutputHidden """
        w = oldWeight + learningRateAlpha * input * errorSignalDelta * self.transferFunctionDerivate(old_output)
        return w

    def calcWeightHiddenInput(self, oldWeight, learningRateAlpha, input, errorSignalDelta):
        """ generated source for method calcWeightHiddenInput """
        w = oldWeight + learningRateAlpha * input * errorSignalDelta
        return w

    def getDeltaForHiddenNeuron(self, deltaBefore, weights):
        """ generated source for method getDeltaForHiddenNeuron """
        return weightedSum(deltaBefore, weights)

    def activationFunction(self, weights, activations):
        """ generated source for method activationFunction """
        return self.transferFunction(weightedSum(weights, activations))

    def weightedSum(self, weights, activations):
        """ generated source for method weightedSum """
        sum = 0.0
        i = 0
        while len(weights):
            sum = sum + weights[i] * activations[i]
            i += 1
        return sum

    def printOutWeightTable(self):
        """ generated source for method printOutWeightTable """
        builder = StringBuilder()
        builder.append("weights_input_hidden" + "\n")
        i = 0
        while len(weightsInputHidden):
            while len(length):
                builder.append("[" + self.weightsInputHidden[i][j] + "]")
                j += 1
            builder.append("\n")
            i += 1
        builder.append("weights_hidden_output" + "\n")
        i = 0
        while len(weightsHiddenOutput):
            while len(length):
                builder.append("[" + self.weightsHiddenOutput[i][j] + "]")
                j += 1
            builder.append("\n")
            i += 1
        print builder.__str__()

    def saveNetToFile(self, filePath):
        """ generated source for method saveNetToFile """
        fs = FileOutputStream(filePath)
        os = ObjectOutputStream(fs)
        os.writeObject(self.weightsInputHidden)
        os.writeObject(self.weightsHiddenOutput)
        os.close()

    def loadNetFromFile(self, filePath):
        """ generated source for method loadNetFromFile """
        fs = FileInputStream(filePath)
        is_ = ObjectInputStream(fs)
        self.weightsInputHidden = float(is_.readObject())
        self.weightsHiddenOutput = float(is_.readObject())
        is_.close()

    @classmethod
    def stateToValues(cls, state):
        """ generated source for method stateToValues """
        values = [None]*
        i = 0
        while len(state):
            if state[i]=='X':
                values[i] = 1.0
            elif state[i]=='O':
                values[i] = -1.0
            else:
                values[i] = 0.0
            i += 1
        return values

    def getNextDecision(self, currentState, unoccupiedFieldSign, playerSign):
        """ generated source for method getNextDecision """
        return self.selector.getNextDecision(currentState, unoccupiedFieldSign, playerSign)

