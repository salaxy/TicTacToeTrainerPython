#!/usr/bin/env python
""" generated source for module StartTests """
# package: de.fhb.infm.knn.trainer
#import de.fhb.infm.knn.neuro.Agent

#import de.fhb.infm.knn.neuro.TemporalDifferenceTrainer

#import de.fhb.infm.knn.trainer.worldmodel.Environment

#import de.fhb.infm.knn.trainer.worldmodel.player

from TemporalDifferenceTrainer import TemporalDifferenceTrainer
from agent import Agent
from environment import Environment
from player import RandomPlayer


class StartTests(object):
    """ generated source for class StartTests """
    game = Environment()
    player = RandomPlayer()
    agent = Agent()
    trainer = TemporalDifferenceTrainer(game, agent, player)

    # 
    # 	 * Test some different parameter settings and save results to file
    # 	 * 
    # 	 * @param args
    # 	 
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        #cls.trainOfflineAndTest(100, 0.1, 0.1, 0.9);
        #cls.trainOfflineAndTest(500, 0.1, 0.1, 1.0);

        cls.trainer.teachActiveAndSaveStatistics("onlineTest", 10, 0.8, 1.0 ,1.0, 0.0, 0.3, True, True,True);
        cls.trainer.teachActiveAndSaveStatistics("path", 10, 0.0, 0.0, 0.0, 0.0, 0.0, True, False, False)

        #trainer.teachActiveAndSaveStatistics("onlineTest", 10000, 0.1f, 0.1f, 1.0f, 0.0f, 0.1f,true, true, true);
        # 		trainer.teachActiveAndSaveStatistics("onlineTest", 10000, 0.1f, 0.1f, 1.0f, 0.0f, 0.1f,
        # 				false, true, true);
        # 		
        # 		testAgentFromFileWithOutLearning("net10000_a0.1_b0.1g_1.0e_0.1_first.net", 10000, true);
        # 		testAgentFromFileWithOutLearning("net10000_a0.1_b0.1g_1.0e_0.1_secound.net", 10000, true);
        #cls.testAgentFromFileWithOutLearning("net10000_a0.1_b0.1g_1.0e_0.1_first.net", 10000, False)
        cls.testAgentFromFileWithOutLearning("net10000_a0.1_b0.1g_1.0e_0.1_secound.net", 10, False)
        # 		testAgentFromFileWithOutLearning("net10000_a0.1_b0.1g_1.0e_0.1.net", 10000, false);

    # 
    # 	 * train an agent offline by numberofgames, save it and test it by the same
    # 	 * number of games as a player A and a player B
    # 	 * 
    # 	 * @param numberOfGames
    # 	 * @param alpha
    # 	 * @param beta
    # 	 * @param gamma
    # 	 
    @classmethod
    def trainOfflineAndTest(cls, numberOfGames, alpha, beta, gamma):
        """ generated source for method trainOfflineAndTest """
        filePath = cls.trainOfflineRandomAndSave(numberOfGames, alpha, beta, gamma)
        cls.testAgentFromFileWithOutLearning(filePath, numberOfGames, True)
        cls.testAgentFromFileWithOutLearning(filePath, numberOfGames, False)

    # 
    # 	 * train an agent offline by numberofgames, save it and test it by the same
    # 	 * number of games
    # 	 * 
    # 	 * @param numberOfGames
    # 	 * @param alpha
    # 	 * @param beta
    # 	 * @param gamma
    # 	 * @return filepath/name of the saved ANN
    # 	 
    @classmethod
    def trainOfflineRandomAndSave(cls, numberOfGames, alpha, beta, gamma):
        """ generated source for method trainOfflineRandomAndSave """
        fileName = "net" + str(numberOfGames) + "_a" + str(alpha) + "_b" + str(beta) + "g_" + str(gamma) + ".save"
        agent = Agent(alpha, beta, 0.0)
        cls.trainer = TemporalDifferenceTrainer(cls.game, agent, cls.player, gamma)
        cls.trainer.teachPassiveRandom(numberOfGames)
        agent.saveNetToFile(fileName)
        return fileName

    # 
    # 	 * test a Agent against a randomplayer,IMPORTANT if isOnlineLearng =false,
    # 	 * then paramters alpha, beta, gamma and lambda doesnt matter anyway,
    # 	 * because the agent is not learning while game is playing
    # 	 * 
    # 	 * @param path
    # 	 * @param numberOfGames
    # 	 * @param agentPlayFirst
    # 	 
    @classmethod
    def testAgentFromFileWithOutLearning(cls, path, numberOfGames, agentPlayFirst):
        """ generated source for method testAgentFromFileWithOutLearning """
        #  load and test
        cls.agent.loadNetFromFile(path)
        cls.trainer.teachActiveAndSaveStatistics(path, numberOfGames, 0.0, 0.0, 0.0, 0.0, 0.0, agentPlayFirst, False, False)


if __name__ == '__main__':
    import sys
    StartTests.main(sys.argv)

