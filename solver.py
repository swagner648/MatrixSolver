
from fraction import Fraction
from matrix import Matrix

M = Matrix(3, 4)
temp = [[20, 4, 4, 5000],
        [10, 14, 5, 8500],
        [5, 5, 12, 10000]]
M.set(temp)
M.reduceSteps()

M = Matrix(3, 4)
temp = [[20, 4, 4, 2000],
        [10, 14, 5, 4000],
        [5, 5, 12, 4000]]
M.set(temp)
M.reduceSteps()

M = Matrix(3, 4)
temp = [[20, 4, 4, 7000],
        [10, 14, 5, 12500],
        [5, 5, 12, 14000]]
M.set(temp)
M.reduceSteps()

# a13
M = Matrix(3, 4)
temp = [[20, 4, 4, 7210],
        [10, 14, 5, 12500],
        [5, 5, 12, 14000]]
M.set(temp)
M.reduceSteps()

# a13
M = Matrix(3, 4)
temp = [[20, 4, 4, 6790],
        [10, 14, 5, 12500],
        [5, 5, 12, 14000]]
M.set(temp)
M.reduceSteps()

# a31
M = Matrix(3, 4)
temp = [[20, 4, 4, 7000],
        [10, 14, 5, 12500],
        [Fraction(515, 100), 5, 12, 14000]]
M.set(temp)
M.reduceSteps()

# a31
M = Matrix(3, 4)
temp = [[20, 4, 4, 7000],
        [10, 14, 5, 12500],
        [Fraction(485, 100), 5, 12, 14000]]
M.set(temp)
M.reduceSteps()

# a33
M = Matrix(3, 4)
temp = [[20, 4, 4, 7000],
        [10, 14, 5, 12500],
        [5, 5, 12, 14420]]
M.set(temp)
M.reduceSteps()

# a33
M = Matrix(3, 4)
temp = [[20, 4, 4, 7000],
        [10, 14, 5, 12500],
        [5, 5, 12, 13580]]
M.set(temp)
M.reduceSteps()

M = Matrix(3, 4)
temp = [[20, 7, 6, 5000],
        [10, 14, 3, 9000],
        [5, 5, 12, 4500]]
M.set(temp)
M.reduceSteps()

M = Matrix(3, 4)
temp = [[20, 7, 0, 5000],
        [10, 14, 0, 8500],
        [5, 5, 0, 10000]]
M.set(temp)
M.reduceSteps()
