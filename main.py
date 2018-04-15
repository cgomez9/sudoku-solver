from Solver import Solver

problemFile = open("sudokus_start.txt", "r")
solutionFile = open("sudokus_finish.txt", "r")
solutions = []
correct = 0
wrong = 0
total = 0

for line in solutionFile:
    solutions.append(str(line))

solver = Solver()

for index,line in enumerate(problemFile):
    print("Testing ",line)
    solution = solver.solve(line)
    print("Expected ",solutions[index])
    print("Got ",solution)
    if solutions[index] == solution:
        print("Correct!")
        correct += 1
    else:
        print("Wrong!")
        wrong += 1
    total += 1
    print("**************************************************")
    break
print("")
print("Corrects: {}, Incorrects: {}, total: {}".format(correct,wrong,total) )
