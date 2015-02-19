#!/usr/bin/env python
""" generated source for module Environment """
# package: de.fhb.infm.knn.trainer.worldmodel
# 
#  * This class hold the game rules of a specific game and this time this is
#  * tic-tac-toe rules. Game fields are in range of 0 to 8
#  * 
#  * @author Andy Klay 2014
#  
class Environment(object):
    """ generated source for class Environment """
    state = []
    finished = False
    lastPlayer = 'X'
    agentPlayer = 'X'
    UNOCCUPIED_FIELD_SIGN = '-'
    PLAYER_SIGN_X = 'X'
    PLAYER_SIGN_O = 'O'
    FIELD_RANGE = 9

    # 
    # 	 * initializer agent plays X, if not changed
    # 	 
    def __init__(self):
        """ generated source for method __init__ """
        #super(Environment, self).__init__()
        self.initState()

    # 
    # 	 * initializes state
    # 	 
    def initState(self):
        """ generated source for method initState """
        self.state = [None]*self.FIELD_RANGE
        i = 0
        while i <= self.FIELD_RANGE - 1:
            self.state[i] = '-'
            i += 1

    # 
    # 	 * set field back / begin a new game
    # 	 
    def renewState(self):
        """ generated source for method renewState """
        self.initState()

    # 
    # 	 * get a game state
    # 	 * 
    # 	 * @return state as char array
    # 	 
    def getState(self):
        """ generated source for method getState """
        return self.state

    # 
    # 	 * get the content of a field by number
    # 	 * 
    # 	 * @param nr
    # 	 * @return sign
    # 	 
    def getFieldContent(self, nr):
        """ generated source for method getFieldContent """
        if self.isFieldInRange(nr):
            return self.state[nr]
        else:
            return 'f'

    # 
    # 	 * do a move for X player by field number
    # 	 * 
    # 	 * @param nr
    # 	 
    def moveX(self, nr):
        """ generated source for method moveX """
        if self.isFieldInRange(nr):
            self.state[nr] = 'X'
            self.lastPlayer = 'X'

    # 
    # 	 * do a move for O player by field number
    # 	 * 
    # 	 * @param nr
    # 	 
    def moveO(self, nr):
        """ generated source for method moveO """
        if self.isFieldInRange(nr):
            self.state[nr] = 'O'
            self.lastPlayer = 'O'

    # 
    # 	 * @return which sign is played by agent
    # 	 
    def getAgentPlayer(self):
        """ generated source for method getAgentPlayer """
        return self.agentPlayer

    # 
    # 	 * sets agent player to X, thats important for the correct giving of rewards
    # 	 
    def setAgentPlayerX(self):
        """ generated source for method setAgentPlayerX """
        self.agentPlayer = self.PLAYER_SIGN_X

    # 
    # 	 * sets agent player to O, thats important for the correct giving of rewards
    # 	 
    def setAgentPlayerO(self):
        """ generated source for method setAgentPlayerO """
        self.agentPlayer = self.PLAYER_SIGN_O

    # 
    # 	 * @return get if the game is final
    # 	 
    def isFinished(self):
        """ generated source for method isFinished """
        return self.checkIfARowOfThreeIsComplete() or self.isUndecided()

    # 
    # 	 * doublechekc if a specific game field is free
    # 	 * 
    # 	 * @param nr
    # 	 * @return isFree?
    # 	 
    def isFieldFree(self, nr):
        """ generated source for method isFieldFree """
        if self.isFieldInRange(nr):
            if self.state[nr] == '-':
                return True
            else:
                return False
        return False

    # 
    # 	 * doublechecks if a fieldnumber existis for this game
    # 	 * 
    # 	 * @param nr
    # 	 * @return
    # 	 
    def isFieldInRange(self, nr):
        """ generated source for method isFieldInRange """
        if nr >= 0 and nr < self.FIELD_RANGE:
            return True
        else:
            return False

    # 
    # 	 * retruns if a row of three is complete
    # 	 * 
    # 	 * @return
    # 	 
    def checkIfARowOfThreeIsComplete(self):
        """ generated source for method checkIfARowOfThreeIsComplete """
        self.finished = False
        #  checks horizontal winning positions
        i = 0
        while i <= 6:
            if (self.state[i] == 'X' or self.state[i] == 'O') and self.state[i] == self.state[i + 1] and self.state[i] == self.state[i + 2]:
                self.finished = True
            i = i + 3
        #  checks vertical winning positions
        i = 0
        while i <= 2:
            if (self.state[i] == 'X' or self.state[i] == 'O') and self.state[i] == self.state[i + 3] and self.state[i] == self.state[i + 6]:
                self.finished = True
            i += 1
        #  checks diagonal winning positions
        if (self.state[4] == 'X' or self.state[4] == 'O'):
            if self.state[4] == self.state[0] and self.state[4] == self.state[8]:
                self.finished = True
            if self.state[4] == self.state[6] and self.state[4] == self.state[2]:
                self.finished = True
        return self.finished

    # 
    # 	 * get status if undecided
    # 	 * 
    # 	 * @return is Remis or not
    # 	 
    def isUndecided(self):
        """ generated source for method isUndecided """
        undecided = False
        if self.isFull() and not self.checkIfARowOfThreeIsComplete():
            undecided = True
        return undecided

    def isFull(self):
        """ generated source for method isFull """
        value = True
        for i in range(len(self.state)):
            if self.state[i] == '-':
                value = value and False
                break
        return value

    # 
    # 	 * get a state for console output
    # 	 * 
    # 	 * @return state as a string
    # 	 
    def stateToString(self):
        """ generated source for method stateToString """
        b = ""
        i = 0
        while i <= 2:
            b = b + self.state[i] + " "
            i += 1
        b = b + "\n"
        i = 3
        while i <= 5:
            b = b + self.state[i] + " "
            i += 1
        b = b + "\n"
        i = 6
        while i <= 8:
            b = b + self.state[i] + " "
            i += 1
        b = b + "\n"
        return b

    # 
    # 	 * Get rewards in agents View setAgentSign before! imporntant!
    # 	 * 
    # 	 * @return reward
    # 	 
    def getReward(self):
        """ generated source for method getReward """
        if self.checkIfARowOfThreeIsComplete():
            print self.lastPlayer + " wins!"
            if self.agentPlayer == self.PLAYER_SIGN_X:
                if self.lastPlayer == self.PLAYER_SIGN_X:
                    return 1
                else:
                    return -1
            else:
                #  agent was O
                if self.lastPlayer == self.PLAYER_SIGN_O:
                    return 1
                else:
                    return -1
        else:
            if self.isUndecided():
                print "Remis!"
                return 0.5
        return 0

    # 
    # 	 * get all possible move by an array of fieldnumbers
    # 	 * 
    # 	 * @param currentState
    # 	 * @param playerSign
    # 	 * @return array of fieldnumbers
    # 	 
    def getPossibleMoves(self, currentState, playerSign):
        """ generated source for method getPossibleMoves """
        numberOfPossibleMoves = 0
        
        for i in range(len(currentState)):
            if currentState[i] == self.UNOCCUPIED_FIELD_SIGN:
                numberOfPossibleMoves += 1
        fieldNumbers = [None]*numberOfPossibleMoves
        possibilityCounter = 0
        #  get all numbers for all possible moves
        for i in range(len(currentState)):
            if currentState[i] == self.UNOCCUPIED_FIELD_SIGN:
                fieldNumbers[possibilityCounter] = i
                possibilityCounter += 1
                
        return fieldNumbers

    # 
    # 	 * doublechecks if a specific move is allowed
    # 	 * 
    # 	 * @param decision
    # 	 * @param playerSign
    # 	 * @return isAllowed?
    # 	 
    def isPossibleMove(self, decision, playerSign):
        """ generated source for method isPossibleMove """
        #  count Signs
        countSignA = self.countSignInState(self.PLAYER_SIGN_X)
        countSignB = self.countSignInState(self.PLAYER_SIGN_O)
        #  possible if the number of signs is equal or less
        if playerSign == self.PLAYER_SIGN_X and countSignA > countSignB:
            #  its not a turn for A
            return False
        if playerSign == self.PLAYER_SIGN_O and countSignB > countSignA:
            #  its not a turn for B
            return False
        possibilites = self.getPossibleMoves(self.state, playerSign)
        isPossible = False

        for i in range(len(possibilites)):
            if decision == possibilites[i]:
                isPossible = True
                break
        return isPossible

    # 
    # 	 * @param countSignA
    # 	 * @return
    # 	 
    def countSignInState(self, sign):
        """ generated source for method countSignInState """
        value = 0
        for i in range(len(self.state)):
            if self.state[i] == sign:
                value += 1
        return value

