import random

def pick_variable(domains, constraints, method="random"):
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
        
        
        max_constraints = 100
        for v in smallest_domain_vars:
            constraint_choices = 0
            for _, constraint in constraints:
                if v in constraint:
                    for cons_var in constraint:
                        if len(domains[cons_var]) != 1:
                            constraint_choices += 1
            if constraint_choices < max_constraints:
                max_constraints = constraint_choices
                var = v 
                
    if method == "most_constraining":                        
        max_constraints = 100
        for v in domains.keys():
            constraint_choices = 0
            for _, constraint in constraints:
                if v in constraint:
                    for cons_var in constraint:
                        if len(domains[cons_var]) != 1:
                            constraint_choices += 1
            #print domains, constraint_choices
            if constraint_choices < max_constraints and constraint_choices != 0:
                max_constraints = constraint_choices
                var = v                                  
    return var


def pick_values(var, domains, constraints, method="random"):
    """Value picking heuristic. Return a list of values for the specified
    var. Values will be assigned in the provided order."""
    
    #all possible values the chosen variable (var) can take
    values = domains[var]
    
    #random
    if method == "random":
        random.shuffle(values)
        
#selects the value that does not reduces the least number of smallest domain    
    if method == "least_constraining":
        min_domain_length = [100]*len(values)
        num_at_minimum = [1]*len(values)
        for _, constraint in constraints:
            if var in constraint:
                for const_var in constraint:
                    if const_var != var:
                        for value in values:
                            if value in domains[const_var]:
                                #print var, const_var, domains[const_var], values
                                if len(domains[const_var]) <= min_domain_length[values.index(value)]:
                                    num_at_minimum[values.index(value)] += 1
                                    if len(domains[const_var]) < min_domain_length[values.index(value)]:
                                        num_at_minimum[values.index(value)] = 1
                                        min_domain_length[values.index(value)] = len(domains[const_var])

        #print min_value,values
        zipped = zip(min_domain_length, num_at_minimum, values)
        zipped = sorted(zipped, key = lambda x: (x[0], x[1]))
        values = [z for y, x, z in zipped]
        #print zipped, values
    return values
