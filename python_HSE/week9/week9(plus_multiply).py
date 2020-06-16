from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other

class Matrix:
    def __init__(self, lst):
        self.lst_my_list = copy.deepcopy(lst)
        self.col = len(self.lst_my_list[0])
        self.row = len(self.lst_my_list)

    def __str__(self):
        self.res = ''
        for i in self.lst_my_list:
            self.res += "\t".join(map(str, i))
            self.res += "\n"
        return self.res.strip()

    def size(self):
        return self.row, self.col

    def __add__(self, other):
        if self.col == other.row and self.col == other.col:
            result = []
            res = []
            for x in range(self.row):
                for y in range(self.col):
                    sum = int(self.lst_my_list[x][y] + other.lst_my_list[x][y])
                    res.append(sum)
                result.append(res)
                res = []
            return Matrix(result)
        else:
            return 'Размерности не совпадают'

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * x for x in y] for y in self.lst_my_list]
            return Matrix(result)
        elif self.col != other.row:
            return 'Нельзя перемножить матрицы таких размерностей'
        else:
            a = range(self.col)
            b = range(self.row)
            c = range(other.col)
            result = []
            for i in b:
                res = []
                for j in c:
                    el, m = 0, 0
                    for k in a:
                        m = self.lst_my_list[i][k] * other.lst_my_lst[k][j]
                        el += m
                    res.append(el)
                result.append(res)
            return Matrix(result)

    def __rmul__(self, other):
        return self.__mul__(other)

exec(stdin.read())
