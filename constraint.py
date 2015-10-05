

def satisfied(cons, vars, ass):
    """If a constraints is satisfied under assignment"""
    if cons == "ALL_DIFF":
        return _satisfied_all_diff(vars, ass)


def all_satisfied(cons, ass):
    """If a list of constraints is satisfied under assignment"""
    for con in cons:
        if satisfied(*con, ass=ass) == False:
            return False
    return True



def _satisfied_all_diff(vars, ass):
    """Check ALL DIFFERENT constraint"""
    for v in vars:
        for vv in vars:
            if vv != v and vv in ass and v in ass and ass[vv] == ass[v]:
                return False

    return True


def propagate(domains, assignment, constraints, last_vars):
    if len(last_vars) == 0:
        return []
    
    unit_domains = []
    for last_var in last_vars:
        for _, const_vars in constraints:
            if last_var in const_vars:
                for var in const_vars:
                    if var != last_var:
                        if assignment[last_var] in domains[var]:
                            domains[var].remove(assignment[last_var])

                            if len(domains[var]) == 0:
                                return False
                            elif len(domains[var]) == 1:
                                assignment[var] = domains[var][0]
                                unit_domains.append(var)

    return unit_domains
