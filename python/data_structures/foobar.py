
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




























































