
import pprint
import inspect

#####
#   level 1
#       1.1
#           comparing list problem
#           sets solution
#           constant time
#   level 2
#       2.1
#           general complex problem
#           dynamic programing solution
#           constant time
#       2.2
#           sorting problem with special elements
#           custom comparison function?
#           
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#####







### level 1
y = [14, 27, 1, 4, 2, 50, 3, 1]
x = [2, 4, -4, 3, 1, 1, 14, 27, 50]

## implementation 1
# sx = set()
# sy = set()

# for e in x:
#     if e not in sx:
#         sx.add(e)

# for e in y:
#     if e not in sy:
#         sy.add(e)

# diff = sx.symmetric_difference(sy)

# print "sx: ", sx
# print "sy: ", sy
# print "diff: ", diff.pop()


## implementation 2
# s_elements = set()
# s_index = set()
# index = -1

# for e in x:
#     if e not in s_elements:
#         s_elements.add(e)
#     if index > 0 and y[index] in s_elements:
#         s_index.add(index)
#     index += 1

# index = 0
# for e in y:
#     if index not in s_index:
#         if e not in s_elements:
#             print "e: ", e
#     index += 1

# print "s_elements: ", s_elements
# print "s_index: ", s_index


## implementation 3
# s_elements = set()
# s_index = set()
# index = -1

# def small_big(x, y):
#     if len(x) > len(y):
#         return (y, x)
#     else:
#         return (x, y)

# smallBig = small_big(x, y)

# x = smallBig[0]
# y = smallBig[1]

# for e in x:
#     if e not in s_elements:
#         s_elements.add(e)
#     if index > 0 and y[index] in s_elements:
#         s_index.add(index)
#     index += 1

# index = 0
# for e in y:
#     if index not in s_index:
#         if e not in s_elements:
#             print "e: ", e
#     index += 1

# print "s_elements: ", s_elements
# print "s_index: ", s_index




# implementation 4
# def small_big(x, y):
#     # len on lists in cpython is O(1)
#     if len(x) > len(y):
#         return (y, x)
#     else:
#         return (x, y)

# smallBig = small_big(x, y)
# x = smallBig[0]
# y = smallBig[1]

# s_elements = set()
# s_index = set()

# index = 0
# for e in x:
#     # checking membership of sets is O(1)
#     if e not in s_elements:
#         s_elements.add(e)
#     if y[index] not in s_elements:
#         s_index.add(index)
#     index += 1

# for e in s_index:    
#     if y[e] not in s_elements:
#         print "y[e]: ", y[e]

# print "s_elements: ", s_elements
# print "s_index: ", s_index


## implementation 5
# if len(x) > len(y): (x, y) = (y, x)

# s_elements = set()
# for e in x:
#     # checking membership of sets is O(1)
#     if e not in s_elements:
#         s_elements.add(e)    

# for e in y:   
#     if e not in s_elements:
#         print "e: ", e

# print "s_elements: ", s_elements



#### level 2

### 2.1
# s = ">----<"
# s = "<<>><"
# s = "--->-><-><-->-"

## implementation 1
# r_arr = 0
# result = 0

# for c in s:
#     if c == '>':
#         r_arr += 1
#     elif c == '<':
#         result += r_arr

# print "result: ", result
# print "saluts: ", result * 2

### 2.2
## implementation 1
# from operator import itemgetter
# l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
# l1 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

# def tuplify(e):    
#     return tuple(map(int, e.split('.')))

# print "\nlist   l:  ", l
# print "\nsorted l:  ", sorted(l, key=tuplify)
# print "test   l:  ", '["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]'

# print "\nlist   l1: ", l1
# print "\nsorted l1: ", sorted(l1, key=tuplify)
# print "test   l1: ", '["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]'

#### level 3

### 3.1

from fractions import Fraction as ff
from fractions import gcd

