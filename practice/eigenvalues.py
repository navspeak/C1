# Import necessary modules: math for calculations and ast for safe input evaluation
import math, ast

# Input has been taken for you
matrix = ast.literal_eval(input())

# Define a function to find the eigenvalues of a 2x2 matrix
def find_eigenvalues(matrix):
    a00 = matrix[0][0]
    a01 = matrix[0][1]
    a10 = matrix[1][0]
    a11 = matrix[1][1]

    a = 1
    b = -(a00+a11)
    c = a00*a11 - a01*a10

    descriminant = math.sqrt(b*b - 4*a*c)
    x = (-b + descriminant)/ (2*a)
    y = (-b - descriminant)/ (2*a)
    return [round(x,2), round(y,2)]

print(find_eigenvalues(matrix))
# Sample Input

# [[4, 2], [1, 3]]



# Sample Output

# [5.0, 2.0]