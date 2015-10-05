def create_domains(size = 9):
    """Returns dictionary of sudoku variables with domains"""
    dom = range(1, size)
    return {"x%s%s"%(x,y): list(dom) for x in dom for y in dom}

def create_constraints(size = 9):
    """Create sudoku constraints"""
    col_cons = [("ALL_DIFF", ["x%s%s"%(row,col) for col in range(1, size)]) for row in range(1,size)]
    row_cons = [("ALL_DIFF", ["x%s%s"%(col,row) for col in range(1, size)]) for row in range(1,size)]
    box_cons = []
    for i in range(0, 9):
        startx = (i*3) % 9
        starty = (i/3) * 3
        box_cons.append(("ALL_DIFF", ["x%s%s"%(row+startx+1,col+starty+1) for col in range(0, 3) for row in range(0, 3)]))

    return col_cons + row_cons + box_cons



def start_assign(board):
    startingAssignments = {}
    counter = 0
    for tile in board:
        if tile != '.' and tile.isdigit():
            row = counter/9
            col = counter%9
            variableName = 'x' + str(row + 1) + str(col + 1)
            startingAssignments[variableName] = int(board[counter])
        counter += 1
    return startingAssignments
    
def print_board(assignments):
    for col in range(1,10):
        for row in range(1,10):
            variable = 'x' + str(col) + str(row)
            if variable in assignments:
                print assignments[variable],
            else:
                print '.',
        print ""

  
