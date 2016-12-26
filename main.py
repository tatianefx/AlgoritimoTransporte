import north_west


class Main(object):

    def __init__(self):
        self.factory = 0
        self.transport = 0
        self.artificial_variable = False
        self.matrix = []
        self.matrix_result = []
        self.offer = []
        self.capacity = []
        self.minZ = 0

        # self.read_inputs()
        # self.initialize_matrix_result()
        # self.initialize_matrix()
        self.test()

        print('Matriz: ')
        print(self.matrix)

        print('Oferta: ')
        print(self.offer)

        print('Capacidade: ')
        print(self.capacity)

        self.minZ = north_west.NorthWest(self.matrix, self.matrix_result, self.offer, self.capacity).calculateMinZ()
        print('minZ: ')
        print(self.minZ)

    def test(self):
        self.factory = 3
        self.transport = 3
        self.artificial_variable = False
        self.matrix = [[6, 4, 3], [5, 6, 1], [0, 0, 0]]
        self.matrix_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.offer = [180, 120, 20]
        self.capacity = [190, 100, 30]
        self.minZ = 0

        # self.factory = 3
        # self.transport = 4
        # self.artificial_variable = False
        # self.matrix = [[1, 2, 3, 4], [4, 3, 2, 4], [0, 2, 2, 1]]
        # self.matrix_result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        # self.offer = [6, 8, 10]
        # self.capacity = [4, 7, 6, 7]
        # self.minZ = 0

    def read_inputs(self):
        print('Número de fábricas: ')
        self.factory = int(input())

        print('Número de transportes: ')
        self.transport = int(input())

        for i in range(self.factory):
            print('Insira a oferta da fábrica {}'.format(i))
            self.offer.append(int(input()))

        for j in range(self.transport):
            print('Insira a capacidade de escoamento do transporte {}'.format(j))
            self.capacity.append(int(input()))

        total_offer = sum(self.offer)
        total_capacity = sum(self.capacity)

        if total_offer < total_capacity:
            self.offer.append(total_capacity - total_offer)
            self.artificial_variable = True
            self.factory += 1

    def initialize_matrix_result(self):
        self.matrix_result = [x[:] for x in [[0] * self.transport] * self.factory]

    def initialize_matrix(self):
        for x in range(self.factory):
            row = []
            if self.artificial_variable and (x == self.factory - 1):
                for y in range(self.transport):
                    row.append(0)
            else:
                print('Insira os custos da linha {}'.format(x))
                for y in range(self.transport):
                    row.append(int(input()))

            self.matrix.append(row)

Main()