from SudokuBoard import SudokuBoard

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
            satisfied = False
            for y in sudokuBoard.getDomain(xj):
                if x != y:
                    satisfied = True
                    break
            if not satisfied:
                sudokuBoard.deleteDomainElement(xi,x)
                revised = True
        return revised
