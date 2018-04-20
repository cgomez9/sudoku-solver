from SudokuBoard import SudokuBoard

import time

class Solver:

    def solve(self,boardString):
        sudokuBoard = SudokuBoard()
        sudokuBoard.fromString(boardString)
        return self.AC3(sudokuBoard)

    def AC3(self,sudokuBoard):
        queue = [(xi, xj) for xi in sudokuBoard.getAllVars() for xj in sudokuBoard.getArcs(xi)]
        while queue:
            (xi, xj) = queue.pop()
            if self.revise(sudokuBoard, xi, xj):
                if len(sudokuBoard.getDomain(xi)) == 0:
                    return False
                for xk in sudokuBoard.getArcs(xi):
                    if xk != xj:
                        queue.append((xk, xi))
        return True

    def revise(self,sudokuBoard, xi, xj):
        revised = False
        for x in sudokuBoard.getDomain(xi):
            if not any([sudokuBoard.constraint(x, y) for y in sudokuBoard.getDomain(xj)]):
                sudokuBoard.deleteDomainElement(xi,x)
                revised = True
        return revised

    def backtracking_search(self, sudokuBoard):
        return self.backtrack(sudokuBoard)

    def backtrack(self,sudokuBoard):
        if sudokuBoard.isComplete():
            return sudokuBoard.toString()
        emptyPosition = sudokuBoard.findEmptyPosition()
        for value in sudokuBoard.getDomain(emptyPosition):
            neighbors = sudokuBoard.getArcs(emptyPosition)
            consistent = True
            for neighbor in neighbors:
                if sudokuBoard.getVar(neighbor) == value:
                    consistent = False
                    break
            if consistent:
                sudokuBoard.setVar(emptyPosition,value)
                result = self.backtrack(sudokuBoard)
                if result:
                    return result
                sudokuBoard.setVar(emptyPosition,0)
        return False
