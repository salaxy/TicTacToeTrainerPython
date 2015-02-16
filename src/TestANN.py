#!/usr/bin/env python
""" generated source for module TestANN """
# package: de.fhb.infm.knn.neuro
# 
#  * only to doublecheck if the agent really leans
#  * 
#  * @author Andy Klay 2014
#  
class TestANN(object):
    """ generated source for class TestANN """
    LEARN_ROUNDS_AGENT = 100000
    agent = Agent(0.05, 0.05, 0.0)

    # 
    # 	 * 
    # 	 * Start learning process
    # 	 * 
    # 	 * @param args
    # 	 
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        last_input = [None]*10
        last_input[0] = 1
        last_input[1] = 0
        last_input[2] = 0
        last_input[3] = -1
        last_input[4] = 0
        last_input[5] = 1
        last_input[6] = -1
        last_input[7] = 0
        last_input[8] = 1
        #  bias
        last_input[9] = 1
        toLearn = 0.5
        cls.agent.initTestInput()
        learnV(last_input, toLearn)
        print "\n"
        print "Soll: \n"
        print "[" + toLearn + "] ",
        print "KNN: \n"
        print "[" + v(last_input, + "] ")

    # 
    # 	 * aksing agent for a value
    # 	 * 
    # 	 * @param state
    # 	 * @param n
    # 	 * @return
    # 	 
    @classmethod
    def v(cls, state):
        """ generated source for method v """
        #  set iput and fire
        cls.agent.setInput(state)
        return cls.agent.responseValue()

    # 
    # 	 * passt den neuronalen Agenten an
    # 	 * 
    # 	 * @param state
    # 	 * @param n
    # 	 * @param input
    # 	 
    @classmethod
    def learnV(cls, state, targetSignal):
        """ generated source for method learnV """
        cls.agent.setInput(state)
        cls.agent.setTargetSignal(targetSignal)
        k = 0
        while k < cls.LEARN_ROUNDS_AGENT:
            cls.agent.responseValue()
            cls.agent.learnByBackpropagation()
            print cls.v(state)
            k += 1


if __name__ == '__main__':
    import sys
    TestANN.main(sys.argv)

