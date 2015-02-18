#!/usr/bin/env python
""" generated source for module RandomPlayer """
# package: de.fhb.infm.knn.trainer.worldmodel
#import java.util.Random
from random import Random

# 
#  * This a random player to be used by the TemporalDifferenceTrainer for training an agent to play
#  * 
#  * @author Andy Klay 2014
#  
class RandomPlayer(object):
    """ generated source for class RandomPlayer """
    # 
    # 	 * smple initializer
    # 	 
    def __init__(self):
        """ generated source for method __init__ """
        super(RandomPlayer, self).__init__()

    # 
    # 	 * 
    # 	 * 
    # 	 * @param fields
    # 	 * @param playersSymbol
    # 	 *            - symbols possible X or O
    # 	 * @return - Fehlerwert -1
    # 	 
    def getMove(self, fields, playersSymbol):
        """ generated source for method getMove """
        #  von 0 bis 8 ... 9 Felder, links nach rechts,
        #  oben nach unten nummeriert
        random = Random()
        #  teste ob weniger symbole des Spielers vorhanden als des anderen
        #  sonst Fehler
        xValues = 0
        oValues = 0
        zeroValues = 0
        decision = 0
        i = 0
        while i <= 8:
            if fields[i] == 'X':
                xValues += 1
            if fields[i] == 'O':
                oValues += 1
            if fields[i] == '-':
                zeroValues += 1
            i += 1
        #  teste ob Rahmenbedingungen stimmen, sonst return Fehlerwert
        if playersSymbol == 'O' and oValues > xValues:
            return -1
        if playersSymbol == 'X' and xValues > oValues:
            return -1
        if zeroValues == 0:
            return -1
        cancel = False
        #  erzeuge randomzahl und teste ob Feld frei ist.
        while not cancel:
            #decision = random.nextInt(9)
            decision = random.randrange(0,9,1)
            #print decision
            if fields[decision] == '-':
                cancel = True
        return decision

