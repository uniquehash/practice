

import numpy as np

from matrix import Matrix

#     #    1 2 3 4 5 6 7
# l = [   
#         [1,2,3,4,5,6,7], # 1 
#         [1,2,3,4,5,6,7], # 2
#         [1,2,3,4,5,6,7], # 3
#         [1,2,3,4,5,6,7], # 4
#         [0,0,0,0,0,0,0], # 5
#         [0,0,0,0,0,0,0], # 6        
#         [0,0,0,0,0,0,0]  # 7
#     ]

l = [   
        [0,1,0,0,0,1],
        [4,0,0,3,2,0],
        [0,0,0,0,0,0],
       	[0,0,0,0,0,0],
    	[0,0,0,0,0,0], 
        [0,0,0,0,0,0]
    ]

matrix = Matrix(l)
m = matrix.x



print "\nmatrix: \n", matrix

matrix.canonical_form()
print "\ncanonical form:\n", matrix

Q = matrix.subset(0, matrix.len - matrix.stable_len, 0, matrix.len - matrix.stable_len)
print "\nQ:\n", matrix.to_str(Q)

I = Matrix.identity(Q)
print "\nI:\n", matrix.to_str(I)

I_minus_Q = Matrix.subtract(I, Q)
print "\nI - Q:\n", matrix.to_str(I_minus_Q)

Matrix.inverse(I_minus_Q)
fundemental_matrix = I_minus_Q
print "\nfundemental matrix:\n", matrix.to_str(fundemental_matrix)

	
R = matrix.subset(0, matrix.len - matrix.stable_len, 0, matrix.len + matrix.stable_len)
print "\nR:\n", matrix.to_str(R)

absoprtion_probabilities = Matrix.multiplaction(fundemental_matrix, R)
print "\nabsoprtion_probabilities:\n", matrix.to_str(absoprtion_probabilities)

answer = Matrix(absoprtion_probabilities).subset(0, 1, matrix.len - matrix.stable_len, matrix.len + matrix.stable_len)
print "\nanswer:\n", matrix.to_str(answer)
# print Matrix.row_scale(dot0[0], 2)
# print Matrix.row_subtract(dot0[0], dot0[1], 1)

# Matrix.inverse_form(dot0)
# print "\ninverse form: \n", matrix.to_str(dot0)


# Matrix.inverse(dot0)
# print "\ninvers full: \n", matrix.to_str(dot0)





# print inverse.I

# print matrix.to_str(inverse)

# print sub0
# print sub1

# print sub0[0][0]
# print Matrix.subtract(sub0, sub1)
# print "dot0: \n", matrix.to_str(dot0)
# print "\ndot1: \n", matrix.to_str(dot1)

# row_len0 =  Matrix.row_col_len(dot0)
# row_len1 =  Matrix.row_col_len(dot1)
# print "row_len1: ", row_len0
# print "row_len1: ", row_len1
# print Matrix.dot_product(dot0, dot1, 0, row_len1[1])

# print matrix.to_str(Matrix.multiplaction(dot0, dot1))

# print matrix
# print ""
# print matrix.stable_len
# matrix.canonical_form()
# print ""
# matrix.push_down_row(matrix.index_to_push())
# matrix.proper_order()
# matrix.canonical_form()
# print "0-4, 2-4"
# matrix.subset(3,7,2,7)
# print matrix
# print matrix.verify_form()
# matrix.verify_form()
# print ""

# def inverse(matrix):
# 	def make_identity(size):
# 	    identity = []
# 	    for i in range(size):
# 	        identity.append([1 if j == i else 0
# 	                         for j in range(size)])
# 	    return identity


# 	def append_identity(matrix):
# 		identity = make_identity(len(matrix))
# 		for i in range(len(matrix)):
# 			matrix[i] += identity[i]

# 	def scale_row(row, factor):
# 		return [x * factor for x in row]

# 	def subtract_row(row1, row2, quantity):
# 		return [row1[i] - row2[i] * quantity for i in range(len(row1))]

# 	dim = len(matrix)
# 	append_identity(matrix)
# 	for x in range(dim):
# 		if matrix[x][x] != 1:
# 			matrix[x] = scale_row(matrix[x], 1 / matrix[x][x]) # matrix[x][x] wont be 0  
# 		for y in range(dim):
# 			if y != x and matrix[y][x] != 0:
# 				matrix[y] = subtract_row(matrix[y], matrix[x], matrix[y][x])
# 	for i in range(dim):
# 		matrix[i] = [matrix[i][x] for x in range(len(matrix[i])) if x >= dim]
# 	return matrix

# ma = inverse(dot1)
# print matrix.to_str(ma)












