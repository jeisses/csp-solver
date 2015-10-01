import sudoku
from constraint import all_satisfied
import random

domains = sudoku.create_domains()
variables = domains.keys()
constraints = sudoku.create_constraints()

print constraints

happy = False
depth = 0

def bt(assignment, domains, lvl):
    if lvl > 1000:
        print "Max depth reached"
        return False

    # Constraint Propagation
    # new_domains = constraint.propagate(...)
    
    # If Empty domains: 
    #    return False

    # If we filled in the entire board
    # TODO: correct check
    if len(assignment) > 50:
        happy = True
        return True

    # If Single Domain:
    #   var = [the_var] 
    # Else:
    #   var = pick_variable(domains, constraints) 
    var = random.choice(variables)
    while var in assignment:
        var = random.choice(variables)

    new_assignment = assignment.copy()
    new_assignment[var] = None

    # Try each value in domain
    for value in domains[var]:
        new_assignment[var] = value
        if all_satisfied(constraints, new_assignment) == True:
            res = bt(new_assignment, domains, lvl + 1)
            if res != False:
                return True
                
    return False
    

bt({}, 0)
print "Done :) --"
print assigned
    
