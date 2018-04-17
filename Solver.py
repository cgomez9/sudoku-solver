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
        for element,domain in sudokuBoard._domains.items():
            print(element, domain)
        time.sleep(40)
        return True

    def revise(self,sudokuBoard, xi, xj):
        revised = False
        print(sudokuBoard.getDomain(xi))
        print(sudokuBoard.getDomain(xj))
        for x in sudokuBoard.getDomain(xi):
            if not any([sudokuBoard.constraint(x, y) for y in sudokuBoard.getDomain(xj)]):
                sudokuBoard.deleteDomainElement(xi,x)
                revised = True
        return revised

    def backtracking_search(self):
        pass

    def backtrack(self):
        pass
