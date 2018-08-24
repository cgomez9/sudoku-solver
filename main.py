from Solver import Solver

initial_sudoku = sys.argv[1]

solver = Solver()
solution = solver.solve(initial_sudoku)

file = open("output.txt","w")
file.write(solution)
file.close()
