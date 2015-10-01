def create_domains():
    """Returns dictionary of sudoku variables with domains"""
    dom = range(1, 10)
    return {"x%s%s"%(x,y): list(dom) for x in dom for y in dom}

def create_constraints():
    """Create sudoku constraints"""
    col_cons = [("ALL_DIFF", ["x%s%s"%(row,col) for col in range(1, 10)]) for row in range(1,10)]
    row_cons = [("ALL_DIFF", ["x%s%s"%(col,row) for col in range(1, 10)]) for row in range(1,10)]
    return col_cons + row_cons
