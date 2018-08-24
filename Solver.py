from SudokuBoard import SudokuBoard

import time

class Solver:

    def solve(self,boardString):
        sudoku_board = SudokuBoard()
        sudoku_board.from_string(boardString)
        if self.AC3(sudoku_board):
            return sudoku_board.to_string('AC3')
        else:
            return self.backtracking_search(sudoku_board)

    def AC3(self,sudoku_board):
        queue = [(xi, xj) for xi in sudoku_board.get_all_vars() for xj in sudoku_board.get_arcs(xi)]
        while queue:
            (xi, xj) = queue.pop()
            if self.revise(sudoku_board, xi, xj):
                if len(sudoku_board.get_domain(xi)) == 0:
                    return False
                for xk in sudoku_board.get_arcs(xi):
                    if xk != xj:
                        queue.append((xk, xi))
        if sudoku_board.try_to_solve_from_domains():
            return True
        else:
            return False;

    def revise(self,sudoku_board, xi, xj):
        revised = False
        for x in sudoku_board.get_domain(xi):
            if not any([sudoku_board.constraint(x, y) for y in sudoku_board.get_domain(xj)]):
                sudoku_board.delete_domain_element(xi,x)
                revised = True
        return revised

    def backtracking_search(self, sudoku_board):
        return self.backtrack(sudoku_board)

    def backtrack(self,sudoku_board):
        if sudoku_board.is_complete():
            return sudoku_board.to_string()
        empty_position = sudoku_board.find_empty_position()
        for value in sudoku_board.get_domain(empty_position):
            neighbors = sudoku_board.get_arcs(empty_position)
            consistent = True
            for neighbor in neighbors:
                if sudoku_board.get_var(neighbor) == value:
                    consistent = False
                    break
            if consistent:
                sudoku_board.set_var(empty_position,value)
                empty_positionDomain = sudoku_board.get_domain(empty_position)
                inference = sudoku_board.set_domain(empty_position,[value])
                if inference:
                    result = self.backtrack(sudoku_board)
                    if result:
                        return result
                sudoku_board.set_var(empty_position,0)
                sudoku_board.set_domain(empty_position,empty_positionDomain)
        return False
