import sudoku
from constraint import all_satisfied, propagate
import random


def bt(assignment, domains, lvl, last_var):
    if lvl > 1000:
        print "Max depth reached"
        return False

    # Constraint Propagation
    new_domains = domains.copy()
    propagate(new_domains, assignment, constraints, last_var)
    
    # If Empty domains: 
    #    return False

    # If we filled in the entire board
    # TODO: correct check
    if len(assignment) == 60:
        return assignment

    # If Single Domain:
    #   var = [the_var] 
    # Else:
    #   var = pick_variable(domains, constraints) 
    var = random.choice(domains.keys())
    while var in assignment:
        var = random.choice(domains.keys())

    new_assignment = assignment.copy()
    new_assignment[var] = None

    # Try each value in domain
    for value in domains[var]:
        new_assignment[var] = value
        if all_satisfied(constraints, new_assignment) == True:
            res = bt(new_assignment, new_domains, lvl + 1, var)
            if res != False:
                return res
                
    return False
    
constraints = sudoku.create_constraints()
asg = bt({}, sudoku.create_domains(), 0, "")

print "Done :) --"
solution = asg
print solution
    
