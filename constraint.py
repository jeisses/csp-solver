

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
