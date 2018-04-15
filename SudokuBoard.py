class SudokuBoard:

    def __init__(self):
        self._board = {}
        self._domains = {}
        self._neighbors = {}
        self.fillCPS()

    def fromString(self,boardString):
        i = 0
        for c in self.char_range('A', 'I'):
            for number in range(0,9):
                self._board[chr(c)+str(number)] = int(boardString[i])
                i += 1

    @staticmethod
    def char_range(c1, c2):
        yield from range(ord(c1), ord(c2)+1)

    def getVar(self,var):
        return self._board[var]

    def fillCPS(self):
        for c in self.char_range('A', 'I'):
            for number in range(0,9):
                xi = chr(c)+str(number)
                self._domains[xi] = [0,1,2,3,4,5,6,7,8]
                self._neighbors[xi] = self.getNeighbors(xi)

    def getNeighbors(self,x1):
        allNeighbors = []
        allNeighbors += self.getRowsNeighbors(x1)
        allNeighbors += self.getColumnsNeighbors(x1)
        allNeighbors += self.getBoxNeighbors(x1)
        print(allNeighbors)
        raise Exception
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
                columnGroup = int(x1[1]) / 3
                for rgroup in group:
                    for column in range(columnGroup * 3, columnGroup * 3 + 3):
                        x = str(rgroup) + str(column)
                        if x1 != x:
                            boxNeighbors.append(x)
                break
        return boxNeighbors
