import csp, sudoku
import time, sys
from copy import deepcopy

# Parse args
if len(sys.argv) < 3:
    print "Please use with 2 arguments, e.g. run_csp sudokus.txt solutions.txt"
    sys.exit()

file_in = sys.argv[1]
file_out = sys.argv[2]

# Setup 
csp.constraints = sudoku.create_constraints(10)
sudoku_domains = sudoku.create_domains(10)

csp.variable_heuristic = "smallest_domain"
csp.value_heuristic = "random"

times = []

print "Start solving the sample file..."

start = time.time()
num_lines = sum(1 for line in open(file_in, "r")) * 1.0
update_step = max(int(num_lines / 100), 1)
with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
    for idx, line in enumerate(f_in):
        assignment = deepcopy(sudoku.start_assign(line))
        domains = deepcopy(sudoku_domains)

        local_start = time.time()
        solution = csp.solve(assignment, domains)
        duration = time.time() - local_start
        times.append(duration) 

        if idx % update_step == 0:
            progress = int(idx / num_lines * 100)

            sys.stdout.write('\r[{0}] {1}%'.format('#'*int(progress/10), progress))
            sys.stdout.flush()

        f_out.write(''.join([str(v) for v in solution.values()]))
        f_out.write("\n")

duration = time.time() - start
print "\nSolved in %s seconds. Check %s for results"%(duration,file_out)

