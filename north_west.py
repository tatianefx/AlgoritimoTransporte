class NorthWest(object):

    def __init__(self, matrix, matrix_result, offer, capacity):
        self.matrix = matrix
        self.matrix_result = matrix_result
        self.offer = offer
        self.capacity = capacity
        self.minZ = 0

    def north_west(self):
        line = 0
        column = 0
        while line != len(self.offer):
            var = self.offer[line]
            if self.offer[line] <= self.capacity[column]:
                self.matrix_result[line][column] = self.offer[line]
                self.capacity[column] -= self.offer[line]
                self.offer[line] = 0
                if self.capacity[column] == 0:
                    column += 1
                line += 1
            else:
                self.matrix_result[line][column] = self.capacity[column]
                self.offer[line] -= self.capacity[column]
                self.capacity[column] = 0
                column += 1

    def calculateMinZ(self):
        self.north_west()

        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                self.minZ += (self.matrix[x][y] * self.matrix_result[x][y])

        return self.minZ


