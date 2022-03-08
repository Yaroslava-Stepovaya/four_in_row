import os, sys
import numpy as np

class Board():
    def __init__(self,rows, columns,  inarow):
        self.grid = np.zeros((columns, rows), dtype =int)
        self.columns = columns
        self.rows = rows
        self.inarow = inarow
        self.grid[0][0] = 1
        self.grid[2][1] = 2