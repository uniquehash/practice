
import numpy as np
from matrix import Matrix


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


# print "\nmatrix: \n", matrix

matrix.canonical_form()
# print "\ncanonical form:\n", matrix

Q = matrix.subset(0, matrix.len - matrix.stable_len, 0, matrix.len - matrix.stable_len)
# print "\nQ:\n", matrix.to_str(Q)

I = Matrix.identity(Q)
# print "\nI:\n", matrix.to_str(I)

I_minus_Q = Matrix.subtract(I, Q)
# print "\nI - Q:\n", matrix.to_str(I_minus_Q)

Matrix.inverse(I_minus_Q)
fundemental_matrix = I_minus_Q
# print "\nfundemental matrix:\n", matrix.to_str(fundemental_matrix)

R = matrix.subset(0, matrix.len - matrix.stable_len, 0, matrix.len + matrix.stable_len)
# print "\nR:\n", matrix.to_str(R)

absoprtion_probabilities = Matrix.multiplaction(fundemental_matrix, R)
# print "\nabsoprtion_probabilities:\n", matrix.to_str(absoprtion_probabilities)

state0 = Matrix(absoprtion_probabilities).subset(0, 1, matrix.len - matrix.stable_len, matrix.len + matrix.stable_len)
# print "\state0:\n", matrix.to_str(state0)

from fractions import Fraction as ff
from fractions import gcd

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

# print answer
















