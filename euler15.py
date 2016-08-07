# Project Euler
# Problem 15 - number of routes in a 20x20 grid

routes_result = {}

def number_routes(i, j, n):
    if (i, j) in routes_result:
        return routes_result[(i, j)]

    routes = 0

    if i == n and j == n:
        routes = 1

    if i < n:
        routes += number_routes(i+1, j, n)

    if j < n:
        routes += number_routes(i, j+1, n)

    
    routes_result[(i, j)] = routes
    return routes

print number_routes(0, 0, 20)
