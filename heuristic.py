import random

def pick_variable(domains, method="random"):
    """Variable picking heuristic. Return value should the variable
    to assign as string. Return None if all variables are assigned"""
    var = None
    variables = domains.keys()

    if method == "smallest_domain":
        smallest_v = 99999
        for v in domains.keys():
            lend = len(domains[v]) 
            if lend > 1:
                if lend < smallest_v:
                    smallest_v = lend
                    var = v

    elif method == "random":
        random.shuffle(variables)
        for v in variables:
            if len(domains[v]) > 1:
                var = v
                break
                    
    if method == "smallest_domain_then_most_constraining":
        smallest_v = 99999
        smallest_domain_vars = []
        for v in domains.keys():
            lend = len(domains[v]) 
            if lend > 1:
                if lend <= smallest_v:
                    if lend < smallest_v:
                        smallest_domain_vars = []
                    smallest_v = lend
                    smallest_domain_vars.append(v)
        
        
        max_constrain = 0
        for v in smallest_domain_vars:
            constraint_choices = 0
            for _, constraint in constraints:
                if v in constraint:
                    for cons_var in constraint:
                        if len(domains[cons_var]) != 1:
                            constraint_choices += 1
            if constraint_choices > max_constrain:
                max_constrain = constraint_choices
                var = v
                
    if method == "most_constraining":
        max_constrain = 0
        for v in domains.keys():
            constraint_choices = 0
            for _, constraint in constraints:
                if v in constraint:
                    for cons_var in constraint:
                        if len(domains[cons_var]) != 1:
                            constraint_choices += 1
            if constraint_choices > max_constrain:
                max_constrain = constraint_choices
                var = v           
                                 
    return var


def pick_values(var, domains, constraints, method="random"):
    """Value picking heuristic. Return a list of values for the specified
    var. Values will be assigned in the provided order."""
    values = domains[var]
    if method == "random":
        random.shuffle(values)
        
    if method == "least_constraining":
        min_value = [100]*len(values)
        for _, constraint in constraints:
            if var in constraint:
                for const_var in constraint:
                    if const_var != var:
                        for value in values:
                            if value in domains[const_var]:
                                if len(domains[const_var]) < min_value[values.index(value)]:
                                    print domains[const_var],
                                    min_value[values.index(value)] = len(domains[const_var])

        zipped = zip(min_value,values)
        zipped.sort(reverse = True)
        values = [x for y, x in zipped]
        print zipped
    return values
