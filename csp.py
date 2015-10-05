import time
from constraint import all_satisfied, propagate
import heuristic as hr
import random
from copy import deepcopy

# Global variables
constraints = []
variable_heuristic = "smallest_domain"
value_heuristic = "random"

def solve(assignment, domains):
    """Solve a CSP problem. Starts the backtrack process"""
    # Use initial assignment to prune domains
    new_assignment = deepcopy(assignment)
    for var in assignment:
        domains[var] = [new_assignment[var]]
        propagate(domains, new_assignment, constraints, [var])

    return bt(assignment, domains, [])

def bt(assignment, domains, last_var):
    """Performs a CSP solving with the Backtrack algorithm"""
    # Copy CSP state
    new_domains = deepcopy(domains)
    new_assignment = deepcopy(assignment)

    # Prune the domains connected with the assigned variables
    assigned_vars = [last_var]
    while assigned_vars != False and len(assigned_vars) > 0:
        assigned_vars = propagate(new_domains, new_assignment, constraints, assigned_vars)

    # Check for inconsistency
    if (assigned_vars == False):
        return False

    # Pick the next variable
    var = hr.pick_variable(new_domains, method="smallest_domain")

    # Check if a solution is found done
    if var == None:
        return new_assignment

    # Backtracking for each value
    values = hr.pick_values(var, domains, constraints, method="random")
    for value in values:
        new_assignment[var] = value
        new_domains[var] = [value]
        res = bt(new_assignment, new_domains, var)
        if res != False:
            return res
                
    return False
    
