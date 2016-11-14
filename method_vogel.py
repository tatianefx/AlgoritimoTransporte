class MethodVogel(object):

    def __init__(self, matrix, matrix_result):
        self.matrix = matrix
        self.matrix_result = matrix_result
        self.difference_row = []
        self.difference_column = []
        self.column = False
        self.row = False

    def differenceMinValues(self, array):
        min1 = min(array)
        array.remove(min1)
        min2 = min(array)
        return abs(min1 - min2)

    def penalty(self):
        length = len(self.matrix)
        transposed = [[row[i] for row in self.matrix] for i in range(length)]

        for x in range(length):
            self.difference_row.append(self.differenceMinValues(self.matrix[x]))

        for x in range(len(self.matrix)):
            self.difference_column.append(self.differenceMinValues(transposed[x]))

        max_row = max(self.difference_row)
        max_column = max(self.difference_column);

        if max_row > max_column:
            self.row = True
            return self.difference_row.index(max_row)
        elif max_row < max_column:
            self.column = True
            return self.difference_column.index(max_column)
        else:
            return self.difference_column.index(max_column)

    def vogel(self):
        index = self.penalty()
        if self.column:
            print("Coluna {}".format(index))
        elif self.row:
            print("Linha {}".format(index))
        else:
            print("Colunas e linhas iguais")







