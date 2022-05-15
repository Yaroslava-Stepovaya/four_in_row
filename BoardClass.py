import os, sys
import numpy as np

class Board():
    def __init__(self, columns, rows,  inarow):
        self.grid = np.zeros((rows,columns), dtype =int)
        self.columns = columns
        self.rows = rows
        self.inarow = inarow

    def reset(self):
        self.grid = np.zeros((self.rows, self.columns), dtype=int)

