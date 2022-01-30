import pickle
import os

class pickler(object):
    def __init__(self, topickle):
        self.puzzles = topickle
    def pickle(self):
        if(os.path.exists("sudoku_puzzles.txt")):
            os.remove("sudoku_puzzles.txt")
        outfile = open("sudoku_puzzles.txt", 'ab')
        pickle.dump(self.puzzles, outfile)
        outfile.close()
    def unpickle(self):
        if(os.path.exists("sudoku_puzzles.txt")):
            self.pickle()
        outfile = open("sudoku_puzzles", 'rb')
        self.puzzles = pickle.load(outfile)
        outfile.close()
    def addpuzzle(self, sudoku):
        self.unpickle()
        self.puzzles.append(sudoku)
        self.pickle()
    def removepuzzle(self, index):
        self.unpickle()
        self.puzzles.remove(index)
        self.pickle()

sp1=[[0,0,0,2,6,0,7,0,1],
     [6,8,0,0,7,0,0,9,0],
     [1,9,0,0,0,4,5,0,0],
     [8,2,0,1,0,0,0,4,0],
     [0,0,4,6,0,2,9,0,0],
     [0,5,0,0,0,3,0,2,8],
     [0,0,9,3,0,0,0,7,4],
     [0,4,0,0,5,0,0,3,6],
     [7,0,3,0,1,8,0,0,0]]

sp2=[[0,2,0,5,0,1,0,9,0],
     [8,0,0,2,0,3,0,0,6],
     [0,3,0,0,6,0,0,7,0],
     [0,0,1,0,0,0,6,0,0],
     [5,4,0,0,0,0,0,1,9],
     [0,0,2,0,0,0,7,0,0],
     [0,9,0,0,3,0,0,8,0],
     [2,0,0,8,0,4,0,0,7],
     [0,1,0,9,0,7,0,6,0]]

sp3=[[1,0,0,4,8,9,0,0,6],
     [7,3,0,0,0,0,0,4,0],
     [0,0,0,0,0,1,2,9,5],
     [0,0,7,1,2,0,6,0,0],
     [5,0,0,7,0,3,0,0,8],
     [0,0,6,0,9,5,7,0,0],
     [9,1,4,6,0,0,0,0,0],
     [0,2,0,0,0,0,0,3,7],
     [8,0,0,5,1,2,0,0,4]]

sp4=[[5,3,0,0,7,0,0,0,0],
     [6,0,0,1,9,5,0,0,0],
     [0,9,8,0,0,0,0,6,0],
     [8,0,0,0,6,0,0,0,3],
     [4,0,0,8,0,3,0,0,1],
     [7,0,0,0,2,0,0,0,6],
     [0,6,0,0,0,0,2,8,0],
     [0,0,0,4,1,9,0,0,5],
     [0,0,0,0,8,0,0,7,9]]

sp5=[[0,0,0,8,0,0,0,0,0],
     [4,0,0,0,1,5,0,3,0],
     [0,2,9,0,4,0,5,1,8],
     [0,4,0,0,0,0,1,2,0],
     [0,0,0,6,0,2,0,0,0],
     [0,3,2,0,0,0,0,9,0],
     [6,9,3,0,5,0,8,7,0],
     [0,5,0,4,8,0,0,0,1],
     [0,0,0,0,0,3,0,0,0]]

sp6=[[0,2,0,6,0,8,0,0,0],
     [5,8,0,0,0,9,7,0,0],
     [0,0,0,0,4,0,0,0,0],
     [3,7,0,0,0,0,5,0,0],
     [6,0,0,0,0,0,0,0,4],
     [0,0,8,0,0,0,0,1,3],
     [0,0,0,0,2,0,0,0,0],
     [0,0,9,8,0,0,0,3,6],
     [0,0,0,3,0,6,0,9,0]]

sp7=[[0,6,0,3,0,0,8,0,4],
     [5,3,7,0,9,0,0,0,0],
     [0,4,0,0,0,6,3,0,7],
     [0,9,0,0,5,1,2,3,8],
     [0,0,0,0,0,0,0,0,0],
     [7,1,3,6,2,0,0,4,0],
     [3,0,6,4,0,0,0,1,0],
     [0,0,0,0,6,0,5,2,3],
     [1,0,2,0,0,9,0,8,0]]

s=[[[]]]
s.append(sp1)
s.append(sp2)
s.append(sp3)
s.append(sp4)
s.append(sp5)
s.append(sp6)
s.append(sp7)

p=pickler(s)
p.pickle()
p.unpikkle()
p.addpuzzle()
p.removepuzzle()