import math, ast
data = ast.literal_eval(input())
v, b1, b2 = data

# Input has been taken for you and the v, b1, b2 vectors have been extracted
def vector_in_new_basis(v, b1, b2):
    det = b1[0]*b2[1] - b2[0]*b1[1]
    if det == 0:
        return "Invalid input"

    b1_inv =[ b2[1], -b1[1]]
    b2_inv =[ -b2[0], b1[0]]

    v1_new = (1/det)*(b2[1]*v[0] - b2[0]*v[1])
    v2_new = (1/det)*(-b1[1]*v[0] + b1[0]*v[1])
    return [v1_new, v2_new]

print(vector_in_new_basis(v, b1, b2))