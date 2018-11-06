#Hosein Kangavar Nazari
# Matrix Class

import random


class matrix:
    answer = 1
    # initialization
    # check for right size of a matrix

    def __init__(self, size):
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        self.size = size
    # overriding + for matrix

    def __add__(self, other):
        Answer = matrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                Answer.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Answer
    # overrriding * for matrix [ordinary Cross]

    def __sub__(self, other):
        Answer = matrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                Answer.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Answer

    def __mul__(self, other):
        Answer = matrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    Answer.matrix[i][j] += self.matrix[i][k] * \
                        other.matrix[k][j]
        return Answer

    # put random values into matrix elements
    def random_variable(self):
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] = random.randint(0, 1)

    def set_all_elem(self, value):
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] = value
    # set given value into matrix

    def set_matrix(self, value):
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] = value[i][j]

    def combine(self, topLeft, topRight, downLeft, downRight):
        start = 0
        mid = int((self.size/2)-1)
        end = self.size

        # fill TopLeft
        for i in range(start, mid+1):
            for j in range(start, mid+1):
                self.matrix[i][j] = topLeft.matrix[i][j]

        # topRight
        for i in range(start, mid+1):
            for j in range(mid+1, end):
                self.matrix[i][j] = topRight.matrix[i][j-mid-1]
        # downLeft
        for i in range(mid+1, end):
            for j in range(start, mid+1):
                self.matrix[i][j] = downLeft.matrix[i - mid - 1][j]

        # downRight
        for i in range(mid+1, end):
            for j in range(mid+1, end):
                self.matrix[i][j] = downRight.matrix[i - mid - 1][j-mid-1]


    def split(self):
        start = 0
        mid = int((self.size/2)-1)
        end = self.size
        topLeft = matrix(int(self.size/2))
        topRight = matrix(int(self.size/2))
        downLeft = matrix(int(self.size/2))
        downRight = matrix(int(self.size/2))

        # TopLeft
        for i in range(start, mid+1):
            for j in range(start, mid+1):
                topLeft.matrix[i][j] = self.matrix[i][j]

        # topRight
        for i in range(start, mid+1):
            for j in range(mid+1, end):
                topRight.matrix[i][j-mid-1] = self.matrix[i][j]
        # downLeft
        for i in range(mid+1, end):
            for j in range(start, mid+1):
                downLeft.matrix[i - mid - 1][j] = self.matrix[i][j]

        # downRight
        for i in range(mid+1, end):
            for j in range(mid+1, end):
                downRight.matrix[i - mid - 1][j-mid-1] = self.matrix[i][j]

        return topLeft, topRight, downLeft, downRight
    # def show(self):
    #     for i in range (self.size):
    #         print("\n")
    #         for j in range (self.size):
    #             print(self.matrix[i][j] , " ")
