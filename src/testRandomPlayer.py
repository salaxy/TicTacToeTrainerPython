'''
Created on 17.02.2015

@author: Salaxy
'''
from RandomPlayer import RandomPlayer


if __name__ == '__main__':
    
    
    fields = ['X','X','O','-','-','X','O','O','-']
    
    r = RandomPlayer()
    
    for i in range(50):
        num = r.getMove(fields, 'O')
        print num
    
    pass