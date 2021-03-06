import time
from constraint import all_satisfied, propagate
import heuristic as hr
import random
import sudoku

# Global variables
constraints = []
variable_heuristic = ""
value_heuristic = ""

# Stats
backtracks = 0
splits = 0

def solve(assignment, domains):
    """Solve a CSP problem. Starts the backtrack process"""
    global backtracks, splits, constraints

    backtracks = splits = 0

    # Fast deepcopy the initial state
    new_domains = {k: [v for v in values] for k,values in domains.iteritems()}
    new_assignment = {k: v for k,v in assignment.iteritems()}
    
    # Use initial assignment to prune domains
    assigned_vars = assignment.keys()
    while assigned_vars != False and len(assigned_vars) > 0:
        assigned_vars = propagate(new_domains, new_assignment, constraints, assigned_vars)

    # Start the solver
    return bt(new_assignment, new_domains, [])

def bt(assignment, domains, last_var):
    """Performs a CSP solving with the Backtrack algorithm"""
    global backtracks, splits, constraints

    # Fast deepcopy the CSP state
    new_domains = {k: [v for v in values] for k,values in domains.iteritems()}
    new_assignment = {k: v for k,v in assignment.iteritems()}


    # Prune the domains connected with the assigned variables
    assigned_vars = [last_var]
    while assigned_vars != False and len(assigned_vars) > 0:
        assigned_vars = propagate(new_domains, new_assignment, constraints, assigned_vars)

    # Check for inconsistency
    if (assigned_vars == False):
        return False

    # Pick the next variable
    var = hr.pick_variable(new_domains, constraints, method=variable_heuristic)
    #sudoku.print_board_domains(domains)

    # Check if a solution is found done
    if var == None:
        return new_assignment

    # Backtracking for each value
    values = hr.pick_values(var, domains, constraints, method=value_heuristic)
    for value in values:
        new_assignment[var] = value
        res = bt(new_assignment, new_domains, var)
        if res != False:
            return res
        backtracks += 1
        
    splits += 1
    return False
    
