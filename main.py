import csp, sudoku
import time, sys
from copy import deepcopy

import numpy

# Parse args
if len(sys.argv) < 3:
    print "Please use with 2 arguments, e.g. run_csp sudokus.txt solutions.txt"
    sys.exit()

file_in = sys.argv[1]
file_out = sys.argv[2]

# Setup 
csp.constraints = sudoku.create_constraints(10)
sudoku_domains = sudoku.create_domains(10)

csp.variable_heuristic = "smallest_domain" #random, smallest_domain, smallest_domain_then_reduces_most_domains
csp.value_heuristic = "highest_promise" #random, reduce_least_num_of_smallest_domains, highest_promise

stats = []

print "Start solving the sample file..."

start = time.time()

# Setup progress bar
num_lines = sum(1 for line in open(file_in, "r")) * 1.0
update_step = max(int(num_lines / 100), 1)

with open(file_in, "r") as f_in,\
     open(file_out, "w") as f_out:
    for idx, line in enumerate(f_in):
        assignment = sudoku.start_assign(line)

        # Solve CSP and store time
        local_start = time.time()
        solution = csp.solve(assignment, sudoku_domains)
        duration = time.time() - local_start
        stats.append((duration, csp.backtracks, csp.splits))

        # Progress bar
        if idx % update_step == 0:
            progress = int(idx / num_lines * 100)
            sys.stdout.write('\r[{0}] {1}%'.format('#'*int(progress/10), progress))
            sys.stdout.flush()

        f_out.write(''.join([str(v) for v in solution.values()]))
        f_out.write("\n")

duration = time.time() - start
print "\nSolved in %s seconds. Check %s for results"%(duration,file_out)

stats = numpy.asarray(stats)
numpy.savetxt("stats/"+csp.variable_heuristic + "_" + csp.value_heuristic + "_" + str(int(time.time()))[-7:], stats)

print "Times: %s  BTs: %s  Splits: %s"%(numpy.average(stats[:,0]), numpy.average(stats[:,1]), numpy.average(stats[:,2]))
