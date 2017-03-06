# absorbing markov chains practice


import numpy as np
from fractions import Fraction as ff



							   # a  b  c  d  e  f
							   # 0  1  2  3  4  5


n4 = 4.0 / 9
n3 = 3.0 / 9
n2 = 2.0 / 9
t1 = 1.0 / 2


transition_matrix = np.matrix([
								[ 0, t1,  0,  0,  0, t1], 
								[n4,  0,  0, n3, n2,  0],
								[ 0,  0,  1,  0,  0,  0],
								[ 0,  0,  0,  1,  0,  0],
								[ 0,  0,  0,  0,  1,  0],
								[ 0,  0,  0,  0,  0,  1]
							])

print "\ntransition matrix:"
print transition_matrix

# rearranging matrix with numpy http://stackoverflow.com/questions/10936767/rearranging-matrix-elements-with-numpy


canonical_form = np.matrix(transition_matrix)
print "\ncanonical form:"
print canonical_form


# subsetting a matrix http://stackoverflow.com/questions/30917753/subsetting-a-2d-numpy-array
Q = np.matrix(canonical_form[:2, :2])
print "\nQ:"
print Q

I = np.identity(2	)
print "\nI:"
print I

I_minus_Q = I - Q
print "\nI - Q:"
print I_minus_Q


fundemental_matrix =  np.matrix(I_minus_Q).I
print "\nfundemental matrix:"
print fundemental_matrix

R = np.matrix(canonical_form[0:2, 2:6])
print "\nR:"
print R

absoprtion_probabilities = fundemental_matrix * R

print "\nabsoprtion_probabilities:"
print absoprtion_probabilities

# print ff(absoprtion_probabilities[0][0])
print "\nfractions"
print ff(absoprtion_probabilities[0, 1]).limit_denominator(max_denominator=30)
print ff(absoprtion_probabilities[0, 2]).limit_denominator(max_denominator=30)
print ff(absoprtion_probabilities[0, 3]).limit_denominator(max_denominator=30)





























