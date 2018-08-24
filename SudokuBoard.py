from math import floor
import time

class SudokuBoard:

    def __init__(self):
        self._board = {}
        self._domains = {}
        self._neighbors = {}

    def from_string(self,board_string):
        i = 0
        for c in self.char_range('A', 'I'):
            for number in range(0,9):
                self._board[chr(c)+str(number)] = int(board_string[i])
                i += 1
        self.fill_cps()

    @staticmethod
    def char_range(c1, c2):
        yield from range(ord(c1), ord(c2)+1)

    def get_arcs(self,x):
        return self._neighbors[x]

    def get_var(self,var):
        return self._board[var]

    def set_var(self,var,value):
        self._board[var] = value

    def get_all_vars(self):
        return list(self._board.keys())

    def get_domain(self,x):
        return self._domains[x]

    def set_domain(self,x,value):
        self._domains[x] = value
        neighbors = self.get_arcs(x)
        for neighbor in neighbors:
            domain_copy = list(self._domains[neighbor])
            if value in domain_copy:
                domain_copy.remove(e)
                if len(domain_copy) == 0:
                    return False
        return True

    def delete_domain_element(self,x,e):
        self._domains[x].remove(e)

    def fill_cps(self):
        for c in self.char_range('A', 'I'):
            for number in range(0,9):
                xi = chr(c)+str(number)
                if self._board[xi] != 0:
                    self._domains[xi] = [int(self._board[xi])]
                else:
                    self._domains[xi] = [1,2,3,4,5,6,7,8,9]
                self._neighbors[xi] = self.get_neighbors(xi)

    def get_neighbors(self,x1):
        all_neighbors = []
        all_neighbors += self.get_rows_neighbors(x1)
        all_neighbors += self.get_columns_neighbors(x1)
        all_neighbors += self.get_box_neighbors(x1)
        all_neighbors = list(set(all_neighbors))
        return all_neighbors

    def get_rows_neighbors(self,x1):
        row_neighbors = []
        row = x1[0]
        for i in range(9):
            neighbor = row + str(i)
            if neighbor != x1:
                row_neighbors.append(neighbor)
        return row_neighbors

    def get_columns_neighbors(self,x1):
        column_neighbors = []
        column = x1[1]
        for c in self.char_range('A', 'I'):
            neighbor = chr(c) + column
            if neighbor != x1:
                column_neighbors.append(neighbor)
        return column_neighbors

    def get_box_neighbors(self,x1):
        box_neighbors = []
        row = x1[0]
        row_groups = (('A','B','C'),('D','E','F'),('G','H','I'))
        for group in row_groups:
            if row in group:
                column_groups = floor(int(x1[1]) / 3)
                for rgroup in group:
                    for column in range(int(column_groups * 3), int(column_groups * 3 + 3)):
                        x = str(rgroup) + str(column)
                        if x1 != x:
                            box_neighbors.append(x)
                break
        return box_neighbors

    def constraint(self,x,y):
        return x != y

    def is_complete(self):
        return 0 not in self._board.values()

    def to_string(self,algo = 'BTS'):
        solution = ''
        for c in self.char_range('A', 'I'):
            for number in range(0,9):
                solution += str(self._board[chr(c)+str(number)])
        return solution + ' ' + algo

    def find_empty_position(self):
        min_domain = 10
        min_element = ''
        for c in self.char_range('A', 'I'):
            for number in range(0,9):
                xi = chr(c)+str(number)
                if self._board[xi] == 0 and len(self._domains[xi]) < min_domain:
                    min_domain = len(self._domains[xi])
                    min_element = xi
                    if min_domain == 1:
                        return min_element
        return min_element

    def try_to_solve_from_domains(self):
        for c in self.char_range('A', 'I'):
            for number in range(0,9):
                xi = chr(c)+str(number)
                if len(self._domains[xi]) == 1:
                    self._board[xi] = self._domains[xi][0]
                else:
                    return False
        return True
