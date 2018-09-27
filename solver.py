
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

