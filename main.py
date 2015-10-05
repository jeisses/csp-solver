import csp, sudoku
import time
from copy import deepcopy


# Setup 
csp.constraints = sudoku.create_constraints(10)
sudoku_domains = sudoku.create_domains(10)

csp.variable_heuristic = "smallest_domain"
csp.value_heuristic = "random"

times = []

print "Start solving the sample file..."

with open("sudokus.txt") as f:
    for line in f:
        assignment = deepcopy(sudoku.start_assign(line))
        domains = deepcopy(sudoku_domains)

        start = time.time()
        solution = csp.solve(assignment, domains)
        duration = time.time() - start
        times.append(duration) 

        print "Done! Solution found in %s seconds:"%duration
        sudoku.print_board(solution)


