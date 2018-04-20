from math import floor
import time

class SudokuBoard:

    def __init__(self):
        self._board = {}
        self._domains = {}
        self._neighbors = {}

    def fromString(self,boardString):
        i = 0
        for c in self.char_range('A', 'I'):
            for number in range(0,9):
                self._board[chr(c)+str(number)] = int(boardString[i])
                i += 1
        self.fillCPS()

    @staticmethod
    def char_range(c1, c2):
        yield from range(ord(c1), ord(c2)+1)

    def getArcs(self,x):
        return self._neighbors[x]

    def getVar(self,var):
        return self._board[var]

    def getAllVars(self):
        return list(self._board.keys())

    def getDomain(self,x):
        return self._domains[x]

    def deleteDomainElement(self,x,e):
        self._domains[x].remove(e)

    def fillCPS(self):
        for c in self.char_range('A', 'I'):
            for number in range(0,9):
                xi = chr(c)+str(number)
                if self._board[xi] != 0:
                    self._domains[xi] = [int(self._board[xi])]
                else:
                    self._domains[xi] = [1,2,3,4,5,6,7,8,9]
                self._neighbors[xi] = self.getNeighbors(xi)

    def getNeighbors(self,x1):
        allNeighbors = []
        allNeighbors += self.getRowsNeighbors(x1)
        allNeighbors += self.getColumnsNeighbors(x1)
        allNeighbors += self.getBoxNeighbors(x1)
        allNeighbors = list(set(allNeighbors))
        return allNeighbors

    def getRowsNeighbors(self,x1):
        rowNeighbors = []
        row = x1[0]
        for i in range(9):
            neighbor = row + str(i)
            if neighbor != x1:
                rowNeighbors.append(neighbor)
        return rowNeighbors

    def getColumnsNeighbors(self,x1):
        columnNeighbors = []
        column = x1[1]
        for c in self.char_range('A', 'I'):
            neighbor = chr(c) + column
            if neighbor != x1:
                columnNeighbors.append(neighbor)
        return columnNeighbors

    def getBoxNeighbors(self,x1):
        boxNeighbors = []
        row = x1[0]
        rowGroups = (('A','B','C'),('D','E','F'),('G','H','I'))
        for group in rowGroups:
            if row in group:
                columnGroup = floor(int(x1[1]) / 3)
                for rgroup in group:
                    for column in range(int(columnGroup * 3), int(columnGroup * 3 + 3)):
                        x = str(rgroup) + str(column)
                        if x1 != x:
                            boxNeighbors.append(x)
                break
        return boxNeighbors

    def constraint(self,x,y):
        return x != y

    def isComplete(self):
        return 0 not in self._board.values()

    def toString(self):
        return "".join([str(value) for value in self._board.values()])
