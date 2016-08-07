# Project Euler
# Problem 18 - Maximum total in triangle from top to bottom 

triangle = []

with open('euler18.txt', 'r') as triangle_file:
    for line in triangle_file:
        triangle.append([int(i) for i in line.split()])

def find_best_path(tri):
    if len(tri) == 0:
        return 0
    elif len(tri) == 1:
        return tri[0][0]

    
    #if tri[1][0] < tri[1][1]:
    reduced_tri = []
    for line in tri[1:]:
        reduced_tri.append(line[1:])
    left_tree = find_best_path(reduced_tri)

    reduced_tri = []
    for line in tri[1:]:
        reduced_tri.append(line[:-1])
    right_tree = find_best_path(reduced_tri)

    return tri[0][0] + max(left_tree, right_tree)

print find_best_path(triangle)
