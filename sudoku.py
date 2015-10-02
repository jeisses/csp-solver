def create_domains():
    """Returns dictionary of sudoku variables with domains"""
    dom = range(1, 10)
    return {"x%s%s"%(x,y): list(dom) for x in dom for y in dom}

def create_constraints():
    """Create sudoku constraints"""
    col_cons = [("ALL_DIFF", ["x%s%s"%(row,col) for col in range(1, 10)]) for row in range(1,10)]
    row_cons = [("ALL_DIFF", ["x%s%s"%(col,row) for col in range(1, 10)]) for row in range(1,10)]
    box_cons = []
    for horiz in range(3):
        for vert in range(3):
            box_cons.append(("ALL_DIFF", ["x%s%s"%(col,row) for col in range(vert*3 + 1, vert*3 + 4) for row in range(horiz*3 + 1, horiz*3 + 4)]))
    return col_cons + row_cons + box_cons



def start_assign(board):
    startingAssignments = {}
    counter = 0
    for item in board:
        if item != '.':
            row = counter/9
            col = counter%9
            variableName = 'x' + str(row + 1) + str(col + 1)
            startingAssignments[variableName] = board[counter]
        counter += 1
    return startingAssignments
    
def print_board(assignment):
    counter = 0
    for item, value in assignment.iteritems():
        print value
        if counter%9 == 0:
            print "\n"
        counter += 1
        
        

  
