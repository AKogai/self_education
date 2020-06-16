from sys import stdin
import copy


class Matrix:
    def __init__(self, lst):
        self.lst_my_list = copy.deepcopy(lst)

    def __str__(self):
        self.res = ''
        for i in self.lst_my_list:
            self.res += "\t".join(map(str, i))
            self.res += "\n"
        return self.res.strip()

    def size(self):
        self.col = len(self.lst_my_list[0])
        self.row = len(self.lst_my_list)
        return self.row, self.col

exec(stdin.read())
