class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(n) for n in line.split()] for line in matrix_string.splitlines()]
        self.matrixT = [list(r) for r in zip(*self.matrix)]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
    	return self.matrixT[index - 1]
