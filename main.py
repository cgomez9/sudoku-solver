from Solver import Solver

initialSudoku = sys.argv[1]

solver = Solver()
solution = solver.solve(initialSudoku)

file = open("output.txt","w")
file.write(solution)
file.close()
