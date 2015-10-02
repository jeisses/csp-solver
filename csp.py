import sudoku
from constraint import all_satisfied, propagate
import random
from copy import deepcopy

# Global variables
constraints = sudoku.create_constraints()

def bt(assignment, domains, lvl, last_var):
    # Copy CSP state
    new_domains = deepcopy(domains)
    new_assignment = deepcopy(assignment)

    # Constraint Propagation. This prunes the domains.
    propagate(new_domains, assignment, constraints, last_var)
    
    # If Empty domains: 
    #    return False

    # If we filled in the entire board
    # TODO: correct check
    if len(assignment) == 81:
        return assignment

    # If Single Domain:
    #   var = [the_var] 
    # Else:
    #   var = pick_variable(domains, constraints) 
    var = random.choice(domains.keys())
    while var in assignment:
        var = random.choice(domains.keys())

    new_assignment[var] = None

    # Try each value in domain
    for value in domains[var]:
        new_assignment[var] = value
        if all_satisfied(constraints, new_assignment) == True:
            res = bt(new_assignment, new_domains, lvl + 1, var)
            if res != False:
                return res
                
    return False
    
# Board setup
board1 = "............942.8.16.....29........89.6.....14..25......4.......2...8.9..5....7.."
start_assignment = sudoku.start_assign(board1)

print "Solving CSP for sudoku..."

solution = bt(start_assignment, sudoku.create_domains(), 0, "")

print "Done! Solution: "
print solution
