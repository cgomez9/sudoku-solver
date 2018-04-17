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
            #print("Procesando el arco: ",xi,xj)
            if self.revise(sudokuBoard, xi, xj):
                #time.sleep(3)
                #print("Revise TRUE")
                if len(sudokuBoard.getDomain(xi)) == 0:
                    return False
                for xk in sudokuBoard.getArcs(xi):
                    if xk != xj:
                        queue.append((xk, xi))
        return True

    def revise(self,sudokuBoard, xi, xj):
        #time.sleep(10)
        #print("**Entramos en revise**")
        revised = False
        #print("Dominio de: ",xi)
        #print(sudokuBoard.getDomain(xi))
        #print("Dominio de: ",xj)
        #print(sudokuBoard.getDomain(xj))
        for x in sudokuBoard.getDomain(xi):
            satisfied = False
            for y in sudokuBoard.getDomain(xj):
                if sudokuBoard.constrain(xi,x,xj,y):
                    satisfied = True
                    break
            if not satisfied:
                sudokuBoard.deleteDomainElement(xi,x)
                revised = True
        return revised

    def backtracking_search(self):
        pass

    def backtrack(self):
        pass