class Matrix(object):

    def __init__(self, array2d):
        self.x = array2d
        self.len = len(array2d)
        self.ident = Matrix.identity(array2d)
        self.stable_len = self.terminals_len()

    def __str__(self):
        return self.to_str()    

    def to_str(self, arr=None):
        s = ""
        s += "[\n"

        count = 0
        if not arr:
            arr = self.x

        for x in arr:
            s += "  ["
            s += "  "
            for y in x:     
                s += str(y)
                s += ", "               
            s += "], "+ str(count)+"\n"
            count += 1
        s += "]"
        return s



    def subset(self, rs, rf, cs, cf):
        col = range(cs, cf)
        row = range(rs, rf)

        sub = []
        tmp = []
        for j, e in enumerate(self.x):
            if j in row:
                tmp = []
                for i, x in enumerate(e):
                    if i in col:
                        tmp.append(x)
                sub.append(tmp)
        return sub

    @classmethod
    def identity(cls, trix):
        ident = []
        size = len(trix)
        for x in range(size):
            tmp = [0] * size
            tmp[x] = 1
            ident.append(tmp)

        return ident




    @classmethod
    def subtract(cls, trix0, trix1):
        matrix = []
        if len(trix0) != len(trix1):
            return []
        for i, y in enumerate(trix0):
            row = []
            for j, x in enumerate(y):
                row.append(trix0[i][j] - trix1[i][j])
            matrix.append(row)
        return matrix

    @classmethod
    def multiplaction(cls, trix0, trix1):
        rc_0 = Matrix.row_col_len(trix0)
        rc_1 = Matrix.row_col_len(trix1)

        if rc_0[1] != rc_1[0]:
            return []
        
        nm = []
        for i, y in enumerate(trix0):
            row = Matrix.dot_product(trix0, trix1, i, rc_1[1])
            nm.append(row)
        return nm


    @classmethod
    def row_col_len(cls, trix):
        row = len(trix)
        col = 0
        for x in trix[0]:
            col += 1            
        return (row, col)   

    @classmethod
    def dot_product(cls, trix0, trix1, row, col1):
        new_row = []        
        colum = 0
        for x in range(col1):
            dot_prod = 0
            col = 0
            for y in trix1:
                dot_prod += y[colum] * trix0[row][col]
                col += 1
            colum += 1
            new_row.append(dot_prod)
        return new_row

    @classmethod
    def inverse(cls, trix):
        size = len(trix)
        Matrix.inverse_form(trix)

        for x in range(size):
            if trix[x][x] != 1:
                trix[x] = Matrix.row_scale(trix[x], 1 / trix[x][x])
            for y in range(size):
                if y != x and trix[y][x] != 0:
                    trix[y] = Matrix.row_subtract(trix[y], trix[x], trix[y][x])

        return Matrix.extract_inverse(trix, size)
        

    @classmethod
    def row_subtract(cls, row0, row1, scale):
        new_row = []
        for i in range(len(row0)):
            new_row.append(row0[i] - (row1[i] * scale))
        return new_row

    @classmethod
    def row_scale(cls, row, scale):
        new_row = []
        for e in row:
            new_row.append(e * scale)
        return new_row

    @classmethod
    def inverse_form(cls, trix):
        ident = Matrix.identity(trix)
        for i, e in enumerate(trix):
            trix[i] += ident[i]

    @classmethod
    def extract_inverse(cls, trix, size):
        for y in range(size):
            tmp = []
            for x in range(len(trix[y])):
                if x >= size:
                    tmp.append(trix[y][x])
            trix[y] = tmp
        

    def canonical_form(self):       
        self.proper_order()
        self.proper_form()      

    def proper_form(self):
        for i, e in enumerate(self.x):
            if e == [0] * self.len:
                self.x[i][i] = 1
            else:
                self.fractionize(i)

    def proper_order(self):     
        while not self.verify_form():
            index = self.index_to_push()
            self.shift_right(index)
            self.push_down_row(index)

    def fractionize(self, index):
        total = 0
        for e in self.x[index]:
            total += e
        for i, e in enumerate(self.x[index]):
            self.x[index][i] = ff(e, total)

    def index_to_push(self):
        well_formed = True
        for i, e in enumerate(reversed(self.x)):            
            if e != [0] * self.len:         
                well_formed = False
            if e == [0] * self.len and well_formed == False:                
                return (self.len - i - 1)

    def shift_right(self, index):       
        for e in self.x:
            tmp = e[index + 1]
            e[index + 1] = e[index]
            e[index] = tmp

    def push_down_row(self, index):
        tmp = self.x[index+1]
        self.x[index+1] = self.x[index]
        self.x[index] = tmp

    def verify_form(self):      
        arr = self.x[self.len - self.stable_len:]
        count = 0       
        for e in arr:
            if e == [0] * self.len:
                count += 1
        if count == self.stable_len:
            return True
        else:
            return False

    def terminals_len(self):
        stable = 0
        for e in self.x:
            if e == [0] * self.len:
                stable += 1
        return stable


matrix = Matrix(l)
m = matrix.x

matrix.canonical_form()
Q = matrix.subset(0, matrix.len - matrix.stable_len, 0, matrix.len - matrix.stable_len)
I = Matrix.identity(Q)
I_minus_Q = Matrix.subtract(I, Q)
Matrix.inverse(I_minus_Q)
fundemental_matrix = I_minus_Q
R = matrix.subset(0, matrix.len - matrix.stable_len, 0, matrix.len + matrix.stable_len)
absoprtion_probabilities = Matrix.multiplaction(fundemental_matrix, R)
state0 = Matrix(absoprtion_probabilities).subset(0, 1, matrix.len - matrix.stable_len, matrix.len + matrix.stable_len)

numerator = []
denominator = []
for e in state0[0]:
    numerator.append(e.numerator)
    denominator.append(e.denominator)

def lcm(numbers):
    def lcm(a, b):
        return (a * b) / gcd(a, b)        
    return reduce(lcm, numbers, 1)

least = lcm(denominator)

answer = []
for i, e in enumerate(numerator):
    answer.append((least / denominator[i]) * e)
answer.append(least)

return answer
























































