
from fraction import Fraction


class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.mx = [[0 for _ in range(n)] for _ in range(m)]

    def __repr__(self):
        out = ""
        for i in range(0, self.m):
            out = out + str(self.mx[i]) + '\n'
        return out[:-1]

    def fill(self):
        for i in range(self.m):
            for j in range(self.n):
                try:
                    value = int(input("Value in row " + str(i) + " and column " + str(j) + ":"))
                except ValueError:
                    print("Matrix can only be filled with Integers, to use fractions use set()")
                self.mx[i][j] = value

    def set(self, matrix):
        try:
            matrix[0][0]
        except TypeError:
            raise TypeError("Matrix must be 2-dimensions")

        if self.m != len(matrix) or self.n != len(matrix[0]):
            raise IndexError("Matrix set does not have same dimensions as initialization")

        for row in range(self.m):
            for col in range(self.n):
                if type(matrix[row][col]) != int and type(matrix[row][col]) != Fraction:
                    raise ValueError("Matrix must include only Integers and/or Fractions")
                self.mx[row][col] = matrix[row][col]

    def reduceSteps(self):
        print("-------------------------------------")
        print("INITIAL:")
        print(self)

        free = 0
        cols = []
        for step in range(self.m):
            col = step + free

            swapped = -1
            if self.mx[step][col] == 0:
                swapped = 0
                for row in range(step, self.m):
                    if self.mx[row][col] != 0:
                        print("--------------------")
                        print("Row", step, "swapped with row", row)
                        self.mx[step], self.mx[row] = rowSwapRow(self.mx[col], self.mx[row])
                        print(self)
                        swapped = 1

            if swapped == 0:
                free   = free + 1
                col = step + free

            for row in range(step, self.m):
                if self.mx[row][col] == 0 or self.mx[row][col] == 1:
                    continue
                print("--------------------")
                print("Row", row, "divided by", self.mx[row][col])
                self.mx[row] = scalarDivRow(self.mx[row], self.mx[row][col])
                print(self)

            for row in range(step + 1, self.m):
                if self.mx[row][col] == 0:
                    continue
                print("--------------------")
                print("Row", row, "minus row", step)
                self.mx[row] = rowSubRow(self.mx[row], self.mx[step])
                print(self)

            cols.append(col)

        for step in reversed(range(1, self.m)):
            for row in reversed(range(0, step)):
                print("--------------------")
                print("Row", row, "minus", self.mx[row][cols[step]], "times row", step)
                self.mx[row] = rowSubRow(self.mx[row], scalarMulRow(self.mx[step], self.mx[row][cols[step]]))
                print(self)

        print("-------------------------------------")
        print("ANSWER:")
        print(self)


def scalarMulRow(row, scalar):
    if type(scalar) != Fraction:
        scalar = Fraction(scalar, 1)
    out = [0 for _ in range(len(row))]
    for i in range(len(row)):
        out[i] = row[i] * scalar
    return out


def scalarDivRow(row, scalar):
    if type(scalar) != Fraction:
        scalar = Fraction(scalar, 1)
    out = [0 for _ in range(len(row))]
    for i in range(len(row)):
        out[i] = row[i] / scalar
    return out


def rowAddRow(list1, list2):
    out = [0 for _ in range(len(list1))]
    for i in range(len(list1)):
        out[i] = list1[i] + list2[i]
    return out


def rowSubRow(list1, list2):
    out = [0 for _ in range(len(list1))]
    for i in range(len(list1)):
        out[i] = list1[i] - list2[i]
    return out


def rowSwapRow(row1, row2):
    return row2, row1

