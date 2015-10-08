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
                    
    if method == "smallest_domain_then_reduces_most_domains":
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
            if len(domains[v]) > 1:
                for _, constraint in constraints:
                    if v in constraint:
                        for cons_var in constraint:
                            if len(domains[cons_var]) > 1:
                                constraint_choices += len(domains[cons_var])
            #print domains, constraint_choices
            if constraint_choices < max_constraints and constraint_choices > 0:
                max_constraints = constraint_choices
                var = v 
                
    #Selecting a variable which prunes the largest number of domains
    if method == "reduces_least_domains":                       
        max_constraints = 100
        for v in domains.keys():
            constraint_choices = 0
            if len(domains[v]) > 1:
                for _, constraint in constraints:
                    if v in constraint:
                        for cons_var in constraint:
                            if len(domains[cons_var]) > 1:
                                constraint_choices += len(domains[cons_var])
            #print domains, constraint_choices
            if constraint_choices < max_constraints and constraint_choices > 0:
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
        
    #selects the value that reduces the least number of the smallest domains available   
    if method == "reduce_least_num_of_smallest_domains":
        min_domain_length = [99999]*len(values)
        num_at_minimum = [1]*len(values)
        for _, constraint in constraints:
            if var in constraint:
                for const_var in constraint:
                    if const_var != var:
                        for value in values:
                            if value in domains[const_var]:
                                #if find a second min_domain_length increase num_at_minimum
                                if len(domains[const_var]) <= min_domain_length[values.index(value)]:
                                    num_at_minimum[values.index(value)] += 1
                                    #if find smaller min reset num_at_minimum, and change min_domain_length
                                    if len(domains[const_var]) < min_domain_length[values.index(value)]:
                                        num_at_minimum[values.index(value)] = 1
                                        min_domain_length[values.index(value)] = len(domains[const_var])

        zipped = zip(min_domain_length, num_at_minimum, values)
        zipped = sorted(zipped, key = lambda x: (x[0], x[1]))
        values = [z for y, x, z in zipped]
        #print zipped, values
        
    #selects the value that reduces the least number of the smallest domains  available   
    if method == "highest_promise":
        promise = [1]*len(values)
        for _, constraint in constraints:
            if var in constraint:
                for const_var in constraint:
                    if const_var != var:
                        for value_index in range(len(values)):
                            if values[value_index] in domains[const_var]:
                                promise[value_index] = promise[value_index]*len(domains[const_var]) - 1
                            else:
                                promise[value_index] = promise[value_index]*len(domains[const_var])
                        

        zipped = zip(promise, values)
        zipped.sort()
        values = [x for y, x in zipped]
        #print zipped, values
        
    return values
