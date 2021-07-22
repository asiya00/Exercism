class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.splitlines()
        self.matrix = [[int(j) for j in i.split()] for i in self.matrix_string]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        li = [i[index-1] for i in self.matrix]
        return li
