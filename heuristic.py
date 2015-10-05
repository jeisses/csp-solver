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

    return var


def pick_values(var, domains, constraints, method="random"):
    """Value picking heuristic. Return a list of values for the specified
    var. Values will be assigned in the provided order."""
    values = domains[var]
    if method == "random":
        random.shuffle(values)

    return values
