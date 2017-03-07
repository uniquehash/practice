
from matrix import Matrix

    #    1 2 3 4 5 6 7
l = [   
        [1,2,3,4,5,6,7], # 1 
        [1,2,3,4,5,6,7], # 2
        [1,2,3,4,5,6,7], # 3
        [1,2,3,4,5,6,7], # 4
        [0,0,0,0,0,0,0], # 5
        [0,0,0,0,0,0,0], # 6        
        [0,0,0,0,0,0,0]  # 7
    ]

l = [   
        [1,5,2,3,6,4,7], # 1 
        [0,0,0,0,0,0,0], # 5
        [1,5,2,3,6,4,7], # 2        
        [1,5,2,3,6,4,7], # 3
        [0,0,0,0,0,0,0], # 6        
        [1,5,2,3,6,4,7], # 4                
        [0,0,0,0,0,0,0]  # 7
    ]



matrix = Matrix(l)
m = matrix.x



print matrix
# print ""
# print matrix.stable_len
# matrix.canonical_form()
# print ""
# matrix.push_down_row(matrix.index_to_push())
# matrix.proper_order()
matrix.canonical_form()
print matrix
# print matrix.verify_form()
# matrix.verify_form()
print ""














