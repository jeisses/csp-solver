Knowledge Representation Project - CSP solver
==========
Value Ordering Heuristics for Sudoku CSPs

### Requirements
Python 2.7

### Usage

From the shell run:
```
./my-csp-solver data/sudoku-1000.txt sudoku-1000-solution.txt
```
Or use python directly:
```
python main.py data/sudoku-1000.txt sudoku-1000-solution.txt
```

### Project layout
Functions are split in files

- **csp.py** contains the CSP sovler backtrack algorithm
- **sudoku.py** contains functions for generating, parsing and displaying sudoku CSPs
- **constraint.py** contains implementation of the constraints and propagation algorithm. Currently only the `all different` constraint is supported.
- **heuristic.py** contains heuristic functions discussed in the paper

### Adding constraints

The Sudoku constraints are generated in the `create_constraints` function in `sudoku.py`. This function returns an array of constraint and can be modified to add/remove them. A constraint is a Python tuple of the following structure:

```python
(type, [var1, var2, var3])
e.g.
("ALL_DIFF", ["x11", "x12", "x13", "x14", "x15", "x16", "x17", "x18", "x19"])
```

The following constraint types are supported:
 - `ALL_DIFF`: all different constraint

### Changing heuristics

The default heuristics when running the solver are:

- **variable heuristic**:  `smallest_domain`
- **value_heuristic**: `highest_promise`

Heuristics can be changed in `main.py`, e.g.:

```python
csp.variable_heuristic = "smallest_domain" 
csp.value_heuristic = "reduce_least_num_of_smallest_domains"
```

