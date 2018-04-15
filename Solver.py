from SudokuBoard import SudokuBoard

class Solver:

    def __init__(self):
        self.sudokuBoards = []
        self.solutions = []

    def solve(self,boardString):
        sudokuBoard = SudokuBoard()
        sudokuBoard.fromString(boardString)

    def AC3(csp, queue=None):
        queue = [(Xi, Xk) for Xi in csp.vars for Xk in csp.neighbors[Xi]]
        while queue:
            (Xi, Xj) = queue.pop()
            if remove_inconsistent_values(csp, Xi, Xj):
                for Xk in csp.neighbors[Xi]:
                    queue.append((Xk, Xi))

    def remove_inconsistent_values(csp, Xi, Xj):
        "Return true if we remove a value."
        removed = False
        for x in csp.curr_domains[Xi][:]:
            # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
            if every(lambda y: not csp.constraints(Xi, x, Xj, y),
                    csp.curr_domains[Xj]):
                csp.curr_domains[Xi].remove(x)
                removed = True
        return removed
