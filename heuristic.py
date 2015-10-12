import random

def pick_variable(domains, constraints, method="random"):
    """Variable picking heuristic. Return value should the variable
    to assign as string. Return None if all variables are assigned"""
    var = None
    variables = domains.keys()

    # Picks the smallest domain
    if method == "smallest_domain":
        smallest_v = 99999
        for v in domains.keys():
            lend = len(domains[v]) 
            if lend > 1:
                if lend < smallest_v:
                    smallest_v = lend
                    var = v

    # Picka a random variable from the unassigned set (domain > 1)
    elif method == "random":
        random.shuffle(variables)
        for v in variables:
            if len(domains[v]) > 1:
                var = v
                break
                
    return var


def pick_values(var, domains, constraints, method="random"):
    """Value picking heuristic. Return a list of values for the specified
    var. Values should be assigned in the provided order."""
    
    # The possible values to choose from
    values = domains[var]
    
    # The promise heuristic should be reversed if "lowest" is selected
    reverse = False
    if method == "lowest_promise":
        reverse = True
        method = "highest_promise"
        

    # Randomly asserts the values
    if method == "random":
        random.shuffle(values)
        
    # Selects the value that reduces the least number of the smallest domains available   
    elif method == "least_constraining":
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
        
    # Selects the value that reduces the least number of the smallest domains  available   
    elif method == "highest_promise":
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
        # Zip sorts highest value first. If highest promise, reverse = True
        zipped.sort(reverse=not reverse)
        values = [x for y, x in zipped]
        
    return values
